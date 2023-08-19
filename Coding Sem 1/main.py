from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}





@app.get("/user/{num}")
async def oddEven(num):
    if int(num) % 2 == 0:
        return 'Even'
    else:
        return 'odd'

