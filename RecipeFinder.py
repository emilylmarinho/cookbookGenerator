"""Get a random sweet recipe and save it."""
import time
from random import randrange
from selenium.webdriver import Chrome
from RobotUtils import waitXpath

# init webdriver
driver = Chrome()
driver.maximize_window()

# acessing recipe website
driver.get("https://www.tastemade.com.br/receitas")
waitXpath(driver, "//*[@id='react-root']/div[2]/div/div/div/div/h1/span")

# choose sweet recipe option
driver.find_element_by_xpath("//*[@id='react-root']/div[2]/div/div/ul[1]/li[1]/div").click()
waitXpath(driver, "//h1[text()='receitas de doce']")

# choose a random sweet recipe
index_recipe = randrange(1, 12)
driver.find_element_by_xpath(f"//*[@id='react-root']/div[2]/div/div/ul/li[{index_recipe}]").click()
time.sleep(3)

# get and write recipe information
recipe_info = driver.find_element_by_xpath(
    "//*[@id='react-root']/div[2]/main/div[2]/div[2]/div[1]").text

# get recipe title
recipe_title = driver.find_element_by_xpath(
    "//*[@id='react-root']/div[2]/main/div[2]/div[2]/div[1]/div[1]/div/div[1]/h1/a").text

file = open(f"cookbook/recipe-{recipe_title}.txt", "w")
file.write(str(recipe_info))
file.close()

driver.close()
