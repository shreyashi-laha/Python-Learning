#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = "Shreyashi Laha"
print(name)


# In[2]:


a =5
b =2
if a>b:
    print("a is greater than b")


# In[4]:


a = 12
b = 23
c = a+b 
#a-b a*b a/b; exponent a**b; remainder a%b, quotient a//b
print(c)


# In[6]:


#membership operator
l = ["bananas", "grapes", "orange"]
print("bananas" in l)


# ### Calculator
# 
# * Addition
# * Substraction
# * Multiplication
# * Division

# In[10]:


a = 100
b = 200
operation = input("What operation you want to do?")


# In[11]:


if operation=="Addition":
    print(a+b)
if operation=="Substraction":
    print(a-b)
if operation=="Multiplication":
    print(a*b)
if operation=="Division":
    print(a/b)


# In[12]:


#using single quotation within quotes
var = 'I\'m good'
print(var)


# In[14]:


#String extraction
a = "Hello World"
print(a[1])
print(a[0:5])  #1st index i.e 0 is always includes and last index i.e 5 is excluded


# In[15]:


#String concatenation
str1 = "My first string"
str2 = "My second string"
str3 = str1+str2
print(str3)


# In[16]:


str4 = str1*5
print(str4)


# In[17]:


a.capitalize()   #capitalizes first letter only


# In[18]:


a.upper()   #capitalizes all letters


# ## F strings is used to embed Python exp inside strings

# In[19]:


name = "abc"
age = 10
print(f"{name} is {age} years old")


# ## Casting

# In[21]:


c = "123.5"
d = "256.8"


# In[22]:


a = float(c)
b = float(d)
print(a,b)


# In[23]:


print(type(a))
print(type(b))


# In[24]:


print(a+b)
print(c+d)


# In[25]:


#cannot covert string with decimal into int..have to use float function
a = int(c)
b = int(d)


# In[26]:


a_int = int(a)
b_int = int(b)
a_int,b_int


# ## Data Types
# * List - ordered, changeable, allows duplicate members; created by square brackets; l = ["a", "b", "12", "3.6"], l[0], l[1]; adding 2 list will concatenate all items in both list
# * Tuple - ordered, unchangeable, allows duplicate members; created by round brackets; fruits = ("grapes, "banana","mamgo")
# * Set - Unordered, unindexed, no duplicate members; created by curly brackets, cannot be access with index as they are unordered
# * Dictionary - Unordered, changeable, indexed, no duplicate members; created by curly brackets, have keys and values

# In[29]:


# slicing
l = ["a", "b", "c", "d", "e", "12", "3.6"]
print(l[0:5:2]) # 2 denotes the steps that it will take starting from 0th index and ending at 5-1 = 4th index


# In[35]:


# list are also indexed from last position starting with -1 index

print(l[::-1]) # will print all the items in reverse order due to -1
print(l[-1:-5:-1])
print(l[-1:-5:1])
print(l[-5:-1:1])
print(l[-5::1])


# In[36]:


fruits_t = ("grapes", "banana","mango")
fruits_l = ["grapes", "banana","mango"]


# In[38]:


fruits_l[0] = "kiwi"
print(fruits_l)


# In[45]:


fruits_t[0]


# In[39]:


fruits_t[0] = "kiwi"


# In[40]:


list1 = [1,2,3]
list2 = [4,5,6]
tup = (list1, list2)
print(tup)


# In[41]:


list2[0] = 9
print(tup)


# In[47]:


myset = {"grapes", "banana","mango"}


# In[43]:


print(myset)


# In[44]:


myset[0]


# In[48]:


#accessing items in set
for x in myset:
    print(x)


# In[49]:


mydict = {"fname":"Shreyashi", "lname": "Laha", "age": 23}
print(mydict)


# In[50]:


print(mydict['age'])


# ## If-Else statement

# In[53]:


a = 100
b = 100
if b>a:
    print('b is greater')
elif a==b:
    print('a is same as b')
else:
    print('a is greater')


# ## While and For loop

# In[54]:


# while
i= 1
while i<6:
    print(i)
    i+=1


# In[55]:


# For
fruits = ["grapes", "banana","mango"]
for x in fruits:
    print(x)


# In[56]:


for x in fruits:
    print(x,len(x))


# In[62]:


a,b = 0,1
while a <= 100:
    print(a, end=",")
    a,b = b, a+b


# In[64]:


