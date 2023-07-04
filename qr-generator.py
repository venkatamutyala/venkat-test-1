from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
import qrcode
from io import BytesIO
from PIL import Image

app = FastAPI()

@app.get("/v1/qr")
def generate_qr(url: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()

    return Response(content=img_bytes, media_type="image/png")


