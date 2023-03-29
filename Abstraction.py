# from abc import ABC, abstractmethod


# ## we are creating Human class as abstract class
# class Human(ABC):   # ABC is base class and Human is child class  Helper class that provides a standard way to create an abstraction using inheritance.
#     def __init__(self) -> None: # as soon as obejct gets created and before assing to obejct variable in left side
#         print("Human init")

#     @abstractmethod
#     def speak(self):        # abstract method
#         print("human speak")
#         pass

#     @abstractmethod     #decorator - give special meaning to medhod/class
#     def walk(self):         # abstract method
#         pass

#     def hobby(self):        # class method
#         print("Hobby Human")


# class Dad(Human):       # Inheritance.. Dad class inherited from Human (abstract class).. so we need to define or implement all abtract methods present in Human class
#     def __init__(self) -> None: # as soon as obejct gets created and before assing to obejct variable in left side
#         print("Dad init")

#     def speak(self):        # abstract method
#         print("Speak Hindi")
    
#     def walk(self):         # abstract method
#         print("Fast walk")

#     def hobby(self):        # class method
#         print("Dad hobby")
# dad = Dad() #  # can not creat obbject of class if we dont have impletementation of abstract methods in Dad class #Can't instantiate abstract class Dad with abstract methods speak, walk

# dad.walk()      #Fast walk
# dad.speak()     #Speak Hindi
# dad.hobby()     #Dad hobby
 

# class Mom(Human):
#     def __init__(self) -> None:
#         super().__init__()      #Human init # super points to base class which Human
#         super().speak()
#         print("Mom Init")   #Mom Init

#     def speak(self):        # abstract method
#         print("Speak Hindi")
    
#     def walk(self):         # abstract method
#         print("slow walk")

    


# mom = Mom() # can not creat obbject of class if we dont have impletementation of abstract methods in Dad class #Can't instantiate abstract class Dad with abstract methods speak, walk

# mom.walk()
# mom.speak()
# mom.hobby()

# ##human = Human() #TypeError: Can't instantiate abstract class Human with abstract methods speak, walk
# # we can not create object of abstract class.. means class have atleast one abstract method
# # Abstract class is basically meant for inheritance and contract
# # abstract class can have abstract + non abstract methods
# # Every inheriting class of abstract class has to provide implementation for abstract mehtod other wise class will be incomplete
# # and we can not create object of that class


# # When to use abstract class ?
# # when we want to share common logic across inheriting class alogn with share some contract or standard   

# #we can have contructor inside abstract class however we can not create object
# # to intantiate attribute of abstract class


# # can we call mehtod of abstact class in child class??





