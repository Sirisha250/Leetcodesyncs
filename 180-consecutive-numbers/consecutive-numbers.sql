SELECT num AS ConsecutiveNums
FROM (
    SELECT num, 
           LEAD(num, 1) OVER (ORDER BY id) AS next_num,
           LEAD(num, 2) OVER (ORDER BY id) AS next_num_2
    FROM Logs
) AS subquery
WHERE num = next_num AND num = next_num_2
GROUP BY num;
