class Employee:
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.department = department

    def get_details(self):
        return f"[{self.emp_id}] {self.name} | {self.department} | ₹{self.salary}"

    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount

    def calculate_bonus(self):
        return 0.10 * self.salary


class Manager(Employee):
    def __init__(self, name, emp_id, salary, department, team_size):
        super().__init__(name, emp_id, salary, department)
        self.team_size = team_size

    def calculate_bonus(self):
        return 0.20 * self.salary

    def approve_leave(self, emp_name):
        return f"{self.name} approved leave for {emp_name}"


class Intern(Employee):
    def __init__(self, name, emp_id, salary, department, mentor):
        super().__init__(name, emp_id, salary, department)
        self.mentor = mentor

    def calculate_bonus(self):
        return 0.05 * self.salary

    def get_mentor(self):
        return f"{self.name}'s mentor is {self.mentor}"