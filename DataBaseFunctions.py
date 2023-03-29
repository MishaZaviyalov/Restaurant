import decimal
import random

import DataBaseClass
import RestaurantMath
import CheeseBurger
import re


def EnterSystem(LoginUser: str, PasswordUser: str) -> bool:
    CollectionInfo = DataBaseClass.Read(
        f'select * from [dbo].[User] where [Login] = \'{LoginUser}\' and [Password] = \'{PasswordUser}\'')
    if len(CollectionInfo) > 0:
        return True
    else:
        return False


def InputSystem(LoginUser: str):
    CollectionInfo = DataBaseClass.Read(
        f'select [Id_User], [Role_Name] from [dbo].[User] where [Login] = \'{LoginUser}\'')
    if len(CollectionInfo) > 0:
        return CollectionInfo
    else:
        return None


def GetMoney(Id: int):
    CollectionInfo = DataBaseClass.Read(
        f'select [Balance] from [dbo].[User] where [Id_User] = {Id}')
    if CollectionInfo[0][0] == None:
        return 0
    else:
        return CollectionInfo[0][0]


def IsExistAccount(LoginUser: str) -> bool:
    CollectionInfo = DataBaseClass.Read(
        f'select * from [dbo].[User] where [Login] = \'{LoginUser}\'')
    if len(CollectionInfo) > 0:
        return True
    else:
        return False


def IsExistAccount_NumberPhone(phoneUser: str) -> bool:
    CollectionInfo = DataBaseClass.Read(
        f'select count(*) from [dbo].[User] where [NumberPhone] = \'phoneUser\'')
    if int(CollectionInfo[0][0]) == 0:
        return False
    else:
        return True


def Loyalty_card(Id: int, min, medium, max, max_max):
    CollectionInfo = DataBaseClass.Read("select case" 
                                        f" when sum([Price]) >= {min} and sum([Price]) < {medium} then 1" 
                                        f" when sum([Price]) >= {medium} and sum([Price]) < {max}  then 2" 
                                        f" when sum([Price]) >= {max} and sum([Price]) < {max_max} then 3" 
                                        f" else 0 end from [dbo].[Order] where [User_ID] = {Id}")
    return CollectionInfo[0][0]



def Registration():
    NumberPhone = input("Введите номер телефона в формате (80000000000):\t")
    if len(NumberPhone) == 11:
        LoginUser = input("Введите логин:\t")
        if not IsExistAccount(LoginUser):
            Password = input("Введите пароль:\t")
            if len(Password) >= 4 and len(LoginUser) >= 4:
                Price = RestaurantMath.plusDiscountPrice(70)
                query = str.format("insert into [dbo].[User] ([NumberPhone], [Login], [Password], [Balance])"
                                   " values ('{0}', '{1}', '{2}', {3})",
                                   NumberPhone,
                                   LoginUser,
                                   Password,
                                   Price)
                DataBaseClass.Write(query)
            else:
                print("Пароль или логин слишком лёгкий!")
        else:
            print("Пользователь с подобным логин уже существует!")
    else:
        print("Ошибка номер телефона")


def CollectionKeys():
    list_keys = []
    product = CheeseBurger.CheeseBurger()
    product.bun = CheeseBurger.Ing(CheeseBurger.getBuns())
    product.steak = CheeseBurger.Ing(CheeseBurger.getSteak())
    product.ketchup = CheeseBurger.Ing(CheeseBurger.getKetchup())
    product.cucumber = CheeseBurger.Ing(CheeseBurger.getCucumber())
    product.onion = CheeseBurger.Ing(CheeseBurger.getOnion())
    product.mustard_sauce = CheeseBurger.Ing(CheeseBurger.getMustardSouse())
    product.seasoning = CheeseBurger.Ing(CheeseBurger.getSeasoning())
    list_keys.append(product.bun)
    list_keys.append(product.steak)
    list_keys.append(product.ketchup)
    list_keys.append(product.cucumber)
    list_keys.append(product.onion)
    list_keys.append(product.mustard_sauce)
    list_keys.append(product.seasoning)
    return list_keys


def getLastOrderUser(Id: int):
    CollectionInfo = DataBaseClass.Read(f"select top 1 [Price] from [dbo].[Order] where [User_ID] = {Id}")
    if len(CollectionInfo) == 0:
        return -1
    else:
        return CollectionInfo[0][0]


def payProduct(Id_User: int):
    DataBaseClass.Write(f"execute [dbo].[Last_Order] @Id_user={Id_User}")


def priceProduct(list_keys):
    CollectionInfo = DataBaseClass.Read(
        f"select [dbo].[Sum_Order]({list_keys[0]}, {list_keys[1]}, {list_keys[2]}, {list_keys[3]},"
        f" {list_keys[4]}, {list_keys[5]}, {list_keys[6]})")
    return float(CollectionInfo[0][0])


def randomPrice(price):
    bool_type = random.randint(1, 5) == random.randint(1, 5)
    if bool_type:
        print("Вам в заказ попались грязные деньги! Вам полагается скидка!")
        return RestaurantMath.discountPrice(price, 30)
    else:
        return price


