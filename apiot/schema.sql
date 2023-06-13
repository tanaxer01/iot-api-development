
/*
DROP TABLE IF EXISTS Admin;
DROP TABLE IF EXISTS Sensor;
DROP TABLE IF EXISTS Location;
DROP TABLE IF EXISTS Company;
*/


CREATE TABLE IF NOT EXISTS Admin (
    username    TEXT NOT NULL PRIMARY KEY,
    password    TEXT NOT NULL 
);

CREATE TABLE IF NOT EXISTS Company (
    id      INTEGER PRIMARY KEY AUTOINCREMENT, 
    name    TEXT UNIQUE,
    api_key TEXT
);

CREATE TABLE IF NOT EXISTS Location (
    id      INTEGER PRIMARY KEY, 
    name    TEXT,
    country TEXT,
    city    TEXT,
    meta    TEXT
);

CREATE TABLE IF NOT EXISTS Sensor (
    id          INTEGER PRIMARY KEY, 
    location_id INTEGER,
    name        TEXT,
    country     TEXT,
    city        TEXT,
    meta        TEXT,
    api_key     TEXT,
    CONSTRAINT fk_location FOREIGN KEY (location_id)
        REFERENCES Location(id)
);
