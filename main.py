from fastapi import FastAPI
from dotenv import load_dotenv

# Load .env variables in the app
load_dotenv()

app = FastAPI()

@app.get("/")
def root():
	return "Welcome to the blogservice API"