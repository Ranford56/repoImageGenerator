from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGBA', (900, 900), "white")
data = "lorem ipsum"

font = ImageFont.truetype("RobotoCondensed-Regular.ttf", 75)
w,h = font.getsize(data)

draw = ImageDraw.Draw(img)
draw.text(((900-w)/2,(900-h)/2), data, font=font, fill="black")

img.show()