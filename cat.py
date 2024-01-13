import requests
from PIL import Image
import json
import re
import os

# api link
url = "https://randomfox.ca/floof/"
response = requests.get(url)

# convert to json
data = json.loads(response.text)

# image url
pic_url = data["image"]

# image url request
req_pic = requests.get(pic_url)

# regex
regex = re.search(r'https://randomfox.ca/images/(\S+.\w{2,5})' , pic_url)
regex = regex.group(1)


# http code (200 = success)
print(req_pic.status_code)

# Set the project directory
project_directory = os.path.dirname(os.path.abspath(__file__))

# download and save the image in the project directory
image_path = os.path.join(project_directory, regex)
with open(image_path, 'wb') as img:
    img.write(req_pic.content)

# show the image
img = Image.open(image_path)
img.show()
