from page_objects.product_page import ProductPage

PAGE = "/laptop-notebook"


def test_items_exist_catalog_page(browser, base_url):
    product_page = ProductPage(browser, base_url)
    product_page._element_visibility(ProductPage.LEFT_MENU)
    product_page._element_visibility(ProductPage.BTN_GRID_VIEW)
    product_page._element_visibility(ProductPage.NAV)
    product_page._element_visibility(ProductPage.SEARCH)
    product_page._element_visibility(ProductPage.SUMMA)
