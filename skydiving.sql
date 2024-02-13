DROP DATABASE IF EXISTS skydiving;
CREATE DATABASE skydiving;
USE skydiving;

DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
	employee_id TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	employee_name VARCHAR(20),
    employee_surname VARCHAR(20),
    employee_position ENUM('skydiving-instructor', 'safety-instructor', 'trainer', 'manager', 'mechanic', 'pilot'),
    contact_info VARCHAR(13)
);

INSERT INTO employees (employee_name, employee_surname, employee_position, contact_info) VALUES
('Ivan', 'Petrov', 'skydiving-instructor', '+3754567890'),
('Maria', 'Ivanova', 'skydiving-instructor', '+3757654321'),
('Alexey', 'Smirnov', 'safety-instructor', '+3757902468'),
('Elena', 'Kozlova', 'safety-instructor', '+3758013579'),
('Sergey', 'Nikolaev', 'trainer', '+3752581470'),
('Olga', 'Stepanova', 'trainer', '+3752583690'),
('Dmitriy', 'Kovalev', 'manager', '+3753691470'),
('Anna', 'Semenova', 'manager', '+3757538246'),
('Pavel', 'Morozov', 'mechanic', '+3759518246'),
('Natalia', 'Fedorova', 'mechanic', '+3756159370'),
('Alexander', 'Kuznetsov', 'pilot', '+3759370824'),
('Lyudmila', 'Ivanova', 'pilot', '+3750824615');

