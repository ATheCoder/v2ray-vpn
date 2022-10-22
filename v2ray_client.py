from turtle import update
from urllib.request import urlretrieve
from progress.bar import Bar
import atexit
import os
import zipfile

from json_template import generate_json

class Downloader:
    def __init__(self, url, to):
        self.url = url
        self.to = to
        
        self.progress = None
        self.delete_on_exit = atexit.register(self.delete_file)
        
        urlretrieve(url, to, self.update)
        
    def update(self, blocks, bs, size):
        if not self.progress:
            self.progress = Bar(self.to, max=size)
        else:
            self.progress.goto(blocks * bs)
            
        if blocks * bs >= size:
            atexit.unregister(self.delete_file)

    def delete_file(self):
        if os.path.exists(self.to):
            os.remove(self.to)
        

def download_v2ray_client():
    save_path = 'v2ray-macos-64.zip'
    Downloader('https://github.com/v2fly/v2ray-core/releases/download/v5.1.0/v2ray-macos-64.zip', save_path)
    
    with zipfile.ZipFile(save_path, 'r') as zip_ref:
        zip_ref.extractall('v2ray-macos-64')

def generate_v2ray_config(ip_addr, port, user_id):    
    res = generate_json('./config_template.json', {"variable": ip_addr, "port": port, "user_id": user_id})
    
    with open('./config.json', 'w') as file:
        file.write(res)
    
    
    
generate_v2ray_config('37.32.29.37', 1310, '2b163471-8f76-453f-8990-cb3375cd2eec')