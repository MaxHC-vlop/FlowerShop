import telegram
from environs import Env


def tg_send_message(name, number):
    env = Env()
    env.read_env()    
    tg_token = env.str('TG_BOT_TOKEN')
    tg_chat_id = env.str("TG_CHAT_ID")

    bot = telegram.Bot(token=tg_token)

    bot.send_message(chat_id=tg_chat_id, text=f'поступила заявка на консультацию {name} {number}')
