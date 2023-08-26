AVAILABLE_STATUSES = ["happy", "cry"]

name = "atousa"
age = 20
male = False
score = 19.99
status = AVAILABLE_STATUSES[1]

person_one = {
    "name of person": name,
    "age of person": age,
    "male of person": male,
    "score of person": score,
    "status of person": status,
}

# All Of This Prints Does Not Set The Variable.
print(age > 18)
print(score <= 19)  # Check If score Is Less Than Or Equals To 19
print(male == True)  # Check If male is True

# Check If male is True and age is more that 18
print(male == True and age > 18)
# Check If male is True or name is atousa
print(male == True or name == "atousa")

print(age + 20)
print(age - 18)
print(age * 2)  # Multiply
print(age / 2)  # Divide
print(age // 2)  # Divide And Convert To Int ( Removes Floating Parts )
print(age % 2)  # Divide To 2 And Gives You The Reminder. In This Case Its 0
print(age ** 2)  # Powers The Number. Its Like ( age * age ) In This Case
print("Hello" + " " + name)  # Prints "Hello atousa"

#! Important
print(AVAILABLE_STATUSES + "sad")  # Prints "['happy', 'cry', 's', 'a', 'd']"
AVAILABLE_STATUSES = ["happy", "cry"]

print(AVAILABLE_STATUSES + ["sad"])  # Prints "['happy', 'cry', 'sad']"
#! Important

# Check Id "sad" Is In AVAILABLE_STATUSES Or Not. Its False In This Case
print("sad" in AVAILABLE_STATUSES)

# Checks Provided String In Keys. Returns True In This Case
print("name of person" in person_one)

# Checks Provided String In Keys. Returns True In This Case
print("atousa" in person_one)  # Returns False ("atousa" Is value)
print(name in person_one)  # Returns False  ("atousa" Is value)

# This Will Change The Value Too.
age += 10
age -= 10
age += score
age -= score
age *= score
age /= score
score //= 10
score = 19.99

#! Important
#! Raises Error ! Because name is String Does Not Supports += And -= Operand.
name += " Mohhamadi"

# You Can Do This Like :
name = name + " Mohhamadi"
#! Important

sum_of_age_and_score = score + age
