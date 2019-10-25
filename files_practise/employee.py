class Employee:
    def __init__(self, eno, ename, location):
        self.eno = eno
        self.ename = ename
        self.location= location

    def display(self):
        print('Employee Name : ',self.ename,'\nEmployee No : ',self.eno,'\nLocation : ',self.location)

