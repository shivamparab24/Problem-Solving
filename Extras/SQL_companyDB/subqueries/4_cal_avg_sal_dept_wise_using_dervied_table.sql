-- Calculate average salary department-wise using a derived table.

select
    d.department_id,
    round(avg_salary, 4)
from (
    select 
        department_id,
        avg(salary) as avg_salary
    from employees
    group by department_id
) as a
inner join departments d
on d.department_id = a.department_id
;