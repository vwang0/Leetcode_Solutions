DATA customer;
   INFILE '/home/u49657251/sas_book/data/CustAddress.dat' TRUNCOVER;
   INPUT CustomerNumber Name $ 5-21 Address $ 23-42;
run;
   
DATA orders;
   INFILE '/home/u49657251/sas_book/data/OrdersQ3.dat';
   INPUT CustomerNumber Total;
PROC SORT DATA = orders;
   BY CustomerNumber;
RUN;
* Combine the data sets using the IN= option;
DATA noorders;
   MERGE customer (in=b) orders (IN = a);
   BY CustomerNumber;
   IF a = 0 and b = 1;
run;

PROC PRINT DATA = noorders;
   TITLE 'Customers with No Orders in the Third Quarter';
RUN;

/*=========================*/


options missing = ' ';
DATA customer;
   INFILE '/home/u49657251/sas_book/data/CustAddress.dat' TRUNCOVER;
   INPUT CustomerNumber Name $ 5-21 Address $ 22-42;
   if missing(cats(of _all_)) then delete;
run;

/* 
1. The MISSING= system option is used to display the missing values as a single space rather than 
	as the default period (.) options missing = ' '; 
2. The CATS function concatenates the values. It also removes leading and trailing blanks. 
	cats(of _all_) - Concatenate all the variables
3.  missing(cats(of _all_)) - Identifies all the rows in which missing values exist in all the variables. 
https://github.com/sassoftware/little-sas-book-exercises-6ed/blob/master/README.md
*/

DATA orders;
   INFILE '/home/u49657251/sas_book/data/OrdersQ3.dat';
   INPUT CustomerNumber Total;
run;

/*
PROC SORT DATA = orders;
   BY CustomerNumber;
RUN;

* Combine the data sets using the IN= option;
DATA noorders;
   MERGE customer  orders (IN = Recent);
   BY CustomerNumber;
   IF Recent = 0;
PROC PRINT DATA = noorderss;
   TITLE 'Customers with No Orders in the Third Quarter';
RUN;
*/

proc sql;
	create table noorderss as
	select * from customer
	where CustomerNumber NOT IN (select distinct CustomerNumber from orders);
quit;
   
PROC PRINT DATA = noorderss;
   TITLE 'Customers with No Orders in the Third Quarter';
RUN;


