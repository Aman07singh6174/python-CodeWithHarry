dict={
    "key1": "value1",
    "aman":10,
    "raj":30.2,
    1:"surya"
}

print(dict.items())
print(dict.keys())# this will print all the keys in the dictionary

print(dict.values())#this will print all the values in the dictionary

dict.update({"aman":"value2","isu":"20"})#this will add a new key value pair in the dictionary
print(dict)

print(dict.get("raj"))#this will print the value of the key "raj" in the dictionary
#but the difference between dict["raj"] and dict.get("raj") is that if the key is not present in the dictionary then dict["raj"] will give an error but dict.get("raj") will return None
print(dict.get("raj1"))#this will return None because the key "raj1" is not present in the dictionary


print(dict["raj"])#this will print the value of the key "raj" in the dictionary
#but the difference between dict["raj"] and dict.get("raj") is that if the key is not present in the dictionary then dict["raj"] will give an error but dict.get("raj") will return None

# print(dict["raj1"])#this will give an error because the key "raj1" is not present in the dictionary

print(dict.pop("raj"))#this will remove the key "raj" from the dictionary and return its value
print(dict.items())#this will print all the key value pairs in the dictionary after removing the key "raj"
print(dict.popitem())#this will remove the last key value pair from the dictionary and return it