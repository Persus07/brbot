import asyncio, random
import time 

from hangupsbot.utils import strip_quotes, text_to_segments
from hangupsbot.commands import command
from random import randint
from math import sqrt
from math import pi


@command.register
def paradoja(bot, event, *args):
    """Los [ro]bots no soportan las paradojas\n Uso: <bot> Este enunciado es mentira [frase]"""
    text = _('No pienses en ello, no pienses en ello, no pienses en ello')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def amame(bot, event, *args):
    """El bot manda amor de bot, ¿las maquinas sienten no?\n Sintaxis: bot amame"""
    text = _('te mando amor')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def saluda(bot, event, *args):
    """Saluda a la persona. \nUso: bot saluda [Persona]"""
    text = 'Hola '+' '.join(args)
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def dime(bot, event, *args):
    """Regresa una frase despues de 'dime'\n Uso: <bot> dime [frase]"""
    text = ' '.join(args)
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def dile(bot, event, *args):
    """Regresa una frase despues de 'dile'\n Uso: <bot> dime [frase]"""
    text = ' '.join(args)
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def te(bot, event, *args):
    """Creo que el tambien siente lo mismo \n Uso: <bot> te [frase]"""
    text = 'Yo tambien te '+' '.join(args)
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def dame(bot, event, *args):
    """Dame algo bot! \n Uso: <bot> dame [frase]"""
    text = 'toma '+' '.join(args)
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def malo(bot, event, *args):
    """Se disculpa por ser un mal mal bot \n Uso: <bot> malo [frase]"""
    text = _('Lo siento mucho :\'c')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def mala(bot, event, *args):
    """Se disculpa por ser una mala bot ;) \n Uso: <bot> mala [frase]"""
    text = _('Lo siento mucho :\'c')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def gracias(bot, event, *args):
    """Estoy para servirte, no hay necesidad de agradecer\n Uso: <bot> gracias"""
    text = _('Un placer')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def bueno(bot, event, *args):
    """Buen bot !\nUso: <bot> gracias"""
    text = _('Gracias, me esfuerzo')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def buen(bot, event, que, *args):
    """Que bueno es el bot\b <bot> buen (bot)"""
    if strip_quotes(que)=="bot":
        text = _('Gracias, me esfuerzo')
    else:
        text = _('QUE?')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def emoticon(bot, event, emon, *args):
    """
    😪 bozteso 
    😐 serio 
    😊 contento
    😀 sonriente
    😂 lol
    😃 feliz
    😅 preocupado
    😇 angel
    😠 enojado
    😬 furioso
    😢 lagrima
    😴 sueño
    😮 sorpresa
    😥 angustiado
    😟 jum
    😞 triste
    😎 cool
    😘 beso
    😗 .3.
    😒 Sospechoso
    😶 nada
    😭 llanto
    😏 yeah
    🙋saludo
    🙅nope
    🙌festejo
    🍪 galleta
    """
    arg = ' '.join(args)
    text= '???'

    if emon == 'bozteso':
        text= '😪'
    elif emon == 'serio':
        text= '😐'
    elif emon == 'contento':
        text= '😊'
    elif emon == 'sonriente':
        text= '😀'
    elif emon == 'lol':
        text= '😂'
    elif emon == 'feliz':
        text= '😃'
    elif emon == 'preocupado':
        text= '😅'
    elif emon == 'angel':
        text= '😇'
    elif emon == 'furioso':
        text= '😬'
    elif emon == 'lagrima':
        text= '😢'
    elif emon == 'sueño':
        text= '😴'
    elif emon == 'sorpresa':
        text= '😮'
    elif emon == 'angustiado':
        text= '😥'
    elif emon == 'jum':
        text= '😟'
    elif emon == 'triste':
        text= '😞'
    elif emon == 'cool':
        text= '😎'
    elif emon == 'beso':
        text= '😘'
    elif emon == '.3.':
        text= '😗'
    elif emon == 'Sospechoso':
        text= '😒'
    elif emon == 'nada':
        text= '😶'
    elif emon == 'llanto':
        text= '😭'
    elif emon == 'yeah':
        text= '😏'
    elif emon == 'saludo':
        text= '🙋'
    elif emon == 'nope':
        text= '🙅'
    elif emon == 'festejo':
        text= '🙌'
    elif emon == 'galleta':
        text= '🍪'
    #elif emon == '':
    #    text= ''
    yield from event.conv.send_message(text_to_segments(text))
    
### BUSQUEDAS ###    

