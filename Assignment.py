#ASSIGNMENT 1      DATE- 11/01/2023
#DISPLAY Table of 10

#First way to display
'''print(10*1)
print(10*2)
print(10*3)
print(10*4)
print(10*5)
print(10*6)
print(10*7)
print(10*8)
print(10*9)
print(10*10)'''

#2nd way to display
'''print(10*1,10*2,10*3,10*4,10*5,10*6,10*7,10*8,10*9,10*10)'''
#--------------------------------------------------------------------------------------------------
# ASSIGNMENT 2        DATE- 11/01/2023

#play song in python
'''from playsound import playsound 
#playsound("E:\\Innovant IT\\music1.wav")'''

#play video in python
'''import os
os.startfile("E:/photos/priya moble backup/video1.mp4")'''
#----------------------------------------------------------------------------------------------------

#ASSIGNMENT 3          DATE - 12/03/2023

#1. Write a program to print * or # pattern in python.
#
##
###
####
#####
# 1st way
#a = '''#
       #
       ##
       ###
       ####
       #####'''
#print(a)      

# 2nd way
'''a = "#"
print(1*a)
print(2*a)
print(3*a)
print(4*a)
print(5*a)'''
#--------------------------------------------------------------------------------------------------
#ASSIGNMENT 4              DATE : 13/01/2023

#a=20
#b=30
#Write a program to swap values inside variables
# 1) Using third variable
'''a = 20
b = 30
c = a
a = b
b = c
print("a =",a, ",",  "b =",b)
print(f"a={a} b= {b}")'''

# 2) Without any third variable
'''a = input(int("a ="))
b = input(int("b ="))
print("swapping output is  a =", a and b, ",", "b =", a or b )'''

# 3 rd way
'''a=a+b
b=a-b
a=a-b'''

#4rth way
'''a=20
b=30
a, b = b, a
print(a,b)'''
#=====================================================================================================
#                                 PRACTICE SET 2
# 1)Write a python program to print the contents of a directory using os module.Search online for the function which does that.
'''import os
path = "E:\\Innovant IT"
dirlist = os.listdir(path)
print(f"content in directory = {dirlist}")'''

# 2) Already done in assignment 2

# 3)Write a Python program to add two numbers.

#====================================================================================================
#      ASSIGNMENT 5           DATE :15/01/2023
'''avalue = 123456
print(avalue % 10)        # will print last digit from % module
print(int(avalue/10))'''

#=====================================================================================================
#      ASSIGNMENT 6           DATE: 17/01/2023

'''avalue ="welcome"
result = avalue.replace('come','done').replace('done','played').upper()                             # fiding 2nd e in string 
print(f" replace 'come' with 'done' in{avalue}: {result}")'''

'''result = avalue.find("e")
print(f"index position of 1st 'e' of{avalue} = {result}")'''

'''result =  avalue.find("e",2)'''

'''avalue = "saurabh is a intelligent boy"
result = avalue.replace('saurabh','sawan').replace('intelligent','hardworking').capitalize()
print(f"replacing output of {avalue} = {result}")'''
#=====================================================================================================
#                                   PRACTICE SET                  DTAE: 17/01/2023

# 1)Write program to detect double spaces in a string. (count of double space or count of any char)
'''avalue = "Hello  Priya"
result = avalue.find(" ")
print(f"Double space is given in index no. = {result}")'''
'''result = avalue.count(" ")
print(f"count of double is = {result} ")'''
#-------------------------------------------------------------------------------------------------
# 2)Write a program to format the following letter using escape sequence characters.
#Dear  Candidate, 
	#We are delight to inform you that you have cleared all rounds of interview and we are extending offer to join us.
#Thank you,
#HR

'''print("Dear Candidate, \n \t we are delight to inform you have cleared all rounds of interview and we are extending offer to join us. \n thank you, \n HR")'''
#-----------------------------------------------------------------------------------------------------
# 3)From above solution (2) replace ‘Candidate’ with your name and HR name with some other name. By using some string operation function

'''avalue = ("Dear Candidate, \n \t we are delight to inform you have cleared all rounds of interview and we are extending offer to join us. \n thank you, \n HR")
result = avalue.replace('Candidate','Priya').replace('HR','Namrata')
print(f"replace output is =\n {result}")'''
#---------------------------------------------------------------------------------------------------
# 4)Replace the double spaces from problem 3 with single spaces.
'''avalue = "Hello  Priya"
result = avalue.replace('  ',' ')
print(f"replace {avalue} is = {result}")'''
#==========================================================================================================
#     ASSIGNMENT 7                                    DATE : 24/01/2023

## 1. take input from user and print numbers till given number
## 2. take input from user and print all even number till given number
## 3. take input from user and print all odd number till given number

'''avalue= int(input("Enter the number you wants to display ="))
while avalue > 0:
       c=avalue/2 
       if (c == int(c)):
              print(f"It is Even number = {avalue}")
       else :
              print(f"It is Odd number = {avalue}")    # here all values get printed in descending order
       avalue = avalue - 1'''

avalue= int(input("Enter the number you wants to display ="))
bvalue = 0
while bvalue <= avalue:
       c=bvalue/2 
       if (c == int(c)):
              print(f"It is Even number = {bvalue}")
       else :
              print(f"It is Odd number = {bvalue}")     # here all value get printed in ascending order
       bvalue = bvalue + 1
#-----------------------------------------------------------------------------------------------------
#         ASSIGNMENT                                    DATE : 1/2/2023
## Interview program recently asked 4 days back
#string = "i7n3no8va9nt"
#reverse string by using while loop 
## digit position should not get changed.. without changing digit location only reverse character inside string 
## string = "t7n3av8on9ni"
## if digit then increment or decrement counter
## swap only if both are char and not digit
string = "i7n3no8va9nt4"
liststring = list(string)
lower = 0
upper = len(string)-1
while lower<upper:
        if not liststring[lower].isalpha():
                lower+=1
        elif not liststring[upper].isalpha():
                upper-=1
        else:
                liststring[lower],liststring[upper] = liststring[upper],liststring[lower]
                lower+=1
                upper-=1
strop=' '.join(liststring)
print(strop)

print("hello")


