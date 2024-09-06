from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "hello world"}
@app.get('/items/{item_id}')
async def get_item(item_id: int):
    return {"itemby_id": item_id}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.01", port=8000)