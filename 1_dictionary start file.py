import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

print()
print('*****  start section 1 - print dictionary *****************************************')
print()

print(phonebook)
print(type(phonebook))

print(len(phonebook)) ##if you want to know how many values there are in your dictionary
mydictionary = {} ##a way you can add a blank dictionaty
mydict = dict(m=8, n=9) #using dict function
print(mydict)

phoneno = phonebook['Chris'] #can't change to lower case because then you will get a keyerror. u get his number 

print(phoneno)

print()
print('*****  end section 1 *************************************************************')
print()



print()
print('*****  start section 2 - search dictionary ***************************************')
print()

name = 'Chris'

if name in phonebook: #make sure that default search is keys in the dictionary
    print(phonebook[name])
else:
    print(f"{name} not found in phonebook")


print()
print('*****  end section 2 *************************************************************')
print()


print()
print('*****  start section 3 - edit/append dictionary **********************************')
print()

## mutable = it can change
## you cannot update an existing KEY. you would have to delete that key value pair and append it
#you can update/edit the phone number but not the key

print(phonebook)
phonebook['Chris'] = '555-4444' #chris already exists 
phonebook['Joe'] = '555-0123'
print(phonebook)



print()
print('*****  end section 3 *************************************************************')
print()


print()
print('*****  start section 4 - delete/remove from dictionary **************************')
print()

print(phonebook)
del phonebook['Chris']
print(phonebook)


print()
print('*****  end section 4 **************************************************************')
print()


print()
print('*****  start section 5 - iterate through keys, values, items **********************')
print()

for key in phonebook: ##first way. does not have to be the work key,key is a variable name, it can be any name but b consistent
    print(f" the key is: {key} and the value is: {phonebook[key]}") #key is a string

for value in phonebook.values(): ##second way #values method;s purpose is to cycle through all the numbers
    print(value)

for k,v in phonebook.items():  ##third way - returns a tuple
    print(f"the key is {k} and the value is {v}")
    #print(k,v)

for item in phonebook.items():  
    print(item)


print()
print('*****  end section 5 ************************************************************')
print()

print()
print('*****  start section 6 - using get and clear ************************************')
print()

print(phonebook)
phone = phonebook.get('Chris','Not Found') #assign a value. Get method avoids the key error mentioned earlier
print(phone)

phonebook.clear() #does not get rid of the object, it just clears it out
print(phonebook)




print()
print('*****  end section 6 ***********************************************************')
print()

print()
print('*****  start section 7 - using pop method **************************************')
print()

print(phonebook)
a = phonebook.pop('Chris', 'notfound') #pops out the last item -- 
print(a)
print(phonebook)
## if you want a random one popped out, use a list sec(9)

print()
print('*****  end section 7 **********************************************************')
print()

print()
print('*****  start section 8 - using popitem ****************************************')
print()

keyvalue = phonebook.popitem()
print(phonebook)
## if you want a random one popped out, use a list sec(9)


print()
print('*****  end section 8 *******************************************************')
print()
print()
print('*****  start section 9 - using random and converting to list ***************')
print()

list_of_keys = list(phonebook)
print(list_of_keys)
random_key = random.choice(list_of_keys)
print(random_key)
print(phonebook[random_key]) #you get name and # with this code

#condensed version------------------------------------------
print(phonebook[random.choice(list(phonebook))])
#to only print the key
print(random.choice(list(phonebook)))



print()
print('*****  end section 9 ******************************************************')
print()

