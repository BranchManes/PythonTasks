#!/usr/bin/env python
# coding: utf-8

# In[4]:


a=int(input())
b=int(input())
h=int(input())
if h<a:
    print("Недосып")
elif h>b:
    print("Пересып")
else:
    print("Это нормально")


# In[7]:


year = int(input())
if year%4==0 and year%100!=0:
    print("Високосный")
elif year%400==0:
    print("Високосный")
else:
    print("Обычный")


# In[9]:


a=int(input())
b=int(input())
c=int(input())
p=(a+b+c)/2
squre=(p*(p-a)*(p-b)*(p-c))**0.5
print(squre)


# In[11]:


number=int(input())
if number>-15 and number<=12 or number>14 and number <17 or number >=19:
    print('True')
else:
    print('False')


# In[18]:


number1 = float(input())
number2 = float(input())
operation =input()
if operation == '+':
    print(number1+number2)
elif operation =='-':
    print(number1-number2)
elif operation =='/':
    if number2 !=0:
        print(number1/number2)
    else:
        print("Деление на 0!")
elif operation =='*':
    print(number1*number2)
elif operation =='mod':
    if number2 !=0:
        print(number1%number2)
    else:
        print("Деление на 0!")
elif operation =='pow':
    print(number1**number2)
elif operation =='div':
    if number2!=0:
        print(number1//number2)
    else:
        print("Деление на 0!")



# In[27]:


figure = input()
if figure =='треугольник':
    number1 = float(input())
    number2 = float(input())
    number3 = float(input())
    p=(number1+number2+number3)/2
    squre=(p*(p-number1)*(p-number2)*(p-number3))**0.5
    print(squre)
elif figure == 'прямоугольник':
    number1 = float(input())
    number2 = float(input())
    print(number1*number2)
elif figure == 'круг':
    radius = float(input())
    print(3.14*radius**2)


# In[29]:


number1 = int(input())
number2 = int(input())
number3 = int(input())
countMax=max(number1,number2,number3)
countMin=min(number1,number2,number3)
print(countMax)
print(countMin)
if countMax != number1 
    print(number1)
elif countMax !=number2
    


# In[ ]:




