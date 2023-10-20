# File: <Pet Class>
# Description: <It can use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.>
# Assignment Name and Number:1. Pet Class
#
# Name: <Vincent Chen>
# GitHub: <https://github.com/chenshangxian/pythoncoding>
#
# On my honor, <Vincent Chen>, this programming assignment is my own work
# and I have not provided this code to any other student.
class Pet:
    def __init__(self,name,animal_type,age):
        self.__name=name
        self.__animal_type=animal_type
        self.__age=age
    def set_name(self,name):
        self.__name=name
    def set_animal_type(self,animal_type):
        self.__animal_type=animal_type
    def set_age(self,age):
        self.__age=age
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type 
    def get_age(self):
        return self.__age
def create():
    ss=Pet("","",0)
    name=input("Please input the name:")
    type=input("Please input the type:")
    age=int(input("Please input the age:"))
    ss=Pet(name,type,age)
    print("name=",ss.get_name())
    print("type=",ss.get_animal_type())
    print("age=",ss.get_age())
create()


        
        
        
        

