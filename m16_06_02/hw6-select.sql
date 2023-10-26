SELECT 
    s.id, 
    s.fullname, 
    ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 5;

WITH StudentGrades AS (
    SELECT 
        s.id,
        s.fullname,
        ROUND(AVG(g.grade)) as average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    WHERE g.subject_id = 1  -- Предмет, з якого ви хочете знайти середній бал
    GROUP BY s.id
)
SELECT 
    id, 
	fullname, 
    average_grade
FROM StudentGrades
ORDER BY average_grade DESC
LIMIT 1;

SELECT 
    s.id, 
    s.fullname, 
    ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
where g.subject_id = 1
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;
