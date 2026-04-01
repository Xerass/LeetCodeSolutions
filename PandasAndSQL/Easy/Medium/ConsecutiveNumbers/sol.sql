# Write your MySQL query statement below
#we can use windowing tech
WITH Nums AS (
    #here we can use LAG, to see past 1 then past 2
    SELECT
    #select the number and the past 3 ones
    num,
    LAG(num, 1) OVER (ORDER BY id) AS prev_num,
    LAG(num, 2) OVER (ORDER BY id) AS prev_prev_num

    FROM Logs
)
#then we select over that
SELECT DISTINCT num AS ConsecutiveNums
#get from newly generated table
FROM Nums
WHERE num = prev_num AND num = prev_prev_num
