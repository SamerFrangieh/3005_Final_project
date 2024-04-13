--DO NOT DELETE
DO $$ DECLARE
    r RECORD;
BEGIN
    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
        EXECUTE 'DELETE FROM ' || quote_ident(r.tablename);
    END LOOP;
END $$;


-- Inserting into Rooms
INSERT INTO myapp_room (room_id, name)
VALUES 
(101, 'Aerobics Room'),
(102, 'Spin Studio');

-- Inserting into Trainers
INSERT INTO myapp_trainer (trainer_id, name, password)
VALUES 
(1, 'Jane Smith', 'securepassword'),
(2, 'Bob Williams', 'anothersecurepassword');

-- Inserting into Members
INSERT INTO myapp_member (member_id, name, password, health_metrics, height, weight, goal_weight, weeks_to_goal, diastolic_bp, systolic_bp, fitness_goal, act_levels)
VALUES 
(1, 'John', 'password123', '{"bmi": 22, "fat_percentage": 15}', 175.5, 70.0, 65.0, 12, 80, 120, 'Lose Weight', '1-3 x times a week'),
(2, 'Alice', 'password456', '{"bmi": 25, "fat_percentage": 20}', 165.0, 80.0, 70.0, 10, 85, 125, 'Gain Muscle', '1-3 x times a week');

-- Inserting into Trainer Availability
INSERT INTO myapp_traineravailability (trainer_id, day_of_week, check_in, check_out)
VALUES 
(1, 1, '08:00:00', '12:00:00'),
(2, 3, '10:00:00', '14:00:00');

-- Inserting into Personal Sessions
INSERT INTO myapp_personalsession (trainer_id, member_id, date, start_time, end_time)
VALUES 
(1, 1, '2024-04-15', '09:00:00', '10:00:00'),
(2, 2, '2024-04-16', '11:00:00', '12:00:00');

-- Inserting into Group Fitness Classes
INSERT INTO myapp_groupfitnessclass (trainer_id, room_id, date, start_time, end_time)
VALUES 
(1, 101, '2024-04-16', '10:00:00', '11:00:00'),
(2, 102, '2024-04-17', '09:00:00', '10:00:00');

-- Inserting into Member Group Fitness Registration
INSERT INTO myapp_membergroupfitnessregistration (group_fitness_class_id, member_id, registration_date)
VALUES 
(1, 1, '2024-04-01'),
(2, 2, '2024-04-02');



INSERT INTO myapp_trainer (trainer_id, name, password)
VALUES (3, 'dhirran', 'dhirran');

INSERT INTO myapp_trainer (trainer_id, name, password)
VALUES (4, 'Samer', 'samer');

INSERT INTO myapp_trainer (trainer_id, name, password)
VALUES (5, 'James', 'james');

INSERT INTO myapp_trainer (trainer_id, name, password)
VALUES (6, 'Amir', 'amir');

INSERT INTO myapp_trainer (trainer_id, name, password)
VALUES (7, 'Cristina', 'cristina' );

INSERT INTO myapp_trainer (trainer_id, name, password)
VALUES (8, 'Jenny', 'jenny');

INSERT INTO myapp_admin (admin_id, name, password)
VALUES (1, 'dhirran', 'dhirran');

INSERT INTO myapp_admin (admin_id, name, password)
VALUES (2, 'admin', 'admin');

INSERT INTO myapp_member (member_id, name, password, health_metrics, height, weight, goal_weight, weeks_to_goal, diastolic_bp, systolic_bp, fitness_goal, act_levels)
VALUES 
(3, 'dhirran', 'dhirran', '{"bmi": 25, "fat_percentage": 20}', 165.0, 80.0, 70.0, 10, 85, 125, 'Lose weight','1-3 x times a week');

