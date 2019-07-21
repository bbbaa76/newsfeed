from .tools.dateTImeFormator import DateTimeFormator
from .db.query import Query

class NzHerald:
    
    def __init__(self, driver):
        self.driver = driver
    
    def fetch(self):
        articles = self.driver.find_elements_by_class_name("story-hero ")
        myQuery = Query()

        for article in articles:
            organization = "NZ HERALD"
            header = article.find_element_by_css_selector("header")

            hThree = header.find_element_by_css_selector("h3")
            link = hThree.find_element_by_css_selector("a")

            newsLink = link.get_attribute("href")
            title = link.text.encode('utf-8')

            rawLinkDateTime = header.find_element_by_css_selector("div.publish.col-sm-12").text.split("\n")[0]
            
            imageLink = article.find_element_by_css_selector("img").get_attribute("src")

            try:
                catalogue = header.find_element_by_css_selector("span.caps-header").text
            except:
                catalogue = "Others"

            dateTimeFormat = DateTimeFormator(rawLinkDateTime)
            postDateTime = dateTimeFormat.nzHerald()

            # print("---------------------------")
            # print(title)
            # print(newsLink)
            # print("image link: " + imageLink)
            # print(postDateTime)
            # print(catalogue)
            # print(organization)
            # print("---------------------------")

            posts = myQuery.findByTitle(title)
            if len(posts) == 0 :
                # add database
                myQuery.addOne(title, newsLink, imageLink, postDateTime, catalogue, organization)
            

        myQuery.close()