SELECT DISTINCT first_name /* DISTINCT 중복 제거*/
FROM employees;

SELECT first_name AS 사원이름
FROM employees;

SELECT first_name 사원이름 /* AS 삭제 가능 */
FROM employees;

SELECT first_name
FROM employees
WHERE first_name LIKE '%J%'; /* % :1번 이상 나올수 있고 안나와도됨, MYSQL은 대소문자 고분을 안함, Oracle은 대소문자 구분을 함 */

SELECT first_name
FROM employees
WHERE first_name LIKE '%a_'; /* _ : 반드시 나와야되고 1번만 옴 */

SELECT first_name, last_name
FROM employees
ORDER BY first_name, last_name DESC; /* First_name으로 정렬후 같은 이름이 있으면 Last_name으로 정렬, ASC(default) / DESC */

-- 1. First_name에 A가 들어가는 사원들의 이름을 출력하시오
SELECT first_name
FROM employees
WHERE first_name LIKE '%A%';

-- 2. 이름과 월급을 출력하는데 월급이 낮은사원부터 높은 사원순으로 출력하시오
SELECT first_name, salary
FROM employees
ORDER BY salary;

-- 3. 사원번호가 110인 사원의 First_name과 부서이름(Department_name)을 출력하시오
SELECT e.first_name, d.department_name
FROM employees e, departments d /* 테이블에 변수이름을 줄 때는 AS가 아닌 띄어쓰기로 부여한다 */
WHERE e.employee_id=110 AND e.department_id = d.department_id;

-- 4. 모든 사원의 First_name과 부서이름(Department_name)을 출력하시오
/* JOIN하는 컬럼에 Null 값이 있으면 출력되지 않으므로 OUTER JOIN으로 해결해야함 */
SELECT e.first_name, d.department_name
FROM employees e, departments d
WHERE e.department_id = d.department_id;

-- 4.1 모든 사원의 First_name과 부서이름(Department_name)을 출력하시오
SELECT e.first_name, d.department_name
FROM employees e JOIN departments d
ON e.department_id = d.department_id;

-- 5. 사원번호 108번인 사원의 이름과 사수의 이름, 사수의 사원번호를 출력하시오(SELF-JOIN)
/* SELF-JOIN을 할때는 반드시 변수명(익명)을 줘야함(같은 테이블이기 때문에 구별 해줘야함) */
SELECT e.first_name AS "사원이름", e2.first_name AS "사수이름", e2.employee_id AS "사원번호"
FROM employees e, employees e2
WHERE e.employee_id = 108 AND e.manager_id = e2.employee_id;

-- 6. First_name에 Z가 들어가는 사원의 이름과 부서이름을 출력하시오
SELECT e.first_name AS "사원이름", d.department_name AS "부서이름"
FROM employees e, departments d
WHERE e.first_name LIKE "%Z%" AND e.department_id = d.department_id;

-- 7. 부서이름(City)이 'Toronto'인 사원의 이름, 부서이름을 출력하시오
SELECT e.first_name AS "사원이름", d.department_name AS "부서이름"
FROM employees e, departments d, locations loc
WHERE loc.city = 'Toronto' AND loc.location_id = d.location_id AND e.department_id = d.department_id;

/* Null 값을 찾을때는 IS NULL or IS NOT NULL */
SELECT first_name
FROM employees
/* WHERE department_id = NULL -> 값이 안나옴 */
WHERE department_id IS NULL;

SELECT first_name, commission_pct
FROM employees
WHERE commission_pct IS NOT NULL;

-- 8. 모든 사원의 급여와 상여금(salary * commission_pct)을 출력하시오
SELECT first_name AS '사원이름', salary AS '급여', salary*ifnull(commission_pct,0) AS '상여금'
FROM employees;

SELECT first_name, department_id
FROM employees
WHERE department_id != 20; /* <>와 같음  */

-- 9. 부서이름(City)이 'Toronto'인 사원의 이름, 부서이름을 출력하시오 (JOIN이 아닌 서브쿼리로)
SELECT e.first_name, d.department_name
FROM employees e, departments d
WHERE e.department_id = d.department_id 
		AND d.location_id	=(SELECT location_id 
			  					  FROM locations 
			  					  WHERE city = 'Toronto');

-- 10. 평균 급여보다 많이 받는 사원의 이름과 급여를 출력하시오 (AVG : 평균 구하는 함수(자동으로 Null을 빼고함))
SELECT last_name AS '사원이름', salary AS '급여'
FROM employees
WHERE salary > (SELECT avg(salary)
					 FROM employees)
ORDER BY salary;

-- 11. 'Ernst'(Last_name)의 급여와 동일하거나 더 많이 받는 사원의 이름(Last_name)과 급여를 출력하시오
SELECT last_name, salary
FROM employees
WHERE salary >= (SELECT salary
					 FROM employees
					 WHERE last_name LIKE 'Ernst');

-- 12. 11번 문제를 JOIN으로 풀어보시오
SELECT e.last_name, e.salary
FROM employees e, employees e2
WHERE e2.last_name = 'Ernst' AND e.salary >= e2.salary;

-- 13. 부서번호가 30인 부서에 근무하는 사원들의 이름, 부서위치(City), 직급(Job_title)을 출력하시오
SELECT e.last_name, l.city, j.job_title
FROM employees e, locations l, jobs j, departments d
WHERE d.department_id = 30 AND e.department_id = d.department_id AND l.location_id = d.location_id AND j.job_id = e.job_id;

SELECT COUNT(*)
FROM employees
WHERE department_id = 30;

-- 14. 직급(Job_title)이 'Accountant'도 아니고 'Programmer'도 아닌 사람을 출력하시오
SELECT e.first_name, j.job_title
FROM employees e, jobs j
WHERE j.job_title != 'Accountant' AND j.job_title <> 'Programmer' AND j.job_id = e.job_id;

/* IN(NOT IN)은 or의 개념 */
SELECT e.first_name, j.job_title
FROM employees e, jobs j
WHERE j.job_title NOT IN ('Accountant','Programmer') AND j.job_id = e.job_id;

/* LIMIT(Num1,Num2) : 순서(0부터 시작) Num1 부터 Num2 개수 만큼 출력 */
SELECT first_name
FROM employees 
ORDER BY first_name
LIMIT 5,3;

/* OUTER JOIN */
SELECT e.first_name, d.department_name
FROM employees e LEFT OUTER JOIN departments d /* Default는 Inner, LEFT를 붙이면 OUTER는 생략가능 */
ON e.department_id = d.department_id;

/* FULL OUTER JOIN 형식으로 만들기 (형식만) */
SELECT e.first_name, d.department_name
FROM employees e LEFT OUTER JOIN departments d
ON e.department_id = d.department_id
UNION
SELECT e.first_name, d.department_name
FROM employees e RIGHT OUTER JOIN departments d
ON e.department_id = d.department_id;

-- 15. 모든 사원의 이름, 부서위치(City), 직급(Job_title)을 출력하시오
SELECT e.last_name, l.city, j.job_title
FROM employees e LEFT JOIN departments d 
ON e.department_id = d.department_id
LEFT JOIN locations l 
ON d.location_id = l.location_id
JOIN jobs j
ON e.job_id = j.job_id;

SELECT e.first_name, l.city, j.job_title
FROM employees e LEFT JOIN (departments d,locations l, jobs j)
ON e.department_id = d.department_id
AND d.location_id = l.location_id
AND e.job_id = j.job_id;
