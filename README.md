# Keylogger

## Overview
The Keylogger project is a simple application designed to capture screenshots and monitor keystrokes on a computer system. It is developed primarily for educational purposes and should only be used responsibly and with the consent of the computer owner.

## Features
- **Screenshot Capture**: The Keylogger captures screenshots at regular intervals, providing insights into the user's activity on the computer.
- **Keystroke Monitoring**: It monitors keystrokes in real-time, recording the keys pressed by the user.
- **Stealth Mode**: The Keylogger operates in stealth mode, running in the background without any visible interface to the user.
- **Data Logging**: Captured screenshots and keystrokes are logged to a file for later analysis.

## Usage Steps
 - Code updation
1. Open the main code(Windows Update Service 22.4.2.py)
2. Check for the reciever ip, port number comment.
3. Update the variables i.e. ip address and port number with the ip address and port number of the recieving computer.
4. (Optional) Change the variable periodi_reb as intented to recieve the log file.
5. Change or remove the stopping variable or condition from the code.
6. Convert the code to .exe using compiling tools like auto-py-to-exe, etc.
 
 - Compressing all scripts into one
1. Compress all the scripts into one file along with the image file.
2. Use the sfx options whike compressing and set the image to load first then the driver script

- At the Reciever's end.
1. Install netcat tool on the machine from https://nmap.org/download.html
2. Run the toola and set your computer as listner for the portnumber assigned in the code.
3. Save the recived file to the desired folder.
4. Change the extention of the file to .zip to open it.

## Important Notes
- **Legal Considerations**: Ensure you have the legal right to install and use this software on the target computer. Unauthorized use may violate privacy laws.
- **Ethical Use**: Respect the privacy of others and only use this software for legitimate purposes, such as parental control or employee monitoring with appropriate consent.
- **Security**: Be cautious when handling the captured data. Store it securely and avoid transmitting it over unsecured channels.

## Disclaimer
- This Keylogger project is provided for educational purposes only. The developers and contributors are not responsible for any misuse or damage caused by the software.
- Script for complete removal of this keylogger is still pending so use the keylogger at your own risk.
