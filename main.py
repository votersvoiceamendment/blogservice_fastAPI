from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
	return "Welcome to the blogservice API"