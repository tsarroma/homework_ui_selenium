
page = "/laptop-notebook"


def test_driver_get(browser, base_url):
    browser.get(base_url + page)
    assert browser.title == "Laptops & Notebooks"
