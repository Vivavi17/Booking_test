from datetime import date

from pydantic import BaseModel


class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_days: int
    total_cost: int

    class Config:
        from_attributes = True


class UsersBookings(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int
    image_id: int
    name: str
    description: str | None
    services: list | None


class AddBooking(BaseModel):
    id: int
    user_id: int
    room_id: int
    date_from: date
    date_to: date

    class Config:
        from_attributes = True
