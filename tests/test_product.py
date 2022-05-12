
page = "/test"


def test_title_name(browser, base_url):
    browser.get(base_url + page)
    assert browser.title == "Apple Cinema 30"