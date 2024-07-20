#_____________Functions______________
# function is a block of code to perform a specific task 
# execution of function in two parts
# 1.define
# 2.calling of function
# no need to write the code again and again  after creating a function

# there are two types of function in 
# 1. predefind(in  built) ex-> len,append,pop, print
# 2. user defined example-> Madhav()

# syntax of creating a user defined function
# def Functioname 

# ls=[10,20,30,40,50,60]
# def mylength(lm):   # user created length fucntion to find the length of lsit
#     count=0
#     for i in lm:
#         print(i)
#         count=count+1
#     return count

# lm=[20,13,14,56,67]
# print(mylength(lm))


# assignment 
# create Min and Max function

#1
#12
#123
#1234
#12345

#*
#**
#***
#****
#*****

#  Research about Lambda function
 
 
# user defined min funciton   
# def my_min(lst):
#     if lst==None:
#         return None
#     mini=lst[0]
#     for i in lst:
#         if i<=mini:
#            mini=i
#     return mini

lst=[16,13,45,67,89]
# print(mu_min(lst))


def my_max(lst):
    if lst==None:
        return None
    maxii=lst[0]
    for i in lst:
        if i>=maxii:
           maxii=i
    return maxii

print(my_max(lst))






    
    

 