from randominfo import get_first_name, get_last_name
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string


def random_char(y):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(y))


def login():
    driver.find_element_by_id("email").send_keys("hcyyk1@nottingham.admin")
    driver.find_element_by_id("password").send_keys("123456")
    driver.find_element_by_id("login").click()


def student():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'Student')))
    driver.find_element_by_id("Student").click()

    for x in range(10):
        driver.find_element_by_id("fName").send_keys(get_first_name())
        driver.find_element_by_id("lName").send_keys(get_last_name())

        programme = ['Computer Science', 'Business', 'Engineering']
        driver.find_element_by_id("programme").send_keys(random.choice(programme))

        driver.find_element_by_id("email").send_keys(random_char(7) + "@nottingham.edu.my")
        driver.find_element_by_id("password").send_keys("123456")

        driver.find_element_by_id("submit").click()


def lecturer():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'Lecturer')))
    driver.find_element_by_id("Lecturer").click()

    for x in range(10):
        driver.find_element_by_id("LfName").send_keys(get_first_name())
        driver.find_element_by_id("LlName").send_keys(get_last_name())

        select_pos = Select(driver.find_element_by_id('position'))
        position = ['Assistant Professor', 'Associate Professor', 'Professor']
        select_pos.select_by_value(random.choice(position))

        select_fac = Select(driver.find_element_by_id('faculty'))
        faculty = ['Computer Science', 'Business', 'Engineering']
        select_fac.select_by_value(random.choice(faculty))

        module_set = ['Set1', 'Set2']
        driver.find_element_by_id("set").send_keys(random.choice(module_set))

        driver.find_element_by_id("Lemail").send_keys(random_char(7) + "@nottingham.edu.my")
        driver.find_element_by_id("Lpassword").send_keys("123456")

        driver.find_element_by_id("Lsubmit").click()


def module():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'Module')))
    driver.find_element_by_id("Module").click()
    module_codes1 = ["COMP1001", "COMP1002", "COMP1003", "COMP1004"]
    module_codes2 = ["BSC1001", "BSC1002", "BSC1003", "BSC1004"]
    module_codes3 = ["ENG1001", "ENG1002", "ENG1003", "ENG1004"]
    module_names1 = ["Computer Fundamentals", "Software Engineering", "Discrete Maths", "Software Maintenance"]
    module_names2 = ["Business Communication", "Leadership", "Business Principles", "Business Writing"]
    module_names3 = ["Thermodynamics", "Natural Mechanics", "Electricity", "Computer Skills"]
    module_selector("Computer Science", module_names1, module_codes1)
    module_selector("Business", module_names2, module_codes2)
    module_selector("Engineering", module_names3, module_codes3)


def module_selector(plan, modules, module_code):
    for n in range(4):
        driver.find_element_by_id("mID").send_keys(module_code[n])

        driver.find_element_by_id("mName").send_keys(modules[n])

        driver.find_element_by_id("mPlan").send_keys(plan)

        select_type = Select(driver.find_element_by_id('moduleType'))
        module_type = ['Core', 'Elective']
        select_type.select_by_value(module_type[0])

        module_set = ['Set1', 'Set2']
        driver.find_element_by_id("mSet").send_keys(random.choice(module_set))

        driver.find_element_by_id("Add").click()


def timetable():
    date = 20210401
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'Timetable')))
    driver.find_element_by_id("Timetable").click()
    module_codes1 = ["COMP1001", "COMP1002", "COMP1003", "COMP1004"]
    module_codes2 = ["BSC1001", "BSC1002", "BSC1003", "BSC1004"]
    module_codes3 = ["ENG1001", "ENG1002", "ENG1003", "ENG1004"]
    for x in range(5):
        timetable_selector(module_codes1, date)
        timetable_selector(module_codes2, date)
        timetable_selector(module_codes3, date)
        date += 1


def timetable_selector(codes, date):
    for x in range(4):
        date_entry = str(date)
        driver.find_element_by_id("date").send_keys(date_entry)

        driver.find_element_by_id("module_id").send_keys(codes[x])

        session_type = ["Lecture", "Tutorial", "Lab"]
        driver.find_element_by_id("sessionType").send_keys(random.choice(session_type))

        driver.find_element_by_id("status").send_keys("Closed")

        if x < 2:
            time = ["0900", "1100", "1300"]
            driver.find_element_by_id("time_begin").send_keys(time[x])
            driver.find_element_by_id("time_end").send_keys(time[x + 1])
        else:
            time = ["1400", "1600", "1800"]
            driver.find_element_by_id("time_begin").send_keys(time[x - 2])
            driver.find_element_by_id("time_end").send_keys(time[x + 1 - 2])

        driver.find_element_by_id("Tsubmit").click()
        x += 1


def logout():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'logout')))
    driver.find_element_by_id("logout").click()


driver = webdriver.Edge("C:\\Users\\Yoong Joo\\Downloads\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://beam-5845a.web.app")
action = ActionChains(driver)
login()
module()
timetable()
student()
lecturer()
logout()
