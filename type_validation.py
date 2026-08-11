from pydantic import BaseModel
from typing import List, Dict, Optional 
class Patient(BaseModel):

    name: str
    age: int
    weight: float 
    married: bool
    allergies: Optional[List[str]] = None 
    contact_details: Dict[str, str]

def insert_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print("Data is inserted")

def update_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print("Data is updated")


patient_info = {"name": "Babar", "age": '33', "weight": '55.4',"married": True,
                 "contact_details":
                {"email": "bacabba@gm.com", "phone_no": "0937839393"}}

#patient_info2 = {"name": "John", "age": 33}

patient1 = Patient(**patient_info)
#patient2 = Patient(**patient_info2)
insert_data(patient1)
# update_data(patient1)