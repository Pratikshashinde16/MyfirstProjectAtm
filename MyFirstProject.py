# my first project using python  
#  atm machine
import random 

print("*****welcome to bank of Maharashtra*******")
chances=3                                                                                #a single person has atleast 3 chances
restart=('y')
balance=50000                                                                            #initiazing the minimum balance 
while chances > 0:                                                                        # the while loop check the chances                                                                   
    restart=('y')                                                                          # if user wants to return then 'y' is used
    pin = int(input("Enter your pin:"))
    if pin==1234:
        print("you have entered your pin correctly\n")
        while restart not in ('no','NO','No','n','N'):
            print("1)BALANCE ENQUIRY:\n")
            print("2)WITHDRAW:\n")
            print("3)CREDIT MONEY:\n")
            print("4)CANCEL TRANSACTION:\n")
            option=int(input("ENTER YOUR CHOICE:\n"))
            if option==1:                                                                   #   it checks the balance and display the  amount number on screen
                amount=f"Your balance is {balance} \n2"
                print(amount)
                restart=input("Would you like to go back:\n")                                  # if person wants to continue over transaction 
                while restart in ('no','NO','No','n','N'):                                     
                    print("Thank you!!")
                    break
            elif option == 2:
                option2=('y')                                                   #it will ask pin
                withdraw1=int(input("enter amount to withdraw:\n"))
                if withdraw1 in range(1,10000):                                 # range function takes any random number between 1 to 10000
                    balance= balance-withdraw1                                  #it will subtract the amount and give the current balance
                    print("Your current balance is {}".format(balance))
                    restart=input("Would you like to restart:\n")
                    if restart in ('no','NO','No','n','N'):
                        print("Thank you!!")
                    break
                elif withdraw1!=range(0,10000):                                  #if the amount is more than 10000 then message will popup 
                    print("You are only allowed 10k at a time")
                    print(" Invalid amount!please try again!!!\n")
                    restart=('y')
                elif  withdraw1==1:
                    withdraw1=int(input("Enter desired amount\n"))

            elif option ==3:
                credit = int(input('Enter money which you want to add\n'))
                balance = balance + credit                                      # it will add current balance +amount enterd in balance
                print('Your balance is = ',balance)
                restart = input('Would you like to go back\n')
                if restart in ['n','no','NO','N','No']:
                    print('Thank you')
                    break

            elif option ==4:
                print("Your transaction is cancelled")
                print("Thank you for your service")
                break
            else:
                print("Please enter correct number:\n")
                restart=("y")
    elif pin!=("1234"):
        print("INcorrect pin\n") 
        chances=chances-1                                      # it will decrement the chances if pin is wrong
        if chances==0:                                                             
            print("Sorry you have already tried 3 times : \n")       # only 3 chances are allocated 
            break            


