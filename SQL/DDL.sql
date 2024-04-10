-- DDL.sql

-- Create table for Members
CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    fitness_goal VARCHAR(255),
    health_metrics JSONB
);

-- Create table for Trainers
CREATE TABLE trainers (
    trainer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    availability JSONB, 
    password VARCHAR(255) NOT NULL

);

-- Create table for Administrative Staff
CREATE TABLE admin_staff (
    staff_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL, 
    password VARCHAR(255) NOT NULL,

);

-- Create table for Fitness Classes
CREATE TABLE fitness_classes (
    class_id SERIAL PRIMARY KEY,
    class_name VARCHAR(255) NOT NULL,
    room_id INT NOT NULL,
    schedule TIMESTAMPTZ NOT NULL, 
);

-- Create table for Room Bookings
CREATE TABLE room_bookings (
    booking_id SERIAL PRIMARY KEY,
    room_id INT NOT NULL,
    booking_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL
);

-- Create table for Equipment Maintenance
CREATE TABLE equipment_maintenance (
    equipment_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    last_maintenance_date DATE NOT NULL,
    next_maintenance_date DATE NOT NULL
);

-- Create table for Billing
CREATE TABLE billing (
    bill_id SERIAL PRIMARY KEY,
    member_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    paid BOOLEAN DEFAULT FALSE,
    payment_date DATE,
    FOREIGN KEY (member_id) REFERENCES members (member_id)
);

-- Deleting all tables in the schema
DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
        EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE;';
    END LOOP;
END $$;

