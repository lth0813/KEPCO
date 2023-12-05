/* 대소문자 구분, BINARY는 곧 삭제될 함수라서 CAST로 쓰자 */
SELECT e.first_name, d.department_name
FROM employees e, departments d
WHERE binary(first_name) LIKE '%M%'
AND e.department_id = d.department_id;

SELECT e.first_name, d.department_name
FROM employees e, departments d
WHERE CAST(first_name AS BINARY) LIKE '%A%'
AND E.department_id = d.department_id;

SELECT e.first_name, j.job_title
FROM employees e, jobs j
WHERE e.job_id=j.job_id
AND j.job_title NOT IN ('Accountant','Programmer');

/* IN 안에서도 SELECT문 작성 가능(서브쿼리) */
SELECT e.first_name, j.job_title, j.min_salary
FROM employees e, jobs j
WHERE e.job_id = j.job_id
AND j.job_title IN(SELECT job_title
						 FROM jobs
						 WHERE min_salary > 7000);
						 
-- 16. 사원의 이름(Last_name)이 'Abel'인 사원과 같은 부서에 근무하는 사원의 이름과 부서번호을 출력하시오
SELECT e.last_name AS '사원이름', e.department_id AS '부서번호', d.department_name AS '부서이름'
FROM employees e, employees e2, departments d
WHERE e2.last_name = 'Abel' AND e.department_id = e2.department_id AND e2.department_id = d.department_id;

SELECT last_name, department_id
FROM employees
WHERE department_id = (SELECT department_id
							  FROM employees
							  WHERE last_name = 'Abel');
							  
SELECT e2.last_name, e.department_id
FROM employees e LEFT JOIN employees e2
ON e.department_id = e2.department_id
WHERE e.last_name = 'Abel'
AND e.last_name != e2.last_name;

/* DMA
	INSERT : 테이블(뷰)에 데이터를 입력
	UPDATE : 테이블의 값을 수정 : 한 컬럼에 특정 값만 삭제할때는 UPDATE
	DELETE : 테이블을 삭제 
	
	INSERT INTO 테이블(뷰) 이름(컬럼명, 컬럼명...) VALUES(값, 값...) 
	보통은 테이블을 전부 작성하기 때문에 컬럼명을 안쓰고 테이블 이름만 적고 VALUES를 적는 경우가 많다. 
	
	UPDATE 테이블
	SET 컬럼명 = 값, 컬럼명 = 값... 
	WHERE.. 
	
	DELETE
	FROM 테이블 이름
	WHERE.. */
	
/* COMMIT : INSERT, UPDATE, DELETE은 임시 테이블에서 따로 적용되는데 COMMIT을 사용해서 본 테이블에 확정 적용 시킨다.
	ROLLBACK : 바로 전COMMIT 한 상태까지 ROLLBACK 한다. */

/* 오토 커밋 상태 확인 및 온/오프 */
SELECT @@autocommit;
SET autocommit = TRUE;
SET autocommit = FALSE;
	
INSERT INTO employees
VALUES(300,'A','A','A','A','2011-01-01','AD_VP',8000,NULL,111,80);

UPDATE employees
SET first_name = 'bbbB', last_name = '45634534'
WHERE employee_id = 300;

DELETE
FROM employees
WHERE employee_id = 300;

COMMIT;

ROLLBACK;

/* DDL :	CREATE, ALTER, DROP */

/* 테이블 만들기 */
-- AUTO_INCREMENT : 인덱스 값 자동으로 + 인데 INSERT로 줄때는 NULL로 표시해야함
CREATE TABLE BBS(
ARTICLE_NUM INT AUTO_INCREMENT PRIMARY KEY,
WRITER_ID VARCHAR(30) NOT NULL,
TITLE VARCHAR(200) NOT NULL,
CONTENTS VARCHAR(10000) NOT NULL,
WRITE_DATE DATETIME NOT NULL);

CREATE TABLE COMMENTS(
COMMENTS_NUM INT AUTO_INCREMENT PRIMARY KEY,
WRITER_ID VARCHAR(30) NOT NULL,
CONTENTS VARCHAR(1500) NOT NULL,
ARTICLE_NUM INT NOT NULL,
CONSTRAINT COMM_ARTIC_FK FOREIGN KEY(ARTICLE_NUM) REFERENCES BBS(ARTICLE_NUM)); /* Foreign Key 주기 */
/* INSERT */
INSERT INTO bbs VALUE(NULL,'A','A','A',NOW());
INSERT INTO COMMENTS VALUES (NULL,'A','A',3);
/* TABLE 삭제 */
DROP TABLE bbs;

/* 뷰 만들기 */
CREATE OR REPLACE VIEW EMP
AS SELECT FIRST_NAME, LAST_NAME, SALARY
FROM employees;

/* 뷰 칼럼 이름만 가져오기 */
CREATE OR REPLACE VIEW EMP1
AS SELECT First_name, last_name, salary
FROM employees
WHERE 1 = 2;

DROP VIEW emp1;

/* 제약조건 이름 확인할수 있는 뷰 */
SELECT *
FROM information_schema.TABLE_CONSTRAINTS;

/* 함수 */
SELECT NOW();
SELECT SYSDATE();
SELECT SLEEP(5), CURRENT_TIMESTAMP(), NOW(), sysdate();
SELECT CURRENT_TIMESTAMP;

SELECT CONCAT(first_name,'의 급여는 ',round(salary,0),'입니다')
FROM employees;

