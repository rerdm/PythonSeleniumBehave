import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By

class SeleniumCommonFunctions:

    """
    With this class it is possible to create a Selenium driver instance
    without downloading the drivers form teh internet.
    The programm will do it automatically and therefore the : webdriver_manager is used
    Be sure that you have installed it properly : pip install webdriver-manager ( install via Terminal)

    PRECONDITION:  Be sure tha the latst webdriver-manager is installed
    pip install --upgrade webdriver-manager

    You can use a Firefox ore a Chrome driver and you can set a zoom level or not.

    # Selenium Basic Functions
    driver = webdriver.Chrome()
    driver.quit()
    driver.close()
    driver.get("Website-URL")

    """

    def __init__(self, driver_name="chrome", zoom=False):

        self.driver = None
        self.driver_name = driver_name

        print(driver_name)
        print(zoom)

        if self.driver_name == "firefox" and zoom:
            self._get_firefox_webdriver_mit_zoom()

        elif self.driver_name == "firefox" and not zoom:
            self._get_firefox_webdriver_ohne_zoom()

        elif self.driver_name == "chrome" and zoom:
            self._get_chrome_webdriver_mit_zoom()

        elif self.driver_name == "chrome" and not zoom:
            self._get_firefox_webdriver_ohne_zoom()

        else:
            # Default Setup chrome without zoom level
            self._get_chrome_webdriver_ohne_zoom()

    def _get_chrome_webdriver_ohne_zoom(self):

        """
        This Method will create a chrome driver instance.
        The Zoom-Level is set to 100% (No-Zoom)
        """

        if not self.driver:
            chrome_options = Options()

            chrome_service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

            # Webdriver Window auf Maximum setzen
            self.driver.maximize_window()

        return self.driver

    def _get_chrome_webdriver_mit_zoom(self):
        """
        This Method will create a chrome driver instance.
        The Zoom-Level is set to 90%
        """
        if not self.driver:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--force-device-scale-factor=0.90")

            chrome_service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
            self.driver.maximize_window()

    def _get_firefox_webdriver_ohne_zoom(self):

        """
        This Method will create a firefox instance.
        The Zoom-Level is set to 100% (No-Zoom)
        """

        if not self.driver:
            firefox_options = FirefoxOptions()

            firefox_service = FirefoxService(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
            self.driver.maximize_window()

    def _get_firefox_webdriver_mit_zoom(self):
        """
        This Method will create a firefox instance.
        The Zoom-Level is set to 90%
        """
        if not self.driver:

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--force-device-scale-factor=0.90")

            chrome_service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
            self.driver.maximize_window()

    def open_website(self, url_name):
        self.driver.get(url_name)

    def webdriver_close(self):

        """
        closes the driver
        """
        if self.driver:
            self.driver.close()
            self.driver = None

    def webdriver_quit(self):

        """
        quit the driver
        """
        if self.driver:
            self.driver.quit()
            self.driver = None

    def get_element_text_by_xpath(self):

        element = self.driver.find_element(By.XPATH, "//span[normalize-space()='Anmelden']" )
        element_title_as_text = element.text
        return element_title_as_text

    def get_element_by_xpath(self):
        pass

    def get_element_by_id(self):
        pass

    def get_element_by_css(self):
        pass

    def button_press(self):
        pass


if __name__ == "__main__":

    driver = SeleniumCommonFunctions(driver_name="chrome", zoom=True)
    driver.open_website("https://test.id.bund.de/de")
    time.sleep(5)
    print(driver.get_element_text_by_xpath())






