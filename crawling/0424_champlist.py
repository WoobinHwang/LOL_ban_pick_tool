from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://game.naver.com/lounge/League_of_Legends/db/champion")
time.sleep(5)

# # 1번째 챔피언 이름 추출
fir= ".card_content-header__title__oJkdR"
# target : 챔피언 박스 list
target= driver.find_elements_by_css_selector(fir)

sec= ".gamedb_icon__1jSHy"
# more : 더보기 버튼
more= driver.find_element_by_css_selector(sec)

while True:
    more.click()
    time.sleep(1)
    target= driver.find_elements_by_css_selector(fir)
    if divmod(len(target), 30)[1] != 0 :
        break

names= []
for i in target:
    # print(i.text)
    # print(len(target))
    names.append(i.text)
    # break
print(names)

# 종료 단계
driver.close()
print("end...")
