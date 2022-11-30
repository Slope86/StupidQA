# **Stupid QA**

## **簡介**

以維基百科字詞出現頻率與字詞出現文章為依據答題的簡易QA機器人

## **如何執行**

* **命令列工具( 環境需安裝有 Python 3.10 或 以上)**

  ```cmd
  git clone --depth 1 https://github.com/Slope86/StupidQA.git
  pip install -r StupidQA/requirements.txt
  python StupidQA
  ```

* **已編譯的執行檔**

  [StupidQA.exe](https://github.com/Slope86/StupidQA/releases/tag/v1.0.0)

## **如何輸入題目**

* 直接於命令列輸入題目與選項
* 以Json檔輸入，範例：

```json
[
  {
    "Question": "中華民國第14任總統，民主進步黨第16屆黨主席，同時也是台灣歷史上首位女性元首，她是:",
    "A": "蔡正元",
    "B": "蔡英文",
    "C": "洪慈庸"
  },
  {
    "Question": "明末清初著名軍事將領，曾因「引清兵入關」而被世人斥責為漢奸，他的名字叫做:",
    "A": "吳一桂",
    "B": "吳二桂",
    "C": "吳三桂"
  }
]
```
