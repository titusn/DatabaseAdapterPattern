from employee_repository import EmployeeRepository
from employee_repository_stub import EmployeeRepositoryStub


class RepoStubFactory:
    @staticmethod
    def get_repo() -> EmployeeRepository:
        return EmployeeRepositoryStub()
