from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/add/{num1}/{num2}")
async def oddEven(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return num1 + num2





@app.get("/user/{num}")
async def oddEven(num):
    if int(num) % 2 == 0:
        return 'Even'
    else:
        return 'odd'

