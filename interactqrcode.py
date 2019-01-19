import html
from PIL import Image
import zbar
import os
import qrcode


# Set up logging
logging.basicConfig(
    format='%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S",
    level = logging.INFO)

logger = logging.getLogger(__name__)


def generateQR(eventID):
    qr = qrcode.QRCode(version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_H,
                        box_size=10,
                        border=4)
    data = "authorize" + eventID
    qrimg = qrcode.make(data)
    return qrimg

def readQR():
    #read QR code here 


"""
incomplete:
"""

#temporary store of info 
INFO_STORE = {}


def photo(bot, update):
    # what pathway can we use to save the photo on the phone?
    save_path = 
    file_id=update.message.photo[-1].file_id
    NewFile=bot.getFile(file_id)
    NewFile.download(os.path.join(save_path, time+'.jpg'))
    filename = datetime.datetime.now().strftime("%d-%m-%y_%H:%M,%S") + 'jpg'
    
    # not very sure how the following code works so might be wrong
    scanner = zbar.ImageScanner()
    pil = Image.open(filename).convert('L')
    width, height = pil.size
    raw = pil.tobytes()
    image = zbar.Image(width, height, 'Y800', raw)
    result = scanner.scan(image)

    for symbol in image:
        answer = symbol.data.decode(u'utf-8')


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)
