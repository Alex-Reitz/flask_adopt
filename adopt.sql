\c colors

CREATE TABLE pets
(
  id SERIAL PRIMARY KEY,
  name TEXT,
  species TEXT,
  photo_url TEXT,
  age INTEGER,
  notes ,
  available
);

INSERT INTO pets 
