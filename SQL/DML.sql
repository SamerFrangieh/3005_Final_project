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
(102, 'Spin Studio'),
(103, 'Yoga Studio'),
(104, 'Weight Room'),
(105, 'Cardio Room');

-- Inserting into Trainers
INSERT INTO myapp_trainer (trainer_id, name, password)
VALUES 
(1, 'Jane Smith', 'securepassword'),
(2, 'Bob Williams', 'anothersecurepassword');

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

-- Inserting into Members
INSERT INTO myapp_member (member_id, name, password, health_metrics, height, weight, goal_weight, weeks_to_goal, diastolic_bp, systolic_bp, fitness_goal, act_levels, age) VALUES 
(1, 'Bob1', 'password813', '{"bmi": 28.4, "fat_percentage": 22.1}', 198.0693813085105, 88.61122378193645, 80.7966657226928, 36, 84, 112, 'Lose Weight', '5-6 x times a week', 50),
(2, 'Theo2', 'password681', '{"bmi": 28.3, "fat_percentage": 10.1}', 150.52391190824187, 70.58540948753958, 61.470377230639706, 11, 88, 111, 'Lose Weight', '1-3 x times a week', 58),
(3, 'Frank3', 'password307', '{"bmi": 22.0, "fat_percentage": 22.8}', 178.05004991976853, 78.19547472980184, 68.63865454492947, 30, 90, 117, 'Lose Weight', '1-3 x times a week', 45),
(4, 'Madison4', 'password990', '{"bmi": 23.4, "fat_percentage": 10.3}', 184.31654574879562, 52.589935368401655, 43.4129207318052, 34, 77, 121, 'Increase Flexibility', '5-6 x times a week', 31),
(5, 'Charlotte5', 'password416', '{"bmi": 25.2, "fat_percentage": 10.7}', 185.07279337877472, 63.50831324936362, 50.06266499987685, 11, 88, 112, 'Gain Muscle', '3-5 x times a week', 55),
(6, 'Alexander6', 'password324', '{"bmi": 25.6, "fat_percentage": 13.9}', 152.8434526584573, 65.23841749109474, 58.13382879859063, 35, 75, 129, 'Increase Flexibility', '1-3 x times a week', 44),
(7, 'Avery7', 'password819', '{"bmi": 22.4, "fat_percentage": 14.8}', 171.98246522077574, 93.05781604072536, 84.54162795566181, 47, 70, 116, 'Gain Muscle', '1-3 x times a week', 19),
(8, 'Carol8', 'password916', '{"bmi": 25.8, "fat_percentage": 11.3}', 186.0260829208661, 88.95036619988892, 83.73651260650905, 43, 75, 112, 'Lose Weight', '3-5 x times a week', 44),
(9, 'Emma9', 'password639', '{"bmi": 24.3, "fat_percentage": 10.3}', 180.61501874293742, 73.79119170396699, 60.74278055779756, 44, 79, 117, 'Gain Muscle', '5-6 x times a week', 26),
(10, 'Grace10', 'password228', '{"bmi": 25.6, "fat_percentage": 15.5}', 195.13066734578024, 56.19736522910681, 46.35196900927508, 40, 72, 117, 'Increase Flexibility', '3-5 x times a week', 54),
(11, 'Harper11', 'password756', '{"bmi": 19.7, "fat_percentage": 15.3}', 186.4954330374381, 83.03776337207746, 71.10626783067895, 27, 73, 122, 'Lose Weight', '1-3 x times a week', 39),
(12, 'David12', 'password332', '{"bmi": 21.1, "fat_percentage": 10.9}', 156.10916562361814, 91.12783178095803, 85.57832473741848, 16, 75, 122, 'Lose Weight', '1-3 x times a week', 29),
(13, 'Emma13', 'password119', '{"bmi": 22.0, "fat_percentage": 18.1}', 171.8815950390094, 80.41732590445572, 71.1056168665473, 13, 75, 120, 'Lose Weight', '3-5 x times a week', 48),
(14, 'Joseph14', 'password187', '{"bmi": 23.2, "fat_percentage": 23.9}', 158.42610736462566, 90.09284639326546, 79.55665894881335, 44, 87, 117, 'Increase Flexibility', '5-6 x times a week', 18),
(15, 'Samuel15', 'password660', '{"bmi": 22.3, "fat_percentage": 17.3}', 190.3062970498027, 92.856116867125, 81.92864330433807, 30, 81, 128, 'Increase Flexibility', '1-3 x times a week', 58),
(16, 'Harper16', 'password362', '{"bmi": 24.5, "fat_percentage": 19.7}', 184.82438067711482, 66.89113989832408, 56.12356779766952, 36, 79, 119, 'Increase Flexibility', '1-3 x times a week', 30),
(17, 'Ivy17', 'password714', '{"bmi": 19.2, "fat_percentage": 15.8}', 165.6221080189312, 86.80439094337878, 81.29002450663091, 9, 87, 118, 'Gain Muscle', '3-5 x times a week', 42),
(18, 'Joseph18', 'password959', '{"bmi": 25.1, "fat_percentage": 19.1}', 165.09497316197184, 67.53343455653166, 53.04634237686003, 27, 73, 111, 'Increase Flexibility', '3-5 x times a week', 32),
(19, 'Avery19', 'password415', '{"bmi": 23.4, "fat_percentage": 12.2}', 157.28197382023026, 55.60405815180699, 43.743845113580846, 47, 83, 111, 'Gain Muscle', '3-5 x times a week', 33),
(20, 'Tom20', 'password210', '{"bmi": 26.6, "fat_percentage": 23.2}', 173.0151826859884, 81.25186342699378, 71.4368096189592, 41, 74, 119, 'Gain Muscle', '1-3 x times a week', 54),
(21, 'Ava21', 'password727', '{"bmi": 19.3, "fat_percentage": 14.2}', 169.99195948227765, 83.92225245995249, 71.51881667178485, 50, 78, 128, 'Increase Flexibility', '1-3 x times a week', 55),
(22, 'Penelope22', 'password188', '{"bmi": 27.3, "fat_percentage": 19.4}', 196.30819632758383, 74.12246003647967, 60.22339543062032, 17, 80, 128, 'Lose Weight', '5-6 x times a week', 23),
(23, 'Grace23', 'password245', '{"bmi": 27.4, "fat_percentage": 14.8}', 168.09379884087767, 79.70527223957131, 65.27566949452631, 47, 86, 121, 'Gain Muscle', '1-3 x times a week', 27),
(24, 'Alexander24', 'password898', '{"bmi": 29.6, "fat_percentage": 20.6}', 161.69726329257958, 79.73036448234197, 66.00467402689024, 30, 75, 117, 'Gain Muscle', '1-3 x times a week', 58),
(25, 'Alice25', 'password858', '{"bmi": 25.3, "fat_percentage": 22.1}', 186.85491060779128, 61.02311869438701, 49.526339156502914, 18, 72, 129, 'Gain Muscle', '3-5 x times a week', 51),
(26, 'Logan26', 'password826', '{"bmi": 19.0, "fat_percentage": 18.7}', 180.30853493695304, 53.559550245215505, 45.15994605408395, 17, 72, 127, 'Gain Muscle', '3-5 x times a week', 52),
(27, 'Noah27', 'password552', '{"bmi": 20.0, "fat_percentage": 14.1}', 159.94780646010886, 90.04283372158199, 78.27505836975521, 21, 82, 110, 'Increase Flexibility', '5-6 x times a week', 46),
(28, 'Frank28', 'password403', '{"bmi": 19.4, "fat_percentage": 17.6}', 156.02461286377218, 78.12766739172808, 64.0039857997436, 41, 82, 127, 'Lose Weight', '1-3 x times a week', 43),
(29, 'Emily29', 'password208', '{"bmi": 29.3, "fat_percentage": 13.5}', 198.7432525417585, 83.76661118002258, 70.06361891755031, 22, 72, 118, 'Lose Weight', '5-6 x times a week', 40),
(30, 'Penelope30', 'password218', '{"bmi": 24.9, "fat_percentage": 13.3}', 170.57675721042276, 74.58392710093489, 64.31992149222572, 40, 90, 111, 'Increase Flexibility', '1-3 x times a week', 30),
(31, 'Madison31', 'password826', '{"bmi": 19.7, "fat_percentage": 12.6}', 159.77053996447242, 65.87135284187912, 60.04829256140481, 50, 90, 125, 'Lose Weight', '5-6 x times a week', 43),
(32, 'Max32', 'password710', '{"bmi": 20.8, "fat_percentage": 19.4}', 152.2352408490018, 54.405770269257395, 41.96800136653148, 14, 81, 130, 'Increase Flexibility', '5-6 x times a week', 58),
(33, 'Emily33', 'password340', '{"bmi": 23.5, "fat_percentage": 19.9}', 169.9596614656307, 94.90504542887015, 85.17485387903854, 42, 90, 117, 'Lose Weight', '1-3 x times a week', 54),
(34, 'Avery34', 'password562', '{"bmi": 22.3, "fat_percentage": 13.1}', 156.3069944930408, 98.99267788375863, 89.0108685784623, 31, 73, 123, 'Gain Muscle', '1-3 x times a week', 37),
(35, 'Michael35', 'password873', '{"bmi": 27.1, "fat_percentage": 21.9}', 174.26813000161764, 93.27915066228422, 82.31432553253076, 27, 70, 129, 'Lose Weight', '1-3 x times a week', 24),
(36, 'Madison36', 'password305', '{"bmi": 19.8, "fat_percentage": 15.0}', 195.59269355294236, 76.7726335417777, 69.6365456509053, 45, 87, 113, 'Lose Weight', '1-3 x times a week', 32),
(37, 'James37', 'password980', '{"bmi": 25.0, "fat_percentage": 17.2}', 166.4292376373232, 87.73739550961764, 80.9054344914498, 44, 80, 124, 'Increase Flexibility', '5-6 x times a week', 18),
(38, 'Bob38', 'password298', '{"bmi": 21.3, "fat_percentage": 21.6}', 182.6848382582577, 59.02667896333881, 52.63063598234896, 26, 85, 122, 'Gain Muscle', '1-3 x times a week', 40),
(39, 'Bob39', 'password347', '{"bmi": 27.6, "fat_percentage": 11.4}', 153.93805713671398, 99.80286536248744, 88.73566877989008, 31, 78, 123, 'Increase Flexibility', '3-5 x times a week', 19),
(40, 'Julia40', 'password809', '{"bmi": 20.8, "fat_percentage": 19.2}', 168.4187270171899, 90.05841204712087, 76.33899085506582, 26, 77, 110, 'Increase Flexibility', '5-6 x times a week', 21),
(41, 'Ivy41', 'password201', '{"bmi": 26.6, "fat_percentage": 15.1}', 183.91666777709727, 59.53715993402416, 54.51783062890369, 25, 77, 112, 'Lose Weight', '5-6 x times a week', 21),
(42, 'Evelyn42', 'password628', '{"bmi": 28.5, "fat_percentage": 11.2}', 188.84787328907072, 80.73750796913268, 66.89101772702541, 43, 78, 110, 'Gain Muscle', '3-5 x times a week', 23),
(43, 'Abigail43', 'password170', '{"bmi": 20.4, "fat_percentage": 24.1}', 154.77520980511494, 65.4531813834081, 58.61193986460853, 16, 90, 125, 'Lose Weight', '3-5 x times a week', 41),
(44, 'Charlotte44', 'password187', '{"bmi": 24.6, "fat_percentage": 21.6}', 198.44651603965696, 99.87336047732794, 92.50446850189664, 39, 70, 111, 'Gain Muscle', '5-6 x times a week', 23),
(45, 'Mia45', 'password162', '{"bmi": 21.6, "fat_percentage": 17.3}', 184.52569521651856, 80.74380747303071, 71.64550727872178, 10, 85, 127, 'Increase Flexibility', '1-3 x times a week', 24),
(46, 'Samuel46', 'password978', '{"bmi": 29.3, "fat_percentage": 12.4}', 193.49485664780238, 55.597646786558606, 48.3893479260422, 28, 89, 124, 'Gain Muscle', '3-5 x times a week', 35),
(47, 'Scarlett47', 'password679', '{"bmi": 24.4, "fat_percentage": 12.3}', 193.8475825972048, 97.89208755487509, 83.8385323576267, 38, 83, 116, 'Gain Muscle', '1-3 x times a week', 41),
(48, 'William48', 'password788', '{"bmi": 26.1, "fat_percentage": 19.8}', 164.18473603559468, 84.13905502583324, 71.46324695148986, 50, 70, 112, 'Lose Weight', '5-6 x times a week', 47),
(49, 'Lucas49', 'password845', '{"bmi": 19.8, "fat_percentage": 23.1}', 150.275687111759, 72.5811366751885, 67.45430448969643, 16, 74, 123, 'Increase Flexibility', '3-5 x times a week', 26),
(50, 'Joseph50', 'password382', '{"bmi": 27.7, "fat_percentage": 22.7}', 153.3271326276333, 60.06987762663082, 46.67593883744037, 14, 90, 127, 'Gain Muscle', '5-6 x times a week', 55),
(51, 'Emma51', 'password217', '{"bmi": 20.2, "fat_percentage": 13.0}', 158.6725674610545, 82.02708007949417, 73.77895128514788, 28, 71, 121, 'Increase Flexibility', '3-5 x times a week', 49),
(52, 'Max52', 'password377', '{"bmi": 24.4, "fat_percentage": 11.5}', 167.19397342344627, 52.00618954287371, 42.71693077998316, 35, 76, 114, 'Increase Flexibility', '3-5 x times a week', 52),
(53, 'Harper53', 'password653', '{"bmi": 29.1, "fat_percentage": 15.6}', 155.83552052129644, 93.70512315316174, 84.80350775973564, 10, 77, 110, 'Increase Flexibility', '3-5 x times a week', 34),
(54, 'Mia54', 'password767', '{"bmi": 20.2, "fat_percentage": 10.9}', 169.00139538545082, 53.38938503411142, 38.80955994046907, 35, 79, 123, 'Lose Weight', '3-5 x times a week', 45),
(55, 'Michael55', 'password595', '{"bmi": 22.5, "fat_percentage": 10.3}', 189.6111014755746, 90.64550638469609, 82.49608509531265, 13, 71, 122, 'Lose Weight', '3-5 x times a week', 24),
(56, 'David56', 'password437', '{"bmi": 24.3, "fat_percentage": 19.8}', 192.70659631677793, 78.29684982772774, 67.84415780398285, 36, 81, 129, 'Increase Flexibility', '3-5 x times a week', 32),
(57, 'Penelope57', 'password294', '{"bmi": 22.7, "fat_percentage": 16.8}', 165.5831217328942, 66.05302046903937, 51.66572314767599, 44, 71, 125, 'Gain Muscle', '3-5 x times a week', 53),
(58, 'Emma58', 'password683', '{"bmi": 19.1, "fat_percentage": 23.4}', 163.66914771959648, 61.060279486899866, 54.682319608661444, 35, 77, 116, 'Gain Muscle', '5-6 x times a week', 32),
(59, 'Ava59', 'password145', '{"bmi": 19.4, "fat_percentage": 17.7}', 193.995291037141, 89.08984800842599, 76.28417336764885, 44, 90, 130, 'Lose Weight', '3-5 x times a week', 56),
(60, 'Isabella60', 'password657', '{"bmi": 23.3, "fat_percentage": 10.2}', 183.08859809599906, 75.2783258168285, 67.89670488692595, 41, 84, 113, 'Increase Flexibility', '3-5 x times a week', 28),
(61, 'Benjamin61', 'password942', '{"bmi": 27.5, "fat_percentage": 18.7}', 162.2890894982305, 97.65989156675064, 91.87370379057106, 51, 74, 121, 'Lose Weight', '3-5 x times a week', 37),
(62, 'Ethan62', 'password463', '{"bmi": 19.6, "fat_percentage": 11.1}', 175.7838680882335, 77.56705471407965, 67.75581293789364, 22, 86, 113, 'Gain Muscle', '1-3 x times a week', 45),
(63, 'Logan63', 'password580', '{"bmi": 20.2, "fat_percentage": 23.3}', 184.59062279959528, 86.57648303439257, 78.40007583425037, 42, 73, 126, 'Gain Muscle', '3-5 x times a week', 53),
(64, 'Abigail64', 'password298', '{"bmi": 26.3, "fat_percentage": 24.7}', 177.06319757045708, 85.82950851164412, 74.48316034962457, 51, 87, 117, 'Gain Muscle', '5-6 x times a week', 51),
(65, 'Olivia65', 'password635', '{"bmi": 21.3, "fat_percentage": 10.3}', 170.84850806761767, 97.10049294967558, 85.83259163701487, 27, 72, 124, 'Gain Muscle', '3-5 x times a week', 42),
(66, 'David66', 'password565', '{"bmi": 28.8, "fat_percentage": 11.8}', 159.72141540978492, 64.05287271214962, 52.10773100592125, 43, 77, 123, 'Increase Flexibility', '1-3 x times a week', 26),
(67, 'Julia67', 'password345', '{"bmi": 25.1, "fat_percentage": 19.3}', 175.6089551031755, 78.78396782126855, 67.55209657122326, 18, 77, 110, 'Lose Weight', '3-5 x times a week', 45),
(68, 'Penelope68', 'password339', '{"bmi": 26.1, "fat_percentage": 23.6}', 167.372842041709, 53.98348452467876, 41.26491969484112, 51, 81, 110, 'Lose Weight', '1-3 x times a week', 49),
(69, 'Grace69', 'password631', '{"bmi": 26.3, "fat_percentage": 16.8}', 152.64620334727147, 90.72249870876752, 80.30317059117745, 10, 82, 115, 'Increase Flexibility', '3-5 x times a week', 60),
(70, 'Joseph70', 'password351', '{"bmi": 21.9, "fat_percentage": 20.0}', 183.41059434837635, 71.79407630179507, 59.52276995866336, 29, 76, 120, 'Increase Flexibility', '3-5 x times a week', 49);

