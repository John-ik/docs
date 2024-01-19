import urllib.request
import zipfile

url = f'https://api.github.com/repos/John-ik/docs/zipball/main'
print('url:', url)

file = "./zip.zip"
local_filename, _ = urllib.request.urlretrieve(url, filename=file)

with zipfile.ZipFile(file) as z:
    z.extractall()
