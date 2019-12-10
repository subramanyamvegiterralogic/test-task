import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')
root = tree.getroot()
print(root.tag)
print(root.attrib)

# Child Names
for child in root:
    print(child.tag, child.attrib)

# All Tags Names
li = [elem.tag for elem in root.iter()]
# print(li)
print()

# print(ET.tostring(root, encoding='utf8').decode('utf8'))
for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)

for movie in root.findall("./genre/decade/movie/format[@multiple='yes']"):
    print(movie.attrib)

# for movie in root.iter('genre'):
#     print(movie.attrib)

# for movie in root.iter('decade'):
#     print(movie.attrib)
#
# for movie in root.iter('movie'):
#     print(movie.attrib)
#
# for movie in root.iter('description'):
#     print(movie.text)

