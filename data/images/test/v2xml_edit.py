import glob
from xml.etree import ElementTree as et

prefix = 'C:\\Users\\Gokhan GOK\\Google Drive\\YlisansBiyoloji\\01Cetoniinae\\01_Cetonia_aurata\\'

for entry in glob.glob('*.jpg'):
    print(entry)
    tree = et.parse(entry)
    print(tree.find('path').text)
    tree.find('path').text = prefix + entry
    tree.find('filename').text = entry.replace("xml","jpg")
    tree.write(entry)

