# import pandas as pd
#
# df = pd.DataFrame(columns = ["1","2"])
#
# # 데이터프레임을 추가해서 원래 데이터프레임에 저장하기
# df = df.append(pd.DataFrame(data= {"1": [70, 50], "2": [80, 60]}), ignore_index=True)
# df = df.append(pd.DataFrame(data= {"1": [70, 50], "2": [80, 60]}), ignore_index=True)
# #print(df)
#
# df2 = pd.DataFrame(columns = ["1","2"])
#
# # 데이터프레임을 추가해서 원래 데이터프레임에 저장하기
# df2 = df.append(pd.DataFrame(data= {"1": [70, 50], "2": [80, 60]}), ignore_index=True)
# df2 = df.append(pd.DataFrame(data= {"1": [70, 50], "2": [80, 60]}), ignore_index=True)
#
# dfs = [df , df2]
# print(dfs[0])

a = 1
print(a*10+2)


NoSuchElementException                    Traceback (most recent call last)
Input In [6], in <cell line: 9>()
      7 token = 0
      8 while True :
----> 9     count = browser.find_element_by_xpath('//*[@id="content"]/div/div[5]/div/div/div['+str(i)+']/div/table/tbody/tr/td[2]/div/div[2]/span[2]')
     10     review_count = int(count.text[3:])
     11     if review_count < review_least :

File ~\anaconda3\envs\kmsohn\lib\site-packages\selenium\webdriver\remote\webdriver.py:521, in WebDriver.find_element_by_xpath(self, xpath)
    499 """
    500 Finds an element by xpath.
    501 
   (...)
    514         element = driver.find_element_by_xpath('//div/td[1]')
    515 """
    516 warnings.warn(
    517     "find_element_by_xpath is deprecated. Please use find_element(by=By.XPATH, value=xpath) instead",
    518     DeprecationWarning,
    519     stacklevel=2,
    520 )
--> 521 return self.find_element(by=By.XPATH, value=xpath)

File ~\anaconda3\envs\kmsohn\lib\site-packages\selenium\webdriver\remote\webdriver.py:1248, in WebDriver.find_element(self, by, value)
   1245     by = By.CSS_SELECTOR
   1246     value = '[name="%s"]' % value
-> 1248 return self.execute(Command.FIND_ELEMENT, {
   1249     'using': by,
   1250     'value': value})['value']

File ~\anaconda3\envs\kmsohn\lib\site-packages\selenium\webdriver\remote\webdriver.py:425, in WebDriver.execute(self, driver_command, params)
    423 response = self.command_executor.execute(driver_command, params)
    424 if response:
--> 425     self.error_handler.check_response(response)
    426     response['value'] = self._unwrap_value(
    427         response.get('value', None))
    428     return response

File ~\anaconda3\envs\kmsohn\lib\site-packages\selenium\webdriver\remote\errorhandler.py:247, in ErrorHandler.check_response(self, response)
    245         alert_text = value['alert'].get('text')
    246     raise exception_class(message, screen, stacktrace, alert_text)  # type: ignore[call-arg]  # mypy is not smart enough here
--> 247 raise exception_class(message, screen, stacktrace)

NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id="content"]/div/div[5]/div/div/div[2]/div/table/tbody/tr/td[2]/div/div[2]/span[2]"}
  (Session info: chrome=100.0.4896.127)
Stacktrace:
Backtrace:
   Ordinal0 [0x01207413+2389011]
   Ordinal0 [0x01199F61+1941345]
   Ordinal0 [0x0108C658+837208]
   Ordinal0 [0x010B91DD+1020381]
   Ordinal0 [0x010B949B+1021083]
   Ordinal0 [0x010E6032+1204274]
   Ordinal0 [0x010D4194+1130900]
   Ordinal0 [0x010E4302+1196802]
   Ordinal0 [0x010D3F66+1130342]
   Ordinal0 [0x010AE546+976198]
   Ordinal0 [0x010AF456+980054]
   GetHandleVerifier [0x013B9632+1727522]
   GetHandleVerifier [0x0146BA4D+2457661]
   GetHandleVerifier [0x0129EB81+569713]
   GetHandleVerifier [0x0129DD76+566118]
   Ordinal0 [0x011A0B2B+1968939]
   Ordinal0 [0x011A5988+1989000]
   Ordinal0 [0x011A5A75+1989237]
   Ordinal0 [0x011AECB1+2026673]
   BaseThreadInitThunk [0x76586739+25]
   RtlGetFullPathName_UEx [0x77748E7F+1215]
   RtlGetFullPathName_UEx [0x77748E4D+1165]


# {STORE}로 csv 저장