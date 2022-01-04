from employee_repository import EmployeeRepository
from employee_repository_replit_db import EmployeeRepositoryReplitDb


class ReplitRepoFactory:
    @staticmethod
    def get_repo() -> EmployeeRepository:
        return EmployeeRepositoryReplitDb()
