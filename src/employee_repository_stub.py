from employee_repository import  EmployeeRepository
from employee import Employee


class EmployeeRepositoryStub(EmployeeRepository):
    def __init__(self):
        self.employees_by_id = {
            "001": Employee("Darren"),
            "002": Employee("Atharva"),
            "003": Employee("Misbah")
        }

    def all(self) -> [Employee]:
        return self.employees_by_id.values()

    def get_by_id(self, employee_id: str) -> Employee:
        if employee_id in self.employees_by_id:
            return self.employees_by_id[employee_id]
