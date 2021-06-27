from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    x={"message":"Happy Summer Soltice"}
    return x
