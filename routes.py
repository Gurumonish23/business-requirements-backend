# Placeholder for route handlers
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return [{"name": "Alice", "age": 30}]