import csv
import io
import urllib.request
from typing import Text

from bs4 import BeautifulSoup


def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)

def scrap(address, date, agent):
    print(f'Using agent: {agent}')
    request = urllib.request.Request(
        address,
        headers={
            'User-Agent': agent
        }
    )
    page = urllib.request.urlopen(request)
    soup = BeautifulSoup(page,"html.parser")
    leading_title_text = soup.new_tag("span")
    leading_title_text.string = "Leading Title"
    leading_description_text = soup.new_tag("span")
    leading_description_text.string = "Leading Description"
    sub_title_text = soup.new_tag("span")
    sub_title_text.string = "Sub Title"
    sub_description_text = soup.new_tag("span")
    sub_description_text.string = "Sub Description"

    main_title = []    
    title = soup.find_all("div",attrs={"class":"lead_news"})
    for i in title:
        main_title.append(leading_title_text)
        main_title.append(i.a)
        main_title.append(leading_description_text)       
        main_title.append(i.p)
    main_subTitle = []
    subtitle = soup.find_all("div",attrs={"class":"sub_news"})
    for x in subtitle:
        main_subTitle.append(sub_title_text)
        main_subTitle.append(x.a)
        main_subTitle.append(sub_description_text)
        main_subTitle.append(x.p)
    all_news = main_title+main_subTitle 
    print(all_news)  

    with io.open('output/'+date+'.txt', 'a', encoding='utf-8') as file:
        # writer = csv.writer(file)
        # here writing csv format 
        for i in all_news:
            # writer.writerow(i.get_text())            
            file.write(i.get_text())
            file.write('\n')
            # print(i.get_text(),"\n")
    if len(title) < 20:
        return False
    return True
