import os
import base64
import requests
import json
from gi.repository import Gtk as gtk, Gdk
#

# Common module for calling Mathpix OCR service from Python.
#
# N.B.: Set your credentials in environment variables APP_ID and APP_KEY,
# either once via setenv or on the command line as in
# APP_ID=my-id APP_KEY=my-key python3 simple.py
#

env = os.environ

default_headers = {
    'app_id': env.get('APP_ID', 'YOUR_MATHPIX_ID'),
    'app_key': env.get('APP_KEY', 'YOUR_MATHPIX_APP_KEY'),
    'Content-type': 'application/json'
}

service = 'https://api.mathpix.com/v3/latex'

#
# Return the base64 encoding of an image with the given filename.
#
def image_uri(filename):
    image_data = open(filename, "rb").read()
    return "data:image/jpg;base64," + base64.b64encode(image_data).decode()

#
# Call the Mathpix service with the given arguments, headers, and timeout.
#
def latex(args, headers=default_headers, timeout=30):
    r = requests.post(service,
        data=json.dumps(args), headers=headers, timeout=timeout)
    return json.loads(r.text)


def mathpix_clipboard():
    #im = ImageGrab.grabclipboard()
    #im.save('equa.png','PNG')
    clipboard = gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
    image = clipboard.wait_for_image()
    if image is not None:
        image.savev('equa', 'png', ["quality"], ["100"])
    else:
        print("No image in clipboard")
        return;
    r = latex({
        'src': image_uri("equa"),
        'formats': ['latex_simplified']
    })
    print(r['latex_simplified'])
    clipboard.set_text(r['latex_simplified'], -1)
    clipboard.store()

if __name__ == '__main__':
    mathpix_clipboard()
