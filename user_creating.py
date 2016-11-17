import xmlrpc.client

url = 'http://91.218.214.19:8071'
db = 'demoerp'
username = 'admin'
password = 'admin'

new_login = 'login'
new_username = 'Тестовый пользователь'
new_user_city = 'Киев'
new_user_street = 'Хрещатик'


def login_is_valid(login, db, uid, password):
    login = login.strip()
    if login:
        finded = models.execute_kw(db, uid, password,
                                   "res.users", 'search',
                                   [[['login', '=', login]]])
        if finded:
            print('Пользователь с таким логином уже существует')
            return False, None
        else:
            return True, login
    else:
        print('Некорретный логин')
        return False, None

# noinspection PyBroadException
try:
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
except ConnectionRefusedError:
    print('Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение')
    quit()
except:
    print('Ошибка при аутентификации')
    quit()
#получаем модели для работы
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

isvalid, login = login_is_valid(new_login, db, uid, password)
if not isvalid:
    quit()
#создаем партнера
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': new_username,
    'city': new_user_city,
    'street': new_user_street,
}])
#создаем юзера - дочернего партнеру выше (поле 'partner_id')
u_id = models.execute_kw(db, uid, password, 'res.users', 'create', [{
    'name': new_username,
    'login': login,
    'partner_id': id
}])
#заполняем поле партнера дочерним юзером
models.execute_kw(db, uid, password, 'res.partner', 'write', [[id], {
    'user_id': u_id
}])

