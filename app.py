"""
Scrapes headlines from ABC main page and sends them to one email
"""
from selenium import webdriver
from emails.email_setup import Email
from views.main_page import MainPage

if __name__ == '__main__':
    chrome = webdriver.Chrome(executable_path="/home/tom/Desktop/PythonLearning/chromedriver")
    chrome.get('https://www.abc.net.au/news/')
    main_page = MainPage(chrome)

    HEADLINES = [str(article) for article in main_page.articles]
    chrome.quit()

    EMAIL_CONTENT = "\n\n".join(HEADLINES)
    EMAIL_SUBJECT = 'Latest Headlines'

    Email().send_email(EMAIL_CONTENT, EMAIL_SUBJECT)
