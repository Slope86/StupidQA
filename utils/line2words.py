import time

from udicOpenData.stopwords import rmsw


def Line2Words(line: str) -> list:
    """將一行文字轉成一個一個字詞的list

    Args:
        line (str): 一行文字

    Returns:
        list: 一個一個字詞的list
    """
    return [word for word in rmsw(line) if len(word) > 1]


def __Line2Words(line: str) -> filter:
    return filter(lambda word: len(word) > 1, rmsw(line))


def __test():
    test = "測試用字串 一二三 你好嗎"
    Line2Words(test)
    __Line2Words(test)

    print("test 1 start:")
    start_time = time.time()
    for _ in range(10000):
        Line2Words(test)
    print(f"test 1 end:{time.time()-start_time}")

    print("test 2 start:")
    start_time = time.time()
    for _ in range(10000):
        __Line2Words(test)
    print(f"test 2 end:{time.time()-start_time}")


if __name__ == "__main__":
    __test()
