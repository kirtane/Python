#print("hello priya")   # here we just print hello
# #Ctrl + s => save file
# # To run program in terminal type file name.py 
# ## option 1 :  python INT01/FirstProgram.py
# ## option 2 : if file is in another folder then use cd command to change directory
#             # cd INT01
#             # python FirstProgram.py     
# # if you want step out of folder use "cd.."  
# # if you want step in to folder use "cd foldername"
# #---------------------------------------------------------------------------------------------------------------------
# # # is for single line comment
# ## ctrl + /  => multiple lines comment/uncomment
# ## ctrl + k + c   => multiple lines comment
# ## ctrl + k + u   => multiple lines uncomment


# # Developed By : Innovant batch 1
# # Date : 11-Jan-23
# # Purpose : Just first program

# #print("hello")
# # ===========================================================
# # Multiline comment 

# '''Developed By : Innovant batch 1
# Date : 11-Jan-23
# Purpose : Just first program'''
# #=======================================================================================================
# ## Inbuilt module - comes with python installation
#import math         ## importing or including math library/module

# print("hello")      #hello
# print(3.14)         #3.14

#print(math.pi)

# from math import pi     ## importing or including only pi from math library/module
# print(pi)'''
# ##------------------------------------------------------------------------
# '''print("C:\Development\Class\Innovant\Python\INT01")
# ## print folder path of current working directory
# import os

# print(os.getcwd()) '''  # it will display path of current directory

# ##=============================================================================================================
# #                                   VARIABLE:
#variable are just container to store value of any type
# #A variable name can only start with an alphabet and underscore.
# #A variable can’t start with a digit.
# #Variable names are case sensitive 

# a = 10         # Integer   # 10 is value in variable and it is type of Integer so varible will be of smae type; Integer
# a2 = -20       # Integer 

# b = 15.7       # float type
# b2 = -15.7       # float type

# c = '10'       # string 
# c2= "hello"    # string
# c3= '''hello,   
#         How are you doing today?
#         thank you!'''           # string 
# print(c3)

# d = True        #Boolean type, Boolean can contain either True or False 
# d2 = False      #Boolean Type
# ###d3 = true    # error, coz python is case sensitive and t has to captial in True

# e = None        # None type     ## no specific type, unknown    
# print(e)             
# #----------------------------------------------------------------------------------------------
# '''age = 28  # here age is any variable and 28 is value
# print(age)   # here we print age variable having value 28
# is_adult = True # here we pass is_adult as variable it strore boolean value.
#                   # boolean values are true and false only. 
#                   # in boolean ary non false value is always true.
# print(is_adult) '''  # here just print is_adult which is true
# #---------------------------------------------------------------------------------------
# '''print("Priya" + " " + "Kirtane")    # here we use '+' to concate two strings o/p is priya kiratne
# age = 28
# print(age)
# print("is adult = True")
# '''
# #------------------------------------------------------------------------------------
# '''# SIMPLE ADDITION OF TWO NO.
# a = 10
# b = 20
# result = a + b       # here we store addition of two no. in result and simply print result
# print("addition of two no. is : " , result)'''
# #============================================================================================================
# #                                    TYPE:
# a = 10         # Integer   # 10 is value in variable and it is type of Integer so varible will be of smae type; Integer
# print(a)

# tempType = type(a)          ## type() will accept input and provid variable type as output
# print(tempType) #<class 'int'>

# print(type(a))  #<class 'int'>

# b = 16.8
# print(type(b))      #<class 'float'>

# c2 = "Hello"    ## string type

# c2 = 'something'    ## string type

# c3 = '''something
# sdfsdf 
# sdfdfasdf reytw'''    ## string type


# d = True         ###   Boolean type , Boolean can contain True or False only
# d2 = False       ###   Boolean type
# print(d)          #True
# print(type(d))      #<class 'bool'>

