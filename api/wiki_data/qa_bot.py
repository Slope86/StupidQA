from typing import List

from api.qa_dummy import QADummy
from api.wiki_data.analyzer import Analyzer
from utils.line2words import Line2Words


class QABot(QADummy):
    def __init__(self) -> None:
        self._name = "Wiki QA-Bot"
        self._wiki = Analyzer()
        Line2Words("Initialize")

    def get_answer(self, QA: List[str]) -> int:
        """Answer the input question based on Wikipedia article

        Args:
            QA (List[str]): ["Question", "Option0", "Option1", "Option2", .... , "OptionN"]

        Returns:
            int: answer number, range = 1 ~ N (N: total number of option)
        """

        # Try get answer based on option's word frequency in Wikipedia articles
        frequency_threshold = 1
        answer = -1
        for i, option in enumerate(QA[1:], start=1):
            count = 0
            for word in Line2Words(option):
                count += self._wiki.get_count(word)

            if count >= frequency_threshold:
                if answer != -1:  # If more than one option has high word frequency,
                    break  # use next method to get answer
                answer = i
        else:
            print(f"Q: {QA[0]}\nA: {QA[answer]}\n")
            return answer

        # Get answer by compare the relation between option & question in Wikipedia articles
        answer = -1
        max_score = 0.0
        for i, option in enumerate(QA[1:], start=1):
            score = self.related_score(QA[0], option)
            # print(f'{10*score:4.2f}',end=', ')
            if score > max_score:
                answer = i
                max_score = score

        print(f"Q:{QA[0]}\nA:{QA[answer]}\n")
        return answer

    def related_score(self, line1: str, line2: str) -> float:
        """Calculate how much two input sentences related to each other (based on Wikipedia article)

        Args:
            line1: First sentence
            line2: Second sentence

        Returns:
            average_score: float, range = 0.0 ~ 2.0
        """

        # TODO: Try using TF-IDF algorithm to improve the score accuracy
        #       (https://en.wikipedia.org/wiki/Tf%E2%80%93idf)

        words1 = Line2Words(line1)
        words2 = Line2Words(line2)
        total_round = len(words1) * len(words2)
        if total_round == 0:
            return 0.0

        score = 0.0
        for word1 in words1:
            for word2 in words2:
                local_score = self._wiki.count_article(word1, word2)
                if local_score != 0:
                    score += (local_score / self._wiki.count_article(word1)) + (
                        local_score / self._wiki.count_article(word2)
                    )

        average_score = score / total_round
        return average_score
