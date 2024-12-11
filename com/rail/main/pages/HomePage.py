from selenium.webdriver.common.by import By


class HomePage:
    main_search_box = (By.XPATH, "//form//input[@type='text']")
    list_of_search_results = (By.XPATH, "//div[@id='listofsearchresults']/a[1]")
