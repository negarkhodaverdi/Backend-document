# ?##################################################################?#
# ? Simple Functions
def test():
    print("Hello World !")


test()  # Call The Function

# ?##################################################################?#
# ? Condition With Return State


def test():
    return "Hello"


test()  # Nothing Will Happend !
print(test())  # It Will Print "Hello"
# ?##################################################################?#

# ?##################################################################?#
# Condition With Input And No Return


def sum(a, b):
    print(a + b)


sum(1, 2)  # Prints The Answer.
print(sum(1, 2))  # Prints Answer,After That Prints None.
# ?##################################################################?#

# ?##################################################################?#
# ? Condition With Input And Return


def sum(a, b):
    return a + b


sum(1, 2)  # Nothing Happends
print(sum(1, 2))  # Prints Answer.
# ?##################################################################?#

# *##################################################################*#
"""
! Difference Between A Function With Return And Without Return

Sometimes You Need The Value In A Function. For Example :
*   numbers = [1,2,3,4]
*   sum1 = sum(1,2)
*   sum2 = sum(3,4)
*   answer = sum(sum1,sum2)

Here We Can Get Value Just When We Return The Sum.
For Example Function Must Be Like :

*   def sum(a,b):
*       return a + b
"""
# *##################################################################*#

######################################################################
# Another Type Of Functions And Function Calls.


def divide(a, b):
    return a / b


value1 = divide(10, 5)
value2 = divide(b=5, a=20)  # In Fact Its Like ( divide(20,5) )
print(value1 + value2)


def print_values(*args, **kwargs):
    print(args, kwargs)
    print(*args)
    print(args[1])  # Prints Second Argument
    print(kwargs["name"])  # Prints Value Of "name" If Exists.
    # ? You Can Use **kwargs But Not With Print. You Will Get That In Future


print_values(22, 17.6, name="arshia", family="tamimi",
             instagram_id="...")
######################################################################
