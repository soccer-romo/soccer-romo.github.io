#working with binary files

import pickle, shelve

print("Pickling lists")

variety = ["sweets", "hot", "dill"]
shape = ["whole", "spear","chip"]
brand = ["Claussen", "Heinz", "Vlassic"]
'''
f = open("pickles1.dat", "wb") 
pickle.dump(variety,f)
pickle.dump(shape,f)
pickle.dump(brand,f)
f.close()
'''
f = open("pickles.dat","rb")
variety = pickle.load(f)
test2 = pickle.load(f)
test3 = pickle.load(f)
print(variety)
print(test2)
print(test3)
f.close()

print("\nShelving")
s = shelve.open("pickles2.dat")
s["variety"] = ["sweets", "hot", "dill"]
s["shape"] = ["whole", "spear","chip"]
s["brand"] = ["Claussen", "Heinz", "Vlassic"]

s.sync()

print("\nGetting data from the shelf")
print("brands -", s["brand"]
s.close()
