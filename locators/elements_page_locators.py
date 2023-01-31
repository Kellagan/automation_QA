from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, 'input[id ="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id ="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id ="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id ="submit"]')

    # created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    RADIOBUTTON_YES = (By.CSS_SELECTOR, 'label[class^="custom-control-label"][for="yesRadio"]')
    RADIOBUTTON_Imp = (By.CSS_SELECTOR, 'label[class^="custom-control-label"][for="impressiveRadio"]')
    RADIOBUTTON_NO = (By.CSS_SELECTOR, 'label[class^="custom-control-label"][for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')
    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')
    # buttons


class ButtonsPageLocators:
    DOUBLE_BUTTON = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By.XPATH, "//button[. = 'Click Me'] ")
    # result
    SUCCESS_DOUBLE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    SUCCESS_RIGHT = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    SUCCESS_CLICK_ME = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')


class LinksPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    BAD_REQUEST = (By.CSS_SELECTOR, 'a[id="bad-request"]')
    CREATED_LINK = (By.CSS_SELECTOR, 'a[id="created"]')
    NO_CONTENT_LINK = (By.CSS_SELECTOR, 'a[id="no-content"]')
    MOVED_LINK = (By.CSS_SELECTOR, 'a[id="moved"]')
    UNAUTHORIZED_LINK = (By.CSS_SELECTOR, 'a[id="unauthorized"]')
    FORBIDDEN_LINK = (By.CSS_SELECTOR, 'a[id="forbidden"]')
    NOT_FOUND_LINK = (By.CSS_SELECTOR, 'a[id="id="invalid-url"]')
