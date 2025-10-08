# Classes and Objects in Python

# Defining a simple class
class Student:
    # Constructor to initialize attributes
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    # Method to display student details
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Grade: {self.grade}")

    # Method to update grade
    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"{self.name}'s grade updated to {self.grade}")


# Creating objects of the Student class
student1 = Student("Sahil", 101, "A")
student2 = Student("Priya", 102, "B")

# Accessing class methods
student1.display_info()
print()  # For better spacing
student2.display_info()

print("\n--- Updating Grade ---")
student2.update_grade("A+")

print("\n--- Updated Student Info ---")
student2.display_info()
