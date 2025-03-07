


def addition():
    num1 = int(input("Enter the 1st Numner = "))
    num2 = int(input("Enter the 2nd Numner = "))
    sum = num1 + num2
    print("Sum of {0} and {1} is {2}".format(num1,num2,sum))



def sqrt_method():
        num = int(input("Enter the Numebr = "))
        num_sqrt = num**0.5
        print("The Square Root of %0.3f is %0.3f"%(num,num_sqrt))

        
def negativeOrPositive():
    while True:
        num = int(input("Enter the Numebr = "))
        if num > 0:
            print('Positive Number')
        elif num == 0:
            print('Number is Zero')
        else:
            print('Negative Numbers')

        
def oddOrEven():    
    num = int(input("Enter the Numebr = "))
    if (num %2) == 0:
        print('{0} is even'.format(num))
    else:
        print('{0} is Odd'.format(num))
        

def multTable():
  
        num = int(input("Enter the Numebr = "))
        for i in range(1,11):
            print(num,'X',i,'=',num*i)
         
def looping(method):
        while True:
            method()
            print('______________________')
            choice  = input("I U Want to Continoue, type 1 or exit press 0 =  ")
            if choice == '0':
                break
        
#sqrt_method()

#negativeOrPositive()



def program(op):
    if op == 1:
        looping(addition)
    elif op == 2:
        looping(sqrt_method)
    elif op == 3:
        looping(negativeOrPositive)
    elif op == 4:
        looping(oddOrEven)
    elif op == 5:
        looping(multTable)
    else:
        print("no methd from your Choice")
        

while True:
     print('For Addition, Enter 1')
     print('For SQRT ,Enter 2')
     print('For Positive or Negative, Number Enter 3')
     print('For Odd or Even, Number Enter 4')
     print('For Multiplication table, Enter 5')
     print('---------------------------------------')
     option = int(input("Enter the Option = "));
     print('---------------------------------------')
     program(option)

         
