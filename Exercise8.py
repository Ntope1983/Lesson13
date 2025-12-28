# CRUD with dictionary
students = [{"name": "john",
             "Surname": "Polydoras",
             "FatherName": "Konstantinos",
             "Age": 42,
             "Class": 1,
             "idCard": 1038942,
             "id": 1000},
            {"name": "Maria",
             "Surname": "Papadopoulou",
             "FatherName": "Georgios",
             "Age": 21,
             "Class": 1,
             "idCard": 2038451,
             "id": 1001},
            {"name": "Nikos",
             "Surname": "Dimitriou",
             "FatherName": "Alexandros",
             "Age": 22,
             "Class": 2,
             "idCard": 2038452,
             "id": 1002},
            {"name": "Giannis",
             "Surname": "Papadopoulos",
             "FatherName": "Vasilis",
             "Age": 24,
             "Class": 5,
             "idCard": 2035456,
             "id": 1003},
            {"name": "Georgios",
             "Surname": "Papadopoulos",
             "FatherName": "Ioannis",
             "Age": 45,
             "Class": 3,
             "idCard": 2325452,
             "id": 1004}]


def check_student(x, y, z):
    for stud in students:
        if stud["name"].lower() == x.lower() and stud["Surname"].lower() == y.lower() and stud[
            "FatherName"].lower() == z.lower():
            print("The student you entered already exists:")
            print_student_details(stud["id"], False)
            return True
    return False


def print_student_details(student_id=None, all_students=False):
    if student_id is not None:
        for student in students:
            if student["id"] == int(student_id):
                print(
                    f"id: {student['id']} "
                    f"Name: {student['name']} "
                    f"Surname: {student['Surname']} "
                    f"FatherName: {student['FatherName']} "
                    f"Age: {student['Age']} "
                    f"Class: {student['Class']} "
                    f"idCard: {student['idCard']}"
                )
                return
        print(f"Student with id {student_id} not found.")
    elif all_students:
        for student in students:
            print(
                f"id: {student['id']} "
                f"Name: {student['name']} "
                f"Surname: {student['Surname']} "
                f"FatherName: {student['FatherName']} "
                f"Age: {student['Age']} "
                f"Class: {student['Class']} "
                f"idCard: {student['idCard']}"
            )
    else:
        for student in students:
            print(f"{student['name']} {student['FatherName'][0]} {student['Surname']}")


def get_name():
    while True:
        name = input("Enter name: ").strip()
        if not name:
            print("Name must not be empty.")
        elif not name.isalpha():
            print("Name must contain only letters.")
        else:
            return name


def get_surname():
    while True:
        surname = input("Enter surname: ").strip()
        if not surname:
            print("Surname must not be empty.")
        elif not surname.isalpha():
            print("Surname must contain only letters.")
        else:
            return surname


def get_fathername():
    while True:
        fathername = input("Enter father name: ").strip()
        if not fathername:
            print("Father name must not be empty.")
        elif not fathername.isalpha():
            print("Father name must contain only letters.")
        else:
            return fathername


def get_age():
    while True:
        age_input = input("Enter age: ").strip()
        if age_input.isdigit() and int(age_input) > 0:
            return int(age_input)
        else:
            print("Age must be a positive integer.")


def get_class():
    while True:
        class_input = input("Enter class (1-6): ").strip()
        if class_input.isdigit() and 1 <= int(class_input) <= 6:
            return int(class_input)
        else:
            print("Class must be an integer between 1 and 6.")


def get_id_card():
    while True:
        id_card = input("Enter ID card: ").strip()
        if id_card.isalnum():
            return id_card
        else:
            print("ID Card must contain only letters and numbers.")


def get_id():
    while True:
        id_student = input("Enter student ID: ").strip()
        if id_student.isdigit():
            return int(id_student)
        else:
            print("ID must contain only numbers.")


def insert_student():
    name = get_name()
    surname = get_surname()
    fathers_name = get_fathername()
    if check_student(name, surname, fathers_name):
        option_2 = input("Do you want to continue with these details? 1:Yes 2:No ")
        if option_2 == "2":
            print("Exit without saving.")
            return
    age = get_age()
    class1 = get_class()
    idcard = get_id_card()
    students.append({
        "name": name,
        "Surname": surname,
        "FatherName": fathers_name,
        "Age": age,
        "Class": class1,
        "idCard": idcard,
        "id": next_id()
    })


def next_id():
    return max(student["id"] for student in students) + 1


