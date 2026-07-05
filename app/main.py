from fastapi import FastAPI

app = FastAPI(
    title="Samvaad AI",
    description="A multilingual conversational AI voice agent.",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Samvaad AI!",
        "status": "running"
    }