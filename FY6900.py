import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO

MOKO.Driver('FY6900', 'init', '')

# Команды для set:
#   1. Команда Value. Устанавливает значение переменной Value.
MOKO.Driver('FY6900', 'set', f'WAVE = {wave}')
MOKO.Driver('FY6900', 'set', f'amplitude = {amplitude}')
MOKO.Driver('FY6900', 'set', f'frequency = {frequency}')
