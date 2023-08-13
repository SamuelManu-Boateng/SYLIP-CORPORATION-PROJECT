                           -----------------------------Sylip Corporation Sales Analysis---------------------------

--CREATE DATABASE
CREATE DATABASE SYLIP;

--VIEW DATA
SELECT * FROM SALES_DATA;
                                                                 ---DATA CLEANING---

--Change Ship date from datetime to date.

ALTER TABLE SALES_DATA
ALTER COLUMN Ship_Date date;

--Change Order date from datetime to date.

ALTER TABLE SALES_DATA
ALTER COLUMN Order_date date;

--Converting Units sold column from Datetime to int.

ALTER TABLE SALES_DATA
ADD Units_sold_converted int;

UPDATE SALES_DATA
SET Units_sold_converted = CONVERT (int,Units_Sold);


--Converting Unit Price column from Datetime to money.

ALTER TABLE SALES_DATA
ADD Unit_Price_converted money;

UPDATE SALES_DATA
SET Unit_Price_converted = CONVERT (money, Unit_Price);


--Converting Unit Cost column form Datetime to money.

ALTER TABLE SALES_DATA
ADD Unit_cost_converted money;

UPDATE SALES_DATA
SET Unit_cost_converted = CONVERT (money,Unit_cost);


--Converting Total Revenue column from Datetime to money.

ALTER TABLE SALES_DATA
ADD Total_revenue_converted money;

UPDATE SALES_DATA
SET Total_revenue_converted = CONVERT (money,Total_revenue);


--Converting Total cost column from datetime to money.

ALTER TABLE SALES_DATA
ADD Total_cost_converted money;

UPDATE SALES_DATA
SET Total_cost_converted = CONVERT (money, Total_cost);


--Converting Total_Profit column from datetime to money.

ALTER TABLE SALES_DATA
ADD Total_Profit_converted money;

UPDATE SALES_DATA
SET Total_Profit_converted = CONVERT (money,Total_Profit);


--Deleting columns with previous datatypes.

ALTER TABLE SALES_DATA
DROP COLUMN Units_sold, Unit_Price, Unit_cost, Total_Revenue, Total_Cost, Total_Profit;

 ALTER TABLE SALES_DATA
 DROP COLUMN Sales_Channel, Order_Priority;


 ----VIEW SALES DATA

 SELECT * FROM SALES_DATA;


                                                   ------KEY PERFORMANCE INDICATORS (KPIs)-----
--KPI 1: PROFIT FROM ALL REGIONS.

SELECT
      DISTINCT Region,
	  SUM(Total_Profit_converted) AS Total_Proft
FROM
      SALES_DATA

GROUP BY
      Region;


--KPI 2: REVENUE MADE ANNUALLY.

SELECT
      YEAR(Order_date) AS Year,
	  SUM (Total_revenue_converted) AS Total_Revenue
FROM
      SALES_DATA
GROUP BY
       YEAR(Order_date);


--KPI 3: COMPARE YEAR BY YEAR TOTAL UNITS SOLD.

SELECT 
      Year(Order_date) AS YEAR,
	  SUM ( Units_sold_converted) AS Total_Units_sold
FROM
      SALES_DATA
GROUP BY
       Year(order_date);


--KPI 4: RATE OF TOTAL REVENUE ACHIEVED ANNUALLY.

	SELECT
		  YEAR(Order_date) AS Year,
		  SUM(Total_revenue_converted) * 100/ (SELECT SUM(Total_revenue_converted) FROM SALES_DATA) AS Percentage
	FROM
		SALES_DATA
	GROUP BY
		Year(Order_date);

--KPI 5: AVERAGE AMOUNT OF PROFIT ACHIEVED ANNUALLY.

SELECT
      YEAR(Order_date) AS Year,
	  AVG (Total_Profit_converted) AS AVERAGE
FROM
      SALES_DATA
GROUP BY
      YEAR(Order_date);


--KPI 6: COUNT OF ITEM TYPES SOLD IN EACH REGION.

SELECT
      DISTINCT Region AS REGION,
	  COUNT (Item_Type) AS Items_Sold
FROM
      SALES_DATA
GROUP BY
      Region;


--KPI 7: TOP 4 COUNTRIES WITH HIGHEST REVENUE.

SELECT
      DISTINCT (Country),
	  SUM(Total_Revenue_converted) AS Total_Revenue
FROM
      SALES_DATA
GROUP BY
       Country
ORDER BY
      SUM(Total_revenue_converted) DESC;


--KPI 8: TOP 4 COUNTRIES WITH LOWEST REVENUE.

SELECT
      DISTINCT(Country),
	  SUM(Total_revenue_converted) AS Total_Revenue
FROM
      SALES_DATA
GROUP BY
      Country
ORDER BY 
      SUM(Total_revenue_converted) ASC;


--KPI 9: TOP 5 COUNTRIES WITH LOWEST UNITS SOLD BELOW THE BENCH MARKET TARGET OF 50000 UNITS.

 SELECT
       DISTINCT (Country),
	   SUM(Units_sold_converted) AS Total_Units_Sold
FROM
       SALES_DATA
WHERE
       Units_sold_converted > 5000
GROUP BY
       Country
ORDER BY
       SUM(Units_sold_converted) DESC;


	                                --DATA TRANSFERRED TO POWER BI FOR FURTHER ANALYSIS AND VISUALISATIONS--
