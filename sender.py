text = '''
⚠️ВСЯ ПРОДУКЦИЯ СТРОГО ОРИГИНАЛ⚠️
!МИНСК!
Доброго времени суток, предлагаю вашему вниманию следующие жидкости:
 
 + НЕ ВАЖЕН ВОЗРАСТ!

 + Вкуснейшая линейка жидкостей!
 + Приятная цена!

 —HUSKY (DOUBLE ICE SALT)—
  ВКУСЫ:
   - 🧊🥝Chily Kiwi - Ледяной киви🥝🧊

 ЦЕНА: 14 РУБ!
 
 ——

 —MAD—
  ВКУСЫ:
   - 🍹Фруктовая корзина с тропических островов (Tropic Mix) 🍹
   - 🍊 Классическая газировка с натуральным вкусом спелых сочных апельсинов (Orange Soda) 🍊
   - 🧊 Ледяные плоды личи (Ice Lychee) 🧊
   - 🍬 Кислая фруктовая жвачка со вкусом лайма (Lime Bubble Gum) 🍬
   - 🍓🍑 Малиновый лимонад с добавлением нежных долек персика (Peach Raspberry Lemonade) 🍑🍓
 ЦЕНА: 12 РУБ!
 ——

'''

import vk_api
from time import sleep
from datetime import datetime
import traceback

def captcha_handler(captcha):
    """ При возникновении капчи вызывается эта функция и ей передается объект
        капчи. Через метод get_url можно получить ссылку на изображение.
        Через метод try_again можно попытаться отправить запрос с кодом капчи
    """

    captcha_code = captcha.get_url();
    key = input(f'Enter captcha code {captcha_code}')

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)

vk_session = vk_api.VkApi('+375292938793', '123321AAD', captcha_handler=captcha_handler)
vk_session.auth()

vk = vk_session.get_api()

with open('groups.txt', 'r') as g_file:
    group = g_file.read().splitlines()
image = 'photo692279577_457239039'

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
			print(datetime.today().strftime(f'%H:%M:%S | Все посты были отправлены на сервер. Бот отправляется в режим сна на 20 минут.'))
			sleep(1200)
		except Exception as err:
			print(f'Произошла ошибка:\n', traceback.format_exc())
			print(f'ID Группы:')
			print(gr)
	
if __name__ == '__main__':
    send()
