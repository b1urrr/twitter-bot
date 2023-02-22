from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

USERNAME = "Enter your twitter username"
PASSWORD = "Enter your twitter password"
CHROME_WEBDRIVER_LOCATION = "C:/Data/chromedriver.exe" # insert the path to where yours is

class CheckBot:
	def __init__(self):
		self.chrome_options = Options()
		self.chrome_options.add_experimental_option("detach", True)
		self.chrome_web_driver = CHROME_WEBDRIVER_LOCATION
		self.driver = webdriver.Chrome(executable_path=self.chrome_web_driver, chrome_options=self.chrome_options)
		self.down = 0
		self.up = 0
		self.result_link = ""

	def get_internet_speed(self):
		self.driver.get("https://www.speedtest.net/")
		accept_cookies = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
		accept_cookies.click()
		go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
		go.click()
		time.sleep(60)
		down_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]'
														'/div[3]/div[3]/div/div[3]'
												   '/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
		up_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]'
													  '/div[3]/div[3]/div/div[3]'
												 '/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
		result = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]'
													'/div[3]/div[3]/div/div[3]'
											   '/div/div/div[1]/div/div/div[2]/div[2]/a')
		self.down = float(down_speed.text)
		self.up = float(up_speed.text)
		self.result_link = f"https://www.speedtest.net/result/{result.text}"

	def complaint_in_twitter(self):
		self.driver.get("https://twitter.com/")
		time.sleep(3)
		login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a')
		login.click()
		time.sleep(7)
		# not_now = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]'
		# 											 '/div/div[2]/div/div[2]/div[2]/div[2]/div/span/span')
		# not_now.click()
		acc_login = self.driver.find_element(By.CSS_SELECTOR, 'input')
		acc_login.send_keys(USERNAME)
		acc_login.click()
		acc_login.send_keys(Keys.ENTER)
		time.sleep(3)
		pass_login = self.driver.find_element(By.NAME, "password")
		pass_login.send_keys(PASSWORD)
		pass_login.click()
		pass_login.send_keys(Keys.ENTER)
		time.sleep(5)
		write = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
		time.sleep(3)
		write.send_keys(f"Internet is too slow! Download: {self.down}, Upload: {self.up}! {self.result_link}")
		tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/'
												   'div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/'
												   'div[3]/div/span/span')
		tweet.click()

	def close_browse(self):
		self.driver.quit()










