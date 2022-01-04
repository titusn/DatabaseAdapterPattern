from fastapi import FastAPI, HTTPException, Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from employee_repository import EmployeeRepository
from replit_repo_factory import ReplitRepoFactory

app = FastAPI()
router = InferringRouter()
repository = ReplitRepoFactory.get_repo()


@cbv(router)
class EmployeeEndpoint:
    @router.get("/")
    def ping(self) -> str:
        return 'Pong'

    @router.get("/employees")
    def list_all_employees(self, repo: EmployeeRepository = Depends(repository)):
        return repo.all()

    @router.get("employees/{employee_id}")
    def get_employee_by_id(self, employee_id: str, repo: EmployeeRepository = Depends(repository)):
        result = repo.get_by_id(employee_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        else:
            return result
