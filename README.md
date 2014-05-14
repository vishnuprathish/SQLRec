SQLRec
======

we present a recommendation engine for SQL query language that can be used in the everyday life of a SQL query writer. We use a schema aware approach unlike other systems designed for similar purposes where user history from query logs is used. The key features of our recommendation engine are auto improvisation of attribute recommendations as the user types query and join predicate recommendation using statistical inference. We use a ranking system with weightages for various parameters at different contexts to recommend keywords, table names, column names and boolean conditions. We evaluate the system using query logs on northwind database and it is shown that we are able to recommend useful fea-
tures 99% of times in the top ten results and over 90% of times in the first two results. 



Dependencies: 
JQUERY UI v1.0.4
NTLK 



To use: 

Put the code in a python server with approprite CGI permissions. In your browser type, 

localhost/sql.py


