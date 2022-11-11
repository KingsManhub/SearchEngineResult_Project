#!/usr/bin/python3
from IPython.display import HTML
import re
import urllib.request
from bs4 import BeautifulSoup


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
for j in search(Query, tld="co.in", num=num_of_result, stop=num_of_result, pause=2):
    with open (title, "a") as inside:
        inside.writelines(str(j)+"\n")



"""____________This section is creating and writing plaintext file___________ """
keywords = Query.split(" ")
print(keywords)
def make_plain_text_file(title) -> None:
    with open(title, "r") as Read:
        for line in Read:
            with open("plaintextfile.txt", "a") as plaintext:
                plaintext.write("stripped"+title+"\n")
            r = urllib.request.urlopen(line).read()
            soup = BeautifulSoup(r, "lxml")
            with open("stripped_"+title, "w") as w:
                w.write(soup.get_text())



def query_search():
    with open("plaintextfile.txt", "r") as plaintext:
        Link = plaintext.readlines()
        for eachLink in Link:
            with open(eachLink.strip(), "r") as openLink:
                content = openLink.readlines()
                for keyword in keywords:
                    count = 0
                    for keyword in content.split():
                        count += 1
                        print(f"keyword{count} found")

make_plain_text_file(title)
query_search()