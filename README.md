# clip-mathpix
Extract image from clipboard, use mathpix to recognize, put latex text to clipboard. Tested on Ubuntu1804 Python3

## Complete it

Complete the APP_ID and APP_KEY. Register it on https://dashboard.mathpix.com/. You will have 1000 free requests per month, 200 requests per minute.

## Create shortcut for Ubuntu 18.04

1. create shortcut for partial screenshot to clipboard : gnome-screenshot -ac  --- ctrl+shift+alt+s
2. create shortcut for clip-mathpix : python3 PATH/clip-mathpix.py             --- ctrl+shift+alt+a

## Usage
1. ctrl+shift+alt+s : Partial screenshit by mouse
2. ctrl+shift+alt+a : convert the image using mathpix
3. ctrl+v           : paste the text wherever you want.
