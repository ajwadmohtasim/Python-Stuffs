from sys import argv
from itertools import count, accumulate, takewhile
import re

#main.py

print ("""Hello There! This is my PYTHON LEARNING COMPILATION project.
Here, I am gonna Compile all the stuffs I learnt so far! Take a sit and enjoy XD.

######################################################################
\n
\n
""")

###############  Section 1: String, Variable  ###############

prompt = '> ' #show's ">" before giving input

print("""
Part-1: String and Variable
\n
""")
print("#print(\"Hellow World\")   <- String\n")
print("#Setting up variable by getting input();")

#setting up with name and age
print("What's Your Name?", end = ' ') #tell's not to end the line and go to the next line.
name = input(prompt)
print("What's your age?      (Note: Age must be less than 40)")
age = int(input(prompt))
print(f"So, You are {name} and you're {age}")

#setting up on when he will turn 40
agelimit = 40
ageleft = agelimit - age
print(f"You need more {ageleft} years to turn 40\n")

#String Function
print("String Function:", end=' ')
print(":".join(["Apple", "Banana", "Mango"]))
#setting up with .format
formattter = "{} {} {}"
print("#Trying with .format:\n")
print(formattter.format(1, 2, 3, 4)) ##NEED TO KNOW##
print(formattter.format(formattter,formattter,formattter))

#Tuple
thistuple = ("apple", "banana", "cherry")
print("This is a Tuple: ", thistuple)

print("\nEnd of Part-1v.\n\n")
print("######################################################################")

#setting up with argv

###############  Section 2: If, Else, Elif, List, Sets, Dictionaries, Range, Bools, While loops, Tuples, Arrays  ###############
print("""
Part-2: If Else Statements, Lists , Sets, Dictionaries, Range, Bools, While loops, Tuples, Arrays
\n
""")


#If Else
print("#Intro to If Else:\n")

#Giving Age-Status according to age with If Else and Elif
if age >= 18:
    print(f"You are an Adult!, Since you are {age}")
elif age <= 18 and age >= 13:
    print(f"You're a teenager, Since you are {age}")
else:
    print(f"You are a child..., since you are {age}")




#Intro to list
print("\n#Intro to List:\n")
names = [name, "Jhon", "Albert"]
print("A name list: " , names)
print("Adding Toran to list:")
names.append("Toran")
print("After adding \"Toran\" to list: ", names)

#checking if name is present in list
print("Is your Name present in the list? (Bool) :", name in names) #Bool

#List Slicing
slice_list = [0 , 100, 200, 300, 400, 500 ,600 ,700]
print("List Slice: ", slice_list[1:5:1])

#List Comprehenstion
comprehension_list = [x**2 for x in range(10) if x**2 % 2 ==0]
print("List Comprehenstion: ", comprehension_list)

#Other List Stuffs
print("How many names are there in the list? :", len(names))
print("Let's add another name to 1st Index.")
names.insert(0, "Harbor")
print("After adding \"Harbor\":", names)
print("Index of your name now is: ", names.index(name))

#Intro to sets
print("\nIntro to sets:\n")
test_set = {"apple", "banana", "cherry"}
#test_set.add(1, "mango")
print("This are some name is a set: " , test_set)

#a small list programme: (A problem from Automate the boring stuff with python)
catNames = []
while True:
    print("Enter the name of cat " + 
          str(len(catNames) + 1) +
          "(or do nothing to stop) : ", end='')
    
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #list concatenation
print('The cat names are: ')
for name in catNames:
    print(' ' + name)




#Intro to Arrays
cars_a = ["Ford", "Volvo", "BMW"] 
print("Arrays: ", cars_a)

#Intro to Dictionaries
print("\nIntro to Dictionaries\n")
Car_detail =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(Car_detail)

#Intro to Range
print("\nIntro to Range:\n")
range_numbers = list(range(1,20,2))
print("Range Numbers from 1 - 19 , jumping 2 numbers each :" , range_numbers)

#Intro To For Loops
print("\nIntro To For and While Loops:\n")
print("All the names in the list printed with for loop:")
for Xname in names:
    print(Xname)
print("All the names in the Sets printed with for loop:")    
for Xset in test_set:
      print(Xset)     

print("0-3 printed with while loop:")

while_test = 0
while (while_test <= 3):
    print(while_test)
    while_test+=1


print("\nEnd of Part-2.\n\n")    
print("######################################################################")    
###############  Section-3: Function, Lambdas and others  ###############
print("""
Part-3: Function, Lambdas
\n
""")