@command.register
def wiki(bot, event, *args):
    """Busca algo en la wikipedia\n Uso: bot wiki [Busqueda] """
    nombre =' '.join(args)
    busqueda = '_'.join(args)
    link = 'http://es.wikipedia.org/w/index.php?search={}'.format(busqueda)
    text = _('{} en Wikipedia: '+'\n {}').format(nombre,link)
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def traduce(bot, event, fuente, obj , *args):
    """Hace una busqueda de una oracion en Google translate\n Uso: <bot>
    traduce [idioma 1] [idioma2] [Busqueda] \n Ejemplo: bot traduce es en el
    taco es rico"""
    nombre =' '.join(args)
    busqueda = '%20'.join(args)
    link = 'https://translate.google.com/#{}/{}/{}'.format(fuente,obj,busqueda)
    text = _('\'{}\' en Google Translate: '+'\n {}').format(nombre,link)
    yield from event.conv.send_message(text_to_segments(text))

### Funciones de manuel ###

@command.register
def explosions(bot, event, *args):
    """Mr torgue approves\n Uso: <bot> explosions"""
    text = _('**Explosions!?**\n https://www.youtube.com/watch?v=mEizJ-TWua0')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def bestpony(bot, event, *args):
    """Responde al azar un nombre de pony.\n Uso: <bot> best pony[frase]"""
    var = (randint(0,5))
    if var == 0:
        text = 'Applejack'
    elif var == 1:
        text = 'Pinkie pie'
    elif var == 2:
        text = 'Rarity'
    elif var == 3:
        text = 'Raibow dash'
    elif var == 4:
        text =  'Twilight'
    elif var == 5:
        text =  'Fluttershy'
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def este(bot, event, *args):
    """Los [ro]bots no soportan las paradojas\n Uso: <bot> Este enunciado es mentira [frase]"""
    arg = ' '.join(args)
    text= '???'
    if arg == 'enunciado es mentira':
        text= _('No pienses en ello, no pienses en ello, no pienses en ello')
    yield from event.conv.send_message(text_to_segments(text))

### AZAR ###

@command.register
def sino(bot, event, *args):
    """Simplemente te dice Si o No.\n Uso: <bot> sino [frase]"""
    if (randint(0,1)) == 1:
    	text = 'Si'
    else:
    	text = 'No'
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def verdad(bot, event, *args):
    """Responde al azar si es verdad o no.\n Uso: <bot> verdad [frase]"""
    if (randint(0,1)) == 1:
        text = 'Si'
    else:
        text = 'No'
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def moneda(bot, event, *args):
    """Lanza una moneda y te dice el resultado.\n Uso: <bot> moneda"""
    if (randint(0,1)) == 1:
    	res = '**Cara**'
    else:
    	res = '**Sello**'
    text= 'Se Lanzo una moneda al aire\n Cayó: '+res
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def dado(bot, event, caras, *args):
    """Lanza un dado, es posible definir el numero de caras del dado\n Uso: <bot> dado [numero de caras]"""
    text = 'Se lanzo un dado de {} caras\n El resultado fue: '.format(strip_quotes(caras))+str(randint(1,int(caras)))
    yield from event.conv.send_message(text_to_segments(text))


### Respuestas ### 

@command.register
def como(bot, event, *args):
    """Preguntarle como esta al bot\nUso: <bot> como estas?"""
    arg = ' '.join(args)
    text= '???'
    if arg == 'estas?'or'estas'or'estas??':
        text= 'Bien, gracias'
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def queso(bot, event, *args):
    """Queso? Queso!\nUso: <bot> queso"""
    text = _(
        'ok\n'
        'Yo Queso, tu Queso, nosotros Queseamos'
        )
    yield from event.conv.send_message(text_to_segments(text))


@command.register
def wtf(bot, event, *args):
    """ಠ_ಠ"""
    text = _('ಠ_ಠ\nhttp://www.gfycat.com/AdmirableConcreteDairycow')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def roboass(bot, event, *args):
    """[ro]bots are not for sexual. Please be safe\b Uso: <bot> roboass"""
    text = _('Disfrute: https://www.youtube.com/watch?v=2LWzrE56yf0')
    yield from event.conv.send_message(text_to_segments(text))


@command.register
def tip(bot, event, *args):
    """Tipear fedora o trilby\n <bot> tip <fedora/trilby>"""
    arg = ' '.join(args)
    text= '???'
    if arg == 'fedora'or'trilby':
        text= 'https://youtu.be/oe9uK9QGCUI'
    yield from event.conv.send_message(text_to_segments(text))

### Easter Egg (?) ###

