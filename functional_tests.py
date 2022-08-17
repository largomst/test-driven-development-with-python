from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(
            executable_path="/opt/homebrew/bin/chromedriver"
        )

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # A 打开了网页
        self.browser.get("http://localhost:8000")

        # A 注意到浏览器标题包含 To-Do 这个词
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(by=By.TAG_NAME, value="h1").text
        self.assertIn("To-Do", header_text)

        # A 被请求输入一个待办事项
        inputbox = self.browser.find_element(by=By.ID, value="id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # A 在文本框中输入了 "Buy iPad"
        inputbox.send_keys("Buy iPad")

        # A 输入了回车
        # 页面中出现了 "1. Buy iPad"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(by=By.ID, value="id_list_table")
        rows = table.find_elements(by=By.TAG_NAME, value="tr")
        self.assertTrue(any(row.text == "1. Buy iPad" for row in rows))

        # 页面中出现一个文本框，可以输入其他待办事项
        # A 又输入了 "Use iPad"

        # 页面更新，出现了新的待办事项

        # A 希望自己输入的待办事项是一直保存下来的
        # A 记住了这个网站的 URL

        # A 再次打开 URL 发现内容还在

        self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main()
