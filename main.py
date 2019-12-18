#!/usr/bin/env python3

print("\n******Written By Ani4k-D3V******")
print("\n******Written By Ani4k-D3V******")
import time
def hola():
    while True:
        try:
            global flow
            flow = float(input("Enter First Value : "))
            return 0
        except:
            time.sleep(0.1)
            print("Please Enter Valid Input !")
hola()

def holaTwo():
    while True:
        try:
            global flowTwo
            flowTwo = float(input("Enter Second Value : "))
            return 0
        except:
            time.sleep(0.1)
            print("Please Enter Valid Input !")
holaTwo()


def holaEq():
    while True:
        try:
            global flowEq
            flowEq = str(input("Enter Equation *,/,+,-,% : "))
            if flowEq == "*":
                print("\n",flow * flowTwo)
                return flow * flowTwo
            elif flowEq == "/":
                print("\n",flow / flowTwo)
                return flow / flowTwo
            elif flowEq == "%":
                print("\n",flow % flowTwo)
                return flow % flowTwo
            elif flowEq == "+":
                print("\n",flow + flowTwo)
                return flow + flowTwo
            elif flowEq == "-":
                print("\n",flow - flowTwo)
                return flow - flowTwo
            else:
                print("Please Enter Valid Equation!")
        except:
            time.sleep(0.1)
            print("Please Enter Valid Input !")
holaEq()

