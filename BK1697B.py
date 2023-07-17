import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO

MOKO.Driver('BK1697B', 'init', '')

# Команды для set:
#   1. Команда Value. Устанавливает значение переменной Value.
MOKO.Driver('BK1697B', 'set', 'VDC = {value}')
MOKO.Driver('BK1697B', 'set', 'IDC = {value}')
MOKO.Driver('BK1697B', 'set', 'OUTPUT = ON')
MOKO.Driver('BK1697B', 'set', 'OUTPUT = OFF')

