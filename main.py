from flask import Flask, jsonify
import os

import math
import feedparser
from random import seed
from random import randint
import textwrap

from PIL import Image 
from PIL import ImageFont
from PIL import ImageDraw
from datetime import datetime
import urllib.request
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    
    urllib.request.urlretrieve(
      'https://source.unsplash.com/1080x1080/',
       "gfg.png")
  
    img = Image.open("gfg.png")

    draw = ImageDraw.Draw(img)

    d = feedparser.parse('https://sucesso.hmr1973.com/feed/')

    return 'ok'

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))