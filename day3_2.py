# Conditional Statement and Type Casting in python 

# use of pass Key word -> to remove the error in case we don write the body of conditional statemnt 
# in this case we use pass key work . also in case of pass key we can use ... dots 

available_amount=2000
task=int(input("Choose any option:-"))

if task >=1 and task <= 3:
    print("welcome to the bank:")
    if task == 1:
    #programme of  check balance
        print("thaks for visiting us,your available amount is :",available_amount)

    elif task == 2:
        #programme of Deposit
        pass
    else :
        pass

else:
    print("please choose right option:")

        