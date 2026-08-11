from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: int

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dic = {"city": "Islamabad", "state": "Federal", "pin": 2345}
address1 = Address(**address_dic)

patient_dic = {"name": "Babar", "age": 33, "gender":"male", "address":address1}
patient1 = Patient(**patient_dic)


temp = patient1.model_dump(exclude={"address":["state"]})
print(temp)
print(type(temp))