from page_objects.register_page import RegisterPage


def test_login(browser, base_url):
    registe_page = RegisterPage(browser, base_url)
    registe_page._element_visibility(RegisterPage.FIRSTNAME_INPUT)
    registe_page._element_visibility(RegisterPage.LASTNAME_INPUT)
    registe_page._element_visibility(RegisterPage.EMAIL_INPUT)
    registe_page._element_visibility(RegisterPage.LINK_LOGIN_PAGE)
    registe_page._element_visibility(RegisterPage.RADIO_SUBSCRIBE)
