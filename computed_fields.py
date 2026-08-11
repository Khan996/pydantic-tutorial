# Model validator is doing multiple field_validator at once

from pydantic import BaseModel, EmailStr, field_validator, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name:str 
    age: int 
    email: EmailStr
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi
            
    

def insert_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.height)
    print("BMI", patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Data is inserted")


patient_info = {"name": "John", "age": "65", "email":"abc@gmail.com", "weight": 77, "height":"1.74", 
                "married": True, "allergies": ["Pollen", "mollen", "gollen"], 
                "contact_details": {"Phone No": "9876543", "emergency": "98765432"}
                }

patient = Patient(**patient_info)
insert_data(patient)