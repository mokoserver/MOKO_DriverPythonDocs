import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO


# EN: Here are the INIT commands for the Fluke5000 driver
# RU: Тут собраны INIT команды для драйвера Fluke5000
# 1) EN: Command initialization Fluke5000 driver
#    RU: Команда инициализации драйвера Fluke5000
MOKO.Driver('Fluke5000', 'init', '')

# EN: Here are the SET commands for the Fluke5000 driver
# RU: Тут собраны SET команды для драйвера Fluke5000
# 1) EN: This command sets the VDC value in the Fluke5000 driver
#    RU: Данная команда выставляет значение VDC в драйвере Fluke5000
MOKO.Driver('Fluke5000', 'set', f'VDC = {"Value(Значение)"}')
MOKO.Driver('Fluke5000', 'set', f'VDC {"Value(Значение)"}')
# 2) EN: This command sets the VAC value in the Fluke5000 driver
#    RU: Данная команда выставляет значение VAC в драйвере Fluke5000
MOKO.Driver('Fluke5000', 'set', f'VAC = {"Value(Значение)"}')
MOKO.Driver('Fluke5000', 'set', f'VAC {"Value(Значение)"}')
# 3) EN: This command sets the R value in the Fluke5000 driver
#    RU: Данная команда выставляет значение R в драйвере Fluke5000
MOKO.Driver('Fluke5000', 'set', f'R = {"Value(Значение)"}')
MOKO.Driver('Fluke5000', 'set', f'R {"Value(Значение)"}')
# 4) EN: This command sets the IDC value in the Fluke5000 driver
#    RU: Данная команда выставляет значение IDC в драйвере Fluke5000
MOKO.Driver('Fluke5000', 'set', f'IDC = {"Value(Значение)"}')
MOKO.Driver('Fluke5000', 'set', f'IDC {"Value(Значение)"}')
# 5) EN: This command sets the IAC value in the Fluke5000 driver
#    RU: Данная команда выставляет значение IAC в драйвере Fluke5000
MOKO.Driver('Fluke5000', 'set', f'IAC = {"Value(Значение)"}')
MOKO.Driver('Fluke5000', 'set', f'IAC {"Value(Значение)"}')
# 6) EN: This command sets the output values of the driver in AUX mode
#    RU: Данная команда выставляет значения выхода драйвера в режиме AUX
MOKO.Driver('Fluke5000', 'set', 'OUT = AUX')
MOKO.Driver('Fluke5000', 'set', 'OUT AUX')
# 7) EN: This command sets the output values of the driver in NORMAL mode
#    RU: Данная команда выставляет значения выхода драйвера в режиме NORMAL
MOKO.Driver('Fluke5000', 'set', 'OUT = NORMAL')
MOKO.Driver('Fluke5000', 'set', 'OUT NORMAL')
# 8) EN: This command sets the Conn of the driver
#    RU: Данная команда выставляет значение Conn в драйвере
MOKO.Driver('Fluke5000', 'set', f'Conn = {"Value(Значение)"}')
# 9) EN: This command disables or enables the driver
#    RU: Данная команда выключает или включает работу драйвера
MOKO.Driver('Fluke5000', 'set', 'SwitchOFF = DISABLE')
MOKO.Driver('Fluke5000', 'set', 'SwitchOFF = ENABLE')
# 10) EN: This command stops the driver
#     RU: Данная команда останавливает работу драйвера
MOKO.Driver('Fluke5000', 'set', 'Stop')
# 11) EN: This command sets the Timeout of the driver
#     RU: Данная команда выставляет значение Timeout в драйвере
MOKO.Driver('Fluke5000', 'set', f'Timeout = {"Value(Значение)"}')
MOKO.Driver('Fluke5000', 'set', f'Timeout {"Value(Значение)"}')
# 12) EN: This command resets the previous driver settings
#     RU: Данная команда сбрасывает предыдущие настройки драйвера
MOKO.Driver('Fluke5000', 'set', 'Reset')
