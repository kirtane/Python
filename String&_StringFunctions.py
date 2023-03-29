#                                                   STRING SLICING

# A string in Python can be sliced for getting a part of the string.
# To fetch any substring/word from string you have to provid indexing. indexing always starts from "0"
# index no. always given in [] brackets
# To find length of any string we use "len function"

# avalue = "Welcome"
# print(avalue)
# print(avalue[0])               # here o/p will 0th index word 'W'
# print(avalue[2])               # o/p will  
# print(avalue[7])              # here error will came "index out of range" because it contail index from 0 to 6
# print(len(avalue)-1)           # here o/p is 6 which is lengths of string 7-1=6 to find last index
# strlen = len(avalue)
# print(avalue[strlen-1])        # o/p is 'e' last index will be always len - 1
#--------------------------------------------------------------------------------------------

# avalue = "Welcome"
# print(avalue[0:2])             # here o/p will 'We'
# print(avalue[3:6])             # here o/p will 'com' [3 is index : 6 is length ]
# print(avalue[3:7])             # here o/p will 'come'
# print(avalue[0:7])             # here o/p will 'Welcome'
#------------------------------------------------------------------------------------------------

# avalue = "Welcome"
# print(avalue[-1:-7])             # here o/p is empty string
# print(avalue[0:6])               # here o/p is wlcom ([-7:-1]) logic behind it ([7,-7 : 7,-1 ])
# print(avalue[-7:])               # here o/p is welcome passing only "index :" it will print complete string from that index
# print(avalue[0:])                # here also o/p is wlcome
# print(avalue[:3])                # o/p is wel 1st index it will consider as 0
# print(avalue[:])                 # here we dont pass any index it will take default index 0
#-------------------------------------------------------------------------------------------------

#avalue = "Welcome"
# print(avalue[0:7])                 # o/p is welcome
# print(avalue[0:7:1])               # o/p is welcome
# print(avalue[0:7:2])               # o/p is wloe. alternate words will print
# print(avalue[0:7:3])               # o/p is wce
#=================================================================================================
#                               ASIGNMENT TO REVERSE STRING

# string = "Hello \n \t how are you doing?"
# strlen = len(string)                   # here it store the length of given string
# #print(strlen)
# for item in string:
#     #print(strlen)                       # here we simply print length of string to understand
#     print(string[strlen-1])             # here we get last index of string and simply print it
#     strlen -=1                          # here we drcrese the counter of strlen 
#-------------------------------------------------------------------------------------------------------------------

##Q. Check if a string contains a specific sbustring
#'In' operator will return 'ture' if a string contains a substring

print('priya' in 'priyanka')
print('savan' in 'saurabh')
print('ka' in 'priyanka')


#========================================================================================================================
#                                             STRING FUNCTIONS

# Python has inbuilt method that we can use on string operations
# All string methods returns new values they do not change original string
#------------------------------------------------------------------------------------
# 1) len function : is common in all to find length of unknown string

avalue = "Welcome"
#print(f"the lenghth of string is: {len(avalue)}")
#------------------------------------------------------------------------------------

#2) startswhith Function: 


result = avalue.startswith('W')         # here o/p is true (bool) it check string start with W or not
print(f"{avalue} startwith : {result}")

result = avalue.startswith('w')         # here o/p is false (bool). here we pass w. so it is case sensitive
print(f"{avalue} startwith : {result}")
#------------------------------------------------------------------------------------------------

#3)Endswith function: 

# result = avalue.endswith('e')
# print(f"{avalue} endwith : {result}")   ## here o/p is true (bool) it check string start with e or not

# result = avalue.endswith('E')         # here o/p is false (bool). here we pass E. so it is case sensitive
# print(f"{avalue} endwith : {result}")
#------------------------------------------------------------------------------------------------------

#4) capitlization: it will capital only 1st letter

# result = avalue.capitalize()
# print(f"{avalue} Capitalization: {result}")
#-----------------------------------------------------------------------------------------------------

#5) Upper function : it will write string in upper case

# result = avalue.upper()
# print(f"{avalue} In Upper case : {result}")
#------------------------------------------------------------------------------------------------------

#6) Lower function : it will write string in lower case

# result= avalue.lower()
# print(f"{avalue} in lower case : {result}")
#----------------------------------------------------------------------------------------------------

# 7) Find Function : it will return index value of substring where it starts

# avalue = "welcome"
# result = avalue.find('co')
# print(f"the index of co is : {result}")    # here index of 'co' is 3

# result = avalue.find('Co')
# print(f"the index of co is : {result}")    # here we pass capital "Co" so it show index as -1

result = avalue.find('co',2)   # here we can pass 2 as satrting index from where we have to search string
# it is useful when we know tentative where that search will find so its easy to check to reduse time to find
print(f"index of co is : {result}")

result = avalue.find("l", 2,4)  # here we pass staring index and ending index as 2 and 4 
print(f"index of l is : {result}")

# result = avalue.find('e', 2)   # o/p is 6. 
# print(f"index if e in : {result}")
#----------------------------------------------------------------------------------------------------

# 8) Index function : it will return index value of substring where it starts. like as find but slightly diffrence between them is 
# find returns (-1) if sub string not found and index throw (value error).

print('fastest option is plane'.index('plane'))     # o/p is 18
#print('fastest option is plane'.index('car'))       # It will throw value error
#-----------------------------------------------------------------------------------------------------------

#9) rstrip : this helps in removal of trailling charactors
 
element = "hello!!!" 
print(element.rstrip('!'))
#--------------------------------------------------------------------------------------------------------

#10) split : it splits the given string and returns the seperated string as list item

print(avalue.split()) 

step = "I am disco dancer"
print(step.split()) 

print(avalue.replace)








