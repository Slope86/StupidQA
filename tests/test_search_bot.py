import pytest


@pytest.fixture
def search_bot():
    from argument import Argument

    Argument([])
    from api.google_scrape.search_bot import SearchBot

    return SearchBot()


def test_search_and_check(search_bot):
    # Test if search_and_check returns a valid search result
    search_bot.search_page = lambda query, pause: "200 項結果"
    search_result = search_bot.search_and_check("test query")
    assert search_result is not None
    assert isinstance(search_result, str)
    assert "200" in search_result

    # Test if search_and_check raise error if it fails to get a search result after 5 tries
    search_bot.search_page = lambda query, pause: None
    search_bot.get_proxy = lambda: None
    search_bot.user_input = lambda display: "No\n"
    with pytest.raises(Exception, match=r"Google search error"):
        search_bot.search_and_check("test query")
