# hospital.py
from patient import Patient
from doctor import Doctor

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []

    def admit_patient(self, patient):
        self.patients.append(patient)

    def assign_doctor(self, doctor, patient):
        doctor.assign_patient(patient)
        patient.assign_doctor(doctor)

    def run(self):
        # Implement the main logic of the hospital system here
        pass
