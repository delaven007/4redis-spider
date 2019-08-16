from selenium import webdriver
import time


class JD_spider():
    def __init__(self):
        self.url='https://www.jd.com'
        self.browser=webdriver.Chrome()
    #获取页面信息--到具体商品页面
    def get_html(self):
        self.browser.get(self.url)
        #找到节点
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书籍')
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        #给商品页面加载时间
        time.sleep(3)

    def parse_html(self):
        #提取所有商品的节点li列表
        li_list=self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:

            info_list=(li.text).split('\n')
            if info_list[0].startswith('每满') or info_list[1].startswith('￥'):
                price=info_list[1]
                name=info_list[2]
                comment=info_list[3]
                shop=info_list[4]
            elif info_list[0].startswith('单件'):
                price = info_list[3]
                name = info_list[4]
                comment = info_list[5]
                shop = info_list[6]
            else:
                price = info_list[0]
                name = info_list[1]
                comment = info_list[2]
                shop = info_list[3]
            print(price,comment,shop,name)
    def main(self):
        self.get_html()
        self.parse_html()
if __name__ == '__main__':
    start=time.time()
    spider=JD_spider()
    spider.main()
    end=time.time()
    print("执行时间:",(end-start))



























