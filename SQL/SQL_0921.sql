SELECT FIRST_NAME, SUBSTR(FIRST_NAME, 2, 2)
FROM employees;

SELECT FIRST_NAME, REPLACE(FIRST_NAME,'ex','AAAAAA')
FROM employees;

SELECT FIRST_NAME, DATEDIFF(NOW(),HIRE_DATE)
FROM employees;

-- 모든 사원의 근무 년수를 출력하시오(년수만 나오게) TRUNCATE, CONCAT 사용
SELECT CONCAT(FIRST_NAME,'의 근무 년수는 ', TRUNCATE(DATEDIFF(NOW(),HIRE_DATE) / 365,0),'년입니다.')
FROM employees;

SELECT CONCAT(FIRST_NAME,'의 근무 기간은 ', TRUNCATE(DATEDIFF(NOW(),HIRE_DATE) / 365,0),'년 ',TRUNCATE(MOD(DATEDIFF(NOW(),HIRE_DATE),365)/31,0),'개월입니다.')
FROM employees;

SELECT CONCAT(FIRST_NAME,'의 근무 기간은 ', TRUNCATE(DATEDIFF(NOW(),HIRE_DATE) / 365,0),'년 ',TRUNCATE(MOD(DATEDIFF(NOW(),HIRE_DATE),365)/31,0),'개월 ', 
MOD(MOD(DATEDIFF(NOW(),HIRE_DATE),365),31),'일입니다.')
FROM employees;

SELECT FIRST_NAME, SALARY,
CASE WHEN JOB_ID = 'IT_PROG' THEN SALARY * 1.1
	  WHEN JOB_ID = 'ST_MAN' THEN SALARY *1.2
	  WHEN JOB_ID = 'SA_MAN' THEN SALARY *1.3
	  ELSE SALARY
	  END AS "보너스 포함"
FROM employees;

SELECT FIRST_NAME, SALARY,
CASE JOB_ID 
	WHEN 'IT_PROG' THEN SALARY * 1.1
	WHEN 'ST_MAN' THEN SALARY *1.2
	WHEN 'SA_MAN' THEN SALARY *1.3
	ELSE SALARY
	END AS "보너스 포함"
FROM employees;

/* COUNT 함수 */
SELECT COUNT(*)
FROM employees;

SELECT COUNT(DEPARTMENT_ID)
FROM employees;

-- 사원들의 FIRST_NAME의 총 개수
SELECT COUNT(DISTINCT(FIRST_NAME))
FROM employees;

/* SUM, AVG, MAX, MIN 함수 */
SELECT SUM(SALARY)
FROM employees;

SELECT AVG(SALARY)
FROM employees;

SELECT MAX(SALARY)
FROM employees;

SELECT MIN(SALARY)
FROM employees;

/* 그룹함수
: 특정 속성(ATTRIBUTE)의 값이 같은 튜플을 모아 그룹을 만들어 그룹별 검색
: SELECT절에는 그룹으로 묶은 속성과 그룹함수만 사용 가능
: HAVING을 사용하여 GROUP BY절의 조건 작성 */

SELECT DEPARTMENT_ID, AVG(SALARY)
FROM employees
GROUP BY DEPARTMENT_ID;

SELECT FIRST_NAME, AVG(SALARY)
FROM employees
GROUP BY FIRST_NAME;

SELECT DEPARTMENT_ID, AVG(SALARY)
FROM employees
GROUP BY DEPARTMENT_ID
HAVING DEPARTMENT_ID = 30;
-- 부서 ID를 그룹으로 묶은 뒤 30번 부서를 가져온 것
SELECT DEPARTMENT_ID, AVG(SALARY)
FROM employees
WHERE DEPARTMENT_ID = 30
GROUP BY DEPARTMENT_ID;
-- 30번 부서만 가져와서 하나만 있는걸 그룹으로 묶은 것, 사실상 GROUP BY 절이 필요 없다.

-- 부서인원이 5인 이상인 부서의 평균급여를 구하시오
SELECT DEPARTMENT_ID "부서번호", COUNT(DEPARTMENT_ID) "부서인원", AVG(SALARY) "평균급여"
FROM employees
GROUP BY DEPARTMENT_ID
HAVING COUNT(*) >= 5;

-- 멘티가 1명인 사수의 사원번호 검색(사수가 없는 사원은 제외)
SELECT MANAGER_ID
FROM employees
WHERE MANAGER_ID IS NOT NULL
GROUP BY MANAGER_ID
HAVING COUNT(*) = 1;

/* 계정 사용 */
USE HR;
SHOW DATABASES;
SHOW DATABASE;
SHOW TABLES;
SHOW USER;

-- ROOT로 명령어 실행
CREATE USER 'TAEHWAN'@'LOCALHOST' IDENTIFIED BY '1234'; -- USER 만들기, 비밀번호 부여
GRANT ALL PRIVILEGES ON HR.* TO 'TAEHWAN'@'LOCALHOST'; -- 권한 주기
ALTER USER 'TAEHWAN'@'LOCALHOST' IDENTIFIED BY '1234'; -- 비밀번호 변경
DROP USER 'TAEHWAN'@'LOCALHOST'; -- USER 삭제

/* INDEX 생성 */
CREATE INDEX EMP_IDX ON EMPLOYEES(FIRST_NAME);
-- 인덱스 보기
SHOW INDEX FROM employees;


