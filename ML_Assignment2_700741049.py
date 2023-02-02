#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Question1
rows = 5
#using nested for loop for top 5 rows of star pattern
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
##using nested for loop for bottoms 5rows of star pattern
for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")


# In[11]:


#Question2
#Use looping to output the elements from a provided list present at odd indexes.

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# stat from index 1 with step 2( means 1, 3, 5, an so on)
for i in my_list[1::2]:
   print(i, end=" ")


# In[12]:


#Question3
# Append a list with types of elements
x = [23,'Python', 23.98]
n = []
for i in range(len(x)):
    #using type function to get types of elements and printing them
    n.append(type(x[i]))
print(n)
print(x)


# In[13]:


#Question4
#Write a function that takes a list and returns a new list with unique items of the first list.
#Sample List: [1,2,3,3,3,3,4,5]
def unique_list(l):
  x = []
#using for loop
  for a in l:
    if a not in x:
      x.append(a)
  return x
print(unique_list([1,2,3,3,3,3,4,5])) 


# In[15]:


#Question5
#. Write a function that accepts a string and calculate the number of upper-case letters and lower-case letters. 
#Input String: 'The quick Brow Fox'
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')


# In[ ]:




