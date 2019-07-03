import json
import os.path

class Article(object):

    def __init__(self, blog_id, first_article_id, no):
        self.name = f"{blog_id}-{first_article_id}-{no}"
        self.blog = blog_id
        self.first = first_article_id
        self.no = int(no)
        self.now = 1

    @property
    def progress(self):
        return int((self.now/self.no)*100)
    
    @property
    def now_state(self):
        return json.dumps({"progress":self.progress, "link":f"{self.link}"})

    @property
    def link(self):
        return f"{self.name}.txt"
    
    @property
    def is_exist(self):
        return os.path.isfile(f"./static/{self.link}") 