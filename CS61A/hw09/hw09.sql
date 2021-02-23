CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT d.name as name, s.size
  FROM dogs AS d, sizes AS s
  WHERE d.height <= s.max AND d.height > s.min;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT p.child
  FROM parents as p, dogs as d
  WHERE d.name = p.parent
  ORDER BY - d.height;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT s1.child as sib1, s2.child as sib2
  FROM parents as s1, parents as s2
  WHERE s1.parent = s2.parent and s1.child < s2.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT 'The two siblings, ' || sibs.sib1 || ' plus ' || sibs.sib2 || ' have the same size: ' || sizes1.size AS sentences
  FROM siblings AS sibs, size_of_dogs AS sizes1, size_of_dogs AS sizes2
  WHERE sizes1.name = sibs.sib1 AND sizes2.name = sibs.sib2 AND sizes1.size = sizes2.size;


