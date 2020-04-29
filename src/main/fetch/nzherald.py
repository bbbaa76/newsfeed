from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0

from .tools.dateTImeFormator import DateTimeFormator
from .db.query import Query
import time


class NzHerald:

    def __init__(self, driver):
        self.driver = driver

    def notPremium(self, article):
        articleClassName = article.get_attribute("class")
        if articleClassName.split(" ")[1] == "premium":
            return False
        return True

    def fetch(self):
        articles = self.driver.find_elements_by_class_name("story-hero ")
        myQuery = Query()

        for idx, article in enumerate(articles):

            if self.notPremium(article):

                organization = "NZ HERALD"
                header = article.find_element_by_css_selector("header")

                hThree = header.find_element_by_css_selector("h3")
                link = hThree.find_element_by_css_selector("a")

                newsLink = link.get_attribute("href")
                title = link.text.encode('utf-8')

                rawLinkDateTime = header.find_element_by_css_selector("div.publish.col-sm-12").text.split("\n")[0]

                try:
                    catalogue = header.find_element_by_css_selector("span.caps-header").text
                except:
                    catalogue = "Others"

                dateTimeFormat = DateTimeFormator(rawLinkDateTime)
                postDateTime = dateTimeFormat.nzHerald()

                imgLinkClass = article.find_element_by_css_selector("img")

                self.driver.execute_script("arguments[0].scrollIntoView();", imgLinkClass)

                if idx != 0:
                    time.sleep(5)
                    imageLink = article.find_element_by_css_selector("img").get_attribute("src")
                else:
                    imageLink = article.find_element_by_css_selector("img").get_attribute("src")

                print("---------------------------")
                print(title)
                # print(newsLink)
                # print(imageLink)
                # print(postDateTime)
                print(catalogue)
                print(organization)
                # print("---------------------------")

                posts = myQuery.findByTitle(title)
                if len(posts) == 0:
                    # add database
                    print("adding record to database.......")
                    myQuery.addOne(title, newsLink, imageLink, postDateTime, catalogue, organization)
                else:
                    print("record exist")

        myQuery.close()
