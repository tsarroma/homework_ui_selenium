import allure

from page_objects.product_page import ProductPage

PAGE = "/laptop-notebook"

@allure.feature('Product page')
@allure.story('Validation')
@allure.title('Validation of page elements')
def test_items_exist_product_page(browser, base_url):
    product_page = ProductPage(browser, base_url)
    product_page.open_product_page()
    product_page._element_visibility(ProductPage.LEFT_MENU)
    product_page._element_visibility(ProductPage.BTN_GRID_VIEW)
    product_page._element_visibility(ProductPage.NAV)
    product_page._element_visibility(ProductPage.SEARCH)
    product_page._element_visibility(ProductPage.SUMMA)
