from selenium.webdriver.common.by import By


class RegistrationPage:
    email_input_field = (By.XPATH, "//input[@placeholder='email']")
    password_input_field = (By.XPATH, "//input[@placeholder='password']")
    firstname_input_field = (By.XPATH, "//input[@placeholder='first name']")
    lastname_input_field = (By.XPATH, "//input[@placeholder='last name']")
    email_me_news_and_updates_checkbox = (By.XPATH, "//input[@type='checkbox']")
    submit_signup_button = (By.XPATH, "//button[@type='submit']")
    successful_registration_message = (By.XPATH, "//div[contains(text(), \"We've sent an email to \")]")

