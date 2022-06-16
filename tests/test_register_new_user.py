from page_objects.register_page import RegisterPage

USER = {"firstname": "test", "lastname": "test", "email": "test@email.ru", "telephone": "123456", "password": "test"}

def test_register_new_user(browser, base_url):
    register_page = RegisterPage(browser, base_url)
    register_page.open_register_page()
    register_page.firstname_input(USER["firstname"])
    register_page.lastname_input(USER["lastname"])
    register_page.email_input(USER["email"])
    register_page.telephone_input(USER["telephone"])
    register_page.password_input(USER["password"])
    register_page.click_agree_checkbox()
    register_page.click_continue_btn()