-- Inserting into Trainer Availability
INSERT INTO myapp_traineravailability (trainer_id, day_of_week, check_in, check_out)
VALUES
(2, 1, '10:00:00', '16:00:00'),
(1, 1, '08:00:00', '12:00:00'),
(2, 3, '10:00:00', '14:00:00'),
(3, 1, '09:00:00', '13:00:00'),
(3, 4, '11:00:00', '15:00:00'),
(4, 2, '12:00:00', '18:00:00'),
(4, 5, '10:00:00', '14:00:00'),
(5, 1, '08:00:00', '12:00:00'),
(5, 3, '14:00:00', '18:00:00'),
(6, 2, '06:00:00', '12:00:00'),
(6, 5, '06:00:00', '10:00:00'),
(7, 1, '09:00:00', '13:00:00'),
(7, 3, '12:00:00', '16:00:00'),
(8, 2, '11:00:00', '17:00:00'),
(8, 4, '09:00:00', '13:00:00'),
(1, 2, '13:00:00', '17:00:00'),
(1, 4, '08:00:00', '12:00:00'),
(2, 5, '11:00:00', '15:00:00'),
(3, 6, '09:00:00', '13:00:00'),
(4, 6, '14:00:00', '18:00:00'),
(5, 6, '10:00:00', '14:00:00'),
(6, 7, '08:00:00', '12:00:00'),
(7, 7, '13:00:00', '17:00:00'),
(8, 7, '10:00:00', '16:00:00');


