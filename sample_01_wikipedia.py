from Browser import Browser
from selenium.webdriver.common.by import By


class TestPage(Browser):
    def load(self):
        driver = self.browser
        driver.maximize_window()
        driver.get('https://ru.wikipedia.org/')

        self.wait_load_page(By.NAME, 'search')

        driver.find_element(By.NAME, 'search').send_keys('python')
        driver.find_element(By.ID, 'searchform').submit()
        driver.quit()


if __name__ == '__main__':
    page = TestPage()
    page.load()
