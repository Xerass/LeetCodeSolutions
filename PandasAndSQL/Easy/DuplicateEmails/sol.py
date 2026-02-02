# Write your MySQL query statement below
SELECT
#select col of concern, then get counts of unique values
email
FROM
Person
GROUP BY
#group counts exclusively by email
email
HAVING
#check if counts exceed 1
COUNT(*) > 1;
