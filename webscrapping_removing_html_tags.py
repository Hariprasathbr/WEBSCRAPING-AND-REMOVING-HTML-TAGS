import requests  
from bs4 import BeautifulSoup
import re

#Remove html tags from a string
def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

file_name = "abc.txt"
file = open(file_name,"w")

result = requests.get(input("enter url"))  
#print (result.status_code, result.headers)

scrap = BeautifulSoup(result.content ,'html.parser') 

posts = scrap.find_all("div",attrs={'class':'post'})

for post in posts:  
    postBody = post.find_all('div',attrs={'class':'media-body'})  
    for i in range(len(postBody)):    
      # prints data and time of scrapped data  
      print(postBody[i].find('a', attrs={'class':'title'}).string.strip())  
      print('Category: ',postBody[i].find('a', '').string.strip())
      print('By: ',postBody[i].find('a', attrs={'class':'author'}).string.strip())  
      print('\nDate and Time: ',postBody[i].find('span','hidden-xs').string.strip())

print("\n\n\n")
l=set(scrap)
#print(l)
l=str(l)
l_new=remove_html_tags(l)
file.write(l_new)