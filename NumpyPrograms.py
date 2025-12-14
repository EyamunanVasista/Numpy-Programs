import numpy as np

data structure : list , tuple  , dictionary , set

data types : int float bool str

set : A set is a collection of unique and unordered elements.

1. no index / position
2. elements are immutable  (cannot be changed)
3. no duplicates

1.Union : combines all the elements
A | B or A.union(B)
2. intersection : elements common to both the sets
A & B or A.intersection(B)
3. Difference : Elements in one set which are not in the other set
A - B or A.difference(B)
4. symmetric difference

A ^ B or A.symmetric_difference(B)

set = {1,2,3,4}
seet = {4,5,6,7}
print(set|seet)
print(set&seet)
print(set-seet)
print(set^seet)


set.add(67)
print(set)
set.update([67,69,1000000000000000000])
print(set)
set.remove(4)
print(set)
set.discard(1)
print(set)
set.clear()
print(set)

name = 'Bob'
print(f"Hi {name} , welcome to the class") # formatted strings
hw
create a set with diff dtypes , print the values and its dtypes

s = {1,6.7,"hello",True}
for i in s:
    print(f"data type of {i} is {type(i)}")


OOP : Object Oriented Programming
programming concepts that revolve around real world entities


Class and Objects

Class : blueprint/template
Objects : instance of the class

Class :
1. attributes
2. methods / functions


Car
attributes : color,make,fuel type,brand, model, engine
functions : Driving,racing, drifting

laptop
att : cpu,color, gpu, scree size, camera , core , RAM , storage
functions : typing, coding, gaming, watching videos / movies etc.,




Zomato : ordering food

restaraunt
chef
waiters
delivery people
customers
food


class Fan:

    def __init__(self,color,speed,no_of_blades):
        self.no_of_blades = no_of_blades
        self.color = color
        self.speed = speed

    def recipt(self):
        print(f"color is {self.color}\nspeed is {self.speed} \nnumber of blades is {self.no_of_blades}")

fan  = Fan("red","69",4)
fan.recipt()

class Bank:
  def __init__(self,name,accnt_number,balance):
    self.name = name
    self.accnt_number = accnt_number
    self.balance = balance


  def details(self):
    print(f"Account details:\nName:{self.name}\nAccount number:{self.accnt_number}\nCurrent balance:{self.balance}")

  def withdraw(self,amount):
      if amount < 0:
          print("Invalid")
      elif amount > self.balance:
          print("Balance insufficient")
      else:
          self.balance -= amount
          print(f"amount withdrawn : {amount}\ncurrent balance : {self.balance}")

  def deposit(self,amount):
      if amount < 0:
          print("Invalid")
      else:
        self.balance += amount
        print(f"amount deposited : {amount}\ncurrent balance : {self.balance}")



cust1 = Bank("Alice",18473,1000)

cust1.details()
amountW = int(input("enter amount to be withdrawn : "))
cust1.withdraw(amountW)
amountD = int(input("enter amount to deposit : "))
cust1.deposit(amountD)

NUMPY
|
|
↓

ar = np.array([4.2,2.6,0.1,6.7,7.5,6.9,.9],dtype="float16")
ar = np.array([1,2,3,4,5,6,7],dtype = "int8")
print(ar)
print(type(ar))
print(ar.dtype)
print(ar.size)
print(ar.shape)
print(ar.nbytes)
hw : create a numpy array with all float values and print the dtype,shape,size and nbytes info
a = np.arange(10,0,-1)
print(a)
b = np.zeros(100)
print(b)
c = np.ones(101)
print(c)
d = np.full(69,67)
print(d)
int + float = float
int + bool = bool
int + str

ar = np.linspace(0,100,75)
print(ar)

ar = np.random.randint(0,101,69)
print(ar)

ar = np.random.rand(69)
print(ar)

ar = np.repeat((1,2,3,4,5,6,7,8,9,0),10)
print(ar)

ar = np.tile((1,2,3,4,5,6,7,8,9,0),10)
print(ar)

ar = np.tile({1,2,3,4,5,6,7,8,9,0},10)
print(ar)

random.rand() : generates random float value between 0 to 1


repeat(num,n) : repeats the num , n times

full(n,num) : repeats the num , n times


shuffle() : modifies the order of the original numpy array

np.random.permutation() : makes a copy of the shuffled array

ar = np.array([1,2,3,4,5,6])
np.random.shuffle(ar)
print(ar)

a = np.random.permutation(ar)
print(a)

ar = np.array([1,2,3,4,5,6,7,8,9,0])

a = np.random.choice(ar)
print(a)

# a = np.random.choice(ar,size = 10,replace = 0)
# print(a)
var = "hiii"
print(var.upper())
print(var.lower())

a = ["h","e","l","l","o"]
w = ''.join(a)
print(w)

