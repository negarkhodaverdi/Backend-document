import random
import string

#############################################################


class test:
    """Simple Class"""
    pass


a = test()
a.name = "Arshia"
a.family = "Tamimi"
print(a.name)  # Arshia
print(a.family)  # Tamimi

#############################################################


class test:
    """Class With __init__"""

    def __init__(self):
        print("[+] Created New Instance")


a = test()  # Prints "[+] Created New Instance"
#############################################################


class User:
    """Class With __init__ And Arguments To Get"""

    def __init__(self, user_name, user_family, user_age):
        print("[+] Created New Instance")
        self.name = user_name
        self.family = user_family
        self.age = user_age


a = User("Arshia", "Tamimi", user_age=20)  # Prints "[+] Created New Instance"
a.name  # "Arshia"
a.family  # "Tamimi"
a.age  # 20
#############################################################


class User:
    """Class With Some Methods To Use"""

    def __init__(self, user_name, user_family, user_age):
        print("[+] Created New Instance")
        self.name = user_name
        self.family = user_family
        self.age = user_age
        self._registered = False

    def full_name(self):
        return self.name + " " + self.family

    def register(self, code):
        if code == "12345":
            self._registered = True
            print("[+] User Registered !")
            return True
        else:
            print("[-] Code Is Wrong :(")
            return False


a = User("Arshia", "Tamimi", user_age=20)  # Prints "[+] Created New Instance"
a.name  # "Arshia"
a.family  # "Tamimi"
a.age  # 20
a.full_name()  # "Arshia Tamimi"
a.register("12345")  # Prints "User Registered !" And Returns True
#############################################################


class Authorization(User):
    """Class With Interheit"""
    __AUTHORIZED_USERS = []

    def __init__(self, user_name, user_family, user_age, username, password):
        print("Trying To Save User...")
        super().__init__(user_name, user_family, user_age)
        self.username = username
        self.__password = password
        self.token = self.generate_token()
        self.logined = False
        print("User Saved.")

    def login(self, username, password):
        if not self._registered:
            print("[!] You Need To Register First.")
            return False
        if self.logined:
            print("[!] You Are Logined Now!")
            return False
        if username == self.username and password == self.__password:
            Authorization.__AUTHORIZED_USERS.append(self.username)
            return [True, self.token]
        else:
            return [False, ""]

    def logout(self):
        self.token = self.generate_token()

    def generate_token(self):
        token = ""
        for _ in range(30):
            token += random.choice(string.ascii_letters)
        return token

    @classmethod
    def get_registered_users(cls):
        print(f"{len(cls.__AUTHORIZED_USERS)} User Registered.")
        return cls.__AUTHORIZED_USERS


first_user = Authorization(user_name="Arshia", user_family="Tamimi",
                           user_age=22, username="Arshia", password="12345678")
print(first_user.full_name())  # Arshia Tamimi
print(first_user.register("12345"))  # Prints [+] User Registered !

# Returns [True, "Some Token"]
is_logined, token = first_user.login(username="Arshia", password="12345678")
if is_logined:
    print(f"""
          Yo ! You Are Loggined Now !
          Your Token Is :
          {token}
        """)
else:
    print("Sorry :( There Is Problem In Login:/")

print(Authorization.get_registered_users())
