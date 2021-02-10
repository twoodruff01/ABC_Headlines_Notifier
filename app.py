from selenium import webdriver

from views.main_page import MainPage
from emails.email_setup import Email


if __name__ == '__main__':
    chrome = webdriver.Chrome(executable_path="/home/tom/Desktop/PythonLearning/chromedriver")
    chrome.get('https://www.abc.net.au/news/')
    main_page = MainPage(chrome)

    # Scrapes website and returns string containing all headlines
    headlines = "\n\n".join([str(article) for article in main_page.articles])

    chrome.quit()

    Email().send_email(headlines)
