#!/usr/bin/env python3
# coding=utf-8

# __author__ = 'kira@-築城院 真鍳'

from os.path import exists


def eqmp(t, p):
    """
    Print something between mark "=" and "-"
    """
    eql = "="*45
    print(eql)
    if t:
        print('>> ', t)
    if p:
        print('>> ', p)
    print("-"*45)
    return eql + '\n'

def excp(l, flag):
    save_it = []
    """
    Try to catch Errors while parsing page source
    """
    try:
        if flag == "y":
            for jt in l:
                for it in jt.find_all("a"):
                    srt = it.get("href")
                    save_it.append(srt)
        else:
            for it in l.find_all("a"):
                srt = it.get("href")
                print(' + ', srt)
    except:
        pass
    return save_it

def filter(ttl, link):
    """
    Here you can save links what would you like
    and Think that it's more needly
    """
    _items = excp(link, "y")
    if len(_items) > 0:
        with open('filter_avex_managment_news_links.txt', 'a') as file:
            file.write('\n\n' + ttl)
            for l in _items:
                if "youtube.com" in l or "twitter.com" in l or "instagram.com" in l:
                    file.write("\n" + l)

def save(ttl, link):
    print('>>>', ttl)
    """
    Save all link in one news page
    """
    _items = excp(link, "y")
    if len(_items) > 0:
        with open('save_avex_managment_news_links.txt', 'a') as file:
            file.write('\n\n' + ttl)
            for l in _items:
                file.write("\n" + l)
