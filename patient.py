# patient.py
class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.doctor = None

    def assign_doctor(self, doctor):
        self.doctor = doctor

    def get_patient_info(self):
        return f"Patient Name: {self.name}, Age: {self.age}"
