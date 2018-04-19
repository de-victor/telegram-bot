import telepot
import random
import utils
# -*- coding: utf-8 -*-

bot = None

def bot_boot():
    return telepot.Bot(utils.get_conf('token'))

def adicionar_frase(msg=''):
    tmp = msg.split(':')
    frase = str(tmp[1]).strip()
    with open('frases.txt', 'a+', encoding='utf8') as arq:
        arq.write(frase+'\n')
    return 'ne ne...decorei a frase: '+frase

def random_frase():
    frases = []
    with open('frases.txt', 'r', encoding = 'utf8') as arq:
        frases = [x for x in arq]

    return frases[random.randint(0,len(frases)-1)]

def is_adm(msg):
    return True if msg['from']['id'] in adm else False

def get_bot():
    return bot.getMe()

def gerar_log(msg):
    with open('log.txt', 'a+') as arq:
        arq.write(str(msg)+'\n')

def boot_bot():
    bot = telepot.Bot(utils.get_conf())

def start_msg():
    me = get_bot()
    #print('%s esta acordada...tu-tu-ru' %me['first_name'])
    #bot.sendMessage(group_id, 'tu-tu-ru! Olá grupo!')
    return 'Bot iniciado'

def lendo():
    bot.message_loop(processar_mensagens)

def processar_mensagens(msg):
    gerar_log(msg)
    tipo_msg, tipo_chat, chat_id = telepot.glance(msg)
    resp = pensar(msg)
    if resp != '':
        bot.sendMessage(chat_id, resp)

def pensar(chat):
    msg = str(chat['text']).lower().strip();

    if 'mayuri oi' in msg:
        return 'tu-tu-ru! Olá'
    if 'bad' in msg:
        return 'Ne Okarin....genki da yo?'
    if 'frases' in msg:
        return random_frase()
    if 'mayuri decore:' in msg:
        return adicionar_frase(msg) #if is_adm(chat) else 'Okarin Okarin....você não é o Okarin :('

    return ''