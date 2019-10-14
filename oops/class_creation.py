
class Employee:
    def __init__(self, name, id, address, contact_number):
        self.employee_name = name
        self.employee_id = id
        self.employee_address = address
        self.employee_contect_no = contact_number

    def display(self):
        print('Employee Name \t:\t', self.employee_name)
        print('Employee ID \t:\t', self.employee_id)
        print('Employee Address \t:\t', self.employee_address)
        print('Employee Contact No \t:\t', self.employee_contect_no)

    def get_emp_details(self):
        return {'employee_name':self.employee_name, 'employee_id':self.employee_id,
                'employee_address':self.employee_address, 'employee_contact_no':self.employee_contect_no}


class Branch(Employee):
    def __init__(self, employee_name, employee_id, employee_address, contact_number,
                 branch_name, branch_id, branch_location, branch_city, branch_state, branch_country):
        super().__init__(employee_name, employee_id, employee_address, contact_number)
        self.branch_name = branch_name
        self.branch_id = branch_id
        self.branch_location = branch_location
        self.branch_city = branch_city
        self.branch_state = branch_state
        self.branch_country = branch_country

    def dislay(self):
        super().display()
        print('Branch Name \t:\t',self.branch_name)
        print('Branch ID \t:\t',self.branch_id)
        print('Branch Location \t:\t',self.branch_location)
        print('Branch City \t:\t',self.branch_city)
        print('Branch State \t:\t',self.branch_state)
        print('Branch Country \t:\t',self.branch_country)

    def get_branch_details(self):
        return  {'branch_name':self.branch_name, 'branch_id':self.branch_id, 'branch_location':self.branch_location,
                 'branch_city':self.branch_city, 'branch_state':self.branch_state, 'branch_country':self.branch_country}


class Department(Branch,Employee):
    def __init__(self, employee_name, employee_id, employee_address, contact_number,
                 branch_name, branch_id, branch_location, branch_city, branch_state, branch_country,
                 department_name, department_id):
        super().__init__(employee_name, employee_id, employee_address, contact_number,
                 branch_name, branch_id, branch_location, branch_city, branch_state, branch_country)
        self.department_name = department_name
        self.department_id = department_id

    def display(self):
        super().dislay()
        print('Department Name \t:\t',self.department_name)
        print('Department ID \t:\t',self.department_id)

    def get_department_details(self):
        return {'department_name':self.department_name, 'department_id':self.department_id}

    def get_emp_details(self):
        li = super().get_emp_details()
        li.update(super().get_branch_details())
        li.update(self.get_department_details())
        return li


dept = Department('Subramanyam Vegi', 'PSI-1931', 'Rajampet', '8142642684',
                  'BLR-1', 'BLR-1','Kormangalla', 'Bangalore', 'Karnataka', 'India',
                  'Software Engineer-II', 'SE-II')
# dept.display()
print(dept.get_emp_details())

