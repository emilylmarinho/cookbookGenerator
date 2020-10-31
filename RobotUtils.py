"""Robot Utilities."""
from selenium.webdriver.support.ui import WebDriverWait


def waitId(driver, id):
    """Wait for an ID."""
    WebDriverWait(driver, 60).until(
        lambda x: x.find_element_by_id(
            id
            )
    )


def waitXpath(driver, xpath):
    """Wait for a Xpath."""
    WebDriverWait(driver, 60).until(
        lambda x: x.find_element_by_xpath(
            xpath
            )
    )


def waitClass(driver, classname):
    """Wait for a Class."""
    WebDriverWait(driver, 60).until(
        lambda x: x.find_element_by_class_name(
            classname
            )
    )
