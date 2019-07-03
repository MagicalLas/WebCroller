from selenium import webdriver
from time import sleep
import asyncio

driver_Path = "./chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")


def get_right_nobel(article):
    if article.is_exist:
        article.now = article.no
        return
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(2)

    link = f"https://m.blog.naver.com/{article.blog}/{article.first}"
    driver.get(link)
    make_text(driver, article)
    driver.quit()


def make_text(driver, article):
    with open(f'./static/{article.name}.txt', 'w+', encoding='UTF-8') as f:
        """
        Head
        """
        f.write(get_text_from_article(driver))
        next_article(driver, 3)
        sleep(0.5)
        f.write(get_text_from_article(driver))
        """
        Middle
        """
        for i in range(article.no - 4):
            sleep(0.5)
            article.now = i
            next_article(driver)
            f.write(get_text_from_article(driver))
            print(i)
        """
        Last
        """
        for i in range(2):
            sleep(0.5)
            next_article(driver, 1 - i)
            f.write(get_text_from_article(driver))
            print(i)
        article.now = article.no


def get_text_from_article(driver):
    try:
        return driver.find_element_by_xpath('//*[@id="viewTypeSelector"]').text
    except Exception:
        driver.refresh()
        sleep(1)
        return driver.find_element_by_xpath('//*[@id="viewTypeSelector"]').text


def next_article(driver, no=1):
    category = click_category(driver)
    if not category:
        driver.refresh()
        sleep(0.5)
    result = move_other(category, no)
    if not result:
        move_other(category, no)


def click_category(driver):
    try:
        return driver.find_element_by_xpath('//*[@id="_relatedCategoryPostListFlickingPage_0"]')
    except Exception:
        return False


def move_other(click_category, no):
    try:
        click_category.find_elements_by_tag_name('li')[no].click()
        return True
    except Exception:
        return False
