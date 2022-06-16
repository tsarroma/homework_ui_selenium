from page_objects.main_page import MainPage


def test_items_exist_home_page(browser, base_url):
    main_page = MainPage(browser, base_url)
    main_page.open_main_page()
    main_page._element_visibility(MainPage.NAV)
    main_page._element_visibility(MainPage.SEARCH)
    main_page._element_visibility(MainPage.SUMMA)
    main_page._element_visibility(MainPage.NAVBAR)
    main_page._element_visibility(MainPage.CAROUSEL)
