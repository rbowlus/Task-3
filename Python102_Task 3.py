#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1
def hello_name(user_name):
    """Display a simple greeting"""
    print("hello_" + user_name.upper() + "!")
    
hello_name('username')


# In[2]:


#Question 2
odd_numbers = []
current_number = 0
while len(odd_numbers) < 100:
    current_number += 1
    if current_number % 2 != 0:
        odd_numbers.append(current_number)
    elif len(odd_numbers) == 100:
        break
        
print(odd_numbers)


# In[3]:


#Question 3

def max_num_in_list(a_list):
    """Return the largest number in a list."""
    max_number = max(a_list)
    return max_number
    
#TEST
a_list = [3, 24, 9, 37, 12]
max_num_in_list(a_list)


# In[25]:


#Question 4

def is_leap_year(a_year):
    """Determine if a given year is a leap year."""
    if a_year % 4 == 0: 
        if a_year % 100 == 0:
            if a_year % 400 == 0:
               return True
            else:
                return False
        else:
            return True
    else:
        return False

#TEST
a_year = 104
is_leap_year(a_year)


# In[55]:


#Question 5

def is_consecutive(a_list):
    """Test to see if all numbers in a list are consecutive."""
    current_value = a_list[0]-1
    for number in a_list:
        current_value +=1
        if current_value != number:
            return False
    return True

#TEST
a_list = [4, 5, 6, 17, 8, 9]
is_consecutive(a_list)


# In[46]:




