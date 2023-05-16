import employee
emp_id_generator = 0

def greeting(emp):
    print(f"Hello {emp.firstname} {emp.lastname}")
    print("It's your birthday!")
    emp.age = emp.age + 1
    print(f"You are now {emp.age} years old!")


def adder(number):
    number = number + 1
    print(f"{number}")
    return number


def get_age():
    age_as_string = input("Please enter your age as a number or 'q' to quit: ")
    if age_as_string.lower() == "q":
        print("OK, bye")
        exit(0)
    return age_as_string


def get_employee_details():
    global emp_id_generator
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    age_as_string = get_age()
    while not age_as_string.isnumeric():
        print(f"{first_name}'s age is not numeric. Have another go!")
        age_as_string = get_age()
    emp_id_generator = emp_id_generator + 1

    emp = employee.Employee(emp_id_generator, first_name, last_name, int(age_as_string))

    return emp


emps = {}
while True:
    emp = get_employee_details()
    emps[emp.id] = emp
    if input("Do you want to add another employee to the dictionary? Y/N").upper() == "N":
        break

emp = employee.Employee()
emps[emp.id] = emp

for emp_id in emps:
    emp = emps[emp_id]
    print(emp.get_credentials())
    emp.birthday()
    print(emp)

    emp = emps[1]

    # emp.set_age(256)
    emp.age = 256
    # print(emp.get_age())
    print(emp.age)
