#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from .base_ import base #-----#
from .eqmp_ import eqmp, excp #


def news(stop_page):
    base._stop_page = stop_page
    urls = base.avex_news()
    for url in urls:
        soup = base._get_soup(url)
        news_data = soup.find("span", "date").text
        news_title = soup.find("h1").text.lstrip()
        m = eqmp(news_data, news_title)
        all_links = soup.find_all("div", "item-body-hbr")
        # save(ttl, all_links)    -> to save urls
        # filter(ttl, all_links)  -> to save filtered urls
        for link in all_links:
            excp(link, 'n')
        print(m)
