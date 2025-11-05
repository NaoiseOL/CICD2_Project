from fastapi import FastAPI, HTTPException, status
from app.schemas import Booking_Info

bookingsapp = FastAPI(title="Bookings Service")
bookings: list[Booking_Info] = []

@bookingsapp.get("/")
def get_bookings():
    return bookings

@bookingsapp.get("/{booking_id}")
def get_booking(booking_id: int):
    for b in bookings:
        if b.booking_id == booking_id:
            return b
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")

@bookingsapp.post("/", status_code=status.HTTP_201_CREATED)
def add_booking(booking: Booking_Info):
    if any(b.booking_id == booking.booking_id for b in bookings):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="booking_id already exists")
    bookings.append(booking)
    return booking

@bookingsapp.put("/{booking_id}", status_code=status.HTTP_200_OK)
def update_booking(booking_id: int, new_booking: Booking_Info):
    for i, b in enumerate(bookings):
        if b.booking_id == booking_id:
            bookings[i] = new_booking
            return new_booking
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")

@bookingsapp.delete("/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(booking_id: int):
    for i, b in enumerate(bookings):
        if b.booking_id == booking_id:
            bookings.pop(i)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")