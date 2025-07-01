import unittest

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]



all_list = []
for m in mentors:
    all_list.extend(m)

all_names_list = []
for mentor in all_list:
    name = mentor.split()[0]
    all_names_list.append(name)

all_names_sorted = sorted(all_names_list)

unique_names = all_names_sorted


def popular_names():
    popular = []
    qwe = {}
    rty = ''
    for name in unique_names:
        popular.append([name, unique_names.count(name)])


    for item in unique_names:
        qwe[item] = unique_names.count(item)
    asd = (sorted(qwe.items(), key=lambda item: item[1], reverse=True))


    for i in range(3):
        zxc = asd[i][0] + ': ' + str(asd[i][1]) + ' раз(а), '
        rty += zxc
    return rty[0:-2]

eq_str = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'


def assert_names():
    assert popular_names() == eq_str


class CheckPopNames(unittest.TestCase):
    def test_names(self):
        self.assertMultiLineEqual(popular_names(), eq_str, f'Должно быть {eq_str}')


if __name__ == '__main__':
    unittest.main()
    assert_names()
