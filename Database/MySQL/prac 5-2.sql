-- 1. 성이 '김'씨인 고객의 이름과 주소
SELECT name, address
FROM Customer
WHERE name LIKE '김%';

-- 2. 성이 '박'씨이고 이름이 '성'로 끝나는 고객의 이름과 주소
SELECT name, address
FROM Customer
WHERE name LIKE '박%' AND name LIKE '%성';

select * from book;
select * from customer;
select * from orders;

-- 3. 박지성의 총 구매액(박지성의 고객번호는 1번으로 놓고 작성)
SELECT SUM(saleprice) AS "박지성의 총 구매액"
FROM Orders
WHERE custid = '1';

-- 4. 박지성이 구매한 도서의 수(박지성의 고객번호는 1번으로 놓고 작성)
SELECT count(*) AS "박지성이 구매한 도서의 수"
FROM Orders
WHERE custid = '1';