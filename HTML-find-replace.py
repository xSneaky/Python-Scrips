from bs4 import BeautifulSoup
import re
import os

url = "URL" #Find the URL or Keyword you want to remove from the files 
q = os.listdir("/File/")#location to the html files
for s in q:#loops though the files for the .html 
    with open("/FILE/" + s, "r", encoding="utf8", errors="ignore") as file: #set same as q
        filedata = file.read()
        soup = BeautifulSoup(filedata, "lxml")      
        for a in soup.find_all(href=re.compile(url)): # find all hrefs with the set domain from URL
            z = a.get("href") # Grabs and stores all the hrefs from the domain
            print(str(z)) #Prints the URLS
            filedata = filedata.replace(z, "") #Finds and replaces 
    try:
        with open("/out-file/" + s, "w", encoding="utf8", errors="ignore") as file: # writes the output and saves as same name on orignal
            file.write(filedata)
    except PermissionError:
        pass
