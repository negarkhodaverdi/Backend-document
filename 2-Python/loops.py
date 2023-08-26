list_data = ["a", "b", "c", 4, 5.1]
dict_data = {"name": "Arshia", "family": "Tamimi", "age": 22}

###########################################
# Simple Loop
for i in list_data:
    print(i)

# Loop Through Specific Part Of List
for i in list_data[0:2]:
    print(i)

# Loop Reverse
for i in list_data[::-1]:
    print(i)

# Loop With Index
for c, i in enumerate(list_data):
    print(c, i)  # c is Index And i Is Element

###########################################

# Prints 0 to 10 (10 is not included)
for i in range(10):
    print(i)

# Prints 5 to 10 (10 is not included)
for i in range(5, 10):
    print(i)

# Prints 0 to 10 With 2 steps Like 0,2,4,... (10 is not included)
for i in range(0, 10, 2):
    print(i)

# Prints 10 to 0 With -1 steps Like 10,9,8,... (0 is not included)
for i in range(10, 0, -1):
    print(i)

#! Bonus1
# Just Prints Even Indexes. Result : a , c , 5.1 ( Each , Means Next Line )
for i in range(0, len(list_data), 2):
    print(list_data[i])

#! Bonus2
text = ['A', 'rsh', 'i', 'a']
# Output Is "Arshia"
for i in text:
    print(i, end='')

###########################################


# Loop Through Dictionary
for key, value in dict_data.items():
    print(key, value)

# Loop Through Dictionary (Keys)
for key in dict_data.keys():
    print(key)

# Loop Through Dictionary (Values)
for values in dict_data.values():
    print(values)

###########################################
