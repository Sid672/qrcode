# qrcode
Making qr code with Python


# Program 

First install qrcode library using command line in terminal.
```
pip install qrcode
```

# Code
To genrate QR code one has to create an image using line
```
image = qrcode.make("https://www.youtube.com/watch?v=kJQP7kiw5Fk")  
```

We also need a format to save the image for this use

```
image.save("qr", "PNG")
```
### Final code will looks like
```Python
import qrcode

#format
# image  = qrcode.make("link")

#example
image = qrcode.make("https://www.youtube.com/watch?v=kJQP7kiw5Fk")  

#name of file and its extension. like JPG, PNG.
image.save("qr", "PNG") 
```
### Done!

## Output

