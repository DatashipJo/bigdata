#%%
from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup
import warnings
#%%
# 경고 무시
warnings.filterwarnings('ignore')
# 페이지 접속
browser = webdriver.Chrome()
url = "https://www.yogiyo.co.kr/mobile/#/"
browser.maximize_window()
browser.get(url)
time.sleep(3)

location = '서울특별시 성북구 삼선동5가 411 성북구청'
elem = browser.find_element_by_name("address_input")
elem.clear()
elem.send_keys(location)
time.sleep(1)
search_xpath = '''//*[@id="button_search_address"]/button[2]'''
search = browser.find_element_by_xpath(search_xpath)
browser.execute_script("arguments[0].click();", search)
time.sleep(2)
#%%
# 카테고리 선택
# 일단 치킨만!
cg = browser.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/div/div/div/ul/li[5]')
cg_title = cg.text
cg.click()
#%%
# 음식점 정렬
time.sleep(2)
browser.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/div/select').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/div/select/option[3]').click()
#%%
# 크롤링 함수
def review_crawling() :
    i = 1
    time.sleep(2)
    # store click
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/ul/li[3]/a').click()
    ADDRESS = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[6]/div[2]/p[3]/span').text # 가게 주소
    # 클린리뷰 tap
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/ul/li[2]/a').click()
    time.sleep(1)
    STORE = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div[1]/div[1]/div[1]/span').text
    # 더보기 클릭
    how_many_b = 0
    while True :
        try :
            how_many_b += 1
            try:
                btn1 = browser.find_element_by_class_name('btn-more')
                btn1.click()
            except:
                btn2 = browser.find_element_by_xpath(' /html/body/div[6]/div[2]/div[1]/div[5]/ul/li['+(how_many_b*10+2)+']/a')
                btn2.click()
            time.sleep(0.5)
            print(f"리뷰{count.text}개인 업체의 더보기 클릭 {how_many_b}번 성공!")
        # 더보기 개수제한
            if how_many_b == 3:
                break
        except:
            print("더보기 종료")
            break

    # 내용 가져오기
    df = pd.DataFrame(columns=[])
    STORES = []
    ID_list = []
    BIG_STARS = []
    DATES = []
    REVIEWS = []
    TOTAL_SCORES = []
    ADDRESSES = []
    req = browser.page_source
    soup = BeautifulSoup(req, 'html.parser')
    IDS = soup.select('span.review-id.ng-binding')
    BIG_STAR = str(soup.select(
        '#content > div.restaurant-detail.row.ng-scope > div.col-sm-8 > div.restaurant-info > div.restaurant-content > ul > li:nth-child(1) > span')[
                       0].text)[-3:]
    how_many_r = 0
    for i in range(len(IDS)):
        try:
            how_many_r += 1
            total = len(IDS)
            ID_list.append(IDS[i].text)
            STAR_T = soup.select(
                '#review > li:nth-child({}) > div:nth-child(2) > div > span.category > span:nth-child(3)'.format(
                    i + 2))[0].text
            STAR_A = soup.select(
                '#review > li:nth-child({}) > div:nth-child(2) > div > span.category > span:nth-child(6)'.format(
                    i + 2))[0].text
            STAR_D = soup.select(
                '#review > li:nth-child({}) > div:nth-child(2) > div > span.category > span:nth-child(9)'.format(
                    i + 2))[0].text
            DATES.append(soup.select('span.review-time'.format(i + 2))[0].text)
            REVIEWS.append(soup.select('#review > li:nth-child({}) > p'.format(i + 2))[0].text)
            if (STAR_D != None) & (STAR_T != None) & (STAR_A != None):
                TOTAL_SCORE = round((float(STAR_T) + float(STAR_A) + float(STAR_D)) / 3.0, 1)
                TOTAL_SCORES.append(TOTAL_SCORE)
            else:
                TOTAL_SCORE = (float(STAR_T) + float(STAR_A)) / 2.0
                TOTAL_SCORES.append(TOTAL_SCORE)
            STORES.append(STORE)
            BIG_STARS.append(BIG_STAR)
            ADDRESSES.append(ADDRESS)
            print(f'총 리뷰{total}중 {how_many_r} 크롤링 완료!!!')
            # 크롤링 개수 제한
            if how_many_r == 3:
                break
        except:
            continue

    df['업체명'] = STORES
    df['업체별'] = BIG_STARS
    df['주소'] = ADDRESS
    df['id'] = ID_list
    df['별점'] = TOTAL_SCORES
    df['작성일'] = DATES
    df['리뷰'] = REVIEWS
    print("크롤링 종료")
    # {STORE}로 csv 저장
    df.to_csv(f'{STORE}.csv', mode='a', header=False)
    print(df.head(3))
    print(f'{STORE}.csv 저장완료')
    browser.back()
    time.sleep(1)
#%%
# 최소리뷰 개수 설정
# 설정한 수 이상의 리뷰만 크롤링
time.sleep(1)
i = 1
#review_least = int(input("최소 리뷰 개수 설정 : "))
review_least = 10
#review_maximum = int(input("최대 리뷰 개수 설정 : "))
review_maximum = 100000000000
Q_how_many = int(input("몇개의 업체의 리뷰를 가져올까요?"))
how_many_s = 0
while True :
    count = browser.find_element_by_xpath('//*[@id="content"]/div/div[5]/div/div/div['+str(i)+']/div/table/tbody/tr/td[2]/div/div[2]/span[2]')
    review_count = int(count.text[3:])
    if review_count < review_least :
        break
    browser.find_element_by_xpath('//*[@id="content"]/div/div[5]/div/div/div['+str(i)+']/div').click()
    i = i+1
    if i>review_maximum:
        break
    review_crawling()
    how_many_s += 1
    if how_many_s == Q_how_many:
        break


print("크롤링을 완료하였습니다.")
browser.close()