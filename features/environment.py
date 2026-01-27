from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import subprocess
import time
import os

def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')
    
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.implicitly_wait(10)
    
    context.base_url = 'http://127.0.0.1:5000'
    
    os.environ['FLASK_ENV'] = 'testing'
    context.flask_process = subprocess.Popen(
        ['python', 'app.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=os.path.dirname(os.path.abspath(__file__)) + '/..'
    )
    
    time.sleep(3)

def after_all(context):
    context.driver.quit()
    
    if hasattr(context, 'flask_process'):
        context.flask_process.terminate()
        context.flask_process.wait()
