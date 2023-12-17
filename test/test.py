import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
# service = Service(executable_path=r'/usr/bin/chromedriver')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("http://3.110.188.90")
print(driver.title)
try:
    # Test Case 1: Add a goal
    add_input = driver.find_element(By.XPATH, '//input[@placeholder="Enter task"]')
    add_input.send_keys('First Goal')
    add_button = driver.find_element(By.XPATH,'//button[text()="Add"]')
    add_button.click()
    # time.sleep(1)  
    # Allow time for the item to be added
    
    # Test Case 2: Add multiple goals
    todos = ['goal 1', 'goal 2', 'goal 3']
    for todo in todos:
        add_input = driver.find_element(By.XPATH, '//input[@placeholder="Enter task"]')
        add_input.send_keys(todo)
        add_button = driver.find_element(By.XPATH,'//button[text()="Add"]')
        add_button.click()
        # Allow time for the item to be added
        # time.sleep(1)  

    # # Test Case 3: Check if todos are displayed
    todo_list = driver.find_element(By.TAG_NAME,'ul')
    todo_items = todo_list.find_elements(By.TAG_NAME,'li')
    assert len(todo_items) >0, "Todos are not displayed correctly"

    print("All test cases passed!")
    
except Exception as e:
    print("Test failed:", e)

finally:
    driver.quit()