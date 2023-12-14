#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def my_plus(x,y):
    return x+y

def my_minus(x,y):
    return x-y

def my_multiply(x,y):
    return x*y

def my_division(x,y):
    return x/y

def my_calculate (x,y,opcode='+'):
    if (opcode=='-'):
        return my_minus(x,y)
    elif (opcode=='*'):
        return my_multiply(x,y)
    elif (opcode=='/'):
        return my_division(x,y)
    else:
        return my_plus(x,y)

print('input two numbers : ')
x=int(input())
y=int(input())
opcode=input('input operation: ')

print('Result is', my_calculate(x,y,opcode))

