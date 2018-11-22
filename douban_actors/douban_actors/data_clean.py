import pandas as pd
import numpy as np
from fake_useragent import UserAgent


class get_clean():
    def __init__(self):
        self.true_url = []
        self.table = pd.read_excel("C:\\Users\dfuser.DELLCFFN202\Desktop\douban_actors\douban_actors\spiders\movie_total_3.xlsx")

    def is_trueurl(self,url):
        if "celebrity" in url:
            self.true_url.append(url)
        else:
            self.true_url.append("None")
        return self.true_url

    def mapping(self):
        list_urls = list(map(self.is_trueurl,self.table["comp_urls"]))
        result = np.array(list_urls).flatten()
        return result