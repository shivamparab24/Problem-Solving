-- Find departments whose average employee salary is greater than the company-wide average salary.


SELECT
    d.department_id,
    d.department_name,
    dept.dept_avg_salary
FROM 
    departments d
join (
    -- dept average salary
    SELECT
        department_id,
        avg(salary) as dept_avg_salary
    FROM employees
    group by department_id
) as dept
on d.department_id = dept.department_id
-- overall avg salary
where dept.dept_avg_salary > (
    SELECT avg(salary) 
    from employees
);