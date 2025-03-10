class Employee:

    def __init__(self):
        print('This is a constuctor.')

    def __del__(self):
        print('This is a destructor.')

def create():
    obj = Employee()
    return obj

print(create())