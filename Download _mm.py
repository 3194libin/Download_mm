import urllib.request
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']',a)

    return  html[a:b]

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
         img_addrs.append(html[a+9,b+4])
        else:
         b = a+9
        a = html.find('img src=',b)
    for each in img_addrs:
        print("each")
def save_img(folder,img_addrs):
    pass

def Download_mm(folder = 'OOXX',pages = 10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    page_number = int(get_page(url))

    for i in range(pages):
        page_number -= i
        page_url = url + 'page-' + str(page_number) + 'comments'
        img_addrs = find_imgs(page_url)
        save_img(folder,img_addrs)

if __name__ == '__main__':
    Download_mm()


