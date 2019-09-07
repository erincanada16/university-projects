CREATE DATABASE moviesdb;

CREATE TABLE movies(movieid numeric, title text, year numeric, primary key(movieid));
CREATE TABLE genres(title text, primary key(title)):
CREATE TABLE users(userid numeric, primary key(userid));
CREATE TABLE ratings(userid numeric, movieid numeric, rating, time);
CREATE TABLE tags(userid numeric, movieid numeric, tag, time);
CREATE TABLE has_genre(movieid numeric, title text);

\copy movies  FROM 'C:/Users/Erin Canada/Documents/USF/Fall 2018/Databases/Labs/Project/movies/movies_tables.txt' (DELIMITER('|'));
\copy  ratings FROM 'C:/Users/Erin Canada/Documents/USF/Fall 2018/Databases/Labs/Project/movies/ratings.txt' (DELIMITER('|'));
\copy has_genre  FROM 'C:/Users/Erin Canada/Documents/USF/Fall 2018/Databases/Labs/Project/movies/has_genres.txt' (DELIMITER('|'));
\copy tags  FROM 'C:/Users/Erin Canada/Documents/USF/Fall 2018/Databases/Labs/Project/movies/tags_table.txt' (DELIMITER('|'));
\copy users  FROM 'C:/Users/Erin Canada/Documents/USF/Fall 2018/Databases/Labs/Project/movies/users.txt' (DELIMITER('|'));

INSERT INTO genre VALUE('Action'),('Adventure'),('Animation'),('Children'),('Comedy'),('Crime'),('Documentary'),('Drama'),('Fantasy'),('Film-Noir'),('Horror'),('Musical'),('Mystery'),('Romance'),('Sci-Fi'),('Thriller'),('War'),('Western');

\d+
\d genres
\d movies
\d ratings
\d tags
\d users
\d has_genre

select count(*) from genres ;
select count(*) from movies;
select count(*) from ratings;
select count(*) from tags;
select count(*) from users;
select count(*) from has_genre;

select * from movies limit 5;
select count(title) from movies;
select * from movies order by year desc limit 5;
select * from movies order by year limit 5;
select count(year) from movies;
select count(year) from movies where year = 0;
select count(year) from movies where year > 1500;

SELECT * FROM movies WHERE year IS NULL;
SELECT * FROM ratings WHERE rating IS NULL;
SELECT * FROM genres WHERE title IS NULL;
#SELECT * FROM tags WHERE tag IS NULL;
#SELECT * FROM users WHERE userid IS NULL;

SELECT year, COUNT(*) FROM movies GROUP BY year ORDER BY year;
SELECT (FLOOR(year / 10)*10) AS decade, COUNT(year) AS NumberOfMovies FROM movies GROUP BY decade ORDER BY decade;
SELECT title, count(*) FROM has_genre GROUP BY title ORDER BY COUNT;
SELECT rating, count(*) FROM ratings GROUP BY rating ORDER BY rating;

Update ratings_with_diff r set rating = avg_rating where abs(diff) > 3;
Update ratings_with_diff set rating = rating, avg_rating = (select avg(rating) from ratings), diff = rating - avg_rating;
Update ratings_with_diff r set rating = avg_rating where abs(diff) > 3;