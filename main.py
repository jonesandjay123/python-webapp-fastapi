
from starlette.responses import RedirectResponse
from fastapi import FastAPI, HTTPException
from models import Fdata, Fdata_Pydantic, FdataIn_Pydantic, Sprocket, Sprocket_Pydantic, SprocketIn_Pydantic
from pydantic import BaseModel

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI(title='backend API')

class Message(BaseModel):
    message: str

@app.get('/')
async def read_root():
    return RedirectResponse(url='/docs')

@app.get('/allFactories')
async def read_fdata():
    return await Fdata.all().values('factory_id', 'chart_data')

@app.get('/getFactoryByID/{id}', response_model=Fdata_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def get_one_factory(id: int):
    return await Fdata_Pydantic.from_queryset_single(Fdata.get(factory_id=id))

@app.get('/allSprockets')
async def read_sdata():
    return await Sprocket.all().values('id', 'teeth', 'pitch_diameter', 'outside_diameter', 'pitch')

@app.get('/getSprocketByID/{id}', response_model=Sprocket_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def get_one(id: int):
    return await Sprocket_Pydantic.from_queryset_single(Sprocket.get(id=id))

@app.post('/createNewSprocket', response_model=Sprocket_Pydantic)
async def create(sprocket: SprocketIn_Pydantic):
    obj = await Sprocket.create(**sprocket.dict(exclude_unset=True))
    return await Sprocket_Pydantic.from_tortoise_orm(obj)


@app.put("/updateSprocketByID/{id}", response_model=Sprocket_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def update(id: int, sprocket: SprocketIn_Pydantic):
    await Sprocket.filter(id=id).update(**sprocket.dict(exclude_unset=True))
    return await Sprocket_Pydantic.from_queryset_single(Sprocket.get(id=id))

@app.delete("/sprocket/{id}", response_model=Message, responses={404: {"model": HTTPNotFoundError}})
async def delete(id: int):
    delete_obj = await Sprocket.filter(id=id).delete()
    if not delete_obj:
        raise HTTPException(status_code=404, detail="This sprocket is not found.")
    return Message(message="Succesfully Deleted")

register_tortoise(
    app,
    db_url="sqlite://store.db",
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)
