from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello llama 2!"}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