-- Inserting into Personal Sessions
INSERT INTO myapp_personalsession (trainer_id, member_id, date, start_time, end_time)
VALUES 
(1, 1, '2024-04-15', '09:00:00', '10:00:00'),
(2, 2, '2024-04-16', '11:00:00', '12:00:00'),
(1, 3, '2024-04-18', '10:00:00', '11:00:00'),
(2, 4, '2024-04-19', '13:00:00', '14:00:00'),
(1, 5, '2024-04-20', '08:00:00', '09:00:00'),
(2, 1, '2024-04-21', '14:00:00', '15:00:00'),
(6, 0, '2024-04-14', '08:00:00', '09:00:00');


-- Inserting into Group Fitness Classes
INSERT INTO myapp_groupfitnessclass (trainer_id, room_id, date, start_time, end_time)
VALUES 
(1, 101, '2024-04-16', '10:00:00', '11:00:00'),
(2, 102, '2024-04-17', '09:00:00', '10:00:00'),
(1, 103, '2024-04-18', '12:00:00', '13:00:00'),
(2, 104, '2024-04-19', '15:00:00', '16:00:00'),
(1, 105, '2024-04-20', '07:00:00', '08:00:00'),
(2, 101, '2024-04-21', '16:00:00', '17:00:00');

-- Inserting into Member Group Fitness Registration
INSERT INTO myapp_membergroupfitnessregistration (group_fitness_class_id, member_id, registration_date)
VALUES 
(1, 1, '2024-04-01'),
(2, 2, '2024-04-02');