def CollectBurger(Id_User: int):
    countDishes = int(input("Введите количество блюд:\t"))
    CollectionUserInfo = DataBaseClass.Read(f"select [Balance] from [dbo].[User] where [Id_User] = {Id_User}")
    BalanceUser = 0
    if (CollectionUserInfo[0][0] != None):
        BalanceUser = float(CollectionUserInfo[0][0])
    if BalanceUser >= (countDishes * 50):
        ProductPrice = 0
        KeysList = []
        for i in range(countDishes):
            list_keys = CollectionKeys()
            ProductPrice += priceProduct(list_keys)
            KeysList.append(list_keys)
        if BalanceUser < ProductPrice:
            print("У вас не достаточно денег!")
        else:
            finalPrice = randomPrice(ProductPrice)
            if finalPrice != 0:
                match (Loyalty_card(Id_User, 5000, 15000, 25000, 1000000)):
                    case 1:
                        finalPrice = RestaurantMath.discountPrice(finalPrice, 5)
                    case 2:
                        finalPrice = RestaurantMath.discountPrice(finalPrice, 10)
                    case 3:
                        finalPrice = RestaurantMath.discountPrice(finalPrice, 20)

            DataBaseClass.Write("insert into [dbo].[Order] ([Price], [Count_FOOD], [User_ID])"
                                f" values ({finalPrice}, {countDishes}, {Id_User})")
            for collection in KeysList:
                DataBaseClass.Write("execute [dbo].[ID_Update_Count_Ingr]"
                                    f" @bun={collection[0]},"
                                    f" @steak={collection[1]},"
                                    f" @ketchup={collection[2]},"
                                    f" @cucumber={collection[3]},"
                                    f" @onion={collection[4]},"
                                    f" @mustard_sauce={collection[5]},"
                                    f" @seasoning={collection[6]}")
            DataBaseClass.Write(f"execute [dbo].[Take_Money_User] @Sum = {finalPrice}, @Id_User = {Id_User}")
    else:
        print("Вам не хватит на блюда!")


def select_history(id: int):
    CollectionInfo = DataBaseClass.Read("select [ID_Order], format([Date_Order], 'dd/MM/yyyy'),"
                                        " Price, Count_FOOD from [dbo].[Order]"
                                        f" where [User_ID] = {id}")
    if len(CollectionInfo) != 0:
        for i in CollectionInfo:
            print(
                f"Номер: " + str(i[0]) + " Дата: " + str(i[1]) + " Цена: " + str(i[2]) + " Количество позиций: " + str(
                    i[3]))
    else:
        print("Вы не совершили не одного заказа!")


def getUserBalance():
    phone = input("Введите номер телефона пользователя: ")
    CollectionInfo = DataBaseClass.Read(f"select [Balance] from [dbo].[User] where [NumberPhone] = \'{phone}\'")
    pattern = r'^\d{11}$'  # регулярное выражение для проверки формата номера телефона
    if re.match(pattern, phone):
        print("Баланс пользователя: " + str(CollectionInfo[0][0]))
    else:
        print("Номер телефона не соответствует формату.")


def returnIngID(num_type: int):
    CollectionInfo = []
    match num_type:
        case 0:
            CollectionInfo = CheeseBurger.getBunsAdmin()
        case 1:
            CollectionInfo = CheeseBurger.getSteakAdmin()
        case 2:
            CollectionInfo = CheeseBurger.getCheeseAdmin()
        case 3:
            CollectionInfo = CheeseBurger.getKetchupAdmin()
        case 4:
            CollectionInfo = CheeseBurger.getCucumberAdmin()
        case 6:
            CollectionInfo = CheeseBurger.getOnionAdmin()
        case 7:
            CollectionInfo = CheeseBurger.getMustardSouseAdmin()
        case 8:
            CollectionInfo = CheeseBurger.getSeasoningAdmin()
    return CollectionInfo


def addIng_return_ID():
    type_info = ['Булочка', 'Бифштекс', 'Сыр', 'Кетчуп', 'Огурец', 'Лук', 'Горчица', 'Приправа']
    id_product = -1
    for n, i in enumerate(type_info):
        print('Номер: ' + str(n + 1) + " Название типа: " + i)
    num = int(input("Введите номер тип ингридиента:\t"))
    num -= 1
    CollectionInfo = returnIngID(num)
    for n, i in enumerate(CollectionInfo):
        print('Номер: ' + str(n + 1) + " Название ингридиета: " + str(i[1]) + " Количество ингридиента: " + str(i[2]))
    num = int(input("Введите номер названия:\t"))
    num -= 1
    id_product = CollectionInfo[num][0]
    return id_product


def addIng():
    count = int(input("Введите количество ингридиента для добавления:\t"))
    DataBaseClass.Write("execute [dbo].[AddIng]"
                        f" @Id_Ing={addIng_return_ID()},"
                        f" @Count_Product_Plus={count}")

def getIngsCount():
    CollectionInfo = DataBaseClass.Read("select [name_ingredient], [type_ingredient]," + 
                                        " [Count_ingredients] from [dbo].[Сheeseburger_ingredients]" +
                                         "where [name_ingredient] != \'не добавлять\'")
    print("Наименованияе; Тип; Количество.")
    for element in CollectionInfo:
        print(str(element[0]) + ' - ' + str(element[1]) + ' - ' + str(element[2]))
