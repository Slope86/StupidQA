from typing import List

from api.qa_dummy import QADummy
from utils import num_alpha_convert
from utils.my_thread import MyThread


class QABot(QADummy):
    def __init__(self, wiki_bot: QADummy, google_bot: QADummy) -> None:
        self._name = "Human Assist QA-Bot"
        self.wikiBot = wiki_bot
        self.googleBot = google_bot

    def get_answer(self, QA: List[str], print_result: bool = False) -> int:  # type: ignore
        """Answer the input question based on google search result

        Args:
            QA (List[str]): ["Question", "Option0", "Option1", "Option2", .... , "OptionN"]

        Returns:
            int: answer number, range = 1 ~ N (N: total number of option)
        """
        thread_wiki = MyThread(target=self.wikiBot.get_answer, args=(QA,))
        thread_google = MyThread(target=self.googleBot.get_answer, args=(QA, print_result))
        thread_wiki.start()
        thread_google.start()
        answer_wiki = thread_wiki.result()
        answer_google = thread_google.result()

        if answer_wiki == answer_google:
            return answer_wiki
        print("\a!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        answer_human = -1
        while 1:
            print(f"{QA[0]}")
            for i in range(1, len(QA)):
                print(f"{num_alpha_convert.Num2Alpha(i)}. {QA[i]}")
            print(
                f"答: {num_alpha_convert.Num2Alpha(answer_wiki)}"
                f" or {num_alpha_convert.Num2Alpha(answer_google)}"
            )
            unknown_answer = input("請輸答案: ")
            try:
                if unknown_answer.isnumeric():
                    answer_human = int(unknown_answer)
                else:
                    answer_human = num_alpha_convert.Alpha2Num(unknown_answer)
            except ValueError:
                print("請輸入選項A B C... or 1 2 3 ...\n")
                continue
            if 1 <= answer_human <= len(QA) - 1:
                print("")
                break
            print(f"無選項({num_alpha_convert.Num2Alpha(answer_human)}). 請重新輸入\n")

        return answer_human
