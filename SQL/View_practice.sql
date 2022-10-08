CREATE VIEW tokyo_product(ProductID, ProductName, Unit, Price)
AS
SELECT ProductID, ProductName, Unit, Price
FROM Products
    INNER JOIN Suppliers
    ON Products.SupplierID = Suppliers.SupplierID
WHERE Suppliers.City = 'Tokyo';


CREATE VIEW seafood_product(ProductName)
AS
SELECT ProductName FROM Products
INNER JOIN Categories
ON Categories.CategoryID = Products.CategoryID
WHERE Categories.CategoryName = 'Seafood';

