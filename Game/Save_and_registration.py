# Необходимые файлы
accounts_file = 'accounts.txt'               # Имена и пароли
save_game_file = 'game_save.txt'             # Состояние персонажа

'''Сохранение игры в файл'''
# arthur - экземпляр класса Hero
# story_progress - пройденные ветки
# user_artifacts - артефакты игрока
def save_game(arthur, story_progress, user_artifacts):
    try:
        # Открывает файл game_save.txt в режиме записи 'w'
        with open(save_game_file, 'w', encoding='utf-8') as f:
            # Сохранение характеристик Артура
            f.write(f'Здоровье: {arthur.hp}\n')
            f.write(f'Сила: {arthur.strength}\n')
            f.write(f'Интеллект: {arthur.iq}\n')
            f.write(f'Экскалибур: {int(arthur.excalibur)}\n')
            f.write(f'Священный Грааль: {int(arthur.graal)}\n')
            f.write(f'Эликсир здоровья: {arthur.health_elixir}\n')

            # Сохранение артефактов Артура
            f.write('Артефакты Артура:' + ','.join(user_artifacts) + '\n')

            # Сохранение пройденных веток
            f.write('Пройденные ветки:' + ','.join(story_progress) + '\n')


        print('✅ Вы сохранили игру!')
        # Возвращает True, если сохранение прошло успешно
        return True
    except:
        print('❌ Ошибка сохранения!')
        # Возвращает False, если сохранение не удалось
        return False

'''Загрузка игры в файл'''
def load_game():
    try:
        # Открывает файл game_save.txt в режиме чтения 'r'
        with open(save_game_file, 'r', encoding='utf-8') as f:
            # Читает все строки файла
            lines = f.readlines()

        # Переменные для загрузки данных
        arthur_specific = {}    # Характеристики Артура
        user_artifacts = []     # Артефакты игрока
        story_progress = []     # Пройденные ветки
        artifact_pool = []      # Копилка артефактов

        # Проходит по каждой строке файла
        for line in lines:
            # Удаляет пробелы в начале и в конце
            line = line.strip()
            # Если строка начинается Здоровье:
            if line.startswith('Здоровье:'):
                # Разделяет строку по двоеточию и берет значение
                arthur_specific['hp'] = int(line.split(':')[1])
            elif line.startswith('Сила:'):
                arthur_specific['strength'] = int(line.split(':')[1])
            elif line.startswith('Интеллект:'):
                arthur_specific['iq'] = int(line.split(':')[1])
            elif line.startswith('Экскалибур:'):
                arthur_specific['excalibur'] = bool(int(line.split(':')[1]))
            elif line.startswith('Священный Грааль'):
                arthur_specific['graal'] = bool(int(line.split(':')[1]))
            elif line.startswith('Эликсир здоровья:'):
                arthur_specific['health_elixir'] = int(line.split(':')[1])
            elif line.startswith('Артефакты Артура:'):
                artifacts = line.split(':')[1]
                # Если строка существует
                if artifacts:
                    # Разделяет строку по запятым
                    user_artifacts = artifacts.split(',')
            elif line.startswith('Пройденные ветки:'):
                story = line.split(':')[1]
                if story:
                    story_progress = story.split(",")

        # Возвращает все загруженные данные
        return arthur_specific, user_artifacts, story_progress, artifact_pool
    except:
        print('❌ Ошибка загрузки!')


'''Регистрация нового пользователя'''
def registrations_user():
    print('\n' + '=' * 40)
    print(' ' * 15 + 'Регистрация')
    print('=' * 40)

    # Запрашивает у пользователя данные
    username = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')

    # Проверяет, существует ли пользователь.
    # Открывает файл accounts.txt в режиме чтения 'r'
    with open(accounts_file, 'r', encoding='utf-8') as f:
        # Проходит по строкам файла
        for line in f:
            # Если строка начинается с имени и двоеточия
            if line.startswith(username + ":"):
                print('❌ Такой пользователь уже существует!')
                return None

    # Сохраняет нового пользователя.
    # Открывает файл accounts.txt в режиме добавления 'а'
    with open(accounts_file, 'a', encoding='utf-8') as f:
        # Записывает имя и пароль в формате 'имя:пароль'
        f.write(f'{username}:{password}\n')

    print(f'✅ Пользователь {username} создан!')
    return username

'''Авторизация в игре'''
def log_in_game():
    print('\n' + '=' * 40)
    print(' ' * 8 + 'Вход в игру')
    print("=" * 40)

    # Запрашивает у пользователя данные
    username = input('Имя пользователя: ')
    password = input('Пароль: ')

    try:
        # Открывает файл accounts.txt в режиме чтения 'r'
        with open(accounts_file, 'r', encoding='utf-8') as f:
            # Проходит по строкам файла
            for line in f:
                # Удаляет пробелы и делит строку по двоеточию
                parts = line.strip().split(":")
                # Если есть 2 части (логин и пароль), совпадает имя, совпадает пароль
                if len(parts) == 2 and parts[0] == username and parts[1] == password:
                    print(f'✅ Добро пожаловать в игру, {username}!')
                    return username
    except:
        pass

    print('❌ Неправильное имя или пароль!')
    return None

