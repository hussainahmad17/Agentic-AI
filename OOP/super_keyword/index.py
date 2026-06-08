class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(f"{self.name} has logged in.")

    def logout(self):
        print(f"{self.name} has logged out.")



class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)  # Call the constructor of the parent class
        self.student_id = student_id

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}, Student ID: {self.student_id}")



hussain = Student("Hussain", "hussain@example.com", "S001")
hussain.display_info()