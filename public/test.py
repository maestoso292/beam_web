from randominfo import get_first_name, get_last_name
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string


def hover(element):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, element)))
    mouseover = driver.find_element_by_id(element)
    action.move_to_element(mouseover).perform()


def random_char(y):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(y))


def login():
    driver.find_element_by_id("email").send_keys("hcyyk1@nottingham.admin")
    driver.find_element_by_id("password").send_keys("123456")
    driver.find_element_by_id("login").click()


def student():
    hover('Student')
    driver.find_element_by_id("fName").send_keys(get_first_name())
    driver.find_element_by_id("lName").send_keys(get_last_name())
    driver.find_element_by_id("programme").send_keys("Computer Science")
    driver.find_element_by_id("email").send_keys(random_char(7) + "@nottingham.student")
    driver.find_element_by_id("password").send_keys("123456")
    driver.find_element_by_id("submit").click()


def lecturer():
    hover('Lecturer')
    driver.find_element_by_id("LfName").send_keys(get_first_name())
    driver.find_element_by_id("LlName").send_keys(get_last_name())
    select_pos = Select(driver.find_element_by_id('position'))
    position = ['Assistant Professor', 'Associate Professor', 'Professor']
    select_pos.select_by_value(random.choice(position))
    faculty = ['Computer Science', 'Business', 'Engineering']
    select_fac = Select(driver.find_element_by_id('faculty'))
    select_fac.select_by_value(random.choice(faculty))
    driver.find_element_by_id("Lemail").send_keys(random_char(7) + "@nottingham.lecturer")
    driver.find_element_by_id("Lpassword").send_keys("123456")
    driver.find_element_by_id("Lsubmit").click()


def module():
    hover('Module')
    driver.find_element_by_id("mID").send_keys("COMP1000")
    driver.find_element_by_id("Mname").send_keys('Software Engineering')
    driver.find_element_by_id("Msubmit").click()


def plan():
    hover('Academic Plan')
    driver.find_element_by_id("plan").send_keys("Computer Science")
    driver.find_element_by_id("Pmodule").send_keys('COMP1000')
    driver.find_element_by_id("Psubmit").click()


def record():
    hover('Attendance Record')
    driver.find_element_by_id("moduleID").send_keys("COMP1000")
    driver.find_element_by_id("session_id").send_keys('1234')
    driver.find_element_by_id("Rsubmit").click()


def timetable():
    hover('Timetable')
    select_day = Select(driver.find_element_by_id('day'))
    weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    select_day.select_by_value(random.choice(weekday))
    select_time = Select(driver.find_element_by_id('time'))
    value = ['0900', '1000', '1100', '1200', '1300', '1400', '1500', '1600', '1700']
    select_time.select_by_value(random.choice(value))
    driver.find_element_by_id("module_id").send_keys("COMP1000")
    driver.find_element_by_id("Tsubmit").click()


def lm():
    hover('lm')
    driver.find_element_by_id("lec").send_keys("1")
    driver.find_element_by_id("Lmodule").send_keys("COMP1000")
    driver.find_element_by_id("lmsubmit").click()


def logout():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'logout')))
    driver.find_element_by_id("logout").click()


driver = webdriver.Edge("C:\\Users\\Yoong Joo\\Downloads\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://beam-5845a.web.app")
action = ActionChains(driver)
login()
student()
lecturer()
module()
plan()
record()
timetable()
lm()
logout()
