import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller



chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

##driver = webdriver.Chrome()
##time.sleep(5)
##driver.get("https://mcdonalds.ipconfigure.com/#!/orchids")
##time.sleep(5)

#Lists

#server lists
server_list = []


#camera lists
cam_list = []
cam_name_list = []
cam_report = []
cam_report_len = len(cam_report)

#report
report = []
report_len = len(report)

def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: creating directory. " + directory)


def get_info_save_in_list():
    gate = 0
    cam = 0
    server = 0
    while gate == 0:
        os.system("cls")
        print("1. Server")
        print("2. Camera")
        print("3. Exit\n")
        ask = input("Enter: ")
        NSN_00 = input("Enter NSN: ")
        if ask == "1":
            server_list.append(NSN_00)
            server += 1
            os.system("cls")
        elif ask == "2":
            global cam_name
            cam_name = input("Etner camera name: \n")
            cam_list.append(NSN_00)
            cam_name_list.append(cam_name)
            cam += 1
            os.system("cls")
        elif ask == "3":
            global server_list_count
            server_list_count = server
            global cam_list_count
            cam_list_count = cam
            gate = 1
            os.system("cls")




def check_camera(NSN,cam_name):
    driver = webdriver.Chrome("")
    driver.get("https://mcdonalds.ipconfigure.com/#!/sign-in?redirectTo=%2Forchids")
    time.sleep(0.6)
    search_bar_UN = driver.find_element(By.ID, "mat-input-0")
    search_bar_UN.send_keys("WTSNOC")
    time.sleep(0.6)
    search_bar_PW = driver.find_element(By.ID, "mat-input-1")
    search_bar_PW.send_keys("W@chter01")
    login_click_3 = driver.find_element(By.XPATH, "/html/body/md-content/app-root/sign-in/div/form/mat-checkbox[1]/label").click()
    time.sleep(0.8)
    login_click = driver.find_element(By.CLASS_NAME, "sign-in-text").click()
    time.sleep(0.6)
    login_click_2 = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/greeting/div/div/mat-dialog-actions/button[2]").click()
    elemment = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "input_53")))
    search_bar_NSN = driver.find_element(By.ID, "input_53").send_keys(NSN)
    time.sleep(0.6)
    try:
        online = driver.find_element(By.XPATH, "/html/body/md-content/app-root/ng-component/div/section/ng-component/dashboard/section/md-content/md-content/md-card/md-content/md-list-item/span")
        online_status = str(online.text)
    except Exception:
        pass
    time.sleep(0.6)
    try:
        offline = driver.find_element(By.XPATH, "/html/body/md-content/app-root/ng-component/div/section/ng-component/dashboard/section/md-content/md-content/md-card[10]/md-content/md-list-item/span/md-progress-linear/div")
        offline_status = str(offline.text)
    except Exception:
        pass
    time.sleep(0.6)
    try:
        new_offline = driver.find_element(By.XPATH, "/html/body/md-content/app-root/ng-component/div/section/ng-component/dashboard/section/md-content/md-content/md-card[1]/md-content/md-list-item/span/div")
        new_offline_status = str(new_offline.text)
    except Exception:
        pass
    time.sleep(0.6)
    report.append(NSN + " " + online_status or new_offline_status or offline_status)
    search_bar_NSN = driver.find_element(By.ID, "input_53").send_keys(Keys.ENTER)
    time.sleep(0.6)
    search_bar_click = driver.find_element(By.XPATH, "/html/body/md-content/app-root/ng-component/div/section/ng-component/dashboard/section/md-content/md-content/md-card/md-content/md-list-item[1]/div[1]/span/div[1]")
    time.sleep(0.8)
    search_bar_click.click()
    time.sleep(5.0)
    try:
        search_bar_2 = driver.find_element(By.CLASS_NAME, "//*[@id='input_103']").send_keys(cam_name)
    except Exception:
        pass
    try:
        search_bar_2 = driver.find_element(By.CLASS_NAME, "md-input ng-pristine ng-valid ng-scope ng-empty ng-touched").send_keys(cam_name)
    except Exception:
        pass
    time.sleep(5.0)
    search_bar_3 = driver.find_element(By.XPATH, "/html/body/md-content/app-root/ng-component/div/section/ng-component/dashboard/section/md-content/md-content/md-card[10]/md-content/md-list-item[3]/md-content/md-content/div/camera-config/section/div/md-content/md-card[1]/md-card-content/md-input-container/md-chips/md-chips-wrap").send_keys(Keys.ENTER)
    time.sleep(1.0)
    pic_click = driver.find_element(By.XPATH, "/html/body/md-content/app-root/ng-component/div/section/ng-component/dashboard/section/md-content/md-content/md-card/md-content/md-list-item[3]/md-content/md-content/div/camera-config/section/div/md-content/md-card[2]/md-content/md-list-item/div/table/tbody/tr/td[3]/stream-preview").click()
    time.sleep(5.0)
    driver.get_screenshot_as_file("C:/Users/Ryan.Walker/Desktop/00_Home/17_Python/Digest_info/" + NSN + "_" + cam_name + ".png")
    time.sleep(3.0)
    driver.quit()      

