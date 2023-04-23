from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# configure chrome options
option = Options()
option.add_experimental_option("debuggerAddress","localhost:9222")
driver = webdriver.Chrome(options=option)
# open gmail.com
driver.get('https://gmail.com')




#run it in cmd to
#"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\localhost"
