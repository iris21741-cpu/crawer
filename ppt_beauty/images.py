import time

import requests
from bs4 import BeautifulSoup
import os

def download_img(url, save_path):
    print(f"正在下載圖片{url}")
    response=requests.get(url)
    with open(save_path,"wb") as file:
        file.write(response.content)
        file.flush()
        file.close()
    print("-"*30)


def main():
    url="https://www.ptt.cc/bbs/KoreaDrama/M.1757485040.A.324.html"
    headers={"Cookie":"over18=1"}
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,"html.parser")
    # print(soup.prettify())
    spans=soup.find_all("span",class_="article-meta-value")
    print(spans)
    title=spans[2].text

    dir_name=f"images/{title}"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    links=soup.find_all("a")
    allow_file_name=["jpg","png","jpeg","gif"]
    for link in links:
        href=link.get("href")
        if not href:
            continue
        file_name=href.split("/")[-1]
        extension=href.split(".")[-1].lower()
        # print(extension)
        if extension in allow_file_name:
            print(f"檔案型態:{extension}")
            print(f"url:{href}")
            time.sleep(5)
            download_img(href,f"{dir_name}/{file_name}")

        # print(href)

if __name__=="__main__":
    main()