-- Find employees who are assigned to every project in the company.


SELECT
    e.employee_id,
    e.first_name
FROM employees e

-- For the current employee...
WHERE NOT EXISTS (

    -- Find projects for which the employee has NO assignment
    SELECT 1
    FROM projects p

    WHERE NOT EXISTS (

        -- Check if an assignment exists between
        -- the current employee and the current project
        SELECT 1
        FROM employee_projects ep
        WHERE ep.employee_id = e.employee_id
          AND ep.project_id = p.project_id
    )
);