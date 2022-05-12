
page = "/index.php?route=common/home"


def test_title_name(browser, base_url):
    browser.get(base_url + page)
    assert browser.title == "Your Store"