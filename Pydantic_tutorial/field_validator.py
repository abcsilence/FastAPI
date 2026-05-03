from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : str
    email: EmailStr
    age : int
    weight : float
    married: bool 
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfs.com', 'icic.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("not a valid domain")

        return value 

    @field_validator('name', mode = after) #default value is afete
    @classmethod
    def transform_name(cls, value):
        return value.upper()    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted into database")        

patient_info = {
    'name': 'roshan',
    'email': 'abc@hdfs.com',
    'linkedin_url': 'https://linkedin.com/in/roshan',
    'age': 120,
    'weight': 75.3,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'phone': '23333334'
    }
}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)       