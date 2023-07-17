import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO

MOKO.Driver('AgilentDMM', 'init', '')

# Команды для set:
#   1. Команда Value. Устанавливает значение переменной Value.
MOKO.Driver("AgilentDMM", "set", "range = 10.0000")
MOKO.Driver("AgilentDMM", "set", "range = 10.0000m")
MOKO.Driver("AgilentDMM", "set", "range 10.0000")
MOKO.Driver("AgilentDMM", "set", "range 10.0000m")
#   2. Команда ValueMin. Сравнивает минимальное значение со значением Value. Если Value меньше минимального, то выдается ошибка.
MOKO.Driver('AgilentDMM', 'set', 'func = VDC')
MOKO.Driver('AgilentDMM', 'set', 'func = VAC')
MOKO.Driver('AgilentDMM', 'set', 'func = R2')
MOKO.Driver('AgilentDMM', 'set', 'func = R4')
MOKO.Driver('AgilentDMM', 'set', 'func = IDC')
MOKO.Driver('AgilentDMM', 'set', 'func = IAC')
#   3. Команда ValueMax. Сравнивает максимальное значение со значением Value. Если Value больше максимального, то выдается ошибка.
MOKO.Driver('AgilentDMM', 'set', 'NPLC = 100')
MOKO.Driver('AgilentDMM', 'set', 'NPLC = MAX')
MOKO.Driver('AgilentDMM', 'set', 'NPLC = MIN')

MOKO.Driver('AgilentDMM', 'set', 'BAND = MIN')
MOKO.Driver('AgilentDMM', 'set', 'BAND = MAX')

MOKO.Driver('AgilentDMM', 'set', 'Timeout = 10000')


MOKO.Driver('AgilentDMM', 'set', 'Reset')

# Команды для get:
#   1. Команда Value. Получить значение переменной Value.
MOKO.Driver("AgilentDMM", "get", "read")

