DROP DATABASE IF EXISTS skydiving;
CREATE DATABASE skydiving;
USE skydiving;

DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
	employee_id TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	employee_name VARCHAR(20),
    employee_surname VARCHAR(20),
    employee_position ENUM('skydiving-instructor', 'safety-instructor', 'trainer', 'manager', 'mechanic', 'pylot'),
    contact_info VARCHAR(14),
    employee_photo BLOB
);

INSERT INTO employees (employee_name, employee_surname, employee_position, contact_info) VALUES
('Ivan', 'Petrov', 'skydiving-instructor', '+375456789034'),
('Maria', 'Ivanova', 'skydiving-instructor', '+375765432167'),
('Alexey', 'Smirnov', 'safety-instructor', '+375790246877'),
('Elena', 'Kozlova', 'safety-instructor', '+375801357923'),
('Sergey', 'Nikolaev', 'trainer', '+375258147089'),
('Olga', 'Stepanova', 'trainer', '+375258369076'),
('Dmitriy', 'Kovalev', 'manager', '+375369147064'),
('Anna', 'Semenova', 'manager', '+375753824639'),
('Pavel', 'Morozov', 'mechanic', '+375951824622'),
('Natalia', 'Fedorova', 'mechanic', '+375615937011'),
('Alexander', 'Kuznetsov', 'pylot', '+375937082469'),
('Lyudmila', 'Ivanova', 'pylot', '+375082461529');

