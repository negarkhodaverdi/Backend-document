#! Define Constants
AVAILABLE_STATUSES = ["happy", "sad"]

#! Define Variables
name = "arshia"
age = 20
male = True
score = 17.6
status = AVAILABLE_STATUSES[0]
important_scores = (10, 12, 18, 20)

a1 = 10
a2 = 20
a1, a2 = a2, a1  # Change Variable Values
a1, a2, a3 = 10, 20, 30  # Multi Variable Set

person_one = {
    "name of person": name,
    "age of person": age,
    "male of person": male,
    "score of person": score,
    "status of person": status,
}

user_name = input("Enter Your Name : ")
print(f"Hello My Name Is {user_name}")

# Print A String
print("Hello")

# Print Some Variables
print(name)
print(important_scores)
print(age, male, score)
print(person_one)

print(person_one["name of person"])

# Say Hello To name Variable
print("Hello", name)

# Print Type Of Variables
print(type(name))
print(type(age))
print(type(male))
print(type(score))
print(type(AVAILABLE_STATUSES))
print(type(person_one))
print(type(important_scores))

# Cool String And Array Features
print(name[0])  # "a"
print(name[0:3])  # "ars"
print(name[3:0:-1])  # "hsr"
print(name[-2])  # "i"
print(name[-3:])  # "hia"
print(name[:3])  # "ars"
print(name[::-1])  # "aihsra"

print(AVAILABLE_STATUSES[-1])
print(AVAILABLE_STATUSES[:-1])
print(important_scores[-3])
print(important_scores[-1:])

print(len(AVAILABLE_STATUSES))  # 2
print(len(name))  # 6
print(len(person_one))  # 5
print(len(important_scores))  # 4

#! Converts
# These Are Functions And That You Can Use To Convert.
list, int, str, bool, dict, tuple


int(score)  # 17
float(age)  # 20.0
str(score)  # "17.6"
list(name)  # ['a', 'r', 's', 'h', 'i', 'a']
str(male)  # "True"
bool(score)  # True
bool(0)  # False
bool("")  # False
int(True)  # 1
int(False)  # 0
str(AVAILABLE_STATUSES)  # "['happy', 'sad']"

# "{'name of person': 'arshia', 'age of person': 20, 'male of person': True, 'score of person': 17.6, 'status of person': 'happy'}"
str(person_one)

# One Line Comments Are Like This

"""
Multiline Comments
Are Available
With This Signs
"""
