from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.core.seeds.seed import seed_database
from src.api.v1.router import router as characters_router
from src.api.v1.exceptions import validation_exception_handler, validation_response_exception_handler
from fastapi.exceptions import RequestValidationError, ResponseValidationError
from fastapi_pagination import add_pagination
from fastapi.middleware.cors import CORSMiddleware

#seeding db with mock data
@asynccontextmanager
async def lifespan(app: FastAPI):
    seed_database()
    yield

app = FastAPI(title="Characters API🤖", lifespan=lifespan)
add_pagination(app) #adding pagination

#allowing all origins by default
origins = ["*"] 
app.add_middleware(  
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#routes
app.include_router(characters_router, prefix="/api/v1/character", tags=["characters"])

#custom exceptions
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(ResponseValidationError, validation_response_exception_handler)




@app.on_event("startup")
async def startup_event():
    seed_database()