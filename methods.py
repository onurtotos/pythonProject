"""

Methods or Functions

1) Not returning the value and not taking parameters
2) Not returning the value but taking parameters
3) Returning the values but not taking paramerts
4) Returning the values and taking the parameters


"""

#Creating method for method1
def ayse():
    print("selam")
ayse()

#Creating method for method2
def ayse2(isim,yas):
    print(isim,yas)

ayse2("isim",35)

#Creating method for method3
def ayse3():
    print("merhaba")
    return 25
ayse3()
#If you would like to demonstrate the return value you can put it inside of the print function.
print(ayse3())

#Creating method for method4
def ayse4(ad,puan):
    print(ad,"selam",puan)
    return "ONUR"
ayse4("onur",90)
value=ayse4("elif",80)
print(value)

#Create a method that prints your name 10 times?
def onur1(isim):
    for a in range(10):
        print(isim)
onur1("Onur")

#Create a method that takes a parameter. If the parameter > 50 print:
#you are passed! otherwise print:Failed!
def not1(puan):
    if puan>50:
        print("You are passed",puan)
    else:
        print("You are failed",puan)

not1(80)

#Create a method that takes a parameter. If the parameter>50 print: 10x you are passed
#otherwise print 5 times you are failed.

def onur3(point1):
    if point1>50:
        for x in range(10):
            print("You are passed",point1)
    else:
        b=0
        while b<5:
            print("You are failed!",point1)
            b+=1
onur3(9)


