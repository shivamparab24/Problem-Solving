-- Find employees whose salary is greater than the average salary of their own department.



select
    employee_id,
    first_name,
    department_id,
    salary
from employees e
where salary > (
    select avg(salary)
    from employees
    where department_id = e.department_id
);




-- SELECT
--     employee_id,
--     first_name,
--     department_id,
--     salary,
--     round((
--         SELECT AVG(salary)
--         FROM employees
--         WHERE department_id = e.department_id
--     ), 3) AS dept_avg_salary
-- FROM employees e
-- WHERE salary > (
--     SELECT AVG(salary)
--     FROM employees
--     WHERE department_id = e.department_id
-- );




-- -- using window functions 
-- -- postgres does not allow window functions in where clause
-- select
--     employee_id,
--     first_name,
--     department_id,
--     salary,
--     AVG(salary) over (PARTITION BY department_id) as dept_avg_salary
-- FROM
--     employees e
-- -- where salary > AVG(salary) over (PARTITION BY department_id);
-- where salary > (
--         SELECT AVG(salary)
--         FROM employees
--         WHERE department_id = e.department_id
-- )


-- -- using CTE
-- WITH emp_avg AS (
--     SELECT
--         employee_id,
--         first_name,
--         department_id,
--         salary,
--         round(AVG(salary) OVER (PARTITION BY department_id), 2) AS dept_avg_salary
--     FROM employees
-- )
-- SELECT *
-- FROM emp_avg
-- WHERE salary > dept_avg_salary;