programming_dictionary = {
    "Bug" : "An error in a program that prevents the proggram from running as expected.",
    "Function" : "A piece of code that you can easily call over and over again",
    "Loop" : "The action of doing something over and over again",
    
}

#retrieving the data from the dictionary
print (programming_dictionary["Bug"])

programming_dictionary["loop2"] = "The action of doing something over and over again is called loop"
print(programming_dictionary)

#creating an empty dictionaey
empty_dictionary = {}

#wiping an already existing dicrionary

# programming_dictionary = {}
# print(programming_dictionary)


programming_dictionary["Bug"] = "A moth in the computer"

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
