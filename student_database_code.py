from multiprocessing import Value
import random

used_id = []

def generate_id(min, max):
    while(True):
        identification = random.randint(min, max)
        if identification not in used_id:
            used_id.append(identification)
            return identification
        else:
            pass
    
students = [{
    "name": "Seb",
    "grades": [90.0,95.0,100.0],
    "id": generate_id(1000,9999 )
    },{
    "name": "Ben",
    "grades": [82.0,88.0,94.0],
    "id": generate_id(1000,9999 )
    },{
    "name": "Andre",
    "grades": [81.0,85.0,96.0],
    "id": generate_id(1000,9999 )
    },{
    "name": "Josh",
    "grades": [90.0,91,93.0],
    "id": generate_id(1000,9999 )
    }]

def add_student(student_list):
    student_prefab = {
    "name": input("student name: "),
    "grades": [],
    "id": generate_id(1000,9999)
    }
    student_list.append(student_prefab)
    return print("added student")

def add_grade(student_list):
    if not student_list:
        return print("no students in database")
    student = input("Which student do you want to add to (name or id): ")
    try:
        student_id = int(student)
    except ValueError:
        student_id = None
    try:
        grade = float(input("Grade to add: "))
    except ValueError:
        return print("invalid value")
    
    for student_index in student_list:
        if student == student_index["name"] or student_id == student_index["id"]:
            if grade >= 0 and grade <= 100:
                student_index["grades"].append(grade)
                return print("grade added")
            else:
                return print("Invalid grade, must be between 0-100")
    return print("student not found")
        
def display_students(student_list):
    if not student_list:
        return print("no students in database")
    for student_index in student_list:
        print(f'id: {student_index["id"]} - name: {student_index["name"]} - grades: {student_index["grades"]}')
    return print("students displayed")
    
def display_averages(student_list):
    if not student_list:
        return print("no students in database")
    for student_index in student_list:
        current_average = 0
        grade_amount = 0
        if not student_index["grades"]:
            print(f'id: {student_index["id"]} - name: {student_index["name"]} - average grade: no grades')
            continue
        for grade_index in student_index["grades"]:
            if grade_index > 0:
                current_average += grade_index
            grade_amount += 1
        if current_average <= 0:
            print(f'id: {student_index["id"]} - name: {student_index["name"]} - average grade: invalid average')
        else:
            print(f'id: {student_index["id"]} - name: {student_index["name"]} - average grade: {(current_average / grade_amount)}')
            
def adjust_grades(student_list, grade_adjustment):
    if not student_list:
        return print("no students in database")
    for student_index in student_list:
        if student_index["grades"]:
            for grade_index in range(len(student_index["grades"])):
                student_index["grades"][grade_index] += float(grade_adjustment)
                if student_index["grades"][grade_index] > 100:
                    student_index["grades"][grade_index] = 100
                elif student_index["grades"][grade_index] < 0:
                    student_index["grades"][grade_index] = 0
    return print("grades adjusted")


def filter_averages(student_list, minimum):
    if not student_list:
        return print("no students in database")
    for student_index in student_list:
        current_average = 0
        grade_amount = 0
        if not student_index["grades"]:
            continue
        for grade_index in student_index["grades"]:
            if grade_index > 0:
                current_average += grade_index
            grade_amount += 1
        if current_average <= 0:
            continue
        elif current_average / grade_amount >= minimum:
            print(f'id: {student_index["id"]} - name: {student_index["name"]} - average grade: {(current_average / grade_amount)}')
            
def display_top_bottom(student_list):
    top_student = None
    top_student_average = None
    bottom_student = None
    bottom_student_average = None
    if not student_list:
        return print("no students in database")
    for student_index in student_list:
        current_average = 0
        grade_amount = 0
        if not student_index["grades"]:
            continue
        for grade_index in student_index["grades"]:
            if grade_index > 0:
                current_average += grade_index
            grade_amount += 1
        if current_average <= 0:
            continue
        elif not top_student:
            top_student = student_index
            top_student_average = current_average / grade_amount
        elif not bottom_student:
            bottom_student = student_index
            bottom_student_average = current_average / grade_amount
        elif current_average / grade_amount > top_student_average:
            top_student = student_index
            top_student_average = current_average / grade_amount
        elif current_average / grade_amount < bottom_student_average:
            bottom_student = student_index
            bottom_student_average = current_average / grade_amount
        else:
            continue
    print(f'id: {top_student["id"]} - name: {top_student["name"]} - average grade: {(top_student_average)}')
    print(f'id: {bottom_student["id"]} - name: {bottom_student["name"]} - average grade: {(bottom_student_average)}')
            
def delete_student(student_list):
    try:
        id_selection = int(input("Select ID to remove: "))
    except ValueError:
        print("ID must be an integer")
        return

    for student_index in range(len(student_list)):
        if id_selection == student_list[student_index]["id"]:
            student_list.pop(student_index)
            return print("removed student")
    return print("student not found")   

def count_students(student_list):
    student_count = 0
    for student_index in range(len(student_list)):
        student_count += 1
    return print(f"student count: {student_count}")

def user_loop():
    while(True):
        user = input(">>> ")
        if user == "add student":
            add_student(students)
            continue
        elif user == "add grade":
            add_grade(students)
            continue
        elif user == "display":
            display_students(students)
            continue
        elif user == "display averages":
            display_averages(students)
            continue
        elif user == "adjust grades":
            try:
                grade_add = float(input("grade adjustment: "))
            except ValueError:
                print("invalid value")
                continue
            adjust_grades(students, grade_add)
            continue
        elif user == "filter averages":
            try:
                minimum_grade = float(input("minimum grade: "))
            except ValueError:
                print("invalid value")
                continue
            filter_averages(students, minimum_grade)
            continue
        elif user == "top/bottom students":
            display_top_bottom(students)
            continue
        elif user == "delete":
            delete_student(students)
            continue
        elif user == "count students":
            count_students(students)
            continue
        elif user == "leave":
            print("left program")
            break
        else:
            print("command not found")
            continue
        
user_loop()
