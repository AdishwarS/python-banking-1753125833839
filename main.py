```python
from fastapi import FastAPI, HTTPException
import logging

app = FastAPI()

@app.get("/health")
def read_root():
    return {"Status": "Healthy"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    logging.error(f"Error occurred: {exc}")
    return {"Error": str(exc)}
```