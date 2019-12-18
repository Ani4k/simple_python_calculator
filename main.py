#!/usr/bin/env python3

print("\n******Written By Ani4k-D3V******")

#For Smoothness
import time
def hola():
    while True:
        try:
            #global To Access This Out Side From Def
            global flow
            flow = float(input("Enter First Value : "))
            return 0
        except:
            time.sleep(0.1)
            #if Something Goes Wrong Then!
            print("Please Enter Valid Input !")
hola()

def holaTwo():
    while True:
        try:
            time.sleep(0.1)
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
            time.sleep(0.1)
            global flowEq
            flowEq = str(input("Enter Equation *,/,+,-,% : "))
            if flowEq == "*":
                time.sleep(0.1)
                print("\n",flow * flowTwo)
                return flow * flowTwo
            elif flowEq == "/":
                time.sleep(0.1)
                print("\n",flow / flowTwo)
                return flow / flowTwo
            elif flowEq == "%":
                time.sleep(0.1)
                print("\n",flow % flowTwo)
                return flow % flowTwo
            elif flowEq == "+":
                time.sleep(0.1)
                print("\n",flow + flowTwo)
                return flow + flowTwo
            elif flowEq == "-":
                time.sleep(0.1)
                print("\n",flow - flowTwo)
                return flow - flowTwo
            else:
                time.sleep(0.1)
                print("Please Enter Valid Equation!")
        except:
            time.sleep(0.1)
            print("Please Enter Valid Input !")
holaEq()


