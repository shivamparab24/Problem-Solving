-- Display every employee along with the total number of departments in the company.


SELECT
    employee_id,
    first_name,
    (select count(*)
    from departments) as total_departments
from employees
;