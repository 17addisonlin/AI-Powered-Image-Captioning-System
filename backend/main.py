from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image
from src.captioner import ImageCaptioner
import io

app = FastAPI()

#  static file (frontend image up)
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

@app.get("/")
async def read_root():
    return HTMLResponse(content=open("backend/index.html").read(), status_code=200)

@app.post("/caption/")
async def create_caption(file: UploadFile = File(...)):
    # Read image as binary
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    
    # Generate caption
    captioner = ImageCaptioner()
    caption = captioner.caption(image)

    return {"caption": caption}
