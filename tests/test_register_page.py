from page_objects.register_page import RegisterPage


def test_login(browser, base_url):
    register_page = RegisterPage(browser, base_url)
    register_page.open_register_page()
    register_page._element_visibility(RegisterPage.FIRSTNAME_INPUT)
    register_page._element_visibility(RegisterPage.LASTNAME_INPUT)
    register_page._element_visibility(RegisterPage.EMAIL_INPUT)
    register_page._element_visibility(RegisterPage.LINK_LOGIN_PAGE)
    register_page._element_visibility(RegisterPage.RADIO_SUBSCRIBE)
