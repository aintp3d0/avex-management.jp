import re
from requests import get
from bs4 import BeautifulSoup as bs


class NotTrueUrl(Exception):
    pass

class BaseProjectClass:

    def __init__(self):
        self._page = "?page={}"
        self._base_url = "https://avex-management.jp"
        self._news_url = self._base_url + "/news"
        self._movie_url = self._base_url + "/movie"
        self._artist_url = self._base_url + "/artists"
        self._last_page = 1
        self._stop_page = False

    def __print_in_block(self, fr, evn):
        msg = """
        ==========================================================
        {}:> {}
        ==========================================================
        """.format(fr, evn)
        print(msg)

    def _get_soup(self, url):
        try:
            k = get(url).status_code
            if k == 404:
                raise NotTrueUrl('Wrong url: %s' % url)
            r = get(url).text
            return bs(r, 'lxml')
        except Exception as e:
            self.__print_in_block("_get_soup", e)
            exit(0)

    def __update_last_page(self, url):
        """
        Update news page, and Break while loop with stop_page
        """
        break_in_while = False
        if self._stop_page:
            if self._last_page == self._stop_page:
                self._last_page = False
                break_in_while = True
        if not break_in_while:
            try:
                soup = self._get_soup(url)
                page = soup.find("li", "next_page")
                page_number = page.a.get("href")
                if page_number != "#":
                    self._last_page += 1
                else:
                    self._last_page = False
            except AttributeError:
                pass

    def __get_pages(self, url):
        alive_url = url + self._page.format(self._last_page)
        soup = self._get_soup(alive_url)
        self.__update_last_page(alive_url)
        return soup

    def avex_news(self):
        _news_url = []
        while self._last_page:
            soup = self.__get_pages(self._news_url)
            news_in_center = soup.find('div', 'article_list_01')
            parsed_news_url = re.findall(r'/news/+\w+', str(news_in_center))
            for news in parsed_news_url:
                _news_url.append("{}{}".format(self._base_url, news))
        return _news_url

    def avex_artist(self):
        _artist_urls = []
        soup = self._get_soup(self._artist_url)
        for artists in soup.find_all("a"):
            artist_url = artists.get("href")
            if artist_url.startswith("/artists/"):
                true_url = self._base_url + artist_url
                if true_url not in _artist_urls:
                    _artist_urls.append(true_url)
        return _artist_urls

    def avex_movie(self):
        """
        Parse only Base page
        """
        _movie_title = []
        _movie_urls = []
        soup = self.__get_pages(self._movie_url)
        for movie in soup.find_all("div", "txt"):
            try:
                title = movie.find("h3").a.text
                url = movie.find("a").get("href")
                link = self._base_url + url
                if title:
                    _movie_title.append(title)
                    _movie_urls.append(link)
            except Exception:
                pass
        return _movie_title, _movie_urls


base = BaseProjectClass()
