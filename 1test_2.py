import unittest

models = ['480 ГБ 2.5" SATA накопитель Kingston A400', '500 ГБ 2.5" SATA накопитель Samsung 870 EVO',
              '480 ГБ 2.5" SATA накопитель ADATA SU650', '240 ГБ 2.5" SATA накопитель ADATA SU650',
              '250 ГБ 2.5" SATA накопитель Samsung 870 EVO', '256 ГБ 2.5" SATA накопитель Apacer AS350 PANTHER',
              '480 ГБ 2.5" SATA накопитель WD Green', '500 ГБ 2.5" SATA накопитель WD Red SA500']
available = [1, 1, 1, 1, 0, 1, 1, 0]
manufacturers = ['Intel', 'Samsung', 'WD']


def solve(models: list, available: list, manufacturers: list):
    repair_count = 0  # количество дисков, которые купит сисадмин
    ssds = []  # модели дисков из списка models, которые купит сисадмин

    for hdd, is_now in zip(models, available):
        if hdd.split()[5] in manufacturers and is_now == 1:
            repair_count += 1
            ssds.append(hdd)

    return ssds, repair_count  # Этот код менять не нужно

eq_str = (['500 ГБ 2.5" SATA накопитель Samsung 870 EVO', '480 ГБ 2.5" SATA накопитель WD Green'], 2)


def assert_hdd():
    assert solve(models, available, manufacturers) == eq_str


class CheckHdd(unittest.TestCase):
    def test_hdd(self):
        self.assertEqual(solve(models, available, manufacturers), eq_str, f'Должно быть {eq_str}')


if __name__ == '__main__':
    unittest.main()
    assert_hdd()
