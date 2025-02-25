A simple image steganography tool that hides and retrieves secret messages inside images using Python, OpenCV, and Tkinter. This project provides both command-line and GUI-based interfaces for easy use.

Install dependencies:

pip install opencv-python

Usage :
Run the GUI Application

To use the Tkinter-based interface, run:
python gui.py

Click "Select Image" to choose an image.
Enter the message and password for encryption.
Click "Encrypt" to hide the message inside the image.
To decrypt, enter the password and click "Decrypt" to retrieve the hidden message.

🔹 Run via Command Line
Encrypt a Message into an Image
python encrypt.py
Enter the image path.
Enter the secret message.
Set a password.
The encrypted image will be saved as encryptedImage.jpg.

Decrypt a Message from an Image

python decrypt.py
Enter the encrypted image path.
Enter the original message length.
Provide the correct password.
If the password is correct, the hidden message will be displayed.
