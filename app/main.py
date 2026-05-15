from fastapi import FastAPI
from app.routes import router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(
    title="Mi API de GamerPower",
    description="Una API estructurada para consultar juegos gratuitos.",
    version="1.0.0"
)

# Incluimos las rutas
app.include_router(router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
async def read_index():
    return FileResponse('index.html')