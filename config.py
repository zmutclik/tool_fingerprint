import os
from os.path import join, dirname
from dotenv import load_dotenv

pathfile = os.path.normpath(os.path.dirname(
    os.path.abspath(__file__)) + os.sep)
pathfile = os.path.abspath(os.path.join(pathfile, '..'))
dotenv_path = join(pathfile, '.env')

appFP_path = os.environ.get("appFP_path")
appFP_title =  os.environ.get("appFP_title")
app_user =  os.environ.get("app_user")
app_pass =  os.environ.get("app_pass")