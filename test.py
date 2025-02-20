import random
from DrissionPage import ChromiumPage
from DrissionPage .func_replace import auto_replace
random_port = random.randint(9000, 30000)
cp = ChromiumPage(addr_or_opts=random_port)
auto_replace(cp.tab)
cp.get('https://1997.pro/themes/theme-yazong/assets/html/check_plus.html')
button = cp.ele('xpath://button')
cp.actions.click(button,3)
input("press enter to continue")