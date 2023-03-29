import random

import DataBaseFunctions
import Menu
import os

import RestaurantMath

ID_USER = -1
INFO = None

CanITakeMoney = True


def userPanel(id: int):
    global CanITakeMoney
    if CanITakeMoney:
        DataBaseFunctions.payProduct(id)
        CanITakeMoney = False
    print("Панель пользователя:")
    Answer = Menu.mainMenu("UserPanel")
    match (Answer):
        case 1:
            os.system("cls")
            print("Сборка бургера:")
            DataBaseFunctions.CollectBurger(id)
        case 2:
            os.system("cls")
            print("Ваш баланс: " + str(DataBaseFunctions.GetMoney(id)))
        case 3:
            os.system("cls")
            print("Ваша история покупок:")
            DataBaseFunctions.select_history(id)
        case 4:
            os.system("cls")
            global ID_USER
            ID_USER = -1
            CanITakeMoney = True
        case _:
            os.system("cls")
            print("Подобные действия не предусмотрены!")


def adminPanel(id: int):
    print("Панель администратора:")
    Answer = Menu.mainMenu("AdminPanel")
    match Answer:
        case 1:
            os.system("cls")
            DataBaseFunctions.getIngsCount()
            DataBaseFunctions.addIng()
        case 2:
            os.system("cls")
            print("Ваш баланс: " + str(DataBaseFunctions.GetMoney(id)))
        case 3:
            os.system("cls")
            DataBaseFunctions.getUserBalance()
        case 4:
            os.system("cls")
            global ID_USER
            ID_USER = -1
        case _:
            os.system("cls")
            print("Подобные действия не предусмотрены!")

while (1):
    try:
        if ID_USER == -1:
            print("Добро пожаловать в консольный ресторан!")
            Answer = Menu.mainMenu("AUF")
            if Answer == 1:
                DataBaseFunctions.Registration()
            elif Answer == 2:
                LoginUser = input("Введите логин:\t")
                PasswordUser = input("Введите пароль:\t")
                if DataBaseFunctions.EnterSystem(LoginUser, PasswordUser):
                    INFO = DataBaseFunctions.InputSystem(LoginUser)
                    ID_USER = INFO[0][0]
                else:
                    os.system("cls")
                    print("Неверный логин или пароль!")
            elif Answer == 3:
                break
            else:
                os.system("cls")
                print("Данные действия не предусмотрены!")
        else:
            match (INFO[0][1]):
                case "Пользователь":
                    userPanel(ID_USER)
                case "Администратор":
                    adminPanel(ID_USER)
    except:
        print("Действия не предусмотрены системой")