#Intro to Function
print("\nIntro to Fuction:\n")
def test_function(fname, lname, food):
      print(fname + " " + lname)
      for Xfruits in food:
        print(Xfruits) #from test_set

test_function("Ajwad", "Mohtasim", test_set)

#Intro to Lamda
print("\n Intro to Lamda:\n")
def lamda(n):
    return lambda a : a * n
mytripler = lamda(3)
print("Value getting by 3*11 through Lamda: ", mytripler(11))

#Map
def add_map(map_add):
    return map_add+2
map_list = [10, 20, 30, 40, 50]
map_result = list(map(add_map,map_list))
print("Result1: ", map_result)
#another method:
map_result2 = list(map(lambda add_map2: add_map2*2, map_list))
print("Result2: ", map_result2)

#Filter
new_filter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def test_filter():
    resutl_filter = list(filter(lambda fil_x: fil_x % 2 == 0, new_filter))
    return resutl_filter
re_filter = test_filter()
print("Filter: ", re_filter)

#Generators
print("Generator: ")
def new_generator():
    g_counter = 0
    while g_counter < 5:
        yield g_counter
        g_counter += 1
new_gen = new_generator()
print(new_gen)

def new_generator2(gen_x):
    for gen_num in range(gen_x):
        if gen_num % 2 == 0:
            yield gen_num
print(list(new_generator2(20)))

#Recursion

def factorial(x_fac):
    if(x_fac == 1):
        return 1
    else:
        return x_fac*(factorial(x_fac-1))
fac_result = factorial(5)
print("Recursion: ", fac_result)

###############  Section-4: OOP Programming  ###############
print("""
Part-3: OOP Programming
\n
""")

#Class
print("#Class: ")
class Species:
    dwelling = "Earth"
    __hidden_var = "Hidden Bruh!"
    def __init__(self, s_age, species,country):
        self.s_age = s_age
        self.species = species
        self.country = country
        
    def _country(self):
        self.country = "Bangladesh"
        
    def _country2(self, country):
        self.country = country
        print(self.country)
        
    def _info(self):
        print(f"I am a {self.species}, I am {self.s_age}, my country is {self.country}!")
         
species_class = Species(40, "Human", "America")
print("Class: ", species_class.s_age, ":", species_class.species,)
species_class._country()
print(species_class.country)
species_class._info()
species_class._country2("Arabia")

#Class_2
class Student:
    
    def __init__(self, st_name, st_age):
        self.st_name = st_name
        self.st_age = st_age
        
    def get_st_info(self):
        self.st_name = input("Enter Name :")
        self.st_age = int(input("Enter Age :"))
    def print_info(self):
        print(f"Student: {self.st_name}, age: {self.st_age}")
student_class = Student(name, age)
print("1st: ")
student_class.print_info()
student_class.get_st_info()
print("2nd: ");
student_class.print_info

class ScienceStudent(Student):
    
    def science(self):
        print("You are in Science group!")
sci_st = ScienceStudent("Toran", 18)
sci_st.science()
sci_st.print_info()

class Point:
    def __init__(self, x_point, y_point):
        self.x_point = x_point
        self.y_point = y_point
        
    def __add__(self, other_p):
        x_other = self.x_point + other_p
        y_other = self.y_point + other_p
        return other_p(x_other, y_other)

    def __str__(self):
        return "({0},{1})".format(self.x_point, self)
point1 = Point(1, 4)
point2 = Point(2, 8)
print("Class_Point: ", point1 + point2)
        

#Itertools
print("Itertools: ")
for itertools_test in count(3):
    print(itertools_test)
    
    if itertools_test >= 5:
        break  
iter_numbers = list(accumulate(range(5)))
print("Accumulate: ", iter_numbers)
print("Takewhile: ", list(takewhile(lambda takewhile_x: takewhile_x <= 10, iter_numbers)))


#Regular Expressions
print("Regular Expression: ")

r_pattern = r"hihihi"

print("Say hi!: ")
get_r_p = input()

#re.match()
if re.match(r_pattern, get_r_p):
    print("Match found")
else:
    print("No match found")
    
#re.search()
if re.search(r_pattern, get_r_p):
    print("Match found")
else:
    print("No match found")
    
#re.findall()
print(re.findall(r_pattern, get_r_p))

#re.sub()
re_s = "This is John"
re_sp = r"John"
new_re_s = re.sub(re_sp, "Rob", re_s)
print(new_re_s)

#

#

    



###############  <something>  ###############

##STUFFS:
# 1.Numeric Functions