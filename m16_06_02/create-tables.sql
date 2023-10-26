-- Таблиця груп
drop table if exists groups;
CREATE TABLE groups (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL
);

-- Таблиця студентів
drop table if exists students;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  fullname VARCHAR(150) NOT NULL,
  group_id INTEGER REFERENCES groups(id)
  	on delete cascade
);

-- Таблиця викладачів
drop table if exists teachers;
CREATE TABLE teachers (
  id SERIAL PRIMARY KEY,
  fullname VARCHAR(150) NOT NULL
);

-- Таблиця предметів
drop table if exists subjects;
CREATE TABLE subjects (
  id SERIAL PRIMARY KEY,
  name VARCHAR(175) NOT NULL,
  teacher_id INTEGER  REFERENCES teachers(id)
  	on delete cascade
);

-- Таблиця оцінок
drop table if exists grades;
CREATE TABLE grades (
  id SERIAL PRIMARY KEY,
  student_id INTEGER  REFERENCES students(id)
  on delete cascade,
  subject_id INTEGER  REFERENCES subjects(id)
  on delete cascade,
  grade INTEGER CHECK (grade >= 0 AND grade <= 100),
  grade_date DATE NOT NULL
);
