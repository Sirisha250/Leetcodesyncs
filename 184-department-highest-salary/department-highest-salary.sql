WITH RankedEmployees AS (
    SELECT 
        d.name AS Department,
        e.name AS Employee,
        e.salary,
        RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS `rank`
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
)
SELECT Department, Employee, salary
FROM RankedEmployees
WHERE `rank` = 1;
