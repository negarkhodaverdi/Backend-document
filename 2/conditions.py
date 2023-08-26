a = 10

# Simple Condition
if a > 10:
    print("i is more than 10")

# Condition With else State
if a > 10:
    print("i is more than 10")
else:
    print("Its Not Bigger Than Or Equals To 10")

# Full Condition
if a > 10:
    print("i is more than 10")
elif a == 10:
    print("i is suprisingly 10 !")
else:
    print("Its Not Bigger Than 10")

# You Can Compare Anything. no errors Will Happend.
if a == "Salam":
    print("a Says Salam !")


#! Bonus1
text = "Hello Arshia"
if text.split(" ")[1] == "Arshia":
    print("Hello Dear Admin!")
else:
    print(text)

#! Bonus2
super_admins = ["Arshia", "Reza"]
normal_admins = ["Ali", "Reza"]
if text.split(" ")[1] in super_admins:
    print("Welcome Dear Admin!")
elif text.split(" ")[1] in normal_admins:
    print("Hello Deer Admin!")
else:
    print("Welcome Loser XD")
