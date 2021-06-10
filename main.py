from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 100
PROMISED_UP = 50
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
TWITTER_EMAIL = "Twitter_acc"
TWITTER_PASSWORD = "Password"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")

        sleep(5)
        self.start = self.driver.find_element_by_class_name("start-text")
        self.start.click()
        sleep(45)
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                                                    'div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                                     '/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(f"down: {self.down}")
        print(f"up: {self.up}")
        self.driver.quit()

    def tweet_at_provider(self):
        if self.up < PROMISED_UP or self.down < PROMISED_DOWN:
            self.driver.get("https://twitter.com/login")

            sleep(5)
            self.email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/'
                                                           'div/div[1]/label/div/div[2]/div/input')
            self.password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/'
                                                              'form/div/div[2]/label/div/div[2]/div/input')
            self.email.send_keys(TWITTER_EMAIL)
            self.password.send_keys(TWITTER_PASSWORD)
            self.password.send_keys(Keys.ENTER)
            sleep(5)
            self.message = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                                 'div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                                 'div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/'
                                                                 'div/div/div[2]/div/div/div/div')
            self.message.send_keys(f"Hey @Internet Provider, why is my internet speed {self.down}down/{self.up} when i pay "
                                       f"for {PROMISED_DOWN}down/{PROMISED_UP}up?")
            # tweet button
    #         self.tweet_it = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
    #                                                           'div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/'
    #                                                           'div[4]/div/div/div[2]/div[3]')
    #         self.tweet_it.send_keys(Keys.ENTER)

            sleep(3)
            self.driver.quit()
# #
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()