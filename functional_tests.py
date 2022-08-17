from selenium import webdriver

browser = webdriver.Chrome(executable_path="/opt/homebrew/bin/chromedriver")

# A 打开了网页
browser.get('http://localhost:8000')

# A 注意到浏览器标题包含 To-Do 这个词
assert 'To-Do' in browser.title, "浏览器的标题是 " + browser.title

# A 被请求输入一个待办事项

# A 在文本框中输入了 "Buy iPad"

# A 输入了回车
# 页面中出现了 "1. Buy iPad"

# 页面中出现一个文本框，可以输入其他待办事项
# A 又输入了 "Use iPad"

# 页面更新，出现了新的待办事项

# A 希望自己输入的待办事项是一直保存下来的
# A 记住了这个网站的 URL

# A 再次打开 URL 发现内容还在

# A 完成了测试

browser.quit()