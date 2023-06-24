from oop_roll_on_tables_GLS import RPG_table
import troop_object_settings as s
import logging_tools_GLS as log
import pickle

t = RPG_table(s.TABLE_NAME_DEFAULT)

# class Troops():

#     def __init__(self):
        
#         pass

# class Human(Troops):
    
#     def __init__(self):
#         super().__init__
#         self.race = 'Human'

# program to create class dynamically
  
# constructor
def constructor(self, arg):
    self.constructor_arg = arg
  
# method
def displayMethod(self, arg):
    print(arg)
  
# class method
@classmethod
def classMethod(cls, arg):
    print(arg)



# creating class dynamically
Geekers = type("Geekers", (object, ), {
    # constructor
    "__init__": constructor,
      
    # data members
    "string_attribute": "Geeks 4 geeks !",
    "int_attribute": 1706256,
      
    # member functions
    "func_arg": displayMethod,
    "class_func": classMethod
})


    # creating objects
obj = Geekers("constructor argument")
print(obj.constructor_arg)
print(obj.string_attribute)
print(obj.int_attribute)
obj.func_arg("Geeks for Geeks")
Geekers.class_func("Class Dynamically Created !")


# pickle and unpickle object data

pickled_variable = pickle.dumps(obj)
print(pickled_variable)

obj2 = pickle.loads(pickled_variable)

print(obj2.constructor_arg)
print(obj2.string_attribute)
print(obj2.int_attribute)

# encoding and decoding strings to binary

gls = "Testing String"

gls2 = gls.encode('utf-8')
pickled_variable = pickle.dumps(gls2)
obj3= (gls2.decode('utf-8'))

print (obj3)

