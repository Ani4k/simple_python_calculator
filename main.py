# ___Aniket-DEV____

print("\n******Written By Aniket-DEV******")

a = input("\nEnter First Number : ")
z = float(a)
b = input("\nEnter Second Number : ")
zz = float(b)
c = input("\nEnter +,-,%,* : ")


def minus():
    print("\n")
    cal1 = print(z - zz)
    return cal1


def plus():
    print("\n")
    cal2 = print(z + zz)
    return cal2


def multi():
    print("\n")
    cal3 = print(z * zz)
    return cal3


def per():
    print("\n")
    cal4 = print(z % zz)
    return cal4


if c == "-":
    minus()

elif c == '+':
    plus()

elif c == '*':
    multi()

elif c == '%':
    per()
else:
    print("\nPlease Input Valid '+,-,*,%'")
