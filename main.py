from fastapi import FastAPI 

app = FastAPI()

@app.get("/") #create a route here
def hello():
    return {"message": "Hello world"}

@app.get("/about")
def about():
    return {"message": "CampusX is an educational platform where you can  learn AI"}

@app.get('/learn')

def learn():
    return{"message": "Complete with consistency"}