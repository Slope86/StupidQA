import ast
import importlib.resources as pkg_resources
from functools import cache

import pandas as pd

import data


class Analyzer:
    def __init__(self) -> None:
        """Load Wikipedia data from data package"""
        self.article_df = pd.DataFrame()
        for i in range(4):
            with pkg_resources.path(data, f"word_article{i}.gz") as path:
                df_tmp = pd.read_csv(path, index_col="word")
                self.article_df = pd.concat([self.article_df, df_tmp])

        with pkg_resources.path(data, "word_count.gz") as path:
            self.count_df = pd.read_csv(path, index_col="word")

    @cache
    def get_article(self, *words: str) -> list:
        """Return the Wikipedia article, which contain all input words, id list.

        Args:
            words (str): Input words

        Returns:
            list: Article id list
        """
        article = set(self._get_single_word_article(words[0]))
        for w in words[1:]:
            article = article.intersection(self._get_single_word_article(w))
        return list(article)

    @cache
    def _get_single_word_article(self, word: str) -> list:
        """Return the Wikipedia article, which contain the input word, id list

        Args:
            word (str): Input word

        Returns:
            list: Article id list
        """
        try:
            output = ast.literal_eval(self.article_df.at[word, "id"])
        except KeyError:
            output = []
        return output

    @cache
    def get_count(self, word: str) -> int:
        """Return the word count in Wikipedia article

        Args:
            word (str): Input word

        Returns:
            int: Word count
        """
        df = self.count_df
        try:
            output = df.at[word, "count"]
        except KeyError:
            output = 0
        return output

    def count_article(self, *words: str) -> int:
        """Return how many article contain all input words

        Returns:
            int: Article count
        """
        return len(self.get_article(*words))
