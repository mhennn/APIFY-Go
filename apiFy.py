from fastapi import FastAPI
from request_module.request_params import RequestParam
import uvicorn

app = FastAPI()
reqParams = RequestParam()

@app.get('/')
def home():
    return {
        "Message": "Welcome to APIFY",
        "Available Route": [
            "/simpleData",
            "/keyValue"
            ]
        }

@app.get('/simpleData')
def simple_data():
    all_data = reqParams.request_simple_data()
    return all_data

@app.get('/keyValue/')
def key_value():
    key_value_data = reqParams.request_key_value()
    return key_value_data

if __name__ == "__main__":
    uvicorn.run("apiFy:app", reload=True)