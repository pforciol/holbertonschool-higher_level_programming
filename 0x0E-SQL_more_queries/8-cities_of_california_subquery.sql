-- Lists all the cities of California found in the database hbtn_0d_usa.

  SELECT id, name
    FROM cities
   WHERE state_id IN (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
