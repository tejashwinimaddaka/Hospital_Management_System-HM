from dao.i_hospital_service import IHospitalService
from entity.appointment import Appointment
from util.db_connection import DBConnection
from exception.PatientNumberNotFound import PatientNumberNotFoundException
from  tabulate import tabulate

class HospitalServiceImpl(IHospitalService):

    def getAppointmentById(self, appointmentId):
        conn = DBConnection.getConnection()
        cursor=conn.cursor()
        try:
            query = "select * from Appointment where appointmentId = ?"
            cursor.execute(query, (appointmentId,))
            appointment = cursor.fetchone()

            if appointment:
                appointment_details=[
                    ['Appointment ID',appointment[0]],
                    ["Patient ID",appointment[1]],
                    ["Doctor ID",appointment[2]],
                    ["Appointment Date",appointment[3]],
                    ["Description",appointment[4]],
                ]
                print("Appointment Details")
                print(tabulate(appointment_details,tablefmt="grid"))

            else:
                print("Appointment Not Found")
        except Exception as e:
            print(f"Error in fetching appointment: {e}")
            #return None
        finally:
            cursor.close()


    def getAppointmentsForPatient(self, patientId):
        conn = DBConnection.getConnection()
        cursor=conn.cursor()
        try:
            patient_check_query = "select count(*) from Patient where patientId = ?"
            cursor.execute(patient_check_query, (patientId,))
            patient_exists = cursor.fetchone()[0]

            if not patient_exists:
                raise PatientNumberNotFoundException(patientId)
            query = "select * from Appointment where patientId = ?"
            cursor.execute(query,(patientId,))
            appointments = []
            for row in cursor.fetchall():
                appointments.append(Appointment(
                    appointmentId=row[0],
                    patientId=row[1],
                    doctorId=row[2],
                    appointmentDate=row[3],
                    description=row[4]
                ))

            return appointments
        finally:
            cursor.close()
    
    def getAppointmentsForDoctor(self, doctorId):
        conn = DBConnection.getConnection()
        cursor = conn.cursor()
        try:
            doctor_check_query = "select count(*) from Doctor where doctorId = ?"
            cursor.execute(doctor_check_query, (doctorId,))
            doctor_exists = cursor.fetchone()[0]

            if not doctor_exists:
                return None
            query = "select * from Appointment where doctorId = ?"
            cursor.execute(query, (doctorId,))
            doctors_appointments = []
            for result in cursor.fetchall():
                doctors_appointments.append(Appointment(
                    appointmentId=result[0],
                    patientId=result[1],
                    doctorId=result[2],
                    appointmentDate=result[3],
                    description=result[4]
                ))
            return doctors_appointments
        finally:
            cursor.close()
    

    def scheduleAppointment(self, appointment,appointment_id):
        conn = DBConnection.getConnection()
        cursor = conn.cursor()
        try:
            check_query = "select count(*) from Appointment where appointmentId = ?"
            cursor.execute(check_query, (appointment_id,))
            exists = cursor.fetchone()[0] > 0

            if exists:
                print("The appointment is full.")
                return  
            query = """insert into Appointment(appointmentId, patientId, doctorId, appointmentDate, description)
                   values (?, ?, ?, ?, ?)"""
            cursor.execute(query, (appointment.get_appointmentId(), appointment.get_patientId(), appointment.get_doctorId(), 
                                   appointment.get_appointmentDate(), appointment.get_description()))
            conn.commit()
            print('Appointment scheduled')
            return True
        
        except Exception as e:
            print(f"Error scheduling appointment: {e}")
        finally:
            cursor.close()


    def updateAppointment(self, appointment):
        conn = DBConnection.getConnection()
        cursor = conn.cursor()
        try:
            query = """update Appointment set patientId = ?, doctorId = ?, appointmentDate = ?, description = ?
                   where appointmentId = ?"""
            cursor.execute(query, (appointment.get_patientId(), appointment.get_doctorId(), appointment.get_appointmentDate(), 
                                   appointment.get_description(), appointment.appointmentId))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error in updating an appointment: {e}")
            return False
        finally:
            cursor.close()


    def cancelAppointment(self, appointmentId):
        conn = DBConnection.getConnection()
        cursor = conn.cursor()
        try:
            cursor.execute("select count(*) from Appointment where appointmentId=?",(appointmentId,))
            count = cursor.fetchone()[0]
            if count==0:
                print("Appointment Not Found")
                return False
            query = "delete from Appointment where appointmentId = ?"
            cursor.execute(query, appointmentId)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error in cancelling an appointment: {e}")
            return False  
        finally:
            cursor.close()
