from os import environ
import uvicorn
from app import app

uvicorn.run(
    app,
    host=environ.get('HOST', "0.0.0.0"),
    port=int(environ.get('PORT', 8000)),
)