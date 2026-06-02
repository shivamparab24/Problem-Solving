-- Find all employees whose salary is greater than the average salary of all employees.

select employee_id, salary
from employees
where salary > (
    select avg(salary)
    from employees
)