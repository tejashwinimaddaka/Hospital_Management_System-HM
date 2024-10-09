import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)
from dao.HospitalServiceImpl import HospitalServiceImpl
from entity.appointment import Appointment
from exception.PatientNumberNotFound import PatientNumberNotFoundException
from  tabulate import tabulate

class MainModule:
    def __init__(self):
        self.hospital_service = HospitalServiceImpl()

    def proceed(self):
        while True:
            #self.services()
            data=[
                ["1", "Get Appointment by ID"],
                ["2", "Get Appointments for Patient"],
                ["3", "Get Appointments for Doctor"],
                ["4", "Schedule an Appointment"],
                ["5", "Update an Appointment"],
                ["6", "Cancel an Appointment"],
                ["7", "Exit"]
            ]
            headers=["Option", "Service"]
            print("------Hospital Management System------")
            print(tabulate(data,headers, tablefmt="grid"))
            choice = input("Enter the option from 1 to 7: ")
            if choice == '1':
                self.getAppointmentById()
            elif choice == '2':
                self.getAppointmentsForPatient()
            elif choice == '3':
                self.getAppointmentsForDoctor()
            elif choice == '4':
                self.scheduleAppointment()
            elif choice == '5':
                self.updateAppointment()
            elif choice == '6':
                self.cancelAppointment()
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again...")
    
    def getAppointmentById(self):
        appointment_id = input("Enter appointment ID: ")
        try:
            int_appointment_id=int(appointment_id)
            appointment = self.hospital_service.getAppointmentById(int_appointment_id)
            print(appointment)
        except ValueError as ve:
            print(f"Input type error: Please enter a valid integer for the appointment ID.{ve}")
        except Exception as e:
            print(e)
    
    def getAppointmentsForPatient(self):
        patient_id = input("Enter patient ID: ")
        try:
            appointments = self.hospital_service.getAppointmentsForPatient(patient_id)

            if appointments:
                print(f"Appointments for Patient: {patient_id}")
                rows = [[appointment.appointmentId, appointment.doctorId, appointment.appointmentDate,appointment.description]
                              for appointment in appointments]
                headers = ["Appointment Id", "Doctor Id","Appointment Date", "Appointment Description"]
                print(tabulate(rows, headers=headers,tablefmt="grid"))
            else:
                print(f'Patient with ID {patient_id} have no appointment')
        except PatientNumberNotFoundException as e:
            print("Exception:",e)
    
    def getAppointmentsForDoctor(self):
        doctor_id = input("Enter doctor ID: ")
        try:
            appointments = self.hospital_service.getAppointmentsForDoctor(doctor_id)
            if appointments is None:
                print(f"The doctor ID {doctor_id} does not exist")
            elif appointments:
                print(f"Appointments for Doctor: {doctor_id}")
                table_data = [[appointment.appointmentId, appointment.patientId, appointment.appointmentDate,appointment.description]
                                  for appointment in appointments]
                headers=["Appointment Id", "Patient Id", "Appointment Date", "Appointment Description"]
                print(tabulate(table_data, headers=headers,tablefmt="grid"))
            
            else:
                print(f'Doctor with ID {doctor_id} have no appointments')
        except Exception as e:
            print("Error in fetching details of doctors appointment", e)
    
    def scheduleAppointment(self):
        appointment_id=int(input('Appointment ID:'))
        patient_id = input("Enter patient ID: ")
        doctor_id = input("Enter doctor ID: ")
        appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
        description = input("Enter appointment description: ")
        
        appointment = Appointment(
            appointmentId = appointment_id,
            patientId = patient_id,
            doctorId = doctor_id,
            appointmentDate = appointment_date,
            description = description
        )
        
        success = self.hospital_service.scheduleAppointment(appointment,appointment_id)
        if success:
            print()
        else:
            print("Failed to schedule appointment.")
    
    def updateAppointment(self):
        appointment_id = input("Enter appointment ID: ")
        new_patient_id = input("Enter new patient ID: ")
        new_doctor_id = input("Enter new doctor ID: ")
        new_appointment_date = input("Enter new appointment date (YYYY-MM-DD): ")
        new_description = input("Enter new appointment description: ")
        
        appointment = Appointment(
            appointmentId = appointment_id,
            patientId = new_patient_id,
            doctorId = new_doctor_id,
            appointmentDate = new_appointment_date,
            description = new_description
        )
        
        update = self.hospital_service.updateAppointment(appointment)
        if update:
            print("Appointment updated successfully.")
        else:
            print("Failed to update appointment.")
    
    def cancelAppointment(self):
        appointment_id = int(input("Enter appointment ID to cancel: "))
        cancel = self.hospital_service.cancelAppointment(appointment_id)
        if cancel:
            print("Appointment cancelled successfully.")
        else:
                print("Failed to cancel appointment.")
       


if __name__ == "__main__":
    main_module = MainModule()
    main_module.proceed()
