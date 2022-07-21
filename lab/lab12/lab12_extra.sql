.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT su18.date,su18.color,su18.pet,sp18.pet,su18.number,sp18.number
    FROM students as su18,sp18students as sp18
      WHERE su18.date = sp18.date and su18.color = sp18.color;

-- Q6
CREATE TABLE sevens AS
  SELECT students.seven 
    FROM students,checkboxes
      WHERE students.time=checkboxes.time and students.number=7 and checkboxes.'7'='True';

-- Q7
CREATE TABLE sp18favnum AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE sp18favpets AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE su18favpets AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE su18dog AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE su18alldogs AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE obedienceimages AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
