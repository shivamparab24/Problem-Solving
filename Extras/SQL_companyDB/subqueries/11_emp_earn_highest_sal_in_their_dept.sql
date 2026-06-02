-- Find employees who earn the highest salary in their department.


SELECT 
    employee_id,
    first_name,
    department_id,
    salary
from employees e
where salary = (
    select max(salary)
    from employees
    where e.department_id = department_id
)


SELECT 
    e.employee_id,
    e.first_name,
    e.department_id,
    e.salary
FROM employees e
JOIN (
    SELECT 
        department_id,
        MAX(salary) AS max_salary
    FROM employees
    GROUP BY department_id
) d
ON e.department_id = d.department_id
AND e.salary = d.max_salary;