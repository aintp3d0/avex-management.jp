#!/usr/bin/env python3
# coding=utf-8

# __author__ = 'kira@-築城院 真鍳'

from .base_ import base
from .eqmp_ import eqmp, excp


def artists():
    """
    >> あかり | ACTOR/ARTIST
    >> https://twitter.com/a_akari1219
    """
    artists_ = base.avex_artist()
    for artist in artists_[6:]:
        soup = base._get_soup(artist)
        h1 = soup.find('h1')
        cat_name = soup.find('a', 'cat_name')
        title = []
        if h1:
            title.append(h1.text)
        if cat_name:
            title.append(cat_name.text)
        if not title:
            continue
        title = " | ".join(title)
        links = soup.find_all("div", "article_item artist_link")
        if links:
            m = eqmp(title, False)
            for link in links:
                excp(link, 'n')
            print(m)
