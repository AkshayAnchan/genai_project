from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def home():
    return {"message" : "Hello from FastAPI BackendServer"}

@app.get("/sample_user")
def user():
    return {"id" :1 , "name":"Anand" , "city" : "Bidar"}

@app.get("/access_key")
def access_key():
    return {"message": "This is a sample access key endpoint."}

