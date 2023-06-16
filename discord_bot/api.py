from fastapi import FastAPI

app = FastAPI()

stock = 0

def get_stock():
    return stock


@app.put("/variable/{new_value}")
async def update_variable(new_value: int):
    global stock

    stock = new_value

    return {"message": "Variable updated", "new_value": stock}

@app.get("/get_stock")
async def get_stock():
    return {"stock": stock}