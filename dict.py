# dictionary in python is nothing but key 

# defining dictionary

d1 = {}

#adding items and meanings to the dictionary
d2={"harry":"burger","rohan":"fish","hari":"banana","shyam":"roti"}

#printing dictionary
print(d2)

#printing meanings
print(d2["shyam"])#what shyam eats for 

#adding element to the last 
d2["ankit"]="junk food"
print(d2)

#Pointing to the same
d1=d2
print(d1)

#_connection of both equating variables but not copied variables
d3=d1.copy()
del d1["ankit"]
print(d2) #same as printing d1 as changing one of them changes both
print(d3) #however changing doesn't effect variable where the data is copied

# Adding my girl to the dictionary
d2.update({"mygirl":"Chatpat"})
print(d1) # d1=d2

#printing keys
print(d2.keys())

# Printing items
print(d2.items())

d2.update({"Pabita":"likes to sex with me"})
print(d1)

'''Removes last inserted key value from list'''
d2.popitem()
print(d1)