# e  = None        ###  None type
# print(type(e))      ## <class 'NoneType'>
# ####=====================================================
# ### inteview ka question????
# temp = 0 
# print(type(temp))        # Int 
# print(temp)              # 0 

# temp = 0.0
# print(type(temp))        # float 
# print(temp)              # 0.0
# #================================================================================================================

# #                                  EXTERNAL MODULE
# # As there are two types of module
# #1)INTERNAL MODULE - which is available in python installtion no need to install 
# #2) EXTERNAL MODULE - it is not avilable in python in built, we have to intall it from out side
# #3) to intall external module there is "pip" command
# # Example :   pip install -U selenium

# # assignment play any mp3 song
# #play song in python
# '''from playsound import playsound           # here i have install playsoun external module and import it
# playsound("E:\\Innovant IT\\music1.wav")''' # here given path of music file

# # /  => top will be tilt towards forward so forward slash
# # \  => top will be tilt towards backward so backward slash
# #=================================================================================================================

# #                                 INPUT FUNCTION:
# # input function is used to get input from user 
# # input function always accept input values as string

# '''name = input("what is your name =")  
# print("hello"+ name)'''

# '''old_age = input("enter your old age")
# #after 2 year what is the age
# new_age = old_age + 2
# print(new_age)'''          # here it will give error because input is always string 
#                         # so string and int never get add, so we have to convert str into int call type casting
# ## type casting used to convert given varibale type into expected variable type
# #int(), float(), str(), bool(), ets are typecasting syntax
# # so here given value is string so for addition we have to convert it into int

# '''old_age = int(input("enter your old age "))
# #after 2 year what is the age
# new_age = old_age + 2
# print("after 2 years your age will be :", new_age)'''

# '''first = int(input("enter 1st no: "))    # here in initial stage we convert str into int
# second = int(input("enter 2nd no: "))
# sum = first + second
# print(f"addition of two no is: {sum}")'''
# #====================================================================================================

# #                                  # Arithmatic operators
# # print(10 + 5)       ## addition = 15
# # print(10 - 5)       ## subtraction = 5
# # print(10 * 5)       ## multiplication = 50
# # print(10 / 5)       ## division = 2
# ##----------------------------------------------
# # a = 10
# # b = 20
# # result = a + b 
# # print(result)   # o/p 30
# ##---------------------------------------------------
# # a = 10
# # b = 20
# # a = a + b       ##in case of  '=' evalution and calculation will happen only at right side and will assign value to left side variable
# # print("a = ", a, " b = ", b)        #a =  30  b =  20
# ##----------------------------------------------------
# # a = 10
# # b = 20
# # a += b    #a = a + b   i.e a= 10+20 , a=30
# # print("a = ", a, " b = ", b)        #a =  30  b =  20
# ##----------------------------------------------------
# # a = 10
# # b = 20
# # a -= b    #a = a - b  # a = 10 - 20 , a = -10
# # # print("a = ", a, " b = ", b)        #a =  -10  b =  20
# ##==========================================================================
# # a = 10
# # b = 20
# # print("a == b ", a == b) #a == b = False it give o/p in boolean. comparision operator
# ##---------------------------------------------------------
# # a = 20
# # b = 20
# # print("a == b ", a == b) #a == b = True
# ##---------------------------------------------------------
# #a = 10
# #b = 20
# #print("a != b ", a != b)       #a is not equal to b which is true
# ##---------------------------------------------------------
# # a = 20
# # b = 20
# # print("a != b ", a != b) #o/p is false
# ##=================================================================

# # a = 20
# # b = 20
# # print("a > b ", a > b) #a > b  = False

# # a = 20
# # b = 20
# # print("a >= b ", a >= b) #a >= b  = True

# # a = 30
# # b = 20
# # print("a > b ", a > b) #a > b  = True
# ##=================================================================

# # a = 20
# # b = 20
# # print("a < b ", a < b) #a < b  = False

