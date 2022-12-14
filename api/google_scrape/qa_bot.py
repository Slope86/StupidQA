from typing import List

from api.google_scrape.search_bot import SearchBot
from api.qa_dummy import QADummy
from argument import Argument


class QABot(QADummy):
    def __init__(self) -> None:
        self._name = "Google QA-Bot"
        self.search_bot = SearchBot()

    def get_answer(self, QA: List[str], print_result: bool = Argument().print) -> int:
        """Answer the input question based on google search result

        Args:
            QA (List[str]): ["Question", "Option0", "Option1", "Option2", .... , "OptionN"]
            print_result(bool, optional): print the Question and Answer

        Returns:
            int: answer number, range = 1 ~ N (N: total number of option)
        """
        google_result = self.search_bot.search_and_check(query=QA[0])
        options = QA[1:]

        scores = [0 for _ in options]
        for i, option in enumerate(options):
            scores[i] = google_result.count(option)

        tmp_scores = scores.copy()
        for i, option_i in enumerate(options):
            for j, option_j in enumerate(options):
                if i == j:
                    continue
                if option_i in option_j:
                    scores[i] -= tmp_scores[j]

        answer = scores.index(max(scores)) + 1  # +1 because : A=1, B=2, C=3, ...
        if print_result:
            print(f"Q: {QA[0]}\nA: {QA[answer]}\n")
        return answer
