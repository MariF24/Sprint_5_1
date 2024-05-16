from selenium.webdriver.common.by import By

class StellaburgerLocators:
    #Логотип сервиса
    LOGO_FIELD = (By.CSS_SELECTOR, "[class ='active']")
    # Поле ввода имени в форме регистрации
    NAME_FIELD = (By.XPATH, "//fieldset[1]//input[contains(@name,'name')]")
    # Поле ввода емейла в форме регистрации
    EMAIL_FIELD = (By.XPATH, "//fieldset[2]//input[contains(@name,'name')]")
    # Поле ввода пароля в форме регистрации
    PASSWORD_FIELD = (By.XPATH, "//fieldset[3]//input[contains(@type,'password')]")
    # Кнопка Личный кабинет
    ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href,'/account')]")
    # Кнопка Войти
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    # Кнопка Войти в аккаунт
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    # Кнопка Выход
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    # Кнопка Зарегистрироваться
    REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    # Ссылка Войти
    LOGIN_LINK = (By.XPATH, "//a[contains(@href,'/login')]")
    # Ссылка Зарегистрироваться
    REGISTRATION_LINK = (By.XPATH, "//a[contains(@href,'/register')]")
    # Ссылка Восстановить пароль
    PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[contains(@href,'/forgot-password')]")
    # Кнопка Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//li[1]//p[contains(text(),'Конструктор')]")
    # Переход к разделу Булки
    SECTION_BUNS = (By.XPATH, "//div[1][contains(@class,'pt-4 pr-10')]//span")
    # Переход к разделу Соусы
    SECTION_SAUCES = (By.XPATH, "//div[2]//span[contains(@class,'text')]")
    # Переход к разделу Начинки
    SECTION_FILLINGS = (By.XPATH, "//div[3]//span[contains(@class,'text')]")
    # Надпись Некорректный пароль под полем Пароль
    INCORRECT_PASSWORD_FIELD = (By.XPATH, "//fieldset[3]//p[contains(text(),'Некорректный пароль')]")
    # Поле ввода емейла в форме входа
    EMAIL_FIELD_LOGIN = (By.XPATH, "//fieldset[1]//input[contains(@name,'name')]")
    # Поле ввода пароля в форме входа
    PASSWORD_FIELD_LOGIN = (By.XPATH, "//fieldset[2]//input[contains(@type,'password')]")
    # Кнопка Оформить заказ
    CHECKOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    # Вариант булки
    ITEM_BUN = (By.XPATH, "//a[1]//p[contains(text(),'R2-D3')]")
    # Вариант соуса
    ITEM_SAUCE = (By.XPATH, "//a[1]//p[contains(text(),'Spicy-X')]")
    # Вариант начинки
    ITEM_FILLING = (By.XPATH, "//a[2]//p[contains(text(),'метеорит')]")