INSERT INTO public.myapp_equipmentmaintenance (name, last_maintenance_date, next_maintenance_date, status)
VALUES 
    ('Treadmill 1', '2023-12-15', '2024-05-15', 'FUNCTIONING'),
    ('Elliptical Machine', '2023-11-20', '2024-06-20', 'FUNCTIONING'),
    ('Stationary Bike', '2023-10-10', '2024-07-10', 'IN_MAINTENANCE'),
    ('Weight Bench', '2024-01-05', '2024-08-05', 'BROKEN'),
    ('Dumbbell Set 1', '2024-02-10', '2024-09-10', 'FUNCTIONING'),
    ('Rowing Machine', '2024-03-25', '2024-10-25', 'FUNCTIONING'),
    ('Exercise Ball', '2024-04-08', '2024-11-08', 'IN_MAINTENANCE');
-- Insert 7 rows into myapp_room
INSERT INTO public.myapp_room (name)
VALUES 
    ('Room 101 - Spin Studio'),
    ('Room 102'),
    ('Room 103 - Yoga Studio'),
    ('Room 104'),
    ('Room 105 - Cardio Zone'),
    ('Room 106'),
    ('Room 107 - Weightlifting Area');

-- Insert 7 rows into myapp_roombooking
INSERT INTO public.myapp_roombooking (start_time, end_time, room_id)
VALUES 
    ('2024-04-13 10:00:00', '2024-04-13 11:00:00', 1),
    ('2024-04-13 12:00:00', '2024-04-13 13:00:00', 2),
    ('2024-04-13 14:00:00', '2024-04-13 15:00:00', 3),
    ('2024-04-13 16:00:00', '2024-04-13 17:00:00', 4),
    ('2024-04-13 18:00:00', '2024-04-13 19:00:00', 5),
    ('2024-04-13 20:00:00', '2024-04-13 21:00:00', 6),
    ('2024-04-13 22:00:00', '2024-04-13 23:00:00', 7);




INSERT INTO myapp_admin (admin_id, name, password)
VALUES (1, 'dhirran', 'dhirran'),

INSERT INTO myapp_admin (admin_id, name, password)
VALUES (2, 'admin', 'admin');

INSERT INTO myapp_member (member_id, name, password, health_metrics, height, weight, goal_weight, weeks_to_goal, diastolic_bp, systolic_bp, fitness_goal, act_levels)
VALUES 
(71, 'dhirran', 'dhirran', '{"bmi": 25, "fat_percentage": 20}', 165.0, 80.0, 70.0, 10, 85, 125, 'Lose weight','1-3 x times a week');

