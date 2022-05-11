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
    data = "lorem ipsum"

    font = ImageFont.truetype("RobotoCondensed-Regular.ttf", 75)
    w,h = font.getsize(data)

    draw = ImageDraw.Draw(img)
    draw.text(((width-w)/2,(height-h)/2), data, font=font, fill="black")
    img.show()

generateImage(getInfo(site, False))
#repoInfo = getInfo(site, hasMultipleLang)
#generateImage(width, height, repoInfo)