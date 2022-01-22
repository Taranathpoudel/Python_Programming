# clear() function removes all the elements from the list
from cgi import print_form


dic1={"apple":"fruit","ball":"game","cat":"animal"}
print(dic1)

dic1.clear()
print(dic1)

# copy() function returns a copy of the dictionary
dic2=dic1.copy()
print(dic2)

dic3={"apple":"fruit","ball":"game","cat":"animal"}

#fromkeys() returns a dictionary with the specified keys and value
'''This function creates dictionaries from key and items'''
x=('key1','key2','key3')
y='Items'  # This single item is binded to all the keys
z=dict.fromkeys(x,y)
print(z)

# get() function returns the value of specified key
print(dic3.get("ball"))

#items() function returns the tuple of each (Key , value) pair
print(dic3.items())

# keys() function  returns a list cotaining a dictionary keys
print(dic3.keys())

# The function named pop() removes the element with the specified key
dic3.pop("apple") # Here "Apple" key and its value pair "fruit" gets removed
print(dic3)

# The function popitem() removes the last inserted key value peir
dic3.popitem()
print(dic3)

# The function setdefault() returns the value of specified key. If the key doesn't exists : insert the key , with the specified value
'''case 1 when the argument key matches one of the key of dictionary then the value of dictionary gets printed'''
h=dic3.setdefault("ball","makabhosada") # Here dic3 contains ball so "makabhosada is not printed"
print(h)

'''case 2 when the key argument is unique to the dictionary then argument value pair is printed'''
i=dic3.setdefault("fan","MsDhoni")
print(i) # Note The values pairs are also added to the dictionary

print(dic3)

# The function update add new pairs to the dictionary
dic3.update({"Aarati":"Love"})
print(dic3)

# The function values() returns a list of values in the dictionary
print(dic3.values()) #same as items