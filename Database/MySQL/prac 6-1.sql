-- 1. 박지성의 총 구매액
SELECT name, SUM(saleprice) AS '총 구매액'
FROM Customer, Orders
WHERE Customer.custid = Orders.custid AND Customer.name = '박지성';

-- 2. 박지성이 구매한 도서의 수
SELECT COUNT(*) AS '박지성이 구매한 도서의 수'
FROM Customer, Orders
WHERE Customer.custid = Orders.custid AND Customer.name = '박지성';

-- 3. 고객 아이디와 고객벽 구매액
SELECT Customer.custid AS '고객 아이디', SUM(saleprice) AS '고객별 구매액'
FROM Customer, Orders
WHERE Customer.custid = Orders.custid
GROUP BY Customer.custid;

/* 3번 교수님 답안 */
SELECT custid, sum(saleprice)
FROM Orders
GROUP BY custid;

-- 4. 고객의 이름과 고객별 구매액
SELECT Customer.name AS '고객 이름', SUM(saleprice) AS '고객별 구매액'
FROM Customer, Orders
WHERE Customer.custid = Orders.custid
GROUP BY Customer.custid;

-- 5. 고객의 이름과 고객이 구매한 도서 목록
SELECT Customer.name AS '고객 이름', Book.bookname AS '구매한 도서 목록'
FROM Customer, Orders, Book
WHERE Customer.custid = Orders.custid AND Book.bookid = Orders.bookid;