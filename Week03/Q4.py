#Q4
monday_class = {"Sana", "Karina", "Chaewon", "Winter", "Asa"}
wednesday_class = {"Karina", "Ningning", "Yujin", "Hanni", "Sana"}

monday_class.add("Ryujin")
print(f"Monday Class: {monday_class}")
print(f"Wednesday Class: {wednesday_class}")

print(f"Attended both classes: {monday_class & wednesday_class}")
print(f"Attended either classes: {monday_class | wednesday_class}")
print(f"Only Monday: {monday_class - wednesday_class}")
print(f"Only One Class: {monday_class ^ wednesday_class}")
allStudents = monday_class | wednesday_class
print("Is Monday subset of all students", monday_class <= allStudents)
