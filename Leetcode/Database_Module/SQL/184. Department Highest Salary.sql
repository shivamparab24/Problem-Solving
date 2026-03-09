-- Table: Employee

-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | id           | int     |
-- | name         | varchar |
-- | salary       | int     |
-- | departmentId | int     |
-- +--------------+---------+
-- id is the primary key (column with unique values) for this table.
-- departmentId is a foreign key (reference columns) of the ID from the Department table.
-- Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

-- Table: Department

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- +-------------+---------+
-- id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
-- Each row of this table indicates the ID of a department and its name.
 

-- Write a solution to find employees who have the highest salary in each of the departments.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Employee table:
-- +----+-------+--------+--------------+
-- | id | name  | salary | departmentId |
-- +----+-------+--------+--------------+
-- | 1  | Joe   | 70000  | 1            |
-- | 2  | Jim   | 90000  | 1            |
-- | 3  | Henry | 80000  | 2            |
-- | 4  | Sam   | 60000  | 2            |
-- | 5  | Max   | 90000  | 1            |
-- +----+-------+--------+--------------+


-- Department table:
-- +----+-------+
-- | id | name  |
-- +----+-------+
-- | 1  | IT    |
-- | 2  | Sales |
-- +----+-------+


-- Output: 
-- +------------+----------+--------+
-- | Department | Employee | Salary |
-- +------------+----------+--------+
-- | IT         | Jim      | 90000  |
-- | Sales      | Henry    | 80000  |
-- | IT         | Max      | 90000  |
-- +------------+----------+--------+

-- Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.


-- approach 1
select d.name as department, e.name as employee, e.salary as salary
from employee e
join department d
on e.departmentid = d.id
where e.salary = (select max(salary) from employee where departmentId = e.departmentId)



-- approach 2 with CTE
with MaxDeptSal as (
    select departmentid, max(salary) as max_salary
    from employee 
    group by departmentid
)

select d.name as department, e.name as employee, e.salary as salary
from employee e
inner join maxdeptsal m
    on e.departmentid = m.departmentid
    and e.salary = m.max_salary
inner join department d 
    on e.departmentid = d.id;



-- approach 3 with window func using cte
with ranked_salary as (
    select *,
           max(salary) over (partition by departmentid) as max_salary
    from employee
)

select d.name as department,
       e.name as employee,
       e.salary as salary
from ranked_salary e
join department d
    on e.departmentid = d.id
where e.salary = e.max_salary;