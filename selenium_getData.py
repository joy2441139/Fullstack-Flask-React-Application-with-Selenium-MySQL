from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://www.cs.bsu.edu/homepages/dmz/cs697/langtbl.htm')
driver.maximize_window()

headers = driver.find_elements("xpath", '//table[@width="540"]//tr[1]//td')

language = driver.find_elements(
    "xpath", '//table[@width = "540"]//tr//td[1]')

level = driver.find_elements("xpath", '//table[@width = "540"]//tr//td[2]')

funcPoint = driver.find_elements("xpath", '//table[@width = "540"]//tr//td[3]')

result = []

for i in range(0, len(funcPoint)):
    temp_data = {headers[0].text: language[i].text,
                 headers[1].text: level[i].text,
                 headers[2].text: funcPoint[i].text}
    result.append(temp_data)
driver.close()

print(result)
