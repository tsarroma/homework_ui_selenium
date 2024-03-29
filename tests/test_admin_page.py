import allure

from page_objects.admin_page import AdminPage

@allure.feature('Admin page')
@allure.story('Validation')
@allure.title('Validation of page elements')
def test_items_exist_admin_page(browser, base_url):
    admin_page = AdminPage(browser, base_url)
    admin_page.open_admin_page()
    admin_page._element_visibility(AdminPage.PANEL_BODY)
    admin_page._element_visibility(AdminPage.INPUT_USERNAME)
    admin_page._element_visibility(AdminPage.INPUT_PASSWORD)
    admin_page._element_visibility(AdminPage.BTN_PRIMARY)
    admin_page._element_visibility(AdminPage.FOOTER)
