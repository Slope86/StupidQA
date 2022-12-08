from typing import List

from api import google_scrape, human_assist, qa_dummy, wiki_data


def main() -> None:
    """Main function. Use command line as a sample user interface.

    User can use the following commands:
        (1) Feed QA-Bot a json file: QA-Bot will answer questions in the json file.
        (2) Ask QA-Bot a question: Let user input a question, then let QA-Bot answer it.
        (3) Test QA-Bot: QA-Bot will answer questions in the test file, and show the accuracy.
        (4) Change QA-Bot: Choose which QA-Bot to use.
        (5) Exit!: Exit the program.
    """
    # Initialize QA-Bots
    wikiBot = wiki_data.QABot()
    googleBot = google_scrape.QABot()
    humanAssist = human_assist.QABot(wikiBot, googleBot)

    # Initialize BotCenter
    bot_center = BotCenter(wikiBot, googleBot, humanAssist)

    # Main loop
    while 1:
        try:
            bot_center.start_QA()
        except KeyboardInterrupt:
            if input("\n結束程式? (y/n): ") == "y":
                print("Exit!")
                return
        except SystemExit as e:
            if e.args[0] == "exit":
                print("Exit!")
                return
            else:
                raise e
        except Exception as e:
            if e.args[0] == "Google search error":
                bot_center.choose_bot()
            else:
                raise e


class BotCenter:
    """A class to manage QA-Bots"""

    def __init__(self, *bots: qa_dummy.QADummy) -> None:
        self.qa_bots = bots
        self.choose_bot()

    def start_QA(self) -> None:
        """Let user choose which operation they want QA-Bot to do.

        Raises:
            KeyboardInterrupt: User choose to exit.
        """
        print(f'\n{f"{self.active_qa_bot} is ready":-^34}')
        print(
            "(1) Feed QA-Bot a json file\n"
            "(2) Ask QA-Bot a question\n"
            "(3) Test QA-Bot\n"
            "(4) Change QA-Bot\n"
            "(5) Exit! "
        )
        match input("請輸入要執行的操作: "):
            case "1":
                # (1) Feed QA-Bot a json file
                self.active_qa_bot.answer_from_json()
            case "2":
                # (2) Ask QA-Bot a question
                QA_list: List[str] = []
                while 1:
                    question = input("請輸入問題: ")
                    if len(question) != 0:
                        QA_list.append(question)
                        break
                while 1:
                    option = input(f"請輸入選項{len(QA_list)}. (留空enter即開始回答): ")
                    if len(option) != 0:
                        QA_list.append(option)
                    elif len(QA_list) > 1:
                        break
                    else:
                        print("請輸入至少一個選項")
                print()
                self.active_qa_bot.get_answer(QA_list, print_result=True)
            case "3":
                # (3) Test QA-Bot
                self.active_qa_bot.performance_test()
            case "4":
                # (4) Change QA-Bot
                self.choose_bot()
            case "5":
                # (5) Exit!
                raise SystemExit("exit")
            case _:
                print("未知指令! 請輸入指令編號:1~5")

    def choose_bot(self) -> None:
        """Let user choose which bot to use."""
        while 1:
            print(f'\n{"Bot Select":-^34}')
            for i, bot in enumerate(self.qa_bots):
                print(f"({i + 1}) {bot}")
            bot_id = input("請輸入要呼叫的Bot: ")
            if bot_id.isdigit():
                bot_id = int(bot_id)
                if 1 <= bot_id <= len(self.qa_bots):
                    self.active_qa_bot = self.qa_bots[bot_id - 1]
                    return
            print("未知指令! 請輸入Bot編號:1~3")


if __name__ == "__main__":  # type: ignore
    main()