def check_server(NSN):
    driver = webdriver.Chrome("")
    driver.get("https://mcdonalds.ipconfigure.com/#!/sign-in?redirectTo=%2Forchids")
    time.sleep(0.6)
    search_bar_UN = driver.find_element(By.ID, "mat-input-0")
    search_bar_UN.send_keys("WTSNOC")
    time.sleep(0.4)
    search_bar_PW = driver.find_element(By.ID, "mat-input-1")
    search_bar_PW.send_keys("W@chter01")
    time.sleep(0.4)
    login_click = driver.find_element(By.CLASS_NAME, "sign-in-text").click()
    time.sleep(.4)
    login_click_2 = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/greeting/div/div/mat-dialog-actions/button[2]").click()
    elemment = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "input_53")))
    search_bar_NSN = driver.find_element(By.ID, "input_53").send_keys(NSN)
    time.sleep(0.6)
    search_bar_NSN = driver.find_element(By.ID, "input_53").send_keys(Keys.ENTER)
    time.sleep(0.6)
    try:
        online = driver.find_element(By.XPATH, "/html/body/md-content/app-root/ng-component/div/section/ng-component/dashboard/section/md-content/md-content/md-card/md-content/md-list-item/span")
        online_status = str(online.text)
    except Exception:
        pass
    time.sleep(0.6)
    try:
        offline = driver.find_element(By.XPATH, "/html/body/md-content/app-root/ng-component/div/section/ng-component/dashboard/section/md-content/md-content/md-card[10]/md-content/md-list-item/span/md-progress-linear/div")
        offline_status = str(offline.text)
    except Exception:
        pass
    time.sleep(0.6)
    try:
        new_offline = driver.find_element(By.XPATH, "/html/body/md-content/app-root/ng-component/div/section/ng-component/dashboard/section/md-content/md-content/md-card[1]/md-content/md-list-item/span/div")
        new_offline_status = str(new_offline.text)
    except Exception:
        pass
    report.append(NSN + " " + online_status or new_offline_status or offline_status)
    driver.maximize_window()
    time.sleep(0.6)
    driver.get_screenshot_as_file("C:/Users/Ryan.Walker/Desktop/00_Home/17_Python/Digest_info/" + NSN + "_SERVER.png")
    time.sleep(.4)
    driver.quit()

def status(NSN):
    driver = webdriver.Chrome("")
    driver.get("https://mcdonalds.ipconfigure.com/#!/sign-in?redirectTo=%2Forchids")
    time.sleep(0.6)
    search_bar_UN = driver.find_element(By.ID, "mat-input-0")
    search_bar_UN.send_keys("WTSNOC")
    time.sleep(0.4)
    search_bar_PW = driver.find_element(By.ID, "mat-input-1")
    search_bar_PW.send_keys("W@chter01")
    time.sleep(0.4)
    login_click = driver.find_element(By.CLASS_NAME, "sign-in-text").click()
    time.sleep(.4)
    login_click_2 = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/greeting/div/div/mat-dialog-actions/button[2]").click()
    elemment = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "input_53")))
    search_bar_NSN = driver.find_element(By.ID, "input_53").send_keys(NSN)
    time.sleep(0.6)
    search_bar_NSN = driver.find_element(By.ID, "input_53").send_keys(Keys.ENTER)
    time.sleep(0.6)
    try:
        store_nsn = driver.find_element(By.XPATH, "/html/body/md-content/app-root/ng-component/div/section/ng-component/dashboard/section/md-content/md-content/md-card[8]/md-content/md-list-item/div[1]/span/div[1]/h3")
        store_nsn_status = str(store_nsn.text)
        print(store_nsn.text)
    except Exception:
        pass
    time.sleep(0.6)
    try:
        online = driver.find_element(By.XPATH, "/html/body/md-content/app-root/ng-component/div/section/ng-component/dashboard/section/md-content/md-content/md-card/md-content/md-list-item/span")
        online_status = str(online.text)
    except Exception:
        pass
    time.sleep(0.6)
    try:
        offline = driver.find_element(By.XPATH, "/html/body/md-content/app-root/ng-component/div/section/ng-component/dashboard/section/md-content/md-content/md-card[10]/md-content/md-list-item/span/md-progress-linear/div")
        offline_status = str(offline.text)
    except Exception:
        pass
    time.sleep(0.6)
    try:
        new_offline = driver.find_element(By.XPATH, "/html/body/md-content/app-root/ng-component/div/section/ng-component/dashboard/section/md-content/md-content/md-card[1]/md-content/md-list-item/span/div")
        new_offline_status = str(new_offline.text)
    except Exception:
        pass
    report.append(" " + online_status or new_offline_status or offline_status)
    
    

os.system("cls")
get_info_save_in_list()
create_folder("Digest_info")

# for i in range(server_list_count):
#     status(server_list[i])
#     print(report[i])


for i in range(server_list_count):
    check_server(server_list[i])
    print(report[i])

for i in range(cam_list_count):
    check_camera(cam_list[i],cam_name_list[i])
    print(report[i])
