# Data Type :- Dictionary 
# we have to store the data in key value pair 
# Every key in Dictionary Should be unique
# the key can be of any data type there is no restricton of string 
# we can also create list and tuple in dictionary 
# particular value can also be access in dictionary by passing its key
# update and isertion of element is available in dictionary


dt={"a": 2,"B":3,"C":4}
# print(dt)
# print(type(dt))
# dt2={0: 2,1:3,2:4}
# print(dt2)
# print(dt2[0])

# dt["E"]=12 # syntax to insert the one more pair in Dictionary and the updation is also similar
# print(dt)
# dt.pop('E') # we can remove a pair from the dictionary using pop function

# dt={"a": 2,"B":3,"C":4}
# print(dt)
# print(dt.keys())
# print(dt.values())

student_marks={"Name": ["madhav","manish","mahesh","harsh"],
               "marks": [20,30,40,14],
               "subject":"science"}



print(student_marks["marks"])
print(student_marks["Name"])
student_marks["Name"].pop() # if we want to update a value in the particular key 
print(student_marks)
student_marks["subject"]="data science"
print(student_marks)









