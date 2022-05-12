import requests

def getInfo(site, hasMultipleLang):
    data = site.split('/')[-2:]
    apiSite = 'https://api.github.com/repos/'+data[0]+'/'+data[1]
    html = requests.get(apiSite)
    data = html.json()

    if hasMultipleLang == True:
        #funcion que agarra los varios legnaujes
        langApiSite = apiSite + '/languages'
        html = requests.get(langApiSite)
        langData = html.json()
        lenguajes = list(langData.keys())
    else:
        lenguajes = data['language']
    
    repoInfo = {
        'name' : data['name'],
        'watchers': data['watchers'],
        'subs': data['subscribers_count'],
        'forks': data['forks'],
        'license': data['license']['name'],
        'languages': lenguajes
    }
    
    return repoInfo
