import pandas as pd
# 내용 가져오기
df = pd.DataFrame(columns=[])
STORES = []
ID_list = []
BIG_STARS = []
DATES = []
REVIEWS = []
TOTAL_SCORES = []
ADDRESSES = []
IDS = range(10)
BIG_STAR = "S"
ADDRESS ="주소"
STORE = "점"
how_many_r = 0
for i in range(len(IDS)):
    try:
        how_many_r += 1
        total = len(IDS)
        ID = IDS[i]
        STAR_T = 3
        STAR_A = 3
        STAR_D = 3
        DATE = 3
        REVIEW = 3
        TOTAL_SCORE = (float(STAR_T)+float(STAR_A)+float(STAR_D))/3.0

        ID_list.append(ID)
        DATES.append(DATE)
        REVIEWS.append(REVIEW)
        TOTAL_SCORES.append(TOTAL_SCORE)
        STORES.append(STORE)
        BIG_STARS.append(BIG_STAR)
        ADDRESSES.append(ADDRESS)
        print(STORE)
    except:
        break


df['업체명'] = STORES
df['업체별'] = BIG_STARS
df['주소'] = ADDRESS
df['id'] = ID_list
df['별점'] = TOTAL_SCORES
df['작성일'] = DATES
df['리뷰'] = REVIEWS
print("크롤링 종료")
# {STORE}로 csv 저장
#df.to_csv(f'{STORE}.csv',mode='a', header=False)
print(df)
#print(f'{STORE}.csv 저장완료')
#browser.back()
#time.sleep(1)