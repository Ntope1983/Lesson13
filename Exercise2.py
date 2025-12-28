# default value in argument and  keyword argument
def print_name(first_name, surname, second_name, details=False):
    if details:
        print("First Name: " + first_name + "-" + second_name)
        print("Surname: " + surname)
    else:
        print(f"{first_name}-{second_name} {surname}")


print_name("Charles", second_name="Bob", surname="Kane")
print_name("Charles", "Kane", "Bob", True)
