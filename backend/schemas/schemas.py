from typing import Union, List
from datetime import datetime
from pydantic import BaseModel


class CarBrandBase(BaseModel):
    name: str
    logo: str
    description: Union[str, None] = None

    class Config:
        orm_mode = True


class CreateCarBrandSchema(CarBrandBase):
    pass


class UpdateCarBrandSchema(BaseModel):
    name: str
    logo: str
    description: str
    updated_at: datetime

    class Config:
        orm_mode = True


class CarBrandResponse(CarBrandBase):
    id: int
    name: str
    logo: str
    description: str
    created_at: datetime
    updated_at: datetime


class FilteredCarBrandResponse(CarBrandBase):
    name: str


class CarModelBase(BaseModel):
    brand_id: int
    name: str
    logo: str
    description: Union[str, None] = None

    class Config:
        orm_mode = True


class CreateCarModelSchema(CarModelBase):
    pass


class CarModelResponse(CarModelBase):
    id: int
    name: str
    logo: str
    brand: FilteredCarBrandResponse
    created_at: datetime
    updated_at: datetime


class UpdateCarModelSchema(BaseModel):
    name: str
    logo: str
    description: str
    brand_id: int
    updated_at: Union[datetime, None] = None

    class Config:
        orm_mode = True