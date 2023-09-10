
DROP TABLE IF EXISTS recipes;




CREATE TABLE recipes (
    id serial PRIMARY KEY,
    title varchar,
    avg_cooking_time integer,
    rating integer
);


INSERT INTO recipes (title, avg_cooking_time, rating) VALUES ('cake1', 8, 3);
INSERT INTO recipes (title, avg_cooking_time, rating) VALUES ('cake2', 7, 4);
INSERT INTO recipes (title, avg_cooking_time, rating) VALUES ('cake3', 4, 1);