# # a = 20
# # b = 20
# # print("a <= b ", a <= b) #a <= b  = True

# # a = 30
# # b = 20
# # print("a < b ", a < b) #a < b  = False
# ##=================================================================

# ## Logical Operators
# ## works with boolean

# # a = True
# # b = True
# # print("a and b ", a and b )    # a and b  True

# # a = True
# # b = False
# # print("a and b ", a and b )    # a and b  False

# # a = False
# # b = False
# # print("a and b ", a and b )    # a and b  False
# ##---------------------------------------------------

# # a = 10
# # b = 20
# # print("a > 10 and b < 20 ", a > 10 and b < 20)    # a and b  False
# # print("a > 10 and b <= 20 ", a > 10 and b <= 20)    # a and b  False
# # print("a >= 10 and b <= 20 ", a >= 10 and b <= 20)    # a and b  True
# ##==============================================================

# # a = True
# # b = True
# # print("a or b ", a or b )    # a or b  True

# # a = True
# # b = False
# # print("a or b ", a or b )    # a or b  True

# # a = False
# # b = False
# # print("a or b ", a or b )    # a or b  False
# ##---------------------------------------------------

# # a = 10
# # b = 20
# # print("a > 10 or b < 20 ", a > 10 or b < 20)    # a > 10 or b < 20  False
# # print("a > 10 or b <= 20 ", a > 10 or b <= 20)    # a > 10 or b <= 20  True
# # print("a >= 10 or b <= 20 ", a >= 10 or b <= 20)    # a >= 10 or b <= 20  True
# ##========================================================================

# # Logical operator always consider any non False value as TRUE
# # Only false written given then take it as false

# # a = 10          ## 10 will be consider as True
# # b = 20          ## 20 will be consider as True
# # print("a and b ", a and b )    # a and b  20
# # print("a or b ", a or b )    # a or b  10
# ## ===============================================================

# # a = True
# # b = False
# # #####print("a not", a not )    # wrong in syntax to use not
# # print("a not", not a)    # a not False 
# # print("b not", not b)    # a not True
# #==========================================================================================================

# # VVVVVVV IMP  ASSIGNMNET 
# #SWAPPING OF TWO NUMBERS ------- DONE IN ASSIGNMENT FILE
# #==========================================================================================================

#                              STRING SLICING

# A string in Python can be sliced for getting a part of the string.
#To fetch any substring/word from string you have to provid indexing. indexing always starts from "0"
#index no. always given in [] brackets
# To find length of any string we use "len function"

# avalue = "Welcome"
# print(avalue)
# print(avalue[0])               # here o/p will 0th index word 'W'
# print(avalue[2])               # o/p will  
# #print(avalue[7])              # here error will came "index out of range" because it contail index from 0 to 6
# print(len(avalue)-1)           # here o/p is 6 which is lengths of string 7-1=6
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
# print(avalue[-7:-1])             # here o/p is wlcom
# print(avalue[-7:])               # here o/p is welcome passing only "index :" it will print complete string from that index
# print(avalue[0:])                # here also o/p is wlcome
# print(avalue[:3])                # o/p is wel 1st index it will consider as 0
# print(avalue[:])                 # here we dont pass any index it will take default index 0
#---------------------------------------------------------------------------------

avalue = "Welcome"
# print(avalue[0:7])                 # o/p is welcome
# print(avalue[0:7:1])               # o/p is welcome
# print(avalue[0:7:2])               # o/p is wloe. alternate words will print
# print(avalue[0:7:3])               # o/p is wce
#=================================================================================================
#                               ASIGNMENT TO REVERSE STRING

string = "Hello \n \t how are you doing?"
strlen = len(string)                   # here it store the length of given string
#print(strlen)
for item in string:
    print(strlen)                       # here we simply print length of string to understand
    print(string[strlen-1])             # here we get last index of string and simply print it
    strlen -=1                          # here we drcrese the counter of strlen 
#===================================================================================================================

#

