from fastapi import APIRouter, HTTPException, status, FastAPI
from app.schemas import Payments

paymentsapp = FastAPI(title="Payments Service")
payments: list[Payments] = []

@paymentsapp.get("/")
def get_payments():
    return payments

@paymentsapp.get("/{payment_id}")
def get_payment(payment_id: int):
    for p in payments:
        if p.payment_id == payment_id:
            return p
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")

@paymentsapp.post("/", status_code=status.HTTP_201_CREATED)
def add_payment(payment: Payments):
    if any(p.payment_id == payment.payment_id for p in payments):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="payment_id already exists")
    payments.append(payment)
    return payment

@paymentsapp.put("/{payment_id}", status_code=status.HTTP_200_OK)
def update_payment(payment_id: int, new_payment: Payments):
    for i, p in enumerate(payments):
        if p.payment_id == payment_id:
            payments[i] = new_payment
            return new_payment
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")

@paymentsapp.delete("/{payment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(payment_id: int):
    for i, p in enumerate(payments):
        if p.payment_id == payment_id:
            payments.pop(i)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")