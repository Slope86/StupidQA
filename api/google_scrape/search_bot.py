import time

from fp.errors import FreeProxyException
from fp.fp import FreeProxy
from magic_google import MagicGoogle
from magic_google.config import LOGGER

from utils.units import Seconds


class SearchBot(MagicGoogle):
    def __init__(self, request_delay: Seconds = 1) -> None:
        LOGGER.propagate = False
        self.request_delay = request_delay
        self.proxies = self.get_proxy()

    def get_proxy(self) -> dict[str, str]:
        """Get a random proxy from https://free-proxy-list.net/

        Returns:
            dict[str, str]: A random proxy, example: {"http": "http://192.168.2.207:1080"}
        """
        proxy = None
        while 1:
            try:
                proxy = FreeProxy(google=True, rand=True).get()
                break
            except FreeProxyException:
                time.sleep(self.request_delay)

        proxy = str(proxy)
        protocol = "https" if proxy.startswith("https") else "http"
        return {protocol: proxy}

    def search_and_check(self, query: str) -> str:
        """Google search the query and check if the result is valid,
        if not, search again until the result is valid.

        Args:
            query (str): The query to search

        Returns:
            str: Google search result
        """
        search_result = ""
        search_fail_count = 0
        while 1:  # 重複搜尋直到確實收到搜尋結果 (Google搜尋結果顯示有200個)
            search_result = str(self.search_page(query=query, pause=self.request_delay))
            if "200" in search_result:
                break
            search_fail_count += 1
            if search_fail_count == 3:
                search_fail_count = 0
                self.proxies = self.get_proxy()
        return search_result
