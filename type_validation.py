from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title="Name of the patient", description="Give name of the person in less than 50 chars", example=["John", "Micahel"])]
    age: int = Field(gt=20, lt=33)
    email: EmailStr
    Linkedin: AnyUrl
    weight: Annotated[float, Field(gt=0, lt=120, strict=True)]
    married: Annotated[bool, Field(default=None, description="Is the patient married or not?")]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

def insert_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.Linkedin)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print("Data is inserted")

def update_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print("Data is updated")


patient_info = {"name": "Babar", "age": '32', "email": "abc@gmail.com", 
                "weight": 55.4,"married": True, "Linkedin": "http://linkedin.com/123",
                "contact_details": {"phone_no": "0937839393"}}

#patient_info2 = {"name": "John", "age": 33}

patient1 = Patient(**patient_info)
#patient2 = Patient(**patient_info2)
insert_data(patient1)
# update_data(patient1)