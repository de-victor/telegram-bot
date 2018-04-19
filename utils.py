import ast
import datetime

conf_file_name = 'conf.txt'

def load_conf():
    with open(conf_file_name, 'r+') as arq:
        return [ast.literal_eval(x) for x in arq][0]

def get_conf(type=''):
    conf = load_conf()
    if type != '':
        return conf[type] if type in conf else {}
    return conf

def save_conf(conf):
    with open(conf_file_name, 'w+') as arq:
        arq.write(str(conf))

def load_file():
    with open('log.txt', 'r+') as arq:
        return [(z['message_id'],
                 datetime.datetime.fromtimestamp(z['date']).strftime("%d/%m/%Y %H:%M:%S"),
                 z['from']['first_name'],
                 z['text']) if 'text' in z else ('', '', '')
                for z in [ast.literal_eval(x) for x in arq]]


