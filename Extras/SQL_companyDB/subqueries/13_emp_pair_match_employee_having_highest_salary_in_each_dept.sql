-- Find employees whose (department_id, salary) pair matches the employee having the highest salary in each department.


SELECT
    employee_id,
    first_name,
    department_id,
    salary
FROM
    employees e
WHERE (department_id, salary) IN (
    SELECT
        department_id,
        max(salary)
    FROM employees
    GROUP BY department_id
)