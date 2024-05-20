import faker

EMAIL_DEFAULT = 'm89067536142@yandex.ru'
PASSWORD_DEFAULT = '123456'

def get_registration_data():
    fake = faker.Faker()
    name = fake.name()
    email = fake.email()
    return name, email
