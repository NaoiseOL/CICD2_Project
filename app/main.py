from fastapi import FastAPI, Request
import httpx

app = FastAPI(title="API Gateway")

# Base URLs for each service
BOOKINGS_URL = "http://localhost:8001"
PAYMENTS_URL = "http://localhost:8002"
USERS_URL = "http://localhost:8003"

@app.api_route("/bookings/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def bookings_proxy(request: Request, path: str):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            f"{BOOKINGS_URL}/{path}",
            content=await request.body(),
            headers=request.headers
        )
    return response.json()

@app.api_route("/payments/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def payments_proxy(request: Request, path: str):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            f"{PAYMENTS_URL}/{path}",
            content=await request.body(),
            headers=request.headers
        )
    return response.json()

@app.api_route("/users/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def users_proxy(request: Request, path: str):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            f"{USERS_URL}/{path}",
            content=await request.body(),
            headers=request.headers
        )
    return response.json()