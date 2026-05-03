from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state: str
    pin: str


class Patient(BaseModel):
    name : str
    gender: str
    age : int
    address:Address


address_dict ={'city': 'gurugaun', 'state':'harayana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'roshan', 'gender':'male', 'age':35, 'address': address1}
patient1 = Patient(**patient_dict)

#temp = patient1.model_dump() #convert the obj data type to the dictionary
# temp = patient1.model_dump(include = ['name'])
temp = patient1.model_dump(exclude ={'address':['state']})

#temp = patient1.model_dump_json() #convert the obj data type to the json format.  
print(temp)
print(type(temp))