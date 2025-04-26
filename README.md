# Automotive-Market-Sales-Analysis

To import the data into the database please make sure that you have PostgreSQL in your codespace or you could use Docker to make a virtual one for this porject.

PLEASE MAKE SURE THAT YOU HAVE CREATED THE DATABSE IN YOUR POSTGRESQL

1.dbname: automotive_project to create one database in Postgresql or change the name as you want for database and in config.yaml

2.To run this code in your termianl:
docker run --name automotive-postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=automotive_project -p 5432:5432 -d postgres