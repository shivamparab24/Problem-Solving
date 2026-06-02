-- Find employees whose salary is greater than every employee in department 3.

select
    employee_id,
    first_name,
    salary
FROM employees
where salary > ALL (
    select salary
    from employees
    where department_id = 3
)