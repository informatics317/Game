# Импорт файла с персонажами
from Characters import *
# Импорт библиотеки random для генерации случайных чисел
from random import *

'''Класс босса Мордреда'''
class Boss:
    # Используется дескриптор для ограничения здоровья и маны
    hp = BoundedStat('hp', 0, 800)
    mp = BoundedStat('mp', 0, 300)

    # Устанавливается начальное состояние
    def __init__(self, name, strength, iq, damage, hp = 800, mp= 250):
        self.name = name              # Имя боса
        self.strength = strength      # Сила
        self.iq = iq                  # Интеллект
        self.damage = damage          # Урон
        self.hp = hp                  # Здоровье
        self.mp = mp                  # Мана

    # Метод получения урона боссом
    def take_damage(self, damage):
        self.hp -= damage

    # Простая атака
    def attack(self, target):
        # Урон + сила
        temp = self.damage + self.strength
        # Урон - случайное значение в диапазоне от 10 до урона с силой
        temp_random = randint(10, temp)
        # Увеличивается мана
        self.mp += 10
        # Персонаж получает урон
        target.take_damage(temp_random)
        # Логирование события
        log_event(f'Мордред атакует {target.name}, Урон: {temp_random}')

    # Атака всех персонажей
    def attack_everyone(self, target1, target2, target3):
        # Тратится мана
        self.mp -= 40
        # Урон - случайное значение от 5 до 35
        temp_random = randint(5, 35)
        # Все цели получают одинаковый урон
        target1.take_damage(temp_random)
        target2.take_damage(temp_random)
        target3.take_damage(temp_random)
        # Логирование события
        log_event(f'Мордред атакует всех, Урон: {temp_random}')

    # Декоратор, позволяющий узнать жив ли босс
    @property
    def is_alive(self):
        # Если здоровье больше 0, босс жив
        if self.hp > 0:
            return True
        # Иначе босс умер
        else:
            return False

'''Атака босса'''
def boss_attack():
    try:
        # Генерируем случайное число от 1 до 5 для выбора типа атаки
        b = randint(1, 4)
        # Если 1
        if b == 1:
            # Атакуется Артур
            Mordred.attack(Artur)
        # Если 2 и Мерлин жив
        elif b == 2 and Merlin.is_alive == 1:
            # Атакуется Мерлин
            Mordred.attack(Merlin)
        # Если 3 и Ланселот жив
        elif b == 3 and Lancelot.is_alive == 1:
            # Атакуется Ланселот
            Mordred.attack(Lancelot)
        # Если 4 и у Мордреда достаточно маны
        elif b == 4 and Mordred.mp >= 40:
            # Атакуются все
            Mordred.attack_everyone(Artur, Merlin, Lancelot)
    except:
        pass

# Создание босса
Mordred = Boss('Мордред', strength = 40, iq = 30, damage = 25, hp = 800, mp = 250)
