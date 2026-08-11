from pydantic import BaseModel

class Patient(BaseModel):

    name: str
    age: int


def insert_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print("Data is inserted")

def update_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print("Data is updated")


patient_info = {"name": "Babar", "age": 33}

patient_info2 = {"name": "John", "age": 33}

patient1 = Patient(**patient_info)
patient2 = Patient(**patient_info2)
insert_data(patient1)
update_data(patient2)