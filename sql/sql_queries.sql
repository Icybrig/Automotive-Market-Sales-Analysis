-- 1. Find the total number of cars by model and country 
SELECT country, model, COUNT(*) AS total_cars
FROM consumer_data
GROUP BY model, country
ORDER BY total_cars DESC;

-- 2. Which countries have the most of each model and how many of them they have 
SELECT country, model, SUM(sales_volume) AS total_sales
FROM consumer_data
GROUP BY model, country
ORDER BY total_sales DESC;

-- 3. Are there models that are sold in the United States that are not sold in France 
SELECT DISTINCT model
FROM consumer_data
WHERE country = 'USA'
AND model NOT IN (
    SELECT DISTINCT model
    FROM consumer_data
    WHERE country = 'France'
);

-- 4. Average price of cars by engine type in each country 
SELECT consumer_data.country, car_data.engine_type, AVG(car_data.price) AS average_price
FROM car_data
JOIN consumer_data
ON consumer_data.model = car_data.model
GROUP BY consumer_data.country, car_data.engine_type
ORDER BY consumer_data.country, car_data.engine_type;

-- 5. Average ratings of electric vs. thermal cars
SELECT car_data.engine_type, AVG(consumer_data.review_score) AS average_rating
FROM consumer_data
JOIN car_data
ON consumer_data.model = car_data.model
GROUP BY  car_data.engine_type;
