국가(Country)가 France인 고객 조회
Select * from Customers Where Country='France';

이름이 'Mar'로 시작하는 직원 조회
Select * from Customers Where ContactName LIKE 'Mar%';

이름이 'et'로 끝나는 직원조회
Select * from Customers Where ContactName LIKE '%et';

#WHERE 조건문
SELECT * FROM Customers WHERE Country='France' and ContactName LIKE 'La%';
SELECT * FROM Customers WHERE Country='France' or ContactName LIKE 'La%';
SELECT * FROM Customers WHERE Not Country='France';
SELECT * FROM Customers WHERE Country IN ('Spain', 'France');
SELECT * FROM Products WHERE Price BETWEEN 15 AND 20;

Select * from Customers where PostalCode is NULL;

#내림차순, 오름차순
Select * from Customers Order by CustomerName Asc;
Select * from Products Order by Price Desc;

#10개 제한, 그 다음 10개
Select * from Customers limit 10;
Select * from Customers limit 10 OFFSET 10;

#CASE, WHEN
SELECT *, 
CASE WHEN Price < 30 THEN '저' 
WHEN Price >=30 and Price <=50 THEN '중' 
WHEN Price > 50 THEN '고'
END as 'Level'
FROM Products;

#개수, 평균, 합, 최소, 최대
SELECT COUNT(CustomerID) from Customers where Country='France'
SELECT AVG(Price) from Products;
SELECT SUM(Quantity) from OrderDetails;
SELECT MIN(Price) from Products;
SELECT MAX(Price) from Products;

#Group by
SELECT Country, COUNT(CustomerID) from Customers Group By Country;

#HAVING
SELECT Country, COUNT(CustomerID) from Customers 
Group By Country HAVING COUNT(CustomerID) >5 
ORDER By CustomerID desc;

SELECT LastName, FirstName, BirthDate, Notes from Employees where LastName = 'King'
SELECT ProductName, Price from Products Where ProductName LIKE 'C%' and Price > 20 Order by Price desc;
SELECT CategoryID, SUM(Price), MAX(Price), MIN(Price) from Products Group by CategoryID 
SELECT COUNT(CategoryID),
CASE WHEN COUNT(CategoryID) > 10 THEN '많음' ELSE '적음' END AS 'uantity' from Products Group by CategoryID 
SELECT (COUNT(Country) *100) / (
    SELECT COUNT(CustomerID) from Customers
    ) 
from Customers Group by Country

#Q. Tokyo에 위치한 공급자(Supplier)가 생산한 상품(Products) 목록 조회
SELECT *
FROM Suppliers
INNER JOIN  Products
ON Suppliers.SupplierID = Products.SupplierID
where City = 'Tokyo'

#Q. 분류(CategoryName)가 Seafood인 상품명(ProductName) 조회
SELECT *
FROM Categories
INNER JOIN  Products
ON Products.CategoryID = Categories.CategoryID
where CategoryName = 'Seafood'

#Q. 공급자(Supplier)가 공급한 상품의 공급자 국가(Country), 카테고리별로 상품건수와 평균가격 조회
SELECT Count(ProductID), AVG(Price) FROM Products
INNER JOIN Suppliers
ON Suppliers.SupplierID = Products.SupplierID 
INNER JOIN Categories ON Categories.CategoryID = Products.CategoryID

#Q. 주문별 주문자명(CustomerName), 직원명(LastName), 배송자명(ShipperName), 주문상세갯수
SELECT CustomerName, LastName, ShipperName FROM Orders
INNER JOIN OrderDetails
ON Orders.OrderID = OrderDetails.OrderID 
INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
INNER JOIN Shippers ON Orders.ShipperID= Shippers.ShipperID

#Q. 판매량(Quantity) 상위 TOP 3 공급자(supplier) 목록 조회
SELECT SupplierName, Quantity FROM Products
INNER JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID 
INNER JOIN Suppliers ON Products.SupplierID= Suppliers.SupplierID
ORder by Quantity Desc

#Q. 상품분류(Category)별, 고객지역별(City) 판매량 많은 순 정렬
SELECT COUNT(CategoryName),city FROM Products
INNER JOIN OrderDetails
ON Products.ProductID = OrderDetails.ProductID 
INNER JOIN Categories ON Categories.CategoryID = Products.CategoryID
INNER JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
INNER JOIN Customers ON Customers.CustomerID = Orders.CustomerID
Group by city,CategoryName
Order BY Count(CategoryName) DESC

#Q. 고객국가(Country)가 USA이고, 상품별 판매량(Quantity)의 합이 많은순으로 정렬
SELECT SUM(Quantity) FROM OrderDetails
INNER JOIN Orders
ON OrderDetails.OrderID = Orders.OrderID
INNER  JOIN Products
ON Products.ProductID = OrderDetails.ProductID
INNER JOIN Customers
ON Customers.CustomerID = Orders.CustomerID
Where Country = 'USA'
Group by ProductName
Order by Quantity DESC;