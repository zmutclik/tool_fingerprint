from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="TOOL-FINGERPRINT",
              description="TOOL Biasa, buat Sesuatu yg Biasa, Agar Biasa Biasa AJA",
              version="1.0.0",)


@app.get("/")
def root(request: Request):
    client_ip = request.client.host

    return {"message": "Hello BOZ "+request.client.host+" !!!"}
