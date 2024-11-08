from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from all origins for testing purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify a list of domains instead of "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
async def hello():
    return {"message": "Hello, Maaz!"}
