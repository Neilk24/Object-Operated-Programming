class IOString:
    
    def __init__(self):
        self.str1 = ''

    def get_string(self):
        self.str1 = input('Enter a string: ')

    def upper_string(self):
        print('String in uppercase is ', self.str1.upper())

obj = IOString()
obj.get_string()
obj.upper_string()