#range (start, stop,[step])
for i in range(0,100,2):
    print(i, end=",")


# In[65]:


for i in range(0,100):
    print('hello',i)
    if i>10:
        break
    print('How are you?',i)


# In[66]:


#if continue conditon are met, everything below continue is skipped and rest of the loop continue. 
#All iteration of for loop takes place whereas break stops the iterations all together 

for i in range(0,100):
    print('hello',i)
    if i>10:
        continue
    print('How are you?',i)


# ## Functions

# In[67]:


#function output is in the form of tupple

def is_prime(n):
    for i in range(2, int(n**.5)+1):
        if n%i==0:
            return(False)
    return (True)   


# In[70]:


is_prime(7)


# In[72]:


for i in range(2, 101):
    if(is_prime(i)):
        print(i, end =",")


# ### Lambda function 
# * x = lambda a: a+10, where a is argument and a+10 is returned value, if a = 5, x = 15
# * can take multiple values as input. eg. x = lambda a,b: a*b. So, input is 2 variable & output is product of them

# In[73]:


x = lambda a,b: a*b
print(x(5,6))


# In[75]:


#Iterator
fruits_t = ("grapes", "banana","mango")
myit = iter(fruits_t)

print(next(myit))
print(next(myit))


# ## Classes
# * bundles attributes which are variables and methods which are function
# * an instance of the class can be called by assigning it to some variable

# In[78]:


# def _init_(self,l,b) is a constructor which gets executed when the class is initiated

class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
        
    def area(self):
        return(self.length*self.breadth)
    
    def perimeter(self):
        return(2*self.length + 2*self.breadth)


# In[80]:


#area and perimeter do not need any input as it is taking attributes from self function
r1 = Rectangle(5,6)
r1.area()


# In[81]:


r1.perimeter()


# ## File handling

# In[83]:


#opening a file, r signifies in read mode, w: opens in write mode
f = open("myfile.txt","r") #opens the file

print(f.read())  #reads the entire content of file
f.close()        # closes the file


# In[85]:


f = open("myfile.txt","r") #opens the file
print(f.read(5))  #prints the 1st 5 characters
f.seek(0)         #takes to beginning of file: 0 denotes o bytes
f.close() 


# In[86]:


# wite a file: "a"- append: to add contents to the end of file, "w" - Write: will overwrite the existing file

f = open("myfile.txt","a")
f.write("appending content to the file")
f.close()   


# In[88]:


f = open("myfile1.txt","w")
f.write("these are latest changes")
f.close()


# In[89]:


#\n: new line \t: new tab

f = open("myfile1.txt","a")
f.write("\nthese are latest changes")
f.close()


# ## Modules and File Handling

# In[ ]:


#different ways to import

# import<module_name>               - imports entire module
# from<module_name>import<names>    - specific object or function
# from<module_name>import *         - import everything
# import<module_name> as <alt_name> - alternative name
# from<module_name>import<name> as <alt_name>


# In[90]:


import numpy as np


# In[91]:


a = np.array([0,10,20,30,40])
print(a[:])


# In[92]:


print(a[1:3])


# In[93]:


print(a[1]=15)


# In[95]:


b = np.arange(-5,5,0.5)


# In[97]:


print(b)
print(b**2)


# In[98]:


print(1/b)


# In[100]:


print(1/b[9])


# In[101]:


#multidimensional array
x=np.array([[1,2,3],[4,5,6]])
print(x)


# In[102]:


print(x[1,2])


# In[103]:


a.max()


# In[104]:


a.mean()


# In[105]:


print(a+b)


# In[106]:


n1 = np.array([[1,2],[3,4]])
n2 = np.array([[5,6],[7,8]])
n1+n2


# In[107]:


n1*n2


# In[108]:


n1.dot(n2)


# In[109]:


n2.dot(n1)


# In[110]:


import matplotlib.pyplot as plt


# In[111]:


x = np.array([1,2,3,4])
y = np.array([1,4,9,16])


# In[112]:


plt.plot(x,y)
plt.show()


# In[113]:


import scipy.integrate as integrate


# In[ ]:


result = integrate.quad()


# In[114]:


import scipy.optimize as optimize


# In[ ]:


def quadratic(x,a,b,c):
    return a*x**2+b*x +c


# In[ ]:


xdata = [0,1,2,3,4,5]
ydata = [0,1.1,3.8,9.1,15.8,25.4]

popt,pcov = optimize.curve_fit(quadratic,xdata,ydata)

