class User:

    def login(self):
        print("User logged in")

    def register(self):
        print("User registered")



class Student(User):
    pass



Hussain = Student()

# child class can access the parent's class public methods and public attributes but not private methods and private attributes.
Hussain.login()
Hussain.register()