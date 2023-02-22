import time
from complaint_bot import CheckBot

min_dl_speed = 150.0
min_ul_speed = 150.0

new_check = CheckBot()
new_check.get_internet_speed()
time.sleep(3)

if new_check.down < min_dl_speed or new_check.up < min_ul_speed:
	new_check.complaint_in_twitter()
else:
	print("Speeds are fine!")
	new_check.close_browse()


