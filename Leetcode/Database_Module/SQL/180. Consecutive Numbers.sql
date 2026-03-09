-- Table: Logs

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | num         | varchar |
-- +-------------+---------+
-- In SQL, id is the primary key for this table.
-- id is an autoincrement column starting from 1.
 

-- Find all numbers that appear at least three times consecutively.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Logs table:
-- +----+-----+
-- | id | num |
-- +----+-----+
-- | 1  | 1   |
-- | 2  | 1   |
-- | 3  | 1   |
-- | 4  | 2   |
-- | 5  | 1   |
-- | 6  | 2   |
-- | 7  | 2   |
-- +----+-----+
-- Output: 
-- +-----------------+s
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+
-- Explanation: 1 is the only number that appears consecutively for at least three times.




-- approach 1
select distinct num as ConsecutiveNums
from (
    select
        num,
        lead(num, 1) over (order by id) as num1,
        lead(num, 2) over (order by id) as num2
    from logs
) t
where num = num1 and num = num2;



-- approach 2
select distinct a.num as ConsecutiveNums 
from logs a
join logs b on a.id = b.id + 1 and a.num = b.num
join logs c on a.id = c.id + 2 and a.num = c.num