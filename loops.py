#a loops is a sequence of instruction that is continually repeated until a certain condition is reached
# there are two types of loops in python:
#1. while loop
#2. for loop
#--------------------------------------------------------------
# WHILE LOOP:
#with the while loop we can exicute a set of statements as long as a condition is true.

# i=1                                # here i is any variable is equal to start no. from 0
# while(i<=100):                       # here we give condition range
#         print(i)                    # it will print 0 to i-1 
#         i +=1                   # increament i value
#---------------------------------------------------------------------------------------

#Pass input from user:

#i= int(input("Enter how many no you want: " ))
# i=0
# while(i<10):
#         i = int(input("enter the number: "))    # here we get input form user 
#         print(i)                                # it will print i till condition is reached
#--------------------------------------------------------------------------------------------
# To print any string multiple times:

# print("hello priya")
# print("hello priya")
# print("hello priya")
# print("hello priya")
# print("hello priya")

# icounter = 5
# while icounter > 0:
#         print("hello priya")
#         icounter = icounter - 1

# icounter = 0
# while icounter < 5:
#         print("hello priya")
#         icounter = icounter + 1        

# alist = [10, 20, 30, 40, 50]               # here we pass list 

# icounter = 0                         
# while icounter <= 4:
#     print(alist[icounter])                # here we pass icounter as an index value to the list alist[0]
#     icounter = icounter + 1 

# #==========================================================================================================

# #                                      FOR LOOP
# #for loop is used for iterating over a sequence
# # with for loop we can exicute list, tuple, dictionary,set and string
# #for loop does not required an indexig variable to set beforehand

# for i in range (0,100):   #syntax of for loop i is any variable in range of (0, n-1), here (0,100)
#      print(i)             # here it print 0 to 99. because n-1. if you want 100 so give (0,101)
# #-----------------------------------------------------------------------------------------------------

# alist = [10,45,30,60,25,55,20]
# for item in alist:    # here alist must be define variable, and item is any variable. instade of item we can use any thing
#         print(item)

# for item in alist:
#         if item % 2 == 0:
#                 print("Even number : ", item)
#         else:
#                 print("Odd number: ", item)
#---------------------------------------------------------------------------------------------

# if pass list in for loop:

# list= ["priya","pooja","asha","komal"]  # here we pass list 
# for item in list:
#     print(item)

list =[["priya", 1], ["pooja", 2], ["asha",3], ["komal",4]]     # here we pass list in list
for item in list:
    print(item)             # the o/p is list 

for item, Id in list:
    print(item,"her id is:", Id)         # here we unpack list 
#---------------------------------------------------------------------------

# if pass dictionary in for loop:

list1 =[["priya", 1], ["pooja", 2], ["asha",3], ["komal",4]]
dict1 = dict(list1)      # here we convert list into dictionary
print(dict1)

# for item in dict1:
#     print(item)                    # here it will print key elements only

for item, Id in dict1.items():      # to print key and value both we use .items() inbuilt function
    print(item, Id)                 # so here we get both key and value in o/p

#--------------------------------------------------------------------------

# for index in range(10):      # here index is any temp variable and range is function. which generate sequense of number automatically
#         print(index)         # o/p - 9 but in range it will print till value n-1 

# for index in range(10, 20,2):   # o/p 10, 12, 14, 16, 18 it will step number after 2, 10 is start index 20 is last index   
#         print(index)

# for index in range(10, 1, -1):
#         print(index)                     # here it will print revers order value




