from bs4 import BeautifulSoup


with open("index.html","r") as f:
  doc = BeautifulSoup(f,"html.parser")

#print(doc.prettify())
# tag = doc.title.text
# print(tag)

tags = doc.find_all("p")[0]

print(tags.find_all("b"))



