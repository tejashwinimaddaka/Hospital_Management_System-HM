create DATABASE Hospital_Management;
use Hospital_Management;
create table Patient(
    patientId varchar(5) PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    dateOfBirth DATE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    contactNumber VARCHAR(15) NOT NULL,
    address VARCHAR(255) NOT NULL);

create table Doctor (
    doctorId varchar(5) PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    specialization VARCHAR(50) NOT NULL,
    contactNumber VARCHAR(15) NOT NULL);

create table Appointment(
     appointmentId int primary key, 
      patientId varchar(5) not null,
      doctorId varchar(5) not null,
      appointmentDate DATETIME not null, 
       description varchar(50),
      FOREIGN KEY(patientId) REferences Patient(patientId),
      FOREIGN KEY (doctorId) References Doctor(DoctorId)
);

insert into Patient(patientId, firstName,lastName,dateOfBirth,gender,contactNumber,address) 
values
('p1', 'Anne','John', '2001-10-12','Female','9852654753','14/480,Church street,Miami'),
('p2', 'Emma','Thomas','1998-01-08', 'Female','8695756984','1C-10, Lakeview,Portland'),
('p3', 'Noah','Olivia','2000-09-04', 'Male','789654357','12-B,Grifender street,New York'),
('p4', 'David','Son','1999-02-05', 'Male','7895651423','63/1,Johnson street,San Jose'),
('p5', 'Martin','Rich','2002-04-06', 'Male','9563285412','56/9,Wainut,Tucson'),
('p6', 'Blue','Harris','1997-10-03', 'Male','6859352946','35-D,Main street,Fort Worth'),
('p7', 'Kevin','Jose','2003-07-12', 'Male','8534976581','89/7,Cedar,Honolulu'),
('p8', 'Pat','Carol','2001-04-09', 'Male','7689572612','475,Maple,Omaha'),
('p9', 'Amy','Mathew','2004-10-12', 'Female','7654892642','165/1B,Kingston,Las Vegas'),
('p10', 'Laura','James','1998-03-05', 'Female','9556411791','164,Second street,Phoenix');

insert into Doctor(doctorId,firstName,lastName,specialization,contactNumber)
values
('d1', 'Dr. Amanda','Stone', 'Cardiologist', '9123456780'),
('d2', 'Dr. Michael','Rivera', 'Neurologist', '6329087654'),
('d3', 'Dr. Olivia ','Henry', 'Surgeon', '98766546543'),
('d4', 'Dr. David','Wong', 'Pediatrician', '8769806547'),
('d5', 'Dr. Emily','Johnson', 'Dermatologist', '9876543210'),
('d6', 'Dr. Benjamin','Carter', 'Oncologist', '8907654762'),
('d7', 'Dr. Lily ','Martinez', 'Dermatologist', '9764789432'),
('d8', 'Dr. William','Lee', 'Rhumetologist', '9876867869'),
('d9', 'Dr. Isabella','Thompson', 'Gastroenterologist', '8769806598'),
('d10', 'Dr. Ethan','Brooks', 'Endocrinologist', '7869087651');


insert into Appointment(appointmentId,patientId,doctorId,appointmentDate,description)
values
(1,'p10','d7','2024-10-28','Hair loss'),
(2,'p8','d9','2024-11-02 ','Stomach Ache'),
(3,'p1','d10','2024-10-17','diabetes'),
(4,'p3','d3','2024-10-11','Surgery'),
(5,'p4','d7','2024-10-29','Hair loss'),
(6,'p5','d2','2024-11-03','Migrane'),
(7,'p6','d1','2024-11-01','Hyper Tension'),
(8,'p9','d5','2024-10-30','Hair loss'),
(9,'p1','d2','2024-10-12','Allergy'),
(10,'p7','d8','2024-10-13','Arthritis');

select * from Patient;
select * from Doctor;
select * from Appointment;

