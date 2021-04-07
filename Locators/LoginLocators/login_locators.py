from selenium.webdriver.common.by import By


class LoginLocator:
    username_loc = (By.XPATH, "//*[@id='app']/div[2]/div/div[1]/div[2]/div[2]/input")
    password_loc = (By.XPATH, "//*[@id='app']/div[2]/div/div[1]/div[3]/div/input")
    login_btn_loc = (By.XPATH, '//*[@id="app"]/div[2]/div/div[1]/div[5]/button')
    error_msg_loc = (By.CLASS_NAME, "//*[@class = 'el-message el-message--success']")