def get_valid_input(last_number):
    while True:
        try:
            value = int(input(f"Enter a number (1 to {last_number}): "))
            if 1 <= value <= last_number:
                return value
            else:
                print(f"Number must be between 1 and {last_number}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def search_pupil_by_surname(surname):
    return [student for student in students if student["Surname"].lower() == surname.lower()]


def update_pupil_by_id(id_update):
    update_student = None
    for student in students:
        if student["id"] == int(id_update):
            update_student = student
            break
    if update_student is None:
        print("Student not found!")
        return

    print("--------------------------------")
    print("Choose the field you want to update:")
    menu = ["1: Name", "2: Surname", "3: FatherName", "4: Age", "5: Class", "6: ID Card"]
    for option in menu:
        print(option, end="  ")
    choice = get_valid_input(6)
    if choice == 1:
        update_student["name"] = get_name()
    elif choice == 2:
        update_student["Surname"] = get_surname()
    elif choice == 3:
        update_student["FatherName"] = get_fathername()
    elif choice == 4:
        update_student["Age"] = get_age()
    elif choice == 5:
        update_student["Class"] = get_class()
    else:
        update_student["idCard"] = get_id_card()
    print(f"Student with ID {id_update} has been updated.")


def delete_pupil_by_id(pupil_id):
    for student in students:
        if student["id"] == int(pupil_id):
            students.remove(student)
            print(f"Student with ID {pupil_id} has been deleted.")
            return
    print(f"Student with ID {pupil_id} not found.")

def show_menu_search_id_surname():
    menu3 = {1: "Search by Surname",
             2: "Search by ID"}
    for option in menu3:
        print(f"{option}: {menu3[option]}")
    choose_option3 = get_valid_input(2)
    if choose_option3 == 1:
        surname_list = search_pupil_by_surname(get_surname())
        if len(surname_list) == 0:
            print("Student not found.")
            return None
        elif len(surname_list) > 1:
            print("More than one student with this surname. Enter ID to update.")
            for item in surname_list:
                print_student_details(item["id"], True)
            return get_id()
        else :
            return surname_list[0]["id"]
    else:
        return get_id()




def main():
    menu = {1: "Create Student Record",
            2: "Print",
            3: "Update Record",
            4: "Delete Record",
            5: "Exit"}
    while True:
        print("\n------ MENU ------")
        for option in menu:
            print(f"{option}: {menu[option]}")
        choose_option = get_valid_input(5)

        if choose_option == 1:
            insert_student()
        elif choose_option == 2:
            menu2 = {1: "Print Single Student",
                     2: "Print All Students",
                     3: "Print Only Names"}
            for option in menu2:
                print(f"{option}: {menu2[option]}")
            choose_option2 = get_valid_input(3)
            if choose_option2 == 1:
                std_id = get_id()
                print_student_details(std_id, False)
            elif choose_option2 == 2:
                print_student_details(all_students=True)
            elif choose_option2 == 3:
                print_student_details()
        elif choose_option == 3:
            menu3 = {1: "Search by Surname",
                     2: "Search by ID"}
            for option in menu3:
                print(f"{option}: {menu3[option]}")
            choose_option3 = get_valid_input(2)
            if choose_option3 == 1:
                surname_list = search_pupil_by_surname(get_surname())
                if len(surname_list) == 0:
                    print("Student not found.")
                elif len(surname_list) > 1:
                    print("More than one student with this surname. Enter ID to update.")
                    for item in surname_list:
                        print_student_details(item["id"], True)
                    update_pupil_by_id(get_id())
                else:
                    update_pupil_by_id(surname_list[0]["id"])
            elif choose_option3 == 2:
                choose_id = get_id()
                print_student_details(choose_id, False)
                update_pupil_by_id(choose_id)
        elif choose_option == 4:
            menu4 = {1: "Search by Surname",
                     2: "Search by ID"}
            for option in menu4:
                print(f"{option}: {menu4[option]}")
            choose_option4 = get_valid_input(2)
            if choose_option4 == 1:
                surname_list = search_pupil_by_surname(get_surname())
                if len(surname_list) == 0:
                    print("Student not found.")
                elif len(surname_list) > 1:
                    print("More than one student with this surname. Enter ID to delete.")
                    for item in surname_list:
                        print_student_details(item["id"], True)
                    delete_pupil_by_id(get_id())
                else:
                    delete_pupil_by_id(surname_list[0]["id"])
            elif choose_option4 == 2:
                choose_id = get_id()
                print_student_details(choose_id, False)
                delete_pupil_by_id(choose_id)
        elif choose_option == 5:
            print("Exiting program...")
            break

show_menu_search_id_surname()
main()
