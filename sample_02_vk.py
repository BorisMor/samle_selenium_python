from Browser import Browser
from selenium.webdriver.common.by import By
import os


class VKPage(Browser):
    def load(self):
        driver = self.browser
        driver.maximize_window()
        driver.get('https://vk.com/')

        self.login_vk()
        self.go_to_music()
        self.show_audio()

        driver.quit()

    def login_vk(self):
        """ Входим в VK """
        vk_user = os.environ['VK_USER']
        vk_login = os.environ['VK_PASSWORD']

        driver = self.browser
        self.wait_load_page(By.ID, 'index_login_form')
        driver.find_element(By.ID, 'index_email').send_keys(vk_user)
        driver.find_element(By.ID, 'index_pass').send_keys(vk_login)
        driver.find_element(By.ID, 'index_login_form').submit()
        self.wait_load_page(By.CLASS_NAME, 'side_bar_nav')

    def go_to_music(self):
        """ Переходим в раздел с музыкой """
        driver = self.browser
        driver.find_element(By.ID, 'l_aud').click()
        self.wait_load_page(By.CLASS_NAME, '_audio_section_tab__my')
        driver.find_element(By.CLASS_NAME, '_audio_section_tab__my').find_element(By.LINK_TEXT, 'Моя музыка').click()
        self.wait_load_page(By.CLASS_NAME, 'audio_page__rows_wrap')

    def show_audio(self):
        driver = self.browser
        for audio_row in driver.find_elements(By.CLASS_NAME, 'audio_row__inner'):
            title = audio_row.find_element(By.CLASS_NAME, '_audio_row__title_inner').text
            link_performer = audio_row\
                .find_element(By.CLASS_NAME, 'audio_row__performers')\
                .find_element(By.TAG_NAME,  'a')

            if len(title):
                print(title, ',', link_performer.text, ',', link_performer.get_attribute('href'))


if __name__ == '__main__':
    page = VKPage()
    page.load()
