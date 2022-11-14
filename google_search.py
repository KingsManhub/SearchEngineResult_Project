#!/usr/bin/python3
from IPython.display import HTML
import re
import urllib.request
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


"""____________This section returns the urls_______________"""
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
Query = input("Search Web Page: ")
num_of_result = int(input("Enter number of result:"))
 
link_file_name = ""
for i in Query:
    link_file_name += i.replace(" ", "_")
link_file_name +=".txt"

def file_of_links(Link):
    with open (link_file_name, "a") as inside:
        inside.writelines(str(Link)+"\n")
        
searcher = search(Query, tld="co.in", num=num_of_result, stop=num_of_result, pause=2)
    
with ThreadPoolExecutor(max_workers=num_of_result) as executor:
    executor.map(file_of_links, searcher)


"""____________This section is for ranking___________ """
keywords = Query.split(" ")

count = 0
with open(link_file_name, "r") as Read:
    for eachLink in Read:
        with open("plain_"+link_file_name, "a") as Write:
            Write.write("stripped_"+str(count)+link_file_name+"\n")

        r = urllib.request.urlopen(eachLink.strip()).read()
        soup = BeautifulSoup(r, "lxml")
        with open("stripped_"+str(count)+link_file_name, "w") as w:
            w.write(soup.get_text())
        count += 1
    
with open(link_file_name, "r") as Read:
    list_link = Read.readlines()
for i in range(0, len(list_link)):
    with open("stripped_"+str(i)+link_file_name, "r") as plain:
        whole_content = plain.read()
        summary = ""
        for j in range(len(whole_content)//1.5):
            if j == " " or i == "\n":
                j = ""
            summary += whole_content[j]
        with open("summary.txt", "a") as s:
            s.write(f"{i+1}. {list_link[i].strip()}:")
            s.write("\n\t"+summary+"...\n\n\n")