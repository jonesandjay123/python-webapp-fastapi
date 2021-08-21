from tortoise import fields, models

from tortoise.contrib.pydantic import pydantic_model_creator

class Sprocket(models.Model):
    id = fields.IntField(pk=True)
    teeth = fields.IntField(max_length=50)
    pitch_diameter = fields.IntField(max_length=50)
    outside_diameter = fields.IntField(max_length=50)
    pitch = fields.IntField(max_length=50)

    class PydanticMeta:
        pass

class Fdata(models.Model):
    factory_id = fields.IntField(pk=True)
    chart_data = fields.JSONField()

    class PydanticMeta:
        pass

Sprocket_Pydantic = pydantic_model_creator(Sprocket, name="Sprocket")
SprocketIn_Pydantic = pydantic_model_creator(Sprocket, name="SprocketIn", exclude_readonly=True)
Fdata_Pydantic = pydantic_model_creator(Fdata, name="Fdata")
FdataIn_Pydantic = pydantic_model_creator(Fdata, name="FdataIn", exclude_readonly=True)
