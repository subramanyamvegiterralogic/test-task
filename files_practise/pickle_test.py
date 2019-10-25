from files_practise import employee
import pickle
f = open('emp.dat','ab')
n = int(input("Enter the Number of Employees : "))
for i in range(n):
    eno = input('Employee Number : ')
    ename = input('Employee Name : ')
    location = input('Employee Location : ')
    e = employee.Employee(eno, ename, location)
    pickle.dump(e, f)
    print('Employee details Dumpped Successfully')