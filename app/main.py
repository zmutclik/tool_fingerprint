from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
import time
from config import app_pass,app_user,appFP_path,appFP_title

from pywinauto.application import Application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard


appFP = {}

app = FastAPI(title="TOOL-FINGERPRINT",
              description="TOOL Biasa, untuk mengakali kebusukuannyaa...!!!",
              version="1.0.0",)


@app.on_event('startup')
def init_data():
    print("init call")
    appFP["app"] = Application(backend='uia').start(appFP_path)
    appFP["dlg"] = appFP["app"][appFP_title]
    appFP["posisi"] = "JKN"
    appFP["window"] = appFP["dlg"].wrapper_object()
    appFP["window"].iface_transform.Move(0, 0)  # move the window to top-left corner
    app_login()


@app.get("/")
def root(request: Request):
    client_ip = request.client.host

    return {"message": "Hello BOZ "+request.client.host+" !!!"}


@app.get("/login")
def app_login():
    appFP["dlg"].set_focus()
    time.sleep(2)
    appFP["dlg"].usernameEdit.type_keys(app_user)
    appFP["dlg"].usernameEdit2.type_keys(app_pass)
    time.sleep(1)
    appFP["dlg"].LoginButton.click()


@app.get("/noJKN/{noKartu}")
def withNoJKN(noKartu: str):
    appFP["dlg"].set_focus()
    time.sleep(1)
    keyboard.send_keys('{SPACE}')
    time.sleep(1)
    appFP["dlg"].RadioButton1.click_input()
    appFP["dlg"].Edit3.type_keys(noKartu)
    # appFP["dlg"].print_control_identifiers()


@app.get("/noNIK/{noNIK}")
def withNoNIK(noNIK: str):
    appFP["dlg"].set_focus()
    time.sleep(1)
    keyboard.send_keys('{SPACE}')
    time.sleep(1)
    appFP["dlg"].RadioButton2.click_input()
    appFP["dlg"].Edit3.type_keys(noNIK)
