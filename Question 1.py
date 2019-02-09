class Employee:
    count = 0
    total_salary = 0

    def __init__(self,n,f,s,d):
        self.name       = n
        self.family     = f
        self.salary     = s
        self.department  = d
        Employee.count += 1
        Employee.total_salary += s


    def get_count(self):
        print("Number of Employees: ", self.count)

    def average_salary(self):
        print("Average salary: ", (self.total_salary/self.count))

    def get_name(self):
        print("Name: ", self.name)

    def get_family(self):
        print("Family: ", self.family)

    def get_salary(self):
        print("Salary: ", self.salary)

    def get_department(self):
        print("department: ", self.department)


class FulltimeEmployee(Employee):
    fcount = 0

    def __init__(self,n,f,s,d):
        self.name       = n
        self.family     = f
        self.salary     = s
        self.department  = d
        self.fcount += 1
        self.total_salary += self.salary

    def get_count(self):
        print("Number of Full Time Employees: ", self.fcount)

    def average_salary(self):
        print("Average salary: ", (self.total_salary/self.fcount))

x = Employee("Bob", "Smith", 5000, "Clerk")
y = Employee("Amy", "Brooks", 4500, "Clerk")
z = Employee("John", "Doe", 6000, "Clerk" )
a = FulltimeEmployee("Jane", "Doe", 30000, "Manager")

x.get_count()
x.get_name()
x.get_family()
x.get_department()
x.average_salary()
print('')
a.get_count()
a.get_name()
a.get_family()
a.get_department()
a.average_salary()