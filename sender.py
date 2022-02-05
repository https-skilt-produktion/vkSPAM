text = '''
⚠️ВСЯ ПРОДУКЦИЯ СТРОГО ОРИГИНАЛ⚠️
!МИНСК!
Доброго времени суток, предлагаю вашему вниманию следующие одноразки:
	—HUSKY DOUBLE ICE SALT—
	
	+ НЕ ВАЖЕН ВОЗРАСТ!

	+ Вкуснейшая линейка жидкостей!
	+ Приятная цена!

	ВКУСЫ:
		- 🧊🥭Arctic Strike - Ледяной манго🥭🧊 
		- 🧊🍹Frosty Palm - Смесь ледяных тропических фруктов🍹🧊 
		- 🧊🥤Winter River - Ледяная Coca-Cola🥤🧊

	ЦЕНА: 13 РУБ!
	
	——
'''

import vk_api
from time import sleep
from datetime import datetime
import traceback

vk_session = vk_api.VkApi('+79211933021', '77505055')
vk_session.auth()

vk = vk_session.get_api()

with open('groups.txt', 'r') as g_file:
    group = g_file.read().splitlines()
image = 'photo699854588_457239019'

def send():
	gr = 0;
	while True:
		try:
			for g in group:
				gr = g;
				vk.wall.post(owner_id=g, message=text, attachments=image)
				vk.wall.post(owner_id=g, message=text, attachments=image)
				print(datetime.today().strftime(f'%H:%M:%S | Пост был отправлен на сервер!\n'
					f'Группа: {g}\n'
					f'Картинка: {image}'
				))
			print(datetime.today().strftime(f'%H:%M:%S | Все посты были отправлены на сервер. Бот отправляется в режим сна на 30 минут.'))
			sleep(1800)
		except Exception as err:
			print(f'Произошла ошибка:\n', traceback.format_exc()))
			print(f'ID Группы:')
			print(gr)
	
if __name__ == '__main__':
    send()