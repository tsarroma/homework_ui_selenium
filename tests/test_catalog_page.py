from page_objects.catalog_page import CatalogPage


def test_items_exist_catalog_page(browser, base_url):
    catalog_page = CatalogPage(browser, base_url)
    catalog_page._element_visibility(CatalogPage.LEFT_MENU)
    catalog_page._element_visibility(CatalogPage.BTN_GRID_VIEW)
    catalog_page._element_visibility(CatalogPage.NAV)
    catalog_page._element_visibility(CatalogPage.SEARCH)
    catalog_page._element_visibility(CatalogPage.SUMMA)
