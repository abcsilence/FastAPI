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
print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)



#better organization of related data(eg, vitals, address)


#Reausibility: Use Vitals in multiple models(eg, patient, medical record)

#Readability : Easier for developers and API consumers to understand 

#validation : Nested models are validated automatically-no extra work needed  