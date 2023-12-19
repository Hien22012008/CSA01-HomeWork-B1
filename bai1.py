class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def say_hi(self):
        print('Hi, my name is', self.name)
    
    def tell_position(self):
        print('I am a', self.position)

employee = Employee('John', 'Software Engineer')

employee.say_hi()
employee.tell_position()
