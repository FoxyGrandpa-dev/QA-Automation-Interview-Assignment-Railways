from selenium.webdriver.common.by import By


class LoginPage:
    email_input_field = (By.XPATH, "//input[@placeholder='email']")
    password_input_field = (By.XPATH, "//input[@placeholder='password']")
    login_submit_button = (By.XPATH, "//button[@type='submit']")

