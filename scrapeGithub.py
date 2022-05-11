import requests

site = "https://github.com/spicetify/spicetify-cli"

def getInfo(site, hasMultipleLang):
    data = site.split('/')[-2:]
    apiSite = 'https://api.github.com/repos/'+data[0]+'/'+data[1]
    html = requests.get(apiSite)
    data = html.json()
    nombreDelRepo = data['name']
    ojos = data['watchers']
    subs = data['subscribers_count']
    forks = data['forks']
    licencia = data['license']['name']

    if hasMultipleLang == True:
        #funcion que agarra los varios legnaujes
        langApiSite = apiSite + '/languages'
        html = requests.get(langApiSite)
        data = html.json()
        lenguajes = list(data.keys())
    else:
        lenguajes = data['language']
    
    print(lenguajes)

getInfo(site, True)
