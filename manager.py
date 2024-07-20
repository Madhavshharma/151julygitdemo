##----------------module----------------
## to use the code of one file in another file is the module concept 

# manage_name="kishan sharam "
# manager_id="12-edfr"
# manager_pass="hellomanager"
# manager_salary=50000


## employee recoed 
employe_list=["madhav","kirti","harsh","pushpendr","himanshu"] 

asiistance="mahendra"
asiistant_id="harshrathore@gmail.com"
assistant_pass="rathore135"


# if we want to restrict our some part of data that no one can access or copy it in different module
# if __name__=="__main__":  # this code will restrict the part of code
#     # this will only allow to access the data if manager file will be execute other will not allow
    
#     manage_name="kishan sharam "
#     manager_id="12-edfr"
#     manager_pass="hellomanager"
#     manager_salary=50000
#     def manager_data():
#         print(manage_name)
#         print(manager_id)
#         print(manager_salary)
#         print(manager_pass)
     
# def employe_data():
#     print("Your employee list:",employe_list)
#     print("your assistant name ",asiistance)
#     print("your assistant id",asiistant_id)
#     print("your assistant pass",assistant_pass)
        
# function calling 


# employe_data()
# print()
# manager_data()

employee_salary=[23000,45000,12000,5600,70000]
def min_salary(employee_salary):
    mini=employee_salary[0]
    for i in employee_salary:
        if i<=mini:
            mini=i
        return mini

print("the minimum salary is:",min_salary(employee_salary))
          
