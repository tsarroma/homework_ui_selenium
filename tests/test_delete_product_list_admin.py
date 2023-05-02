import allure

from page_objects.admin_page import AdminPage

LOGIN = "user"
PASSWORD = "bitnami"
PRODUCT = "product"
MODEL = "model"

@allure.feature('Admin page')
@allure.story('Products')
@allure.title('Delete product')
def test_delete_product_of_admin_page(browser, base_url):
    admin_page = AdminPage(browser, base_url)
    admin_page.open_admin_page()
    admin_page.login_admin(LOGIN, PASSWORD)
    admin_page.click_to_product_left_menu()
    admin_page.filter_test_product(PRODUCT, MODEL)
    admin_page.click_checkbox()
    admin_page.click_delete_btn()
    admin_page.switch_to_alert_accept()
    admin_page.find_alert_success()
