from fastapi import FastAPI

from app.routes.tickets import router as tickets_router

app = FastAPI(title="ResolveAI API")


@app.get("/")
def root() -> dict:
    return {"message": "Welcome to ResolveAI API"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/about")
def about() -> dict:
    return {
        "project": "ResolveAI",
        "version": "0.5.0",
        "goal": "Become a production-grade Applied AI Engineer",
    }


@app.get("/ping")
def ping() -> dict:
    return {"message": "pong"}


app.include_router(tickets_router)  #If you don’t include the router, the endpoints won’t exist.