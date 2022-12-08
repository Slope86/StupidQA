import importlib.resources as pkg_resources
import json
import time
import tkinter as tk
from datetime import datetime
from os import path
from pathlib import Path
from tkinter import filedialog
from typing import List

import pandas as pd

import data
from argument import Argument
from utils.num_alpha_convert import NumAlphaConvert


class QADummy:
    def __init__(self) -> None:
        self._name = "QA-Dummy"

    def __str__(self):
        return self._name

    def get_answer(self, QA: List[str], print_result: bool = Argument().print) -> int:
        """Try to answer the input question

        Args:
            QA (List[str]): ["Question", "Option0", "Option1", "Option2", .... , "OptionN"]
            print_result(bool, optional): print the Question and Answer

        Returns:
            int: answer number, range = 1 ~ N (N: total number of option)
        """
        answer = 3  # 猜C就對了
        if print_result:
            print(f"Q:{QA[0]}\nA:{QA[answer]}\n")
        return answer

    def answer_from_json(self, file_path: str | Path = "") -> List[str]:
        """Read question and option from Json file & call function 【get_answer】 to answer it

        Args:
            file_path (str | Path, optional): Json file path.
            If not input, will open a file dialog to select.

        Returns:
            List[str]: List of answer

        Example:
            Input QA json file:
            [
                {"Question":"中華民國第14任總統，民主進步黨第16屆黨主席，同時也是台灣歷史上首位女性元首，她是:"
                , "A":"蔡正元"
                , "B":"蔡英文"
                , "C":"洪慈庸" },

                {"Question":"明末清初著名軍事將領，曾因「引清兵入關」而被世人斥責為漢奸，他的名字叫做:"
                , "A":"吳一桂"
                , "B":"吳二桂"
                , "C":"吳三桂" }
            ]

            Return answer:
                ["A","C"]
        """
        if path.exists(file_path):
            QA_df: pd.DataFrame = pd.read_json(file_path)
        else:
            print("請選取QA Json檔...")
            file_selector = tk.Tk()
            file_selector.title("File select")
            while 1:
                try:
                    file_path = filedialog.askopenfilename(
                        title="請選取QA Json檔(.json)", filetypes=(("json file", "*.json"),)
                    )
                    QA_df: pd.DataFrame = pd.read_json(file_path)
                    break
                except ValueError:
                    if input("讀取檔案失敗，是否要重新選取？(y/n)") == "y":
                        continue
                    else:
                        return []
            file_selector.destroy()

        QA_list: List[list] = [QA_tuple[1].tolist() for QA_tuple in QA_df.iterrows()]  # type: ignore

        num_answer: List[int] = [self.get_answer(single_QA) for single_QA in QA_list]
        alpha_answer: List[str] = [NumAlphaConvert(num) for num in num_answer]  # type: ignore

        log_date = datetime.now().strftime("%Y-%m-%d_%H%M")
        log_file_name = f"Answer {log_date}.json"
        with open(log_file_name, "w", encoding="utf-8") as file:
            json.dump(alpha_answer, file, ensure_ascii=False, indent=None)

        print("\nAnswer:")
        print('["' + '","'.join(alpha_answer) + '"]')
        return alpha_answer

    def performance_test(self) -> float:
        """Test the performance of 【get_answer】 function

        Returns:
            float: The correct rate of 【get_answer】 function, range = 0.0 ~ 100.0
        """
        start = time.time()
        with pkg_resources.path(data, "questions_example.json") as file_path:
            answers = self.answer_from_json(file_path)
        end = time.time()

        correct_answers = [
            "B",
            "C",
            "B",
            "B",
            "A",
            "A",
            "C",
            "A",
            "A",
            "B",
            "B",
            "B",
            "B",
            "C",
            "A",
            "A",
            "B",
            "B",
            "C",
            "B",
            "C",
            "C",
            "C",
            "A",
            "A",
        ]
        correct_count = 0
        for answer, correct_answer in zip(answers, correct_answers):
            if answer == correct_answer:
                correct_count += 1

        score = correct_count / len(correct_answers)
        print(f"Execution time: {end - start:.2f} sec\nScore: {score:.1%}")
        return score