DROP TABLE IF EXISTS contracts;
CREATE TABLE contracts (
	contract_id TINYINT UNSIGNED AUTO_INCREMENT,
	contract_start_date DATE,
    contract_end_date DATE,
    employee_salary DECIMAL(6, 2),
    CONSTRAINT employee_contract FOREIGN KEY (contract_id) REFERENCES employees(employee_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO contracts (contract_start_date, contract_end_date, employee_salary) VALUES
('2021-05-10', '2026-07-15', 1200.00),
('2021-09-20', '2027-02-28', 1500.00),
('2021-11-03', '2028-09-10', 1800.00),
('2022-02-15', '2027-12-31', 2000.00),
('2022-07-08', '2029-03-25', 1600.00),
('2022-10-30', '2028-08-20', 1700.00),
('2023-01-18', '2027-10-05', 1900.00),
('2023-04-22', '2029-01-15', 1400.00),
('2023-09-07', '2026-05-30', 1300.00),
('2022-02-05', '2028-11-18', 800.00),
('2021-06-14', '2027-08-22', 1100.00),
('2023-10-09', '2029-04-03', 1750.00);

DROP TABLE IF EXISTS courses;
CREATE TABLE courses (
	course_id TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	course_name VARCHAR(30),
    course_hours TINYINT UNSIGNED,
    course_jumps TINYINT UNSIGNED
);

INSERT INTO courses
(course_name, course_hours, course_jumps)
VALUES
('Basic Freefall Skills', 60, 20),
('Canopy Control', 40, 0),
('Tandem Jumping', 40, 30),
('Advanced Freefall Techniques', 60, 0),
('Safety Course', 40, 0),
('Competition Training', 40, 0),
('Instructor Courses', 40, 0),
('Specialized Courses', 40, 0);

DROP TABLE IF EXISTS equipment;
CREATE TABLE equipment (
	equipment_id TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	equipment_name VARCHAR(40),
    available_equipment_amount INT UNSIGNED,
    equipment_condition ENUM('operational', 'under-maintenance', 'out-of-service')
);

INSERT INTO equipment 
(equipment_name, available_equipment_amount, equipment_condition) 
VALUES
('Parachute Open Air', 10, 'operational'),
('Parachute JumpMaster', 8, 'operational'),
('Parachute SkyBlaze', 15, 'operational'),
('Parachute SkyPro', 12, 'under-maintenance'),
('Parachute AeroGlide', 20, 'operational'),
('Parachute AirJump', 7, 'out-of-service'),
('Helmet SkySafe', 25, 'operational'),
('Helmet AeroGuard', 20, 'operational'),
('Helmet JumpTech', 18, 'under-maintenance'),
('Helmet SkyVision', 10, 'operational'),
('Helmet AirMaster', 30, 'out-of-service'),
('Goggles SkyView', 15, 'operational'),
('Goggles AirSight', 22, 'operational'),
('Goggles JumpEye', 9, 'under-maintenance'),
('Goggles SkyGuard', 18, 'operational'),
('Goggles AeroOptic', 25, 'out-of-service'),
('Jumpsuit SkySuit', 20, 'operational'),
('Jumpsuit AeroFit', 18, 'operational'),
('Jumpsuit FreeFlow', 13, 'under-maintenance'),
('Jumpsuit SkyFlex', 15, 'operational'),
('Jumpsuit AeroFlow', 10, 'out-of-service'),
('Altimeter SkySense', 30, 'operational'),
('Altimeter AeroAlt', 25, 'operational'),
('Altimeter AirSense', 20, 'under-maintenance'),
('Altimeter SkyMeter', 12, 'operational'),
('Altimeter AeroMeter', 8, 'out-of-service'),
('Radio SkyCom', 10, 'operational'),
('Radio AeroLink', 8, 'operational'),
('Radio AirWave', 5, 'under-maintenance'),
('Radio SkyTalk', 15, 'operational'),
('Radio AeroCall', 12, 'out-of-service'),
('Harness SkyFit', 20, 'operational'),
('Harness AeroGuard', 18, 'operational'),
('Harness AirSecure', 15, 'under-maintenance'),
('Harness SkyHold', 10, 'operational'),
('Harness AeroStrap', 7, 'out-of-service'),
('Packing Mat SkyPack', 25, 'operational'),
('Packing Mat AeroMat', 22, 'operational'),
('Packing Mat AirPack', 18, 'under-maintenance'),
('Packing Mat SkyMat', 20, 'operational'),
('Packing Mat AeroPack', 15, 'out-of-service'),
('Reserve Parachute SkySafe', 30, 'operational'),
('Reserve Parachute AeroGuard', 28, 'operational'),
('Reserve Parachute AirMaster', 24, 'under-maintenance'),
('Reserve Parachute SkyRescue', 15, 'operational'),
('Reserve Parachute AeroRescue', 10, 'out-of-service'),
('Rigging Knife SkyCut', 15, 'operational'),
('Rigging Knife AeroRig', 12, 'operational'),
('Rigging Knife AirKnife', 10, 'under-maintenance'),
('Rigging Knife SkyBlade', 8, 'operational'),
('Rigging Knife AeroEdge', 5, 'out-of-service'),
('Drop Zone Sign SkyZone', 10, 'operational'),
('Drop Zone Sign AeroSign', 8, 'operational'),
('Drop Zone Sign AirSign', 5, 'under-maintenance'),
('Drop Zone Sign SkyMark', 12, 'operational'),
('Drop Zone Sign AeroMark', 10, 'out-of-service'),
('Windsock SkySock', 15, 'operational'),
('Windsock AeroWind', 12, 'operational'),
('Windsock AirFlow', 10, 'under-maintenance'),
('Windsock SkyBreeze', 8, 'operational'),
('Windsock AeroView', 6, 'out-of-service'),
('Rigging Table SkyTable', 8, 'operational'),
('Rigging Table AeroRig', 6, 'operational'),
('Rigging Table AirRig', 5, 'under-maintenance'),
('Rigging Table SkyStation', 10, 'operational'),
('Rigging Table AeroStation', 8, 'out-of-service'),
('First Aid Kit SkyAid', 10, 'operational'),
('First Aid Kit AeroKit', 8, 'operational'),
('First Aid Kit AirKit', 5, 'under-maintenance'),
('First Aid Kit SkySafe', 12, 'operational'),
('First Aid Kit AeroGuard', 10, 'out-of-service'),
('Pack of Bandages SkyBand', 15, 'operational'),
('Pack of Bandages AeroBand', 12, 'operational'),
('Pack of Bandages AirBand', 10, 'under-maintenance'),
('Pack of Bandages SkyPatch', 8, 'operational'),
('Pack of Bandages AeroPatch', 6, 'out-of-service'),
('Splint SkySplint', 8, 'operational'),
('Splint AeroSplint', 6, 'operational'),
('Splint AirSplint', 5, 'under-maintenance'),
('Splint SkyFix', 10, 'operational'),
('Splint AeroFix', 8, 'out-of-service'),
('AED Defibrillator SkyDefib', 10, 'operational'),
('AED Defibrillator AeroDefib', 8, 'operational'),
('AED Defibrillator AirDefib', 5, 'under-maintenance'),
('AED Defibrillator SkyShock', 12, 'operational'),
('AED Defibrillator AeroShock', 10, 'out-of-service'),
('Oxygen Tank SkyOx', 15, 'operational'),
('Oxygen Tank AeroOx', 12, 'operational'),
('Oxygen Tank AirOx', 10, 'under-maintenance'),
('Oxygen Tank SkyAir', 8, 'operational'),
('Oxygen Tank AeroAir', 6, 'out-of-service'),
('Medical Kit SkyAid', 8, 'operational'),
('Medical Kit AeroKit', 6, 'operational'),
('Medical Kit AirKit', 5, 'under-maintenance'),
('Medical Kit SkyRescue', 10, 'operational'),
('Medical Kit AeroRescue', 8, 'out-of-service'),
('Jump Log Book SkyLog', 10, 'operational'),
('Jump Log Book AeroLog', 8, 'operational'),
('Jump Log Book AirLog', 5, 'under-maintenance'),
('Jump Log Book SkyRecord', 12, 'operational'),
('Jump Log Book AeroRecord', 10, 'out-of-service'),
('Training Manual SkyManual', 15, 'operational'),
('Training Manual AeroManual', 12, 'operational'),
('Training Manual AirManual', 10, 'under-maintenance'),
('Training Manual SkyGuide', 8, 'operational'),
('Training Manual AeroGuide', 6, 'out-of-service'),
('Safety Video DVD SkyDVD', 8, 'operational'),
('Safety Video DVD AeroDVD', 6, 'operational'),
('Safety Video DVD AirDVD', 5, 'under-maintenance'),
('Safety Video DVD SkySafe', 10, 'operational'),
('Safety Video DVD AeroGuard', 8, 'out-of-service'),
('Manifest Computer SkyComputer', 10, 'operational'),
('Manifest Computer AeroComputer', 8, 'operational'),
('Manifest Computer AirComputer', 5, 'under-maintenance'),
('Manifest Computer SkyManager', 12, 'operational'),
('Manifest Computer AeroManager', 10, 'out-of-service'),
('Scale SkyScale', 15, 'operational'),
('Scale AeroScale', 12, 'operational'),
('Scale AirScale', 10, 'under-maintenance'),
('Scale SkyBalance', 8, 'operational'),
('Scale AeroBalance', 6, 'out-of-service'),
('Cash Register SkyCash', 8, 'operational'),
('Cash Register AeroCash', 6, 'operational'),
('Cash Register AirCash', 5, 'under-maintenance'),
('Cash Register SkyRegister', 10, 'operational'),
('Cash Register AeroRegister', 8, 'out-of-service'),
('Credit Card Terminal SkyTerminal', 10, 'operational'),
('Credit Card Terminal AeroTerminal', 8, 'operational'),
('Credit Card Terminal AirTerminal', 5, 'under-maintenance'),
('Credit Card Terminal SkyCard', 12, 'operational'),
('Credit Card Terminal AeroCard', 10, 'out-of-service'),
('Computer SkyComputer', 15, 'operational'),
('Computer AeroComputer', 12, 'operational'),
('Computer AirComputer', 10, 'under-maintenance'),
('Computer SkyPC', 8, 'operational'),
('Computer AeroPC', 6, 'out-of-service'),
('Printer SkyPrint', 8, 'operational'),
('Printer AeroPrint', 6, 'operational'),
('Printer AirPrint', 5, 'under-maintenance'),
('Printer SkyPress', 10, 'operational'),
('Printer AeroPress', 8, 'out-of-service'),
('Scanner SkyScan', 10, 'operational'),
('Scanner AeroScan', 8, 'operational'),
('Scanner AirScan', 5, 'under-maintenance'),
('Scanner SkyView', 12, 'operational'),
('Scanner AeroView', 10, 'out-of-service'),
('Photocopier SkyCopy', 15, 'operational'),
('Photocopier AeroCopy', 12, 'operational'),
('Photocopier AirCopy', 10, 'under-maintenance'),
('Photocopier SkyPress', 8, 'operational'),
('Photocopier AeroPress', 6, 'out-of-service'),
('Desk SkyDesk', 8, 'operational'),
('Desk AeroDesk', 6, 'operational'),
('Desk AirDesk', 5, 'under-maintenance'),
('Desk SkyTable', 10, 'operational'),
('Desk AeroTable', 8, 'out-of-service'),
('Chair SkyChair', 10, 'operational'),
('Chair AeroChair', 8, 'operational'),
('Chair AirChair', 5, 'under-maintenance'),
('Chair SkySeat', 12, 'operational'),
('Chair AeroSeat', 10, 'out-of-service');

DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses (
	address_id TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	address_building_name VARCHAR(30),
    address_name VARCHAR(50),
    geographical_coords VARCHAR(30)
);

INSERT INTO addresses
(address_building_name, address_name, geographical_coords) 
VALUES
('Sunset Apartments', '123 Main Street, Sunset Blvd', '35.6895° N, 139.6917° E'),
('Greenwood Villas', '456 Elm Avenue, Greenwood', '40.7128° N, 74.0060° W'),
('Oceanview Towers', '789 Ocean Drive, Oceanview', '33.9416° N, 118.4085° W'),
('Maplewood Manor', '1010 Maple Lane, Maplewood', '51.5074° N, 0.1278° W'),
('Riverside Residences', '1313 River Road, Riverside', '34.0522° N, 118.2437° W'),
('Mountainview Estates', '1515 Hilltop Avenue, Mountainview', '37.3861° N, 122.0839° W');

DROP TABLE IF EXISTS student_groups;
CREATE TABLE student_groups(
	group_id TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    course_id TINYINT UNSIGNED,
    group_name VARCHAR(1)
);

INSERT INTO student_groups
(course_id, group_name)
VALUES
(1, "A"),
(3, "B"),
(5, "C"),
(6, "D"),
(7, "E");

DROP TABLE IF EXISTS students;
CREATE TABLE students (
	student_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	group_id TINYINT UNSIGNED,
    student_first_name VARCHAR(20),
    student_second_name VARCHAR(20),
    student_birthday DATE,
    student_sex ENUM('female', 'male'),
    student_contact_info VARCHAR(13),
    student_level ENUM('beginner', 'intermediate', 'advanced', 'expert', 'master'),
    enrollment_date DATE,
    completion_date DATE,
    status ENUM ('active', 'closed', 'expelled'),
    CONSTRAINT group_student FOREIGN KEY (group_id) REFERENCES student_groups(group_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO students (group_id, student_first_name, student_second_name, student_birthday, student_sex, student_contact_info, student_level, enrollment_date, completion_date, status) VALUES
(1, 'Alice', 'Smith', '2000-03-15', 'female', '+375291234567', 'beginner', '2023-05-01', '2023-11-01', 'closed'),
(1, 'Bob', 'Johnson', '2001-05-20', 'male', '+375291234568', 'intermediate', '2023-05-02', '2023-11-02', 'closed'),
(1, 'Charlie', 'Brown', '1999-09-10', 'male', '+375291234569', 'advanced', '2023-05-03', '2023-11-03', 'closed'),
(1, 'David', 'Wilson', '2002-02-25', 'male', '+375291234570', 'expert', '2023-05-04', '2023-11-04', 'closed'),
(1, 'Emma', 'Anderson', '2000-07-12', 'female', '+375291234571', 'master', '2023-05-05', '2023-11-05', 'closed'),
(1, 'Ethan', 'Martinez', '2001-11-30', 'male', '+375291234572', 'beginner', '2023-05-06', '2023-11-06', 'closed'),
(1, 'Olivia', 'Taylor', '2000-01-08', 'female', '+375291234573', 'intermediate', '2023-05-07', '2023-11-07', 'closed'),
(1, 'Michael', 'Thomas', '2002-04-18', 'male', '+375291234574', 'advanced', '2023-05-08', '2023-11-08', 'closed'),
(1, 'Sophia', 'Hernandez', '2001-06-22', 'female', '+375291234575', 'expert', '2023-05-09', '2023-11-09', 'closed'),
(1, 'William', 'Garcia', '2000-08-05', 'male', '+375291234576', 'master', '2023-05-10', '2023-11-10', 'closed'),
(1, 'Isabella', 'Young', '2001-10-14', 'female', '+375291234577', 'beginner', '2023-05-11', '2023-11-11', 'closed'),
(1, 'James', 'Lopez', '2000-12-28', 'male', '+375291234578', 'intermediate', '2023-05-12', '2023-11-12', 'closed'),
(1, 'Mia', 'Lewis', '1999-02-19', 'female', '+375291234579', 'advanced', '2023-05-13', '2023-11-13', 'closed'),
(1, 'Alexander', 'King', '2002-03-07', 'male', '+375291234580', 'expert', '2023-05-14', '2023-11-14', 'closed'),
(1, 'Charlotte', 'Scott', '2000-05-31', 'female', '+375291234581', 'master', '2023-05-15', '2023-11-15', 'closed'),
(1, 'Benjamin', 'Green', '2001-09-04', 'male', '+375291234582', 'beginner', '2023-05-16', '2023-11-16', 'closed'),
(1, 'Amelia', 'Adams', '1999-11-11', 'female', '+375291234583', 'intermediate', '2023-05-17', '2023-11-17', 'closed'),
(1, 'Daniel', 'Baker', '2002-01-26', 'male', '+375291234584', 'advanced', '2023-05-18', '2023-11-18', 'closed'),
(1, 'Evelyn', 'Rivera', '2000-04-01', 'female', '+375291234585', 'expert', '2023-05-19', '2023-11-19', 'closed'),
(1, 'Joseph', 'Campbell', '2001-07-07', 'male', '+375291234586', 'master', '2023-05-20', '2023-11-20', 'closed'),
(2, 'Harper', 'Mitchell', '2000-09-15', 'female', '+375291234587', 'beginner', '2023-05-21', '2023-11-21', 'closed'),
(2, 'Samuel', 'Perez', '1999-12-02', 'male', '+375291234588', 'intermediate', '2023-05-22', '2023-11-22', 'closed'),
(2, 'Avery', 'Roberts', '2002-02-11', 'female', '+375291234589', 'advanced', '2023-05-23', '2023-11-23', 'closed'),
(2, 'Logan', 'Turner', '2000-06-29', 'male', '+375291234590', 'expert', '2023-05-24', '2023-11-24', 'closed'),
(2, 'Ella', 'Cook', '2001-08-23', 'female', '+375291234591', 'master', '2023-05-25', '2023-11-25', 'closed'),
(2, 'Liam', 'Morris', '2000-11-01', 'male', '+375291234592', 'beginner', '2023-05-26', '2023-11-26', 'closed'),
(2, 'Grace', 'Ward', '2002-01-10', 'female', '+375291234593', 'intermediate', '2023-05-27', '2023-11-27', 'closed'),
(2, 'Lucas', 'Bailey', '1999-03-25', 'male', '+375291234594', 'advanced', '2023-05-28', '2023-11-28', 'closed'),
(2, 'Chloe', 'Cox', '2001-05-12', 'female', '+375291234595', 'expert', '2023-05-29', '2023-11-29', 'closed'),
(2, 'Mason', 'Howard', '2000-07-19', 'male', '+375291234596', 'master', '2023-05-30', '2023-11-30', 'closed'),
(2, 'Lily', 'Long', '2001-10-08', 'female', '+375291234597', 'beginner', '2023-06-01', '2023-11-01', 'closed'),
(2, 'Jack', 'Collins', '2000-12-17', 'male', '+375291234598', 'intermediate', '2023-06-02', '2023-11-02', 'closed'),
(2, 'Aria', 'Bell', '1999-02-03', 'female', '+375291234599', 'advanced', '2023-06-03', '2023-11-03', 'closed'),
(2, 'Jackson', 'Russell', '2002-04-22', 'male', '+375291234600', 'expert', '2023-06-04', '2023-11-04', 'closed'),
(2, 'Aurora', 'Coleman', '2000-06-08', 'female', '+375291234601', 'master', '2023-06-05', '2023-11-05', 'closed'),
(2, 'Ryan', 'Bell', '2001-08-27', 'male', '+375291234602', 'beginner', '2023-06-06', '2023-11-06', 'closed'),
(2, 'Scarlett', 'Foster', '2000-10-14', 'female', '+375291234603', 'intermediate', '2023-06-07', '2023-11-07', 'closed'),
(2, 'Elijah', 'Sanders', '1999-12-31', 'male', '+375291234604', 'advanced', '2023-06-08', '2023-11-08', 'closed'),
(2, 'Hannah', 'Bennett', '2002-02-16', 'female', '+375291234605', 'expert', '2023-06-09', '2023-11-09', 'closed'),
(2, 'Nathan', 'Barnes', '2000-04-03', 'male', '+375291234606', 'master', '2023-06-10', '2023-11-10', 'closed'),
(2, 'Zoe', 'Gray', '2001-06-20', 'female', '+375291234607', 'beginner', '2023-06-11', '2023-11-11', 'closed'),
(2, 'Carter', 'Woods', '2000-09-09', 'male', '+375291234608', 'intermediate', '2023-06-12', '2023-11-12', 'closed'),
(3, 'Madison', 'Knight', '1999-11-24', 'female', '+375291234609', 'advanced', '2023-06-13', '2023-11-13', 'closed'),
(3, 'Henry', 'Porter', '2002-01-11', 'male', '+375291234610', 'expert', '2023-06-14', '2023-11-14', 'closed'),
(3, 'Stella', 'Fisher', '2000-03-29', 'female', '+375291234611', 'master', '2023-06-15', '2023-11-15', 'closed'),
(3, 'Christopher', 'Griffin', '2001-05-16', 'male', '+375291234612', 'beginner', '2023-06-16', '2023-11-16', 'closed'),
(3, 'Leah', 'Hunter', '2000-07-05', 'female', '+375291234613', 'intermediate', '2023-06-17', '2023-11-17', 'closed'),
(3, 'Wyatt', 'Hicks', '1999-09-22', 'male', '+375291234614', 'advanced', '2023-06-18', '2023-11-18', 'closed'),
(3, 'Bella', 'Lawrence', '2002-11-07', 'female', '+375291234615', 'expert', '2023-06-19', '2023-11-19', 'closed'),
(3, 'Andrew', 'Simmons', '2000-01-24', 'male', '+375291234616', 'master', '2023-06-20', '2023-11-20', 'closed'),
(3, 'Nora', 'Harrison', '2001-04-01', 'female', '+375291234617', 'beginner', '2023-06-21', '2023-11-21', 'closed'),
(3, 'Gabriel', 'Reid', '2000-06-18', 'male', '+375291234618', 'intermediate', '2023-06-22', '2023-11-22', 'closed'),
(3, 'Aubrey', 'Murray', '1999-08-05', 'female', '+375291234619', 'advanced', '2023-06-23', '2023-11-23', 'closed'),
(3, 'Eli', 'Cole', '2002-10-22', 'male', '+375291234620', 'expert', '2023-06-24', '2023-11-24', 'closed'),
(3, 'Audrey', 'Stone', '2000-12-09', 'female', '+375291234621', 'master', '2023-06-25', '2023-11-25', 'closed'),
(3, 'Owen', 'Pierce', '2002-02-26', 'male', '+375291234622', 'beginner', '2023-06-26', '2023-11-26', 'closed'),
(3, 'Penelope', 'Ferguson', '2001-04-15', 'female', '+375291234623', 'intermediate', '2023-06-27', '2023-11-27', 'closed'),
(3, 'Lincoln', 'Snyder', '2000-06-02', 'male', '+375291234624', 'advanced', '2023-06-28', '2023-11-28', 'closed'),
(3, 'Clara', 'Howard', '1999-07-19', 'female', '+375291234625', 'expert', '2023-06-29', '2023-11-29', 'closed'),
(3, 'Julian', 'Chambers', '2002-09-05', 'male', '+375291234626', 'master', '2023-06-30', '2023-11-30', 'closed'),
(3, 'Riley', 'Stephens', '2000-11-25', 'female', '+375291234627', 'beginner', '2023-07-01', '2023-11-01', 'closed'),
(3, 'Violet', 'Watson', '2002-01-12', 'female', '+375291234628', 'intermediate', '2023-07-02', '2023-11-02', 'closed'),
(3, 'Tristan', 'Dunn', '2000-03-30', 'male', '+375291234629', 'advanced', '2023-07-03', '2023-11-03', 'closed'),
(4, 'Hazel', 'Ford', '2001-05-17', 'female', '+375291234630', 'expert', '2023-07-04', '2023-11-04', 'closed'),
(4, 'Everett', 'Mcdonald', '1999-07-04', 'male', '+375291234631', 'master', '2023-07-05', '2023-11-05', 'closed'),
(4, 'Luna', 'Grant', '2002-08-21', 'female', '+375291234632', 'beginner', '2023-07-06', '2023-11-06', 'closed'),
(4, 'Emmett', 'Fowler', '2000-10-08', 'male', '+375291234633', 'intermediate', '2023-07-07', '2023-11-07', 'closed'),
(4, 'Adeline', 'Wheeler', '1999-12-25', 'female', '+375291234634', 'advanced', '2023-07-08', '2023-11-08', 'closed'),
(4, 'Hudson', 'Stanley', '2002-02-10', 'male', '+375291234635', 'expert', '2023-07-09', '2023-11-09', 'closed'),
(4, 'Emilia', 'Gordon', '2000-04-27', 'female', '+375291234636', 'master', '2023-07-10', '2023-11-10', 'closed'),
(4, 'Finn', 'Jordan', '2001-06-14', 'male', '+375291234637', 'beginner', '2023-07-11', '2023-11-11', 'closed'),
(4, 'Ivy', 'Barrett', '2000-08-01', 'female', '+375291234638', 'intermediate', '2023-07-12', '2023-11-12', 'closed'),
(4, 'Beckett', 'Newton', '1999-09-18', 'male', '+375291234639', 'advanced', '2023-07-13', '2023-11-13', 'closed'),
(4, 'Aaliyah', 'Holt', '2002-11-05', 'female', '+375291234640', 'expert', '2023-07-14', '2023-11-14', 'closed'),
(4, 'Graham', 'Owen', '2000-01-22', 'male', '+375291234641', 'master', '2023-07-15', '2023-11-15', 'closed'),
(4, 'Reese', 'Rice', '2001-03-11', 'female', '+375291234642', 'beginner', '2023-07-16', '2023-11-16', 'closed'),
(4, 'Lila', 'Church', '2000-05-28', 'female', '+375291234643', 'intermediate', '2023-07-17', '2023-11-17', 'closed'),
(4, 'Kai', 'Saunders', '1999-07-15', 'male', '+375291234644', 'advanced', '2023-07-18', '2023-11-18', 'closed'),
(4, 'Elise', 'Tate', '2002-09-01', 'female', '+375291234645', 'expert', '2023-07-19', '2023-11-19', 'closed'),
(4, 'Zachary', 'Fitzgerald', '2000-10-18', 'male', '+375291234646', 'master', '2023-07-20', '2023-11-20', 'closed'),
(4, 'Lucy', 'Rogers', '2002-12-05', 'female', '+375291234647', 'beginner', '2023-07-21', '2023-11-21', 'closed'),
(4, 'Arthur', 'Morgan', '2001-01-20', 'male', '+375291234648', 'intermediate', '2023-07-22', '2023-11-22', 'closed'),
(5, 'Eleanor', 'Stone', '2000-04-06', 'female', '+375291234649', 'advanced', '2023-07-23', '2023-11-23', 'closed'),
(5, 'Theodore', 'Fleming', '1999-06-23', 'male', '+375291234650', 'expert', '2023-07-24', '2023-11-24', 'closed'),
(5, 'Alice', 'Hawkins', '2002-08-10', 'female', '+375291234651', 'master', '2023-07-25', '2023-11-25', 'closed'),
(5, 'Jasper', 'Walters', '2000-11-27', 'male', '+375291234652', 'beginner', '2023-07-26', '2023-11-26', 'closed'),
(5, 'Quinn', 'Cross', '2002-01-14', 'female', '+375291234653', 'intermediate', '2023-07-27', '2023-11-27', 'closed'),
(5, 'Matilda', 'Carroll', '2000-03-03', 'female', '+375291234654', 'advanced', '2023-07-28', '2023-11-28', 'closed'),
(5, 'Xavier', 'Whitney', '1999-05-20', 'male', '+375291234655', 'expert', '2023-07-29', '2023-11-29', 'closed'),
(5, 'Isla', 'Fuller', '2002-07-07', 'female', '+375291234656', 'master', '2023-07-30', '2023-11-30', 'closed'),
(5, 'Leo', 'Gibson', '2000-09-24', 'male', '+375291234657', 'beginner', '2023-08-01', '2023-11-01', 'closed'),
(5, 'Nova', 'Banks', '2001-11-11', 'female', '+375291234658', 'intermediate', '2023-08-02', '2023-11-02', 'closed'),
(5, 'Gavin', 'Cameron', '2000-01-28', 'male', '+375291234659', 'advanced', '2023-08-03', '2023-11-03', 'closed'),
(5, 'Aria', 'Gill', '2002-03-17', 'female', '+375291234660', 'expert', '2023-08-04', '2023-11-04', 'closed'),
(5, 'Jace', 'Shaw', '2000-05-04', 'male', '+375291234661', 'master', '2023-08-05', '2023-11-05', 'closed'),
(5, 'Aubrey', 'Patrick', '2001-06-21', 'female', '+375291234662', 'beginner', '2023-08-06', '2023-11-06', 'closed'),
(5, 'Peyton', 'Boyd', '2000-08-08', 'male', '+375291234663', 'intermediate', '2023-08-07', '2023-11-07', 'closed'),
(5, 'Zara', 'Keller', '1999-10-25', 'female', '+375291234664', 'advanced', '2023-08-08', '2023-11-08', 'closed'),
(5, 'Kingston', 'Cunningham', '2002-12-12', 'male', '+375291234665', 'expert', '2023-08-09', '2023-11-09', 'closed'),
(5, 'Athena', 'Pearson', '2000-02-29', 'female', '+375291234666', 'master', '2023-08-10', '2023-11-10', 'closed'),
(5, 'Emerson', 'Hunter', '2001-04-17', 'male', '+375291234667', 'beginner', '2023-08-11', '2023-11-11', 'closed');

DROP TABLE IF EXISTS student_schedule;
CREATE TABLE student_schedule (
	class_id TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    employee_id TINYINT UNSIGNED,
    group_id TINYINT UNSIGNED,
    class_name VARCHAR(40),
    class_type ENUM('lecture', 'jumping', 'gym', 'outdoor-practice', 'indoor-practice'),
    class_date DATE,
    class_start TIME,
    class_end TIME,
    address_id TINYINT UNSIGNED,
    CONSTRAINT employee_schedule FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT group_schedule FOREIGN KEY (group_id) REFERENCES student_groups(group_id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT address_schedule FOREIGN KEY (address_id) REFERENCES addresses(address_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO student_schedule
(employee_id, group_id, class_name, class_type, class_date, class_start, class_end, address_id)
VALUES
(2, 5, 'Introduction to parashuting', 'lecture', '2024-07-01', '14:30:00', '15:50:00', 1),
(4, 5, 'Theory of jumping with an instructor', 'lecture', '2024-07-01', '16:00:00', '17:20:00', 1),
(5, 5, 'Practice of jumping with an instructor', 'indoor-practice', '2024-07-02', '14:30:00', '15:50:00', 2),
(2, 5, 'Practice of jumping with an instructor', 'indoor-practice', '2024-07-05', '16:00:00', '17:20:00', 2),
(1, 5, 'Jumping with instructor', 'jumping', '2024-07-06', '12:35:00', '14:20:00', 5),
(1, 5, 'Jumping with instructor', 'jumping', '2024-07-07', '12:35:00', '14:20:00', 5);

DROP TABLE IF EXISTS competitions;
CREATE TABLE competitions (
	competition_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	address_id TINYINT UNSIGNED,
    competition_name VARCHAR(30),
    competition_date DATE,
    competition_start TIME,
    CONSTRAINT address_competition FOREIGN KEY (address_id) REFERENCES addresses(address_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO competitions
(address_id, competition_name, competition_date, competition_start)
VALUES
(3, 'Sky Soar Challenge', '2024-06-15', '09:00'),
(4, 'Airborne Adrenaline Cup', '2023-07-11', '11:00'),
(3, 'High-Flyer Showdown', '2023-08-20', '12:00'),
(4, 'Aerial Mastery Tournament', '2023-09-13', '11:00'),
(4, 'Cloud Nine Competition', '2023-06-02', '13:00');

DROP TABLE IF EXISTS competition_results;
CREATE TABLE competition_results (
	result_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	competition_id INT UNSiGNED,
    student_id INT UNSIGNED,
    student_place ENUM ('1', '2', '3'),
    CONSTRAINT competition_result FOREIGN KEY (competition_id) REFERENCES competitions(competition_id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT student_result FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO competition_results
(competition_id, student_id, student_place)
VALUES
(1, 6, '1'),
(1, 8, '2'),
(1, 10, '3'),
(2, 11, '1'),
(2, 6, '2'),
(2, 8, '3'),
(3, 6, '1'),
(3, 16, '2'),
(3, 10, '3'),
(4, 22, '1'),
(4, 18, '2'),
(4, 6, '3'),
(5, 31, '1'),
(5, 25, '2'),
(5, 28, '3');

DROP TABLE IF EXISTS certificates;
CREATE TABLE certificates(
	certificate_id INT UNSIGNED AUTO_INCREMENT PRiMARY KEY,
    date_of_issue DATE,
    certificate_status ENUM('valid', 'expired', 'revoked', 'pending verification', 'voided'),
    CONSTRAINT student_certificate FOREIGN KEY (certificate_id) REFERENCES  students(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO certificates
(certificate_id, date_of_issue, certificate_status)
VALUES
(1, '2023-12-01', 'valid'),
(2, '2023-12-02', 'valid'),
(3, '2023-12-03', 'valid'),
(4, '2023-12-04', 'valid'),
(5, '2023-12-05', 'valid'),
(6, '2023-12-06', 'valid'),
(7, '2023-12-07', 'valid'),
(8, '2023-12-08', 'valid'),
(9, '2023-12-09', 'valid'),
(10, '2023-12-10', 'valid'),
(11, '2023-12-11', 'valid'),
(12, '2023-12-12', 'valid'),
(13, '2023-12-13', 'valid'),
(14, '2023-12-14', 'valid'),
(15, '2023-12-15', 'valid'),
(16, '2023-12-16', 'valid'),
(17, '2023-12-17', 'valid'),
(18, '2023-12-18', 'valid'),
(19, '2023-12-19', 'valid'),
(20, '2023-12-20', 'valid'),
(21, '2023-12-21', 'valid'),
(22, '2023-12-22', 'valid'),
(23, '2023-12-23', 'valid'),
(24, '2023-12-24', 'valid'),
(25, '2023-12-25', 'valid'),
(26, '2023-12-26', 'valid'),
(27, '2023-12-27', 'valid'),
(28, '2023-12-28', 'valid'),
(29, '2023-12-29', 'valid'),
(30, '2023-12-30', 'valid'),
(31, '2023-12-31', 'valid'),
(32, '2023-12-01', 'expired'),
(33, '2023-12-02', 'valid'),
(34, '2023-12-03', 'valid'),
(35, '2023-12-04', 'valid'),
(36, '2023-12-05', 'valid'),
(37, '2023-12-06', 'valid'),
(38, '2023-12-07', 'valid'),
(39, '2023-12-08', 'valid'),
(40, '2023-12-09', 'valid'),
(41, '2023-12-10', 'valid'),
(42, '2023-12-11', 'valid'),
(43, '2023-12-12', 'valid'),
(44, '2023-12-13', 'valid'),
(45, '2023-12-14', 'valid'),
(46, '2023-12-15', 'valid'),
(47, '2023-12-16', 'valid'),
(48, '2023-12-17', 'valid'),
(49, '2023-12-18', 'valid'),
(50, '2023-12-19', 'valid'),
(51, '2023-12-20', 'valid'),
(52, '2023-12-21', 'valid'),
(53, '2023-12-22', 'valid'),
(54, '2023-12-23', 'valid'),
(55, '2023-12-24', 'valid'),
(56, '2023-12-25', 'valid'),
(57, '2023-12-26', 'valid'),
(58, '2023-12-27', 'valid'),
(59, '2023-12-28', 'valid'),
(60, '2023-12-29', 'valid'),
(61, '2023-12-30', 'valid'),
(62, '2023-12-31', 'expired'),
(63, '2023-12-01', 'valid'),
(64, '2023-12-02', 'valid'),
(65, '2023-12-03', 'valid'),
(66, '2023-12-04', 'valid'),
(67, '2023-12-05', 'valid'),
(68, '2023-12-06', 'valid'),
(69, '2023-12-07', 'valid'),
(70, '2023-12-08', 'valid'),
(71, '2023-12-09', 'valid'),
(72, '2023-12-10', 'valid'),
(73, '2023-12-11', 'valid'),
(74, '2023-12-12', 'valid'),
(75, '2023-12-13', 'valid'),
(76, '2023-12-14', 'valid'),
(77, '2023-12-15', 'valid'),
(78, '2023-12-16', 'valid'),
(79, '2023-12-17', 'valid'),
(80, '2023-12-18', 'valid'),
(81, '2023-12-19', 'valid'),
(82, '2023-12-20', 'valid'),
(83, '2023-12-21', 'valid'),
(84, '2023-12-22', 'valid'),
(85, '2023-12-23', 'valid'),
(86, '2023-12-24', 'valid'),
(87, '2023-12-25', 'valid'),
(88, '2023-12-26', 'valid'),
(89, '2023-12-27', 'valid'),
(90, '2023-12-28', 'expired'),
(91, '2023-12-29', 'valid'),
(92, '2023-12-30', 'valid'),
(93, '2023-12-31', 'valid'),
(94, '2023-12-01', 'valid'),
(95, '2023-12-02', 'valid'),
(96, '2023-12-03', 'valid'),
(97, '2023-12-04', 'revoked'),
(98, '2023-12-05', 'valid'),
(99, '2023-12-06', 'valid'),
(100, '2023-12-07', 'valid'),
(101, '2023-12-08', 'valid');

DROP TABLE IF EXISTS profiles;
CREATE TABLE profiles(
	user_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(20),
    user_surname VARCHAR(20),
    user_cash DECIMAL UNSIGNED
);

INSERT INTO profiles
(user_name, user_surname, user_cash)
VALUES
('John', 'Smith', 50000),
('Emma', 'Johnson', 700),
('Michael', 'Williams', 450),
('Olivia', 'Brown', 600),
('James', 'Jones', 550),
('Sophia', 'Miller', 800),
('William', 'Davis', 400),
('Ava', 'Garcia', 750),
('Alexander', 'Rodriguez', 300),
('Charlotte', 'Martinez', 850),
('Daniel', 'Hernandez', 650),
('Mia', 'Lopez', 480),
('Ethan', 'Gonzalez', 720),
('Isabella', 'Wilson', 520),
('Liam', 'Anderson', 680),
('Amelia', 'Thomas', 420),
('Benjamin', 'Taylor', 780),
('Emily', 'Moore', 380),
('Henry', 'Jackson', 560),
('Harper', 'White', 730);

DROP TABLE IF EXISTS equipment_rent;
CREATE TABLE equipment_rent(
	rent_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNSIGNED,
    equipment_id TINYINT UNSIGNED,
    equipment_amount TINYINT UNSIGNED,
	rent_start DATE,
    rent_end DATE,
    rent_payment DECIMAL,
    CONSTRAINT profile_rent FOREIGN KEY (user_id) REFERENCES profiles(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT equipment_rent FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO equipment_rent
(user_id, equipment_id, equipment_amount, rent_start, rent_end, rent_payment)
VALUES
(4, 13, 5, "2024-03-11", "2024-03-21", 100),
(4, 23, 6, "2024-02-08", "2024-02-18", 200),
(1, 13, 4, "2024-01-16", "2024-03-26", 75),
(7, 23, 2, "2024-02-22", "2024-03-01", 25),
(15, 13, 1, "2024-03-13", "2024-03-23", 10),
(18, 23, 3, "2024-02-01", "2024-02-11", 30),
(15, 13, 3, "2024-03-06", "2024-03-16", 45),
(7, 23, 4, "2024-03-05", "2024-02-14", 80),
(15, 13, 5, "2024-02-25", "2024-03-04", 100),
(7, 23, 1, "2024-02-19", "2024-02-29", 15),
(18, 13, 2, "2024-02-03", "2024-03-13", 30),
(15, 23, 3, "2024-02-14", "2024-02-24", 60);

DROP TABLE IF exists employees_and_courses;
CREATE TABLE employees_and_courses(
	employee_id TINYINT UNSIGNED,
    course_id TINYINT UNSIGNED,
    PRIMARY KEY (employee_id, course_id),
    CONSTRAINT employee_employee FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT course_course FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO employees_and_courses
(employee_id, course_id)
VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(3, 6),
(4, 7),
(4, 8),
(5, 1),
(5, 2),
(6, 3),
(6, 4),
(7, 5),
(7, 6),
(8, 7),
(8, 8),
(9, 1),
(9, 2),
(10, 3),
(10, 4);

SELECT courses.course_id, course_name, course_hours, course_jumps FROM
(SELECT course_id FROM employees_and_courses WHERE employee_id = 5) as employee_and_his_courses
INNER JOIN courses
ON employee_and_his_courses.course_id = courses.course_id;

SELECT * FROM equipment_rent;

SELECT * FROM profiles;

SELECT * FROM employees;

SELECT * FROM profiles
ORDER BY user_id DESC
LIMIT 5;

DROP TABLE IF EXISTS parents;
CREATE TABLE parents(
	parent_id INT UNSIGNED PRIMARY KEY,
    parent_name VARCHAR(20)
);

DROP TABLE IF EXISTS children;
CREATE TABLE children(
	child_id INT UNSIGNED PRiMARY KEY,
    child_name VARCHAR(20),
    CONSTRAINT parent_child FOREIGN KEY (child_id) REFERENCES parents(parent_id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS deceases;
CREATE TABLE deceases(
	decease_id INT UNSIGNED PRIMARY KEY,
    parent_id INT UNSIGNED,
    decease_name VARCHAR(20),
    CONSTRAINT parent_decease FOREIGN KEY (parent_id) REFERENCES parents(parent_id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS doctors;
CREATE TABLE doctors(
	doctor_id INT PRIMARY KEY,
    doctor_name VARCHAR(20)
);

DROP TABLE IF EXISTS cards;
CREATE TABLE cards (
	doctor_id INT,
    parent_id INT UNSIGNED,
    PRIMARY KEY (doctor_id, parent_id),
    CONSTRAINT doctor_card FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE, 
    CONSTRAINT parent_card FOREIGN KEY (parent_id) REFERENCES parents(parent_id) ON DELETE CASCADE
);

use skydiving;

select * from parents;