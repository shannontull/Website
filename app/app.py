from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    x={"message":"Happy 4th of July"}
    return x
