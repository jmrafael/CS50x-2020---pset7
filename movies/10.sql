SELECT p.name FROM people AS p WHERE p.id IN (SELECT d.person_id FROM directors d JOIN ratings r ON r.movie_id = d.movie_id WHERE r.rating >=9.0);