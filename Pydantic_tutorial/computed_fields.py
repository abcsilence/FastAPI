#computed field
from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name : str
    email: EmailStr
    age : int
    weight : float #kg
    height: float #meters
    married: bool 
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi



def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("BMi", patient.bmi)
    print("Updated")        

patient_info = {
    'name': 'roshan',
    'email': 'abc@hdfs.com',
    'linkedin_url': 'https://linkedin.com/in/roshan',
    'age': 120,
    'weight': 75.3,
    'height': 1.72, 
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'phone': '23333334'
    }
}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)             