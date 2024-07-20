# in this file we will import the data of manager file

# import manager


# print(manager.asiistant_id)
# print(manager.asiistance)
# print(manager.assistant_pass)


# import manager as mng  # use of alias(as) key word to give the nick name to 


# print(mng.asiistant_id)
# print(mng.asiistance)
# print(mng.assistant_pass) 

# by using import word directly it will share all the data to new file that can create a problem
# so to avoid this we will use from manager import the variable name wewant to import

# from manager import asiistance,assistant_pass,asiistant_id
# print(asiistant_id)
# print(asiistance)
# print(assistant_pass)

# asiistance="saurabh" # overriding the variable
# print(asiistance)

# from manager import manage_name,manager_id,manager_pass
# print(manage_name)
# print(manager_id)
# print(manager_pass)
# print()

# from manager import employe_data
# employe_data()

from manager import employee_salary,min_salary
min_salary(employee_salary)



