
# coding: utf-8

# In[2]:


#Write a program which accepts a sequence of comma-separated numbers from console and generate a list.

my_list = input("Enter a sequence of comma seperated numbers:\n List: \n")
my_list = my_list.split(",")
print(my_list)


# In[6]:


#Create the below pattern using nested for loop in Python

n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[8]:


#Write a Python program to reverse a word after accepting the input from the user.

word = input("Enter a word to reverse: ")

for i in range(len(word) - 1, -1, -1):
  print(word[i], end="")
print("\n")


# In[12]:


#Write a Python Program to print the given string in the format specified in the sample output.
#WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN,SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens

print("WE, THE PEOPLE OF INDIA, \n\t having solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC, \n\t\tand to secure to all its citizens ")

