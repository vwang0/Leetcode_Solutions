/*
182. Duplicate Emails

*/
SELECT Email
FROM Person
Having COUNT(Email)>1