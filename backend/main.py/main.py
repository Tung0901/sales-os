from fastapi import FastAPI

app = FastAPI(
    title="Sales OS API",
    version="0.0.1"
)

@app.get("/")
def root():
    return {
        "project": "Sales OS",
        "status": "Running"
    }
