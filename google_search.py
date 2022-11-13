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
 
title = ""
for i in Query:
    if i == " ":
        i = "_"
    title = title + i
title = title+".txt"

def write_in_file(Link):
    with open (title, "a") as inside:
        inside.writelines(str(Link)+"\n")

searcher = search(Query, tld="co.in", num=num_of_result, stop=num_of_result, pause=2)

with ThreadPoolExecutor(max_workers=num_of_result) as executor:
    executor.map(write_in_file, searcher)



"""____________This section is creating and writing plaintext file___________ """
keywords = Query.split(" ")
def make_plain_text_file(title) -> None:
    with open(title, "r") as Read:
        link_line = Read.readlines()
        line_count = 0
        for line in link_line:
            with open("plaintextfile.txt", "a") as plaintext:
                plaintext.write("stripped_"+str(line_count)+title+"\n")
            r = urllib.request.urlopen(line).read()
            soup = BeautifulSoup(r, "lxml")
            with open("stripped_"+str(line_count)+title, "w") as w:
                w.write(soup.get_text())
            line_count += 1

    query_search()



def query_search():
    with open("plaintextfile.txt", "r") as plaintext:
        files = plaintext.readlines()
        for eachfile in files:
            with open(eachfile.strip(), "r") as openFile:
                content = openFile.read()
                for keyword in keywords:
                    print(keyword)
            

make_plain_text_file(title)
# query_search()