@command.register
def aptitude(bot, event, *args):
    """Easter egg del aptitude\n Uso:\n<bot> aptitude moo\n<bot> aptitude -v
    moo \n<bot> aptitude -vv moo\n<bot> aptitude -vvv moo\b<bot> aptitude -vvvv
    moo"""
    arg = ' '.join(args)
    text= '???'
    if arg == 'moo':
        text= 'No hay ningun Easter Egg en este bot'
    elif arg == '-v moo':
        text= 'De verdad no hay un Easter Egg en este bot'
    elif arg == '-vv moo':
        text= 'No te dije que no hay Easter Eggs en este bot?'
    elif arg == '-vvv moo':
        text= _('Ok, tu ganas.\n '
                +'____/---'+'\\'+'____\n'
                +'______________\n')
    elif arg == '-vvvv moo':
        text= 'Que que es? pues un elefante dentro de una vibora, obviamente '
    yield from event.conv.send_message(text_to_segments(text))

### Sandwiches ##

@command.register
def sandwich(bot, event, *args):
    """Cosas emparedadas de pan con cosas enmedio... i guess\n ver: make me a sandwich"""
    text = _('Que tiene?')
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def make(bot, event, *args):
    """Make me a sandiwch \n Uso: <bot> make me a sandwich"""
    arg = ' '.join(args)
    text= '???'
    if arg == 'me a sandwich'or'sandwich'or'me a sándwich'or'sándwich':
        text= 'Que? no, haztelo tu'
    yield from event.conv.send_message(text_to_segments(text))
@command.register

def sudo(bot, event, *args):
    """Permisos de administrador! (o no)\n Uso: [bot] sudo make me a sandwich"""
    arg = ' '.join(args)
    text= '???'
    if arg == 'make me a sandwich'or'sandwich'or'make me a sándwich'or'sándwich':
        text= 'A sus ordenes, un sandwich enseguida'
    yield from event.conv.send_message(text_to_segments(text))


### NOTAS ###

@command.register
def recuerda(bot, event, *args):
    """Guarda un mensaje en la libreta de notas\nUso: <bot> recuerda [nota]"""
    arg = ' '.join(args)
    f = open('/home/persus/Documentos/notas.txt','r+')
    s=time.ctime()
    msg= str((s+'\n[{}]\n'+'{}'+'\n\n').format(event.user.full_name,arg))
    f.write(msg)
    f.readlines()
    f.close()
    yield from event.conv.send_message(text_to_segments('Guardado'))

@command.register
def notas(bot, event, *args):
    """Muestra las notas guardadas \n Uso: <bot> notas"""
    f = open('/home/persus/Documentos/notas.txt','r+')
    text= 'Notas:\n'
    r=f.readlines()
    for line in r:
        text= _(text+line)
    f.close()
    yield from event.conv.send_message(text_to_segments(text))

@command.register(admin=True)
def deletenotas(bot, event, *args):
    """Borra la libreta de notas (Solo admins)\n Uso: <bot> deletenotas"""
    arg = ' '.join(args)
    f = open('/home/persus/Documentos/notas.txt','w')
    f.write(' ')
    f.close()
    yield from event.conv.send_message(text_to_segments('Borradas todas las notas'))

### CALCULADORA ###

@command.register
def suma(bot, event, n1, n2, *args):
    """Suma 2 numeros\n Uso: bot suma [numero1] [numero2]"""
    text = str(int(strip_quotes(n1))+int(strip_quotes(n2)))
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def resta(bot, event, n1, n2, *args):
    """Resta 2 numeros\n Uso: bot resta [numero1] [numero2]"""
    text = str(int(strip_quotes(n1))-int(strip_quotes(n2)))
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def multi(bot, event, n1, n2, *args):
    """Multiplica 2 numeros\n Uso: bot multi [numero1] [numero2]"""
    text = str(int(strip_quotes(n1))*int(strip_quotes(n2)))
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def div(bot, event, n1, n2, *args):
    """Divide 2 numeros\n Uso: bot div [numero1] [numero2]"""
    text = str(int(strip_quotes(n1))/int(strip_quotes(n2)))
    yield from event.conv.send_message(text_to_segments(text))

@command.register
def raiz(bot, event, n1, *args):
    """Raiz Cuadrada\n Uso: bot raiz [numero1] """
    num = float(strip_quotes(n1))
    num = sqrt(num)
    text= str(num)
    yield from event.conv.send_message(text_to_segments(text))

#@command.register
#def pi(bot, event, *args):
#    """Calcula pi"""
#    yield from event.conv.send_message(text_to_segments(pi))
