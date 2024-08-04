from fastapi import FastAPI 
app = FastAPI() 
ECHO is off.
@app.get("/") 
def read_root(): 
    return {"Hello": "World"} 
