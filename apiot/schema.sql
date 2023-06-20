
DROP TABLE IF EXISTS Admin;
DROP TABLE IF EXISTS Sensor;
DROP TABLE IF EXISTS Location;
DROP TABLE IF EXISTS Company;

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Admin (
    username TEXT NOT NULL PRIMARY KEY,
    password TEXT NOT NULL 
);

CREATE TABLE IF NOT EXISTS Company (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    company_name TEXT,
    company_api_key TEXT
);

CREATE TABLE IF NOT EXISTS Location (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    company_id INTEGER,
    location_name TEXT,
    location_country TEXT,
    location_city TEXT,
    location_meta TEXT,
    FOREIGN KEY (company_id) REFERENCES Company(id)
);

CREATE TABLE IF NOT EXISTS Sensor (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    location_id INTEGER,
    sensor_name TEXT,
    sensor_country TEXT,
    sensor_city TEXT,
    sensor_meta TEXT,
    sensor_api_key TEXT,
    FOREIGN KEY (location_id) REFERENCES Location(id)
);
