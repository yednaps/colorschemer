import os
from selenium import webdriver
from random import randint

def getcolors(inp):
    return [hextorgb(i) for i in inp[23:].split('-')]

def hextorgb(htmlcol):
    return tuple([int(''.join(i),16) for i in zip(htmlcol[::2],htmlcol[1::2])])

def colorgrab(lis,url):
    browser = webdriver.Firefox()
    for i in range(20):
        browser.get(url)
        delay = randint(4,15)
        print("{}:\twaiting {}sec".format(i,delay))
        os.system("sleep {}".format(delay))
        lis.append(getcolors(browser.current_url))
    return lis
