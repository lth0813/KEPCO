SELECT *
FROM employees;
/*
SELECT 컬럼이름, 컬럼이름...
FROM 테이블 또는 뷰
WHERE 조건절
GROUP BY
ORDER BY employees
*/
SELECT department_id, AVG(salary)
FROM employees
GROUP BY department_id

SELECT *
FROM employees
ORDER BY first_name DESC;

SELECT *
FROM employees
WHERE employee_id =103;

SELECT 5*6
FROM DUAL

-- 급여가 5000 이상 10000 미만인 사원의 이름과 급여를 출력하시오

SELECT first_name, salary
FROM employees
WHERE salary > 5000 AND salary < 10000;

SELECT first_name, salary
FROM employees
WHERE salary BETWEEN 5000 and 10000