w = 'hello'.join(a)
print(w)

#password generator

def Password_Generator(strength):
    letter = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    num = list('1234567890')
    spec_chr = list('!#$%^&*')

    password1 = [np.random.choice(letter),np.random.choice(num),np.random.choice(spec_chr)]
    password1 = ''.join(password1)

    total = np.array(letter+num+spec_chr)

    rempass = list(np.random.choice(total,size = strength - 3,replace = True))
    rempass = ''.join(rempass)

    NewPassword = password1 + rempass


    return NewPassword

val = int(input("enter no of digits : "))
print(f"New password is{Password_Generator(val)}"   )

name = input("Enter your name")
name = name.strip().capitalize()
username = name[0:5]
# print(username)
adj_list = ["TheGreat","TheFast","TheAmazing","TheGray","iscool", "isfast", "isbright", "issilent", "ishappy", "issmart", "iswild", "isbold"]
symbol_list= ['.','_','-','']
adj = np.random.choice(adj_list)
symb = np.random.choice(symbol_list)
num = str(np.random.randint(100,999))
username = username + adj + symb + num
print(username)

hw : create an email generator
1. get the name and domain from the user
2. display the generated email

eg : Name : Alice , domain : yahoo
output : alice123@yahoo.com

name = input("enter your name")
fname = name + str(np.random.randint(100,999))
domain = input("enter domain")
address = fname + "@" + domain + ".com"
print(address)

sorting : arranging the values in an order asc,desc

sorted() : built in python function

np.sort() : works only on numpy arrays

arr.sort() : in place sorting (modifies the original)

l = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()")
for i in l:
    print(ord(i))

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(a)
print(a.shape)
print(a.ndim)
print(a.size)

b = np.zeros((6,7))
c = np.ones((6,7))

print(b)
print(c)

#filtering the values

arr = np.array([10,-5,-4,20,-44,10,20])

print(arr >= 0)
print(arr[arr >= 0])

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(a[a % 2 != 0])

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(a[(a % 2 != 0) & (a > 10)])
print(a[(a % 2 != 0) | (a > 10)])
print(a[~(a % 2 != 0) & ~(a > 10)])
print(a[~(a % 2 != 0) | ~(a > 10)])

a = np.array(['hi,hie,hiie,hiiie,hiiiie'])
print(a[np.char.startswith(a,"h") & np.char.endswith(a,"e")])

b = input("enter the domain") + ".com"
a = np.array(["ali@gmail.com", "john@yahoo.com", "mary@gmail.com", "zara@outlook.com"])
#
# print(a[np.char.endswith(a,b)])
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
a[a > 15] = 69
print(a)

a = np.array([
     [1,2,3],
     [4,5,6],
     [7,8,9]
 ])

a[a > 5] = 67
print(a)

e = np.array(["bob","bill","you","me"])
s = np.array([1,2,3,4])
print(s[s > 2])
print(e[s > 2])

homework

employees = np.array(["Ali", "John", "Mary", "Sara", "Kumar"])
dept      = np.array(["HR", "IT", "IT", "Finance", "IT"])
salaries  = np.array([45000, 76000, 82000, 50000, 79000])

filter all the employees from the IT department whose salary is above 60000 (included)

homework

1 1 1 1 1 1 1 1 1
1 2 2 2 2 2 2 2 1
1 2 3 3 3 3 3 2 1
1 2 3 3 3 3 3 2 1
1 2 3 3 3 3 3 2 1
1 2 3 3 3 3 3 2 1
1 2 2 2 2 2 2 2 1
1 1 1 1 1 1 1 1 1

a = np.ones((8,9), dtype = int)
a[1:7,1:8] = 2
a[2:6,2:7] = 3
print(a)


a = np.array([
    [

        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        [10,11,12],
        [13,14,15],
        [16,17,18]
    ]
])
a = a.reshape(3,6)
print(a)
arr = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])
print(arr[5:15])
print(arr[5:15:3])

a = np.array([1,2,3])
b = np.array([
   [1,2,3],
   [4,5,6],
   [7,8,9]
])
print(a+b)

import numpy as np

a = np.array([
 [12, 15, 18],
 [21, 24, 27],
 [30, 33, 36],
 [39, 42, 45]
]
)

print(a.size)
print(a.shape)
print(a.nbytes)
print(a.min())
print(a.max())


a = np.array([
 [12, 15, 18],
 [21, 24, 27],
 [30, 33, 36],
 [39, 42, 45]
])

print(a.sum())
print(a.sum(axis = 1))
print(a.sum(axis = 0))
print(a.flatten())


a = np.array([
    [12, 28, 14],
    [33, 9, 5],
    [41, 6, 18]
])

print(a.reshape(9,1))
a[1][1] = 900
print(a)
a[a > 25] = 0
print(a)
