from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, tittle = 'Name of the patient',
    description ='Give the name of the patient in less than 50 chars', examples =['Nitish', 'Amit'])] #data validation and meta data attach  
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt =0 , lt=100)
    weight: Annotated[float , Field(gt=0, strict = True)]
    #here strict is used to get the exact data type, cause pydantic , easily 
    # conver the string num into int, so for the restrict we use strict # gt is greater than , it use to validate: 
    married: bool
    allergies: Optional[list[str]] = None
    contact_details: dict[str, str]


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted into database")


patient_info = {
    'name': 'roshan',
    'email': 'abc@gmail.com',
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


# def update_patient_data(patient: UpdatePatient):
#     print(patient.name)
#     print(patient.age)
#     print("Updated in database")


# update_info = {
#     'name': 'roshan',
#     'age': '30'
# }

# patient2 = UpdatePatient(**update_info)
# update_patient_data(patient2)