AVAILABLE_STATUSES = ["happy", "sad"]

name = "asghar"
age = 20
male = True
score = 12
status = AVAILABLE_STATUSES[0]

person_one = {
    "name of person": name,
    "age of person": age,
    "male of person": male,
    "score of person": score,
    "status of person": status,
}

# ?####################################################################?#
# ? String Methods ( The Values Will Not Changed After Calling Methods )?#
name = "asghar taghi zadeh baladeh"
print(" ".join(AVAILABLE_STATUSES))  # happy sad
print(name.replace("a", "A"))  # AsghAr tAghi zAdeh bAlAdeh
print(name.startswith("asghar"))  # True
print(name.startswith("r"))  # False
print(name.split(" "))  # ['asghar', 'taghi', 'zadeh', 'baladeh']
print(name.strip())  # asghar taghi zadeh baladeh

# ? Addtion If You Like To Know More
print(name.capitalize())  # Asghar taghi zadeh baladeh
print(name.count("a"))  # 6
print(name.find("r"))  # 5
print(name.islower())  # True
print(name.lower())  # asghar taghi zadeh baladeh
print(name.isalnum())  # False
print(name.isalpha())  # False
print(name.isdigit())  # False
print(name.isupper())  # False
print(name.upper())  # ASGHAR TAGHI ZADEH BALADEH

# ? String Methods ( The Values Will Not Changed After Calling Methods )?#
# ?####################################################################?#

# ?##################################################################?#
# ? List Methods ( The Values Will Change After Calling The Method ) ?#
some_array = [1, 2, 3, 4, 5]
some_array.append(7)  # some_array : [1, 2, 3, 4, 5, 7]
some_array.pop()  # some_array : [1 ,2, 3, 4, 5, 6]
some_array.pop(0)  # some_array : [2, 3, 4, 5, 6, 7]
some_array.remove(5)  # some_array : [2, 3, 4, 6]


# ? Addtion If You Like To Know More
some_array.count(1)  # 1
some_array.index(1)  # 0
some_array.reverse()  # some_array : [6, 4, 3, 2]
some_array.clear()  # some_array : []
some_array.insert(5, 6)  # some_array : [1, 2, 3, 4, 5, 6, 7]

array1 = ["a", "b", "c", "d"]

array1.remove("c")  # ['a', 'b', 'd']
array1.pop(1)  # ['a', 'd']
# ? List Methods ( The Values Will Change After Calling The Method ) ?#
# ?##################################################################?#

#!##################################################################!#
# !                            Important                            !#
# There Is Some Important Thing That You Need To Know.
array1 = ["a", "b", "c", "d"]
array2 = array1
array2[0] = 10
# Now Both Of array1 And array2 Are [10, 'b', 'c', 'd'] !
# To Prevent This You Can Do This :
array1 = ["a", "b", "c", "d"]
array2 = array1.copy()
array2[0] = 10
# Now array1 is ["a", "b", "c", "d"] and array2 is [10, 'b', 'c', 'd']
#! In Dicitionary That You Will See Below,
#! The copy() Method Act Exactly Like This

# !                            Important                            !#
#!##################################################################!#

# ?########################################################################?#
# ? Dictionary Methods ( Change Of Variable Depends On The Function. )     ?#
me = {"name": "Arshia", "family": "tamimi",
      "age": 22}

# dict_items([('name', 'Arshia'), ('family', 'tamimi'), ('age', 22)])
print(me.items())
print(me.get("name"))  # 'Arshia'


# ? Addtion If You Like To Know More
print(me.values())  # dict_values(['Arshia', 'tamimi', 22])
print(me.keys())  # dict_keys(['name', 'family', 'age'])

# me : {'name': 'Arshia', 'family': 'kazem tamimi', 'age': 22, 'instagram': '...'}
me.update({"family": "kazem tamimi", "instagram": "..."})

print(me.clear())  # me : {}
me.copy()  # Act Like The List. As I Said Before ( In Important ).

# ? Dictionary Methods ( Change Of Variable Depends On The Function. )     ?#
# ?########################################################################?#
