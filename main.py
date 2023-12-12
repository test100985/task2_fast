from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"Лесникова Софья Александровна"}

@app.get('/tools')
async def f_indexT():
    return "Низкие навыки в программировании"

@app.get('/users')
async def f_indexU():
    return "+79564342574"