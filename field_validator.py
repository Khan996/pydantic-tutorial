from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict

class Patient(BaseModel):

    name:str 
    age: int 
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):

        valid_domains = ["gmail.com", "yahoo.com"]
        domain_name = value.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError("Email not valid")

        return value
    @field_validator("name")
    @classmethod 
    def name_validator(cls, value):
        return value.upper()

    #field_validtor can be operated in two modes: before and after (type coercion)
    @field_validator("age", mode="after")
    @classmethod
    def age_validator(cls, value):
        if 0<value< 100:
            return value
        else:
            raise TypeError("Age cannot be string")

    #age is still a string but using 'after' has converted it into int and didn't raise error.

def insert_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Data is inserted")


patient_info = {"name": "John", "age": "33", "email":"abc@gmail.com", "weight": 77, "married": True,
                "allergies": ["Pollen", "mollen", "gollen"], 
                "contact_details": {"Phone No": "9876543"}
                }

patient = Patient(**patient_info)
insert_data(patient)