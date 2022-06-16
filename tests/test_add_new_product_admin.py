from page_objects.admin_page import AdminPage

LOGIN = "user"
PASSWORD = "bitnami"
PRODUCT = "product"
TAG = "tag"
MODEL = "model"

def test_add_new_product_of_admin_page(browser, base_url):
    admin_page = AdminPage(browser, base_url)
    admin_page.open_admin_page()
    admin_page.login_admin(LOGIN, PASSWORD)
    admin_page.click_to_product_left_menu()
    admin_page.click_add_new_product_btn()
    admin_page.input_general_info_new_product(PRODUCT, TAG)
    admin_page.click_data_tab()
    admin_page.input_data_new_product(MODEL)
    admin_page.click_save_btn()
    admin_page.find_alert_success()
