import DataBaseClass


def getIng() -> str:
    query = "select [ID_Cheeseburger], [name_ingredient], [price_ingredient], [Count_ingredients]" \
            " from [dbo].[Сheeseburger_ingredients] where [" \
            "type_ingredient] = \'{0}\' and [Count_ingredients] > 0"
    return query


def getIngAdmin() -> str:
    query = "select [ID_Cheeseburger], [name_ingredient], [Count_ingredients]" \
            " from [dbo].[Сheeseburger_ingredients] where [" \
            "type_ingredient] = \'{0}\' and [name_ingredient] != 'Не добавлять'"
    return query


def getBuns():
    return DataBaseClass.Read(str.format(getIng(), "Булочка"))


def getSteak():
    return DataBaseClass.Read(str.format(getIng(), "Бифштекс"))


def getCheese():
    return DataBaseClass.Read(str.format(getIng(), "Сыр"))


def getKetchup():
    return DataBaseClass.Read(str.format(getIng(), "Кетчуп"))


def getCucumber():
    return DataBaseClass.Read(str.format(getIng(), "Огурец"))


def getOnion():
    return DataBaseClass.Read(str.format(getIng(), "Лук"))


def getMustardSouse():
    return DataBaseClass.Read(str.format(getIng(), "Горчица"))


def getSeasoning():
    return DataBaseClass.Read(str.format(getIng(), "Приправа"))


def getBunsAdmin():
    return DataBaseClass.Read(str.format(getIngAdmin(), "Булочка"))


def getSteakAdmin():
    return DataBaseClass.Read(str.format(getIngAdmin(), "Бифштекс"))


def getCheeseAdmin():
    return DataBaseClass.Read(str.format(getIngAdmin(), "Сыр"))


def getKetchupAdmin():
    return DataBaseClass.Read(str.format(getIngAdmin(), "Кетчуп"))


def getCucumberAdmin():
    return DataBaseClass.Read(str.format(getIngAdmin(), "Огурец"))


def getOnionAdmin():
    return DataBaseClass.Read(str.format(getIngAdmin(), "Лук"))


def getMustardSouseAdmin():
    return DataBaseClass.Read(str.format(getIngAdmin(), "Горчица"))


def getSeasoningAdmin():
    return DataBaseClass.Read(str.format(getIngAdmin(), "Приправа"))


def Ing(CollectionInfo):
    for num, item in enumerate(CollectionInfo):
        print(f"Номер: {num + 1} - " + "Название ингридиента: " + str(item[1]) + "; Стоимость: " + str(item[2]))
    _number = int(input("Выберете и введите номер ингредиента:\t"))
    _number = CollectionInfo[_number - 1][0]
    return _number


def IngAdmin(CollectionInfo):
    for num, item in enumerate(CollectionInfo):
        print(f"Номер: {num + 1} - " + "Название ингридиента: " + str(item[1]) + "; Стоимость: " + str(item[2]))
    _number = int(input("Выберете и введите номер ингредиента:\t"))
    _number = CollectionInfo[_number - 1][0]
    return _number


class CheeseBurger:
    def __init__(self):
        self.bun = int
        self.steak = int
        self.ketchup = int
        self.cucumber = int
        self.onion = int
        self.mustard_sauce = int
        self.seasoning = int
