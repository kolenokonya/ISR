def Str():
    try:
        text=input("Введите строку ")
        print("Длина строки ",len(text))
        print("Количество пробелов ", text.count(" "))
        print("Количество запятых ", text.count(","))
    except Exception:
        print("Что-то введено не так")
