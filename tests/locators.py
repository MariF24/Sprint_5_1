from selenium.webdriver.common.by import By

class StellaburgerLocators:
    #Логотип сервиса
    LOGO_FIELD = (By.CSS_SELECTOR, "[class ='active']")
    # Поле ввода имени в форме регистрации
    NAME_FIELD = (By.XPATH, "//label[(text()='Имя')]/../input")
    # Поле ввода емейла в форме регистрации и входа
    EMAIL_FIELD = (By.XPATH, "//label[(text()='Email')]/../input")
    # Поле ввода пароля в форме регистрации и входа
    PASSWORD_FIELD = (By.XPATH, "//input[contains(@type,'password')]")
    # Кнопка Личный кабинет
    ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href,'/account')]")
    # Кнопка Войти
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    # Кнопка Войти в аккаунт
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    # Кнопка Выход
    LOGOUT_BUTTON = (By.XPATH, "//button[(text()='Выход')]")
    # Кнопка Зарегистрироваться
    REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    # Ссылка Войти
    LOGIN_LINK = (By.XPATH, "//a[contains(@href,'/login')]")
    # Ссылка Зарегистрироваться
    REGISTRATION_LINK = (By.XPATH, "//a[contains(@href,'/register')]")
    # Ссылка Восстановить пароль
    PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[contains(@href,'/forgot-password')]")
    # Кнопка Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    # Переход к разделу Булки
    SECTION_BUNS = (By.XPATH, "//div[contains(@class,'pt-4 pr-10')]/span[(text()='Булки')]")
    # Переход к разделу Соусы
    SECTION_SAUCES = (By.XPATH, "//div[contains(@class,'pt-4 pr-10')]/span[(text()='Соусы')]")
    # Переход к разделу Начинки
    SECTION_FILLINGS = (By.XPATH, "//div[contains(@class,'pt-4 pr-10')]/span[(text()='Начинки')]")
    # Надпись Некорректный пароль под полем Пароль
    INCORRECT_PASSWORD_FIELD = (By.XPATH, "//p[(text()='Некорректный пароль')]")
    # Кнопка Оформить заказ
    CHECKOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    # Активный(открытый)раздел Булки, Соусы или Начинки
    SECTION_ACTIVE = (By.XPATH, "//div[contains(@class,'current')]/span")









