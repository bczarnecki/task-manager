from fastapi import FastAPI
import uvicorn
from items.router import router as items_router

api = FastAPI()
api.include_router(items_router)

if __name__ == '__main__':
    uvicorn.run(api)
