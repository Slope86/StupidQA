import argparse
from typing import List

from api import google_scrape, human_assist, wiki_data


def main() -> None:
    """Main function. Use command line as a sample user interface.

    User can use the following commands:
        (1) Feed QA-Bot a json file: QA-Bot will answer questions in the json file.
        (2) Ask QA-Bot a question: Let user input a question, then let QA-Bot answer it.
        (3) Test QA-Bot: QA-Bot will answer questions in the test file, and show the accuracy.
        (4) Change QA-Bot: Choose which QA-Bot to use.
        (5) Exit!: Exit the program.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--delay", default=1, type=int, help="Delay between Google search requests, default = 1")
    args = parser.parse_args()

    wikiBot = wiki_data.QABot()
    googleBot = google_scrape.QABot(request_delay=args.delay)
    humanAssist = human_assist.QABot(wikiBot, googleBot)

    def choose_bot() -> wiki_data.QABot | google_scrape.QABot | human_assist.QABot:  # type: ignore
        """Let user choose which bot to use.

        Returns:
            wiki_data.QABot | google_scrape.QABot: The bot to use.
        """
        while 1:
            print(f'\n{"Bot Select":-^34}')
            print(f"(1) {wikiBot}  (2) {googleBot} (3) {humanAssist}")
            match input("請輸入要呼叫的Bot: "):
                case "1":
                    return wikiBot
                case "2":
                    return googleBot
                case "3":
                    return humanAssist
            print("未知指令! 請輸入Bot編號:1~3")

    qa_bot = choose_bot()

    while 1:
        print(f'\n{f"{qa_bot} is ready":-^34}')
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
                qa_bot.answer_from_json()

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
                qa_bot.get_answer(QA_list, print_result=True)

            case "3":
                # (3) Test QA-Bot
                qa_bot.performance_test()

            case "4":
                # (4) Change QA-Bot
                qa_bot = choose_bot()

            case "5":
                # (5) Exit!
                print("Exit!")
                break

            case _:
                print("未知指令! 請輸入指令編號:1~5")


if __name__ == "__main__":
    main()
