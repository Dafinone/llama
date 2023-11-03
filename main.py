from fastapi import FastAPI
import uvicorn
import llama

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello llama 2!"}

@app.get("/get_response/")
async def generate_text():
    response = llama()

    return response


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
