# Model validator is doing multiple field_validator at once

from pydantic import BaseModel, EmailStr, field_validator, model_validator
from typing import List, Dict

class Patient(BaseModel):

    name:str 
    age: int 
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError("Age greater than 60 must have emergency contact details")
        else:
            return model
        
            
    

def insert_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Data is inserted")


patient_info = {"name": "John", "age": "65", "email":"abc@gmail.com", "weight": 77, "married": True,
                "allergies": ["Pollen", "mollen", "gollen"], 
                "contact_details": {"Phone No": "9876543", "emergency": "98765432"}
                }

patient = Patient(**patient_info)
insert_data(patient)