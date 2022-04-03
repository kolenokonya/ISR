import math
from xml.etree.ElementInclude import include

S = lambda a, b, d: ((a * b) + (a * d) + (d * b)) * 2
P = lambda a, b, d: (a + b + d) * 4

def Culcul():
    try:
        a,b=(float(input("Введите 2 числа "))for i in range(2))
        spisok=["*","+","-","/","//","**","S-площадь","P-периметр","sin","Atan","Hypot","cos","%"]
        for i in range(len(spisok)):
            print(spisok[i],end=", ")
        sw=input("Выберете задание ")
        match sw:
            case "*":
                print("a * b = ",a*b)
            case "/":
                print("a / b = ",a/b)
            case "+":
                print("a + b = ",a+b)
            case "-":
                print("a - b = ",a-b)
            case "//":
                print("a // b = ",a//b)
            case "**":
                print("a ** b = ",a**b)
            case "%":
                print(f"a % b = ",a%b)
            case "P":
                c=float(input("Введите третью сторону "))
                print("Периметр равен ",P(a,b,c) )
            case "S":
                c=float(input("Введите третью сторону "))
                print("Площадь равна ",S(a,b,c))
            case "sin":
                print("Синус a = ",math.sin(a))
                print("Синус b = ",math.sin(b))
            case "Atan":
                print("Арктангенс = ",math.atan2(a,b))
            case "Hypot":
                print("Гипотенуза = ",math.hypot(a,b))
            case "cos":
                print("Косинус a = ",math.cos(a))
                print("Косинус b = ",math.sin(b))
    except Exception:
        print("Что-то введено не так")


def Str():
    try:
        text=input("Введите строку ")
        print("Длина строки ",len(text))
        print("Количество пробелов ", text.count(" "))
        print("Количество запятых ", text.count(","))
    except Exception:
        print("Что-то введено не так")


def Matrix(a,b,c,d):
    try:
        matrix=[]
        for i in range(b):
            matrix.append([])
            for j in range(a):
                matrix[i].append(c)
                c += d
        for i in range(0, b):
            for j in range(0, a):
                print(matrix[i][j], end=' ')
            print("")
    except Exception:
        print("Что-то введено не так")

while True:
    try:
        turner=int(input("Введите номер задания(1-3), 0-выход "))
        match turner:
            case 1:
                Culcul()
            case 2:
                Str()
            case 3:
                a=int(input("кол-во столбцов в матрице "))
                b=int(input("кол-во строк в матрице "))
                c=int(input("начало "))
                d=int(input("шаг "))
                Matrix(a,b,c,d)
            case 0:
                break
    except Exception:
        print("Что-то введено не так")
