from fastapi import FastAPI
from Routes.users_routes import router as users_router
from Routes.stats_routes import router as stats_router
from Routes.friend_requests_routes import router as friend_requests_router

app = FastAPI(title="EC - En Comunidad")

app.include_router(users_router, prefix="/usuarios", tags=["usuarios"])
app.include_router(stats_router, prefix="/stats", tags=["stats"])
app.include_router(friend_requests_router, prefix="/solicitudes-de-amistad", tags=["solicitudes-de-amistad"])

@app.get("/")
async def root():
    return {"message":"Welcome to the API"}