#!/usr/bin/env python
# coding: utf-8

# PYTHON PROGRAMMING ASSIGNMENT NO. 8 

# WRITE A PYTHON PROGRAM TO ADD TWO MATRICES

# In[1]:


x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[2,5,7],
    [8,9,10],
    [0,4,7]]

Output = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        Output[i][j]= x[i][j] + y[i][j]

for i in Output:
    print(i)


# WRITE A PYTHON PROGRAM TO MULTIPLY TWO MATRICES

# In[2]:


x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[2,5,7],
    [8,9,10],
    [0,4,7]]

Output = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        for k in range(len(y)):
            Output[i][j] += x[i][k] * y[k][j]

for i in Output:
    print(i)


# WRITE A PYTHON PROGRAM TO TRANSPOSE A MATRIX

# In[3]:


x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

output = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(x)):
    for j in range(len(x)):
        output[j][i] = x[i][j]
       
for i in output:
    print(i)


# WRITE A PYTHON PROGRAM TO SORT WORDS IN ALPHABETICAL ORDER

# In[5]:


str = input("Enter a string: ") 

for i in str:
    a = str.lower().split()
a.sort() 
print(a)


# WRITE A PYTHON PROGRAM TO REMOVE PUNCTUATION FROM STRING

# In[6]:


punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
word = input("Enter a string: ")
for i in word:
    if i not in punctuations:
        print(i,end="")


# In[ ]:




