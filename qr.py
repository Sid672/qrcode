import qrcode

#format
# image  = qrcode.make("link")

#example
image = qrcode.make("https://www.youtube.com/watch?v=kJQP7kiw5Fk")  

#name of file and its extension. like JPG, PNG.
image.save("qr", "PNG") 
