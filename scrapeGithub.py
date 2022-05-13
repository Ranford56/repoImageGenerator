import requests

def getInfo(site):
    data = site.split('/')[-2:]
    apiSite = 'https://api.github.com/repos/'+data[0]+'/'+data[1]
    html = requests.get(apiSite)
    data = html.json()

    repoInfo = {
        'name' : data['name'],
        'watchers': data['watchers'],
        'subs': data['subscribers_count'],
        'forks': data['forks'],
        'license': data['license']['name'],
        'languages': data['language']
    }
    
    return repoInfo
