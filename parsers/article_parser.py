from locators.all_locators import AllLocators


class ArticleParser:

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"{self.headline}"

    @property
    def headline(self):
        locator = AllLocators.HEADLINE
        return self.parent.find_element_by_css_selector(locator).text
