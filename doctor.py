# doctor.py
class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.patients = []

    def assign_patient(self, patient):
        self.patients.append(patient)

    def get_doctor_info(self):
        return f"Doctor Name: {self.name}, Specialization: {self.specialization}"
