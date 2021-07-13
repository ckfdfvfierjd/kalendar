
import datetime, time, calendar, re, locale
from colorama import Fore, Back, Style
locale.setlocale(locale.LC_ALL, '')
#------------------------------------
localtime = time.localtime(time.time())
calendar.setfirstweekday(calendar.MONDAY)
cal = calendar.month(localtime[0],localtime[1])
#------------------------------------
parts = cal.split('\n')
cal = Fore.GREEN + '\n'.join(parts)+ Fore.LIGHTYELLOW_EX
regex = '(?<= )%s(?= )|(?<=\n)%s(?= )|(?<= )%s(?=\n)' % (localtime[2], localtime[2], localtime[2])
replace = Fore.BLACK + Back.LIGHTBLUE_EX + '%s'  %   localtime[2] + Back.RESET
newCal = re.sub(regex, replace + Fore.WHITE, cal)
rewek = re.sub('Сб Вс', Fore.RED + 'Сб Вс' + Fore.LIGHTBLACK_EX, newCal)
rewek = re.sub('Пн Вт Ср Чт Пт', Fore.BLUE + 'Пн Вт Ср Чт Пт', rewek)
res = Style.RESET_ALL
#------------------------------------
print (rewek, res)