CREATE TABLE contracts (
	contract_id TINYINT UNSIGNED AUTO_INCREMENT,
	contract_start_date DATE,
    contract_end_date DATE,
    employee_salary DECIMAL(6, 2),
    constraint employee_contract foreign key (contract_id) references employees(employee_id)
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

DROP TABLE IF EXISTS cources;
CREATE TABLE cources (
	cource_id TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	cource_name VARCHAR(30),
    cource_hours TINYINT UNSIGNED,
    cource_jumps TINYINT UNSIGNED
);

INSERT INTO cources
(cource_name, cource_hours, cource_jumps)
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

DROP TABLE IF EXISTS address;
CREATE TABLE address (
	address_id TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	address_building_name VARCHAR(30),
    address_name VARCHAR(50),
    geographical_coords VARCHAR(30)
);

INSERT INTO address 
(address_building_name, address_name, geographical_coords) 
VALUES
('Sunset Apartments', '123 Main Street, Sunset Blvd', '35.6895° N, 139.6917° E'),
('Greenwood Villas', '456 Elm Avenue, Greenwood', '40.7128° N, 74.0060° W'),
('Oceanview Towers', '789 Ocean Drive, Oceanview', '33.9416° N, 118.4085° W'),
('Maplewood Manor', '1010 Maple Lane, Maplewood', '51.5074° N, 0.1278° W'),
('Riverside Residences', '1313 River Road, Riverside', '34.0522° N, 118.2437° W'),
('Mountainview Estates', '1515 Hilltop Avenue, Mountainview', '37.3861° N, 122.0839° W');

DROP TABLE IF EXISTS students;
CREATE TABLE students (
	student_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	cource_id TINYINT UNSIGNED,
    student_first_name VARCHAR(20),
    student_second_name VARCHAR(20),
    student_birthday DATE,
    student_sex ENUM('female', 'male'),
    student_contact_info VARCHAR(13),
    student_level ENUM('beginner', 'intermediate', 'advanced', 'expert', 'master'),
    enrollment_date DATE,
    completion_date DATE,
    status ENUM ('active', 'closed', 'expelled'),
    constraint cource_student foreign key (cource_id) references cources(cource_id)
);

INSERT INTO students (cource_id, student_first_name, student_second_name, student_birthday, student_sex, student_contact_info, student_level, enrollment_date, completion_date, status) VALUES
(1, 'Alice', 'Smith', '2000-03-15', 'female', '+375291234567', 'beginner', '2023-05-01', '2023-11-01', 'closed'),
(2, 'Bob', 'Johnson', '2001-05-20', 'male', '+375291234568', 'intermediate', '2023-05-02', '2023-11-02', 'closed'),
(3, 'Charlie', 'Brown', '1999-09-10', 'male', '+375291234569', 'advanced', '2023-05-03', '2023-11-03', 'closed'),
(4, 'David', 'Wilson', '2002-02-25', 'male', '+375291234570', 'expert', '2023-05-04', '2023-11-04', 'closed'),
(5, 'Emma', 'Anderson', '2000-07-12', 'female', '+375291234571', 'master', '2023-05-05', '2023-11-05', 'closed'),
(6, 'Ethan', 'Martinez', '2001-11-30', 'male', '+375291234572', 'beginner', '2023-05-06', '2023-11-06', 'closed'),
(7, 'Olivia', 'Taylor', '2000-01-08', 'female', '+375291234573', 'intermediate', '2023-05-07', '2023-11-07', 'closed'),
(8, 'Michael', 'Thomas', '2002-04-18', 'male', '+375291234574', 'advanced', '2023-05-08', '2023-11-08', 'closed'),
(1, 'Sophia', 'Hernandez', '2001-06-22', 'female', '+375291234575', 'expert', '2023-05-09', '2023-11-09', 'closed'),
(1, 'William', 'Garcia', '2000-08-05', 'male', '+375291234576', 'master', '2023-05-10', '2023-11-10', 'closed'),
(1, 'Isabella', 'Young', '2001-10-14', 'female', '+375291234577', 'beginner', '2023-05-11', '2023-11-11', 'closed'),
(2, 'James', 'Lopez', '2000-12-28', 'male', '+375291234578', 'intermediate', '2023-05-12', '2023-11-12', 'closed'),
(3, 'Mia', 'Lewis', '1999-02-19', 'female', '+375291234579', 'advanced', '2023-05-13', '2023-11-13', 'closed'),
(4, 'Alexander', 'King', '2002-03-07', 'male', '+375291234580', 'expert', '2023-05-14', '2023-11-14', 'closed'),
(5, 'Charlotte', 'Scott', '2000-05-31', 'female', '+375291234581', 'master', '2023-05-15', '2023-11-15', 'closed'),
(6, 'Benjamin', 'Green', '2001-09-04', 'male', '+375291234582', 'beginner', '2023-05-16', '2023-11-16', 'closed'),
(7, 'Amelia', 'Adams', '1999-11-11', 'female', '+375291234583', 'intermediate', '2023-05-17', '2023-11-17', 'closed'),
(8, 'Daniel', 'Baker', '2002-01-26', 'male', '+375291234584', 'advanced', '2023-05-18', '2023-11-18', 'closed'),
(2, 'Evelyn', 'Rivera', '2000-04-01', 'female', '+375291234585', 'expert', '2023-05-19', '2023-11-19', 'closed'),
(2, 'Joseph', 'Campbell', '2001-07-07', 'male', '+375291234586', 'master', '2023-05-20', '2023-11-20', 'closed'),
(1, 'Harper', 'Mitchell', '2000-09-15', 'female', '+375291234587', 'beginner', '2023-05-21', '2023-11-21', 'closed'),
(2, 'Samuel', 'Perez', '1999-12-02', 'male', '+375291234588', 'intermediate', '2023-05-22', '2023-11-22', 'closed'),
(3, 'Avery', 'Roberts', '2002-02-11', 'female', '+375291234589', 'advanced', '2023-05-23', '2023-11-23', 'closed'),
(4, 'Logan', 'Turner', '2000-06-29', 'male', '+375291234590', 'expert', '2023-05-24', '2023-11-24', 'closed'),
(5, 'Ella', 'Cook', '2001-08-23', 'female', '+375291234591', 'master', '2023-05-25', '2023-11-25', 'closed'),
(6, 'Liam', 'Morris', '2000-11-01', 'male', '+375291234592', 'beginner', '2023-05-26', '2023-11-26', 'closed'),
(7, 'Grace', 'Ward', '2002-01-10', 'female', '+375291234593', 'intermediate', '2023-05-27', '2023-11-27', 'closed'),
(8, 'Lucas', 'Bailey', '1999-03-25', 'male', '+375291234594', 'advanced', '2023-05-28', '2023-11-28', 'closed'),
(3, 'Chloe', 'Cox', '2001-05-12', 'female', '+375291234595', 'expert', '2023-05-29', '2023-11-29', 'closed'),
(1, 'Mason', 'Howard', '2000-07-19', 'male', '+375291234596', 'master', '2023-05-30', '2023-11-30', 'closed'),
(1, 'Lily', 'Long', '2001-10-08', 'female', '+375291234597', 'beginner', '2023-06-01', '2023-11-01', 'closed'),
(2, 'Jack', 'Collins', '2000-12-17', 'male', '+375291234598', 'intermediate', '2023-06-02', '2023-11-02', 'closed'),
(3, 'Aria', 'Bell', '1999-02-03', 'female', '+375291234599', 'advanced', '2023-06-03', '2023-11-03', 'closed'),
(4, 'Jackson', 'Russell', '2002-04-22', 'male', '+375291234600', 'expert', '2023-06-04', '2023-11-04', 'closed'),
(5, 'Aurora', 'Coleman', '2000-06-08', 'female', '+375291234601', 'master', '2023-06-05', '2023-11-05', 'closed'),
(6, 'Ryan', 'Bell', '2001-08-27', 'male', '+375291234602', 'beginner', '2023-06-06', '2023-11-06', 'closed'),
(7, 'Scarlett', 'Foster', '2000-10-14', 'female', '+375291234603', 'intermediate', '2023-06-07', '2023-11-07', 'closed'),
(8, 'Elijah', 'Sanders', '1999-12-31', 'male', '+375291234604', 'advanced', '2023-06-08', '2023-11-08', 'closed'),
(4, 'Hannah', 'Bennett', '2002-02-16', 'female', '+375291234605', 'expert', '2023-06-09', '2023-11-09', 'closed'),
(5, 'Nathan', 'Barnes', '2000-04-03', 'male', '+375291234606', 'master', '2023-06-10', '2023-11-10', 'closed'),
(1, 'Zoe', 'Gray', '2001-06-20', 'female', '+375291234607', 'beginner', '2023-06-11', '2023-11-11', 'closed'),
(2, 'Carter', 'Woods', '2000-09-09', 'male', '+375291234608', 'intermediate', '2023-06-12', '2023-11-12', 'closed'),
(3, 'Madison', 'Knight', '1999-11-24', 'female', '+375291234609', 'advanced', '2023-06-13', '2023-11-13', 'closed'),
(4, 'Henry', 'Porter', '2002-01-11', 'male', '+375291234610', 'expert', '2023-06-14', '2023-11-14', 'closed'),
(5, 'Stella', 'Fisher', '2000-03-29', 'female', '+375291234611', 'master', '2023-06-15', '2023-11-15', 'closed'),
(6, 'Christopher', 'Griffin', '2001-05-16', 'male', '+375291234612', 'beginner', '2023-06-16', '2023-11-16', 'closed'),
(7, 'Leah', 'Hunter', '2000-07-05', 'female', '+375291234613', 'intermediate', '2023-06-17', '2023-11-17', 'closed'),
(8, 'Wyatt', 'Hicks', '1999-09-22', 'male', '+375291234614', 'advanced', '2023-06-18', '2023-11-18', 'closed'),
(6, 'Bella', 'Lawrence', '2002-11-07', 'female', '+375291234615', 'expert', '2023-06-19', '2023-11-19', 'closed'),
(7, 'Andrew', 'Simmons', '2000-01-24', 'male', '+375291234616', 'master', '2023-06-20', '2023-11-20', 'closed'),
(1, 'Nora', 'Harrison', '2001-04-01', 'female', '+375291234617', 'beginner', '2023-06-21', '2023-11-21', 'closed'),
(2, 'Gabriel', 'Reid', '2000-06-18', 'male', '+375291234618', 'intermediate', '2023-06-22', '2023-11-22', 'closed'),
(3, 'Aubrey', 'Murray', '1999-08-05', 'female', '+375291234619', 'advanced', '2023-06-23', '2023-11-23', 'closed'),
(4, 'Eli', 'Cole', '2002-10-22', 'male', '+375291234620', 'expert', '2023-06-24', '2023-11-24', 'closed'),
(5, 'Audrey', 'Stone', '2000-12-09', 'female', '+375291234621', 'master', '2023-06-25', '2023-11-25', 'closed'),
(6, 'Owen', 'Pierce', '2002-02-26', 'male', '+375291234622', 'beginner', '2023-06-26', '2023-11-26', 'closed'),
(7, 'Penelope', 'Ferguson', '2001-04-15', 'female', '+375291234623', 'intermediate', '2023-06-27', '2023-11-27', 'closed'),
(8, 'Lincoln', 'Snyder', '2000-06-02', 'male', '+375291234624', 'advanced', '2023-06-28', '2023-11-28', 'closed'),
(8, 'Clara', 'Howard', '1999-07-19', 'female', '+375291234625', 'expert', '2023-06-29', '2023-11-29', 'closed'),
(1, 'Julian', 'Chambers', '2002-09-05', 'male', '+375291234626', 'master', '2023-06-30', '2023-11-30', 'closed'),
(1, 'Riley', 'Stephens', '2000-11-25', 'female', '+375291234627', 'beginner', '2023-07-01', '2023-11-01', 'closed'),
(2, 'Violet', 'Watson', '2002-01-12', 'female', '+375291234628', 'intermediate', '2023-07-02', '2023-11-02', 'closed'),
(3, 'Tristan', 'Dunn', '2000-03-30', 'male', '+375291234629', 'advanced', '2023-07-03', '2023-11-03', 'closed'),
(4, 'Hazel', 'Ford', '2001-05-17', 'female', '+375291234630', 'expert', '2023-07-04', '2023-11-04', 'closed'),
(5, 'Everett', 'Mcdonald', '1999-07-04', 'male', '+375291234631', 'master', '2023-07-05', '2023-11-05', 'closed'),
(6, 'Luna', 'Grant', '2002-08-21', 'female', '+375291234632', 'beginner', '2023-07-06', '2023-11-06', 'closed'),
(7, 'Emmett', 'Fowler', '2000-10-08', 'male', '+375291234633', 'intermediate', '2023-07-07', '2023-11-07', 'closed'),
(8, 'Adeline', 'Wheeler', '1999-12-25', 'female', '+375291234634', 'advanced', '2023-07-08', '2023-11-08', 'closed'),
(2, 'Hudson', 'Stanley', '2002-02-10', 'male', '+375291234635', 'expert', '2023-07-09', '2023-11-09', 'closed'),
(3, 'Emilia', 'Gordon', '2000-04-27', 'female', '+375291234636', 'master', '2023-07-10', '2023-11-10', 'closed'),
(1, 'Finn', 'Jordan', '2001-06-14', 'male', '+375291234637', 'beginner', '2023-07-11', '2023-11-11', 'closed'),
(2, 'Ivy', 'Barrett', '2000-08-01', 'female', '+375291234638', 'intermediate', '2023-07-12', '2023-11-12', 'closed'),
(3, 'Beckett', 'Newton', '1999-09-18', 'male', '+375291234639', 'advanced', '2023-07-13', '2023-11-13', 'closed'),
(4, 'Aaliyah', 'Holt', '2002-11-05', 'female', '+375291234640', 'expert', '2023-07-14', '2023-11-14', 'closed'),
(5, 'Graham', 'Owen', '2000-01-22', 'male', '+375291234641', 'master', '2023-07-15', '2023-11-15', 'closed'),
(6, 'Reese', 'Rice', '2001-03-11', 'female', '+375291234642', 'beginner', '2023-07-16', '2023-11-16', 'closed'),
(7, 'Lila', 'Church', '2000-05-28', 'female', '+375291234643', 'intermediate', '2023-07-17', '2023-11-17', 'closed'),
(8, 'Kai', 'Saunders', '1999-07-15', 'male', '+375291234644', 'advanced', '2023-07-18', '2023-11-18', 'closed'),
(4, 'Elise', 'Tate', '2002-09-01', 'female', '+375291234645', 'expert', '2023-07-19', '2023-11-19', 'closed'),
(5, 'Zachary', 'Fitzgerald', '2000-10-18', 'male', '+375291234646', 'master', '2023-07-20', '2023-11-20', 'closed'),
(1, 'Lucy', 'Rogers', '2002-12-05', 'female', '+375291234647', 'beginner', '2023-07-21', '2023-11-21', 'closed'),
(2, 'Arthur', 'Morgan', '2001-01-20', 'male', '+375291234648', 'intermediate', '2023-07-22', '2023-11-22', 'closed'),
(3, 'Eleanor', 'Stone', '2000-04-06', 'female', '+375291234649', 'advanced', '2023-07-23', '2023-11-23', 'closed'),
(4, 'Theodore', 'Fleming', '1999-06-23', 'male', '+375291234650', 'expert', '2023-07-24', '2023-11-24', 'closed'),
(5, 'Alice', 'Hawkins', '2002-08-10', 'female', '+375291234651', 'master', '2023-07-25', '2023-11-25', 'closed'),
(6, 'Jasper', 'Walters', '2000-11-27', 'male', '+375291234652', 'beginner', '2023-07-26', '2023-11-26', 'closed'),
(7, 'Quinn', 'Cross', '2002-01-14', 'female', '+375291234653', 'intermediate', '2023-07-27', '2023-11-27', 'closed'),
(8, 'Matilda', 'Carroll', '2000-03-03', 'female', '+375291234654', 'advanced', '2023-07-28', '2023-11-28', 'closed'),
(5, 'Xavier', 'Whitney', '1999-05-20', 'male', '+375291234655', 'expert', '2023-07-29', '2023-11-29', 'closed'),
(6, 'Isla', 'Fuller', '2002-07-07', 'female', '+375291234656', 'master', '2023-07-30', '2023-11-30', 'closed'),
(1, 'Leo', 'Gibson', '2000-09-24', 'male', '+375291234657', 'beginner', '2023-08-01', '2023-11-01', 'closed'),
(2, 'Nova', 'Banks', '2001-11-11', 'female', '+375291234658', 'intermediate', '2023-08-02', '2023-11-02', 'closed'),
(3, 'Gavin', 'Cameron', '2000-01-28', 'male', '+375291234659', 'advanced', '2023-08-03', '2023-11-03', 'closed'),
(4, 'Aria', 'Gill', '2002-03-17', 'female', '+375291234660', 'expert', '2023-08-04', '2023-11-04', 'closed'),
(5, 'Jace', 'Shaw', '2000-05-04', 'male', '+375291234661', 'master', '2023-08-05', '2023-11-05', 'closed'),
(6, 'Aubrey', 'Patrick', '2001-06-21', 'female', '+375291234662', 'beginner', '2023-08-06', '2023-11-06', 'closed'),
(7, 'Peyton', 'Boyd', '2000-08-08', 'male', '+375291234663', 'intermediate', '2023-08-07', '2023-11-07', 'closed'),
(8, 'Zara', 'Keller', '1999-10-25', 'female', '+375291234664', 'advanced', '2023-08-08', '2023-11-08', 'closed'),
(7, 'Kingston', 'Cunningham', '2002-12-12', 'male', '+375291234665', 'expert', '2023-08-09', '2023-11-09', 'closed'),
(1, 'Athena', 'Pearson', '2000-02-29', 'female', '+375291234666', 'master', '2023-08-10', '2023-11-10', 'closed'),
(2, 'Emerson', 'Hunter', '2001-04-17', 'male', '+375291234667', 'beginner', '2023-08-11', '2023-11-11', 'closed');
