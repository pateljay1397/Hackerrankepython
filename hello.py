# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 18:33:58 2020

@author: patel
"""
import random

def hello():
    
    print("Hello World This Jerry is here")
    
    print(random.randrange(1,15))
hello()

x=10.5
y="Jerry"
print(y[2:5])
print(y[-5:-3]+y[2:5])
x=int(x)
print(x)
x=str(x)
print(len(y))
print(y.strip())
print(y.lower())
print(y.upper())
print(y.replace("J","H"))
print(y.split())
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

age=22
txt ="my age is {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder="I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity,itemno,price))
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
    
if "apple" in thislist:
    print("yes") 
thislist.append("Orange")
print(thislist)
thislist.insert(1,"orange")
print(thislist)

list1=["A" "B" "C" "D"]
list2=["1" "2" "3" "4"]
for x in list2:
    list1.append(x)
    print(list1)
    
list1.extend(list2)
print(list1)

thislist = ("apple", "banana", "cherry")
y=list(thislist)
y[1]="kiwi"
thislist=tuple(y)
print(thislist)
thisset = {"apple", "banana", "cherry"}
print(thisset)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

x=thisdict["brand"]
print(x)

for x,y in thisdict.items():
    print(x,y)