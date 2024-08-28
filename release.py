import requests
import argparse
import os
import json
import zipfile
import base64
parser = argparse.ArgumentParser(description='upload release assets to github')
parser.add_argument('--token', type=str, default='GITHUB_TOKEN')
parser.add_argument('--repository', type=str, default='example/repo')
parser.add_argument('--verify', type=bool, default=True, action=argparse.BooleanOptionalAction)
args = parser.parse_args()
token = args.token
verify = args.verify
repository = args.repository
tag_name = 'static_library'
#get release
release_id = 0
headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
url = 'https://api.github.com/repos/'+repository+'/releases'
headers['Authorization'] = 'token ' + token
r = requests.get(url, headers=headers, verify=verify)
releases = r.json()
if r.status_code != 200:
    print(r.text)
assert r.status_code == 200, 'get release list failed'
release_id = 0
#find release
for release in releases:
    if (release['tag_name'] == tag_name):
        release_id = release['id']
        break
    
if release_id != 0:
#delete release
    print("deleting release")
    headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
    url = 'https://api.github.com/repos/'+repository+'/releases/' + str(release_id)

    headers['Authorization'] = 'token ' + token
    r = requests.delete(url, headers=headers, verify=verify)
    if r.status_code != 204:
        print(r.text)
    assert r.status_code == 204, 'delete release failed'
    release_id = 0

#create release
print("creating release")
headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
url = 'https://api.github.com/repos/'+repository+'/releases'
headers['Authorization'] = 'token ' + token
data = {"tag_name":tag_name}
r = requests.post(url, headers=headers,json=data, verify=verify)
if r.status_code != 201:
    print(r.text)
assert r.status_code == 201, 'create release failed'
release_id = r.json()['id']

#upload release asset

f = open('github_scripts/files.json')
assets_to_upload = json.load(f)[tag_name]
f.close()
headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
url = 'https://uploads.github.com/repos/gyc0123/vulkan-and-opengl/releases/' + str(release_id) + '/assets'
headers['Authorization'] = 'token ' + token
headers['Content-Type'] = 'application/octet-stream'
for asset_name in assets_to_upload:
    assetpath = assets_to_upload[asset_name]
   

    if not os.path.exists(assetpath):
        print('asset not found: ' + assetpath)
        continue
    print("uploading asset: " + asset_name)
    with open(assetpath, 'rb') as file:
        params = {'name': asset_name}
        r = requests.post(url, headers=headers, params=params, data=file, verify=verify)
        if r.status_code != 201:
            print(r.text)
        assert r.status_code == 201, 'upload release failed'
