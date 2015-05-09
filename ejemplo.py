@command.register
def NOMBRECOMANDO(bot, event, *args):
    """TEXTO AYUDA"""

    ### TU CODIGO AQUI !
    
    text = _('MENSAJE DESPLEGADO')
    yield from event.conv.send_message(text_to_segments(text))