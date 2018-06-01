from trello import Boards
from trello import Members
import unicodedata

def norm(dataunicode):
    return unicodedata.normalize('NFKD', dataunicode).encode('ascii','ignore')

KEY = '5869b53180c8e5a19ae1e9a9d2d94916'
TOKEN = 'a6c38225f99c5e4cf6ad8c4fc8149a1af77552c0d3f54cf367089f2255d451b3'
BOARD_ID = '5af599329921029aa16425a9' #PROCESOS

membros = Members(KEY,TOKEN)
boards = Boards(KEY,TOKEN)
cards = boards.get_card(BOARD_ID)

cabecalho = 'nome_tarefa'+';'+'responsavel'+';'+'labels'+';'+'data'+';'+'feito'
print(cabecalho)
for i in cards:
    if len(i[u'idMembers'])>0:
        dono = membros.get(i[u'idMembers'][0])
        nome_dono = dono[u'username']
    else:
        nome_dono = 'Sem dono'
    lista_labels = ''
    if len(i[u'labels']) > 0:
        for j in i[u'labels']:
            lista_labels = lista_labels +'|'+ j[u'name']
    if i[u'due']:
        data = ''+i[u'due']
    else:
        data = ''
    if i[u'dueComplete']:
        feito = ''+('sim' if i[u'dueComplete'] else 'nao')
    else:
        feito = 'nao'
    tarefa = (i[u'name'])+';'+nome_dono+';'+lista_labels+';'+data+';'+feito
    print(norm(tarefa))