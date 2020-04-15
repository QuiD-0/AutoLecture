from selenium import webdriver
import time

path ="C:/chromedriver.exe" #C최상위에 파일 위치
driver = webdriver.Chrome(path)
driver.get('https://ecampus.ut.ac.kr/main/MainView.dunet')#학교 홈페이지로이동
login=driver.find_element_by_name("id")
login.send_keys("My-ID")
login=driver.find_element_by_name("pass")
login.send_keys("My-PW")
driver.find_element_by_class_name("btn_login").click()#로그인
time.sleep(7)#로그인 로딩시간 대기
lec=len(driver.find_elements_by_xpath('/html/body/div[7]/div[3]/div/div[3]/div[2]/ul/li')) #총 강의 개수 확인
for j in range (1,lec+1):#강의개수만큼 반복 
    driver.get('https://ecampus.ut.ac.kr/lms/myLecture/doListView.dunet?mnid='+'201008840728')
    driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[3]/div[2]/ul/li["+str(j)+"]/div[1]/a").click();#j번째 과목 클릭
    count=len(driver.find_elements_by_xpath('//*[@id="lenAct"]/div'))#해당 과목의 강의 개수 체크 
    for i in range(1,count+1):
        checkTerm=driver.find_element_by_xpath('//*[@id="lenAct"]/div['+str(i)+']/div[3]')#수강 기간
        checkPercent=driver.find_element_by_xpath('//*[@id="lenAct"]/div['+str(i)+']/div[2]/dl/dd[1]/span[2]')#수강 진행율
        if(checkPercent.text!=" 100%"):#이미 수강완료 했다면  수강하지않는다.
            if(checkTerm.text!="[학습시작전]"):#수강 가능날짜가 되지않았으면 수강하지않는다.
                playtime=driver.find_element_by_xpath('//*[@id="lenAct"]/div['+str(i)+']/div[2]/dl/dd[1]') #들으려는 강의 총 수강시간 확인
                playtime=playtime.text.split('/')
                playtime=playtime[2].split('분')
                driver.find_elements_by_xpath('//*[@id="lenAct"]/div['+str(i)+']/div[3]/a')[0].click();
                checkPercent=checkPercent.text.split('%')#수강시간이 1%~99% 사이일 경우 시간 측정 
                play=int(playtime[0])-int(checkPercent[0])*int(playtime[0])/100  
                time.sleep(play*60+10)#sleep 1은 1초.플레이시간*60초 + 여분의 10초
                print(play+"분 실행후 종료 됩니다.")
    time.sleep(2)
driver.close()
print("학습 종료")
