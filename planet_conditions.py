#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#======================================#
#=         PLANET CONDITIONS          =#
#======================================#

"""
    Выбирает случайное количество и случайные настройки для игры
    в соответствии с весовыми коэффициентами вероятностей.
    Для игры Dome Keeper.
"""


from random import choices
from traceback import extract_stack
from typing import Any


class Settings(dict):
    def __init__(self, *kv_args: tuple[Any, int]):
        super().__init__({setting: prob for (setting, prob) in kv_args})
        (_, _, _, text) = extract_stack()[-2]
        self.defined_name = text[:text.find('=')].strip()

    @staticmethod
    def _pick_one_weighted(settings: dict[Any, int]):
        assert settings
        return choices(list(settings.keys()), list(settings.values()))[0]

    def weighted_choice(self) -> Any:
        return self._pick_one_weighted(self)

    def unique_weighted_choices(self, num_choices: int) -> set[Any]:
        if num_choices == len(self.keys()):
            return set(self.keys())
        
        results: set[Any] = set()
        choices_left: dict = self.copy()
        while len(results) < num_choices:
            result = self._pick_one_weighted(choices_left)
            choices_left.pop(result)
            results.add(result)
            
        return results

class BeatifulHeader:
    def __init__(self, title: str):
        self._title = f' {title} '

    def __repr__(self):
        return f'{self._title:=^55}'


# Количество случайных настроек
AMOUNTS = Settings(
#   Количество             Вероятность
    (0,                    4),
    (1,                    4),
    (2,                    3),
    (3,                    2),
    (4,                    1),
)


# Настройки планеты
PLANET_CONDITIONS = Settings(
#   Настройка              Вероятность
    ('Feeble enemies',     2),
    ('Long cycles',        3),
    ('Double iron',        1),
    ('Maze structure',     4),
)

# tests
def test_weighted_choice(settings: Settings, test_range: int = 10_000):
    print(BeatifulHeader(f'Testing probabilities: {settings.defined_name}'))

    stats = dict.fromkeys(settings, 0)
    for _ in range(test_range):
        choice = settings.weighted_choice()
        stats[choice] += 1
    percented_stats = {setting: f'{prob / test_range:.2%}' for setting, prob in stats.items()}
    
    sum_stats = sum(float(stat[:-1]) for stat in percented_stats.values())
    assert sum_stats > 99.99 and sum_stats < 100.01 # stats can be '100.00000000000001' or '99.99999999999999'
    del sum_stats
    
    print(f'Probability distribution test results:\n{percented_stats}\n')


#===================== MAIN =====================

def main():
    test_weighted_choice(AMOUNTS)
    test_weighted_choice(PLANET_CONDITIONS)
    
    print(BeatifulHeader('Detecting planet conditions'))
    
    num_conditions = AMOUNTS.weighted_choice()
    if num_conditions == 0:
        print('No planet conditions.\n')
        return

    print(f'Amount of planet conditions: {num_conditions}')

    result = PLANET_CONDITIONS.unique_weighted_choices(num_conditions)
        
    print('\n'.join([f'\t+ {r}' for r in result]))
    print()

#================================================


if __name__ == "__main__":
    main()