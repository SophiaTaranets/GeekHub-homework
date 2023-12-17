# 1. Отримайте та прочитайте дані з "https://robotsparebinindustries.com/orders.csv".
# Увага! Файл має бути прочитаний з сервера кожного разу при запускі скрипта, не зберігайте файл локально
# 2. Зайдіть на сайт "https://robotsparebinindustries.com/"
# 3. Перейдіть у вкладку "Order your robot"
# 4. Для кожного замовлення з файлу реалізуйте наступне:
#     - закрийте pop-up, якщо він з'явився. Підказка: не кожна кнопка його закриває.
#     - оберіть/заповніть відповідні поля для замовлення
#     - натисніть кнопку Preview та збережіть зображення отриманого робота.
#     Увага! Зберігати треба тільки зображення робота, а не всієї сторінки сайту.
#     - натисніть кнопку Order та збережіть номер чеку.
#     Увага! Інколи сервер тупить і видає помилку, але повторне натискання кнопки частіше всього вирішує проблему.
#     Дослідіть цей кейс.
#     - переіменуйте отримане зображення у формат <номер чеку>_robot (напр. 123456_robot.jpg).
#     Покладіть зображення в директорію output (яка має створюватися/очищатися під час запуску скрипта).
#     - замовте наступного робота (шляхом натискання відповідної кнопки)
import os
import shutil
import time
from pathlib import Path

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By


class RobotContextManager:

    DEFAULT_SERVICE_ARGS = [
        '--no-sandbox',
        '--allow-running-insecure-content',
        '--disable-web-security',
        '--disable-dev-shm-usage',
        '--disable-gpu',
        '--disable-dev-shm-usage',
        '--disable-setuid-sandbox',
        '--hide-scrollbars'
    ]

    BASE_URL = 'https://robotsparebinindustries.com/'

    def __init__(self, head=None, body=None, legs=None, address=None):
        self.driver = Chrome
        self.head = head
        self.body = body
        self.legs = legs
        self.address = address

    def __init_webdriver(self):
        # initialization webdriver
        chrome_options = ChromeOptions()
        for arg in self.DEFAULT_SERVICE_ARGS:
            chrome_options.add_argument(arg)

        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        chrome_options.add_experimental_option('prefs', {
                'profile.default_content_setting_values.notifications': 2,
                'profile.default_content_settings.popups': 0
            }
        )

        self.driver = Chrome(options=chrome_options)
        self.driver.maximize_window()
        return self.driver

    def __enter__(self):
        print('Entering the context')
        self.__init_webdriver()
        return self

    def _wait(self, selector: str, selector_type: By = By.CSS_SELECTOR, quite: bool = True):
        try:
            condition = EC.presence_of_element_located((selector_type, selector))
            element = WebDriverWait(self.driver, 5).until(condition)
            return element
        except TimeoutError:
            if quite:
                return
            raise

    def open_base_url(self):
        if not self.driver:
            self.__init_webdriver()
        self.__init_webdriver().get(self.BASE_URL)
        self._wait('a.nav-link')
        return self.driver

    def open_order_page(self):
        order_url = self.BASE_URL + '#/robot-order'
        self.driver.get(order_url)
        return self.driver

    def close_popup(self):
        popup_closer = self._wait('button.btn.btn-dark')
        popup_closer.click()

    def choose_head(self, head_element):
        head = Select(self._wait('#head'))
        head.select_by_value(head_element)
        return None

    def choose_body(self, body_element):
        body = self._wait(f'id-body-{body_element}', selector_type=By.ID)
        body.click()
        return None

    def choose_legs(self, legs_element):
        legs = self._wait('input.form-control')
        legs.send_keys(legs_element)
        return None

    def enter_address(self, address_element):
        address = self._wait('address', selector_type=By.ID)
        address.send_keys(address_element)
        return None

    def open_preview(self):
        preview = self._wait('preview', selector_type=By.ID)
        preview.click()

        return None

    def make_robot_picture(self):
        current_dir = Path.cwd()
        time.sleep(5)
        pic = self._wait('robot-preview-image', selector_type=By.ID)
        pic.screenshot(str(Path(current_dir, 'robot_pic.png')))
        return None

    def make_order(self):
        order = self._wait('order', selector_type=By.ID)
        order.click()
        return None

    def rename_robot_pic(self):
        new_filename = f'{self.get_check_number()}_robot.png'
        os.rename('robot_pic.png', new_filename)
        return new_filename

    def add_pic_to_file(self):
        robot_pictures_dirname = 'output'
        filename = self.get_check_number() + "_robot.png"
        source_filepath = os.path.abspath(filename)
        robot_pictures_directory = os.path.abspath(robot_pictures_dirname)
        shutil.move(source_filepath, robot_pictures_directory)
        return None

    def another_robot(self):
        order = self._wait('#order-another')
        order.click()
        return None

    def get_check_number(self):
        while True:
            try:
                element = self.driver.find_element(By.CLASS_NAME, 'badge.badge-success').text
            except:
                self.make_order()
            else:
                return element

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting the context')
        if self.driver:
            self.driver.close()
