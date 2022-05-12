from PIL import Image, ImageDraw, ImageFont
from scrapeGithub import getInfo

site = "https://github.com/spicetify/spicetify-cli"

def getDimension():
    print("Avaliable social media: \n\n1.Instagram stories \n2.Facebook stories \n3.Instagram post\n\n")
    selection = input("Choose an option: ")
    casos = {
        '1': [1080, 1920],
        '2': [1080, 1920],
        '3': [1080, 1350]
    }
    dimension = casos.get(selection, False)
    while dimension == False:
        print("Select a valid option \n\n1.Instagram stories \n2.Facebook stories \n3.Instagram post")
        selection = input("Choose an option: ")
        casos = {
            '1': [1080, 1920],
            '2': [1080, 1920],
            '3': [1080, 1350]
        }
        dimension = casos.get(selection, False)

    return dimension

def generateImage(repoInfo):
    dimension = getDimension()
    width = dimension[0]
    height = dimension[1]
    img = Image.new('RGBA', (width, height), "white")
    logo = Image.open(r"logotipo-de-github.png")
    logo = logo.convert('RGBA')

    font = ImageFont.truetype("RobotoCondensed-Regular.ttf", 50)
    draw = ImageDraw.Draw(img)
    initPosition = 50
    for info in repoInfo:
        data = str(repoInfo[info])
        w,h = font.getsize(data)
        draw.text(((width-w)/2, initPosition), data, font=font, fill="black")
        initPosition += 100
    w, h = logo.size
    img.paste(logo, (int((width-w)/2),int((height-h)/2)), logo)
    img.show()

generateImage(getInfo(site, False))
