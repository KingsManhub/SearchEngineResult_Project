#!/usr/bin/python3


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
for j in search(Query, tld="co.in", num=10, stop=10, pause=2):
    with open (title, "a") as inside:
        inside.writelines(str(j)+"\n")
        
