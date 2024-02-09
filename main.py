#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from scripts.news_ import news #-----#
from scripts.movie_ import movie #---#
from scripts.artists_ import artists #


def _add_limit(name, pages):
    msg = "{} in site more than {} pages, Wanna add limit-page [y/n]?:_ ".format(name, pages)
    stop_page = input(msg).lower()
    if stop_page == 'y':
        page = input("Limit-page[1...9999]?:_ ")
        print('\n')
        try:
            return int(page)
        except:
            return 3
    else:
        return False


def main():
    print("""
1: Avex-Management News
2: Avex-Management Artists
3: Avex-Management Movies   [deprecated]
    """)
    que = input("?: ")
    if que:
        if que == "1":
            limit = _add_limit('News', 1000)
            news(limit)
        elif que == "2":
            artists()
        # elif que == "3":
        #     movie()


if __name__ == "__main__":
    main()
