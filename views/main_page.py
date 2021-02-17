from parsers.article_parser import ArticleParser
from locators.all_locators import AllLocators


class MainPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def articles(self):
        article_wrapper = self.browser.find_element_by_css_selector(AllLocators.ARTICLES_CONTAINER)
        return [ArticleParser(article) for article in article_wrapper.find_elements_by_css_selector(AllLocators.ARTICLES)]
