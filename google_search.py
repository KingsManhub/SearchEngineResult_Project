#!/usr/bin/python3

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
query = input("Search Web Page: ")
num_of_result = int(input("Enter number of result: "))
 
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)