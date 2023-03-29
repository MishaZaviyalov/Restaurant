def mainMenu(nameMenu: str) -> int:
    collectionMenu = ["null"]
    match nameMenu:
        case "MainMenu":
            collectionMenu = ["1. Посмотреть баланс", "2. Приступить к составлению заказа", "3. Сменить аккаунт"]
        case "AUF":
            collectionMenu = ["1. Регистрация", "2. Авторизация", "3. Завершить работу"]
        case "UserPanel":
            collectionMenu = ["1. Сделать заказ", "2. Узнать баланс", "3. Посмотреть историю заказов",
                              "4. Выход из учётной записи"]
        case "AdminPanel":
            collectionMenu = ["1. Заказать ингредиенты", "2. Узнать свой баланс", "3. Узнать баланс пользователя",
                              "4. Выход из учётной записи"]
    for sentence in collectionMenu:
        print(sentence)
    Ans = 99
    try:
        Ans = int(input("Ваш ответ:\t"))
    except:
        print("Данные действия не предусмотрены системой!")
    return Ans

