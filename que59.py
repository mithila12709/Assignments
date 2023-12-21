  ####   STRING QUESTIONS     #####

#59.Write a Python program to find words which are greater
# than given length k.

string =" i am in nashik and i am fine"
k= 3

words= string.split()
for i in words:
    if len (i)> k:
        print(i,end=" ")

# 61.	Write a Python program to split and join a string?
        
# Split:
str= " I am in pune i like pune"
s= str.split()
print(s)

# Join:
s=["apple","banana","grapes"]
ss= " ".join(s)
print(ss)

# 63.Write a Python program to find uncommon words from two Strings?
        
str1 = " this is mithila"
str2= " this is mandar"

s= set(str1.split()) ^ set(str2.split())   # (^ = EXOR)
print(s)

# Method 2:

A = "This is banana and apple"
B= " This is lily and rose"
l=[]
split1= A.split()
split2= B.split()
for i in split1:
    if i in split2:
        pass
    else:
        l.append(i)
for j in split2:
    if j in split1:
        pass
    else:
        l.append(j)
print(l)


#64.Write a Python to find all duplicate characters in string?

str1= "hello bunny"
l=[]
for i in str1:
    if str1.count(i) > 1:
        l.append(i)
print(l)

# 65.Write a Python Program to check if a string contains any special character

splchar= '''!@#$%^&*(){}[]?><;'.,|'''
str2="ohh wow! Whrer do u live?? # "

# for i in str2:
#     if i not in splchar:
#         print("No spl chara is there")
#     else:
#         print("spl chara") 

#####  DICTIONARY QUESTIONS   ########

# 66.	Write a Python program to Extract Unique values dictionary values

dict1= {"model": "xuv",
       "color": "red",
       "make":"mahindra",
       "model2": "seltos",
       "color4": "red"
       }
print(dict1)

# we want unique values.
print(set(dict1.values()))

# 67.	Write a Python program to find the sum of all items in a dictionary?

d={"a":2,
   "b":67,
   "c":45}

sum=0
for i in d.values():
    sum= sum+i

print(sum)

# 68.	Write a Python program to Merging two Dictionaries

dict1= {
        "1":"Rama",
        "2": "seema",
        "3": "kriti"
        }

dict2= {
        "8":"Rohit",
        "9": "sameer",
        "10": "ketan"
        }

dict1.update(dict2)
print(dict1)

# 69.	Write a Python program to convert key-values list to flat dictionary

list1=[1,2,3,4]
list2=["red","yellow","blue","grey"]

d= dict(zip(list1,list2))
print(d)

# 
dict={}
# fill this dictionary:
dict ["t"]=3
dict ["h"]=7
dict ["r"]=78
dict ["k"]=8
print(dict)

# 70.	Write a Python program to insertion at the beginning in OrderedDict.

from collections import OrderedDict

odict= OrderedDict()
odict["a"]=10
odict["b"]=56
odict["c"]=78
odict["d"]=18

print(odict)


#72.Write a Python program to sort Python Dictionaries by Key or Value
dict2= {
        "7":"Rohit",
        "9": "sameer",
        "3": "ketan"
        }

sv= sorted(dict2.items(), key = lambda x:x[0])
print(sv)  # Here we ll get sorted dictionary in list of tuple.

# We can sort keys and values :
v=sorted(dict2.keys())
print(v)









