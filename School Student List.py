import pandas as pd

print("******************** Enter the Student name ********************")

def get_student_names():
    name_list = []
    while True:
        name = input("Enter the name: ")
        name_list.append(name)

        choice = input("Enter another name (y/n): ")
        if choice.lower() == "n":
            break
    return name_list
name_list = get_student_names()

print("******************** Enter the Student ID ********************")

def get_student_id():
    id_list = []
    while True:
        id = input("Enter the id: ")
        id_list.append(id)

        choice = input("Enter another id (y/n): ")
        if choice.lower() == "n":
            break
    return id_list
id_list = get_student_id()

print("******************** Enter the Student Age ********************")

def get_student_age():
    age_list = []
    while True:
        age = input("Enter the age: ")
        age_list.append(age)

        choice = input("Enter another id (y/n): ")
        if choice.lower() == "n":
            break
    return age_list
age_list = get_student_age()

print("******************** Enter the Student Gender ********************")

def get_student_gender():
    gender_list = []
    while True:
        gender = input("Enter the gender: ")
        gender_list.append(gender)

        choice = input("Enter another id (y/n): ")
        if choice.lower() == "n":
            break
    return gender_list
gender_list = get_student_gender()

print(f"\nStudent name list: {name_list}")
print(f"\nID name list: {id_list}")
print(f"\nAge name list: {age_list}")
print(f"\nGender name list: {gender_list}")

print("\n############################## Student list ##############################\n")

df = pd.DataFrame({
    "Student Name": name_list,
    "Student ID": id_list,
    "Student Age": age_list,
    "Student Gender": gender_list})

print(df) 

path=r"E:\python\pandasapp\output.xlsx"
with pd.ExcelWriter(path,mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
    df.to_excel(excel_writer=writer,sheet_name="sheet_1")
    
print("\n############################## Thank You  ##############################\n")