""" A simple automation tool to search LinkedIn jobs """
import pyautogui as pag
import webbrowser as wb
import time as t
from PIL import ImageChops
import zipfile
import glob
import os
import shutil
import pyfiglet

def compareBetweenImages(firstImg, secondImg):
    diff = ImageChops.difference(firstImg, secondImg)
    bbox = diff.getbbox()
    if not bbox:
        return True
    else:
        return False

# 1- Open LinkedIn
wb.open_new_tab("https://www.linkedin.com/feed/")
# 2- Search For The Job
pag.moveTo(564, 141, 5)
pag.click()
pag.write("Embedded Linux")
pag.press("enter")
pag.moveTo(500, 199, 4)
pag.click()
t.sleep(6)
# 3- Screenshot and scroll
previousScreenShot = pag.screenshot("1.jpg")
counter = 2
while True:
    pag.scroll(-5, x=500, y=360)
    t.sleep(3)
    currentScreenShot = pag.screenshot(f"{counter}.jpg")
    counter += 1
    if not(compareBetweenImages(previousScreenShot, currentScreenShot)):
        previousScreenShot = currentScreenShot
    else:
        break
# 4- Send all images to gmail
#   (1) Zip all the images
zip_filename = "EmbeddedLinuxJobs.zip"
image_files = sorted(glob.glob("*.jpg"))
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for file in image_files:
        zipf.write(file)
        print(f"Added: {file}")
print(f"Created zip: {zip_filename}")
home_path = os.path.expanduser("~")
destination = os.path.join(home_path, zip_filename)
shutil.move(zip_filename, destination)
#   (2) Send the zip file to gmail
wb.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
pag.moveTo(83, 220, 11)
pag.click()
t.sleep(3)
pag.write("Sayed Mohsen")
pag.press("enter")
pag.press("tab")
t.sleep(3)
pag.write("Embedded Linux Jobs")
pag.press("tab")
pag.press("tab")
pag.press("tab")
pag.press("tab")
pag.press("enter")
pag.write("EmbeddedLinuxJobs",1)
pag.press("tab")
pag.press("tab")
pag.press("space")
pag.press("enter")
pag.moveTo(1303, 1052, 3)
pag.click()
print(pyfiglet.figlet_format("Email Sent Successfully"))