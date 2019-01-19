#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import logging
import zbar
import pyqrcode
from PIL import Image
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                   level=logging.INFO)


# In[ ]:


# generate a png qr code based on input
qr_code = pyqrcode.create('EVENT CODE GOES HERE')
qr.png('event.png', scale = 6)


# In[ ]:


# scans a image file to process QR code
scanner = zbar.ImageScanner()
pil = Image.open('IMAGE FILE').convert('L')
width, height = pil.size
raw = pil.tobytes()
image = zbar.Image(width, height, 'Y800', raw)
result = scanner.scan(image)

for symbol in image:
    answer = symbol.data.decode(u'utf-8')

