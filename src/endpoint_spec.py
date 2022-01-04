from fastapi import HTTPException
from mamba import description, it, context, before
from expects import expect, equal, raise_error, have_len, be_an

from endpoint import EmployeeEndpoint
from employee import Employee
from repo_stub_factory import RepoStubFactory



with description(EmployeeEndpoint) as self:

    with before.each:
        repo = RepoStubFactory.get_repo()
        self.endpoint = EmployeeEndpoint(repo=self.repo)

    with context("Health service endpoint"):
        with it("returns pong after ping"):
            expect(self.endpoint.ping()).to(equal("Pong"))

    with context("Employees endpoint"):
        with it("returns by default all employees"):
            expect(self.endpoint.list_all_employees(repo=self.repo)).to(have_len(3))

        with it("throws an exception if Employee ID does not exist"):
            expect(lambda: self.endpoint.get_employee_by_id("_non-existent-id_", repo=self.repo)).to(raise_error(HTTPException))

        with it("returns employee by id"):
            employee = self.endpoint.get_employee_by_id("001", repo=self.repo)
            expect(employee).to(be_an(Employee))
