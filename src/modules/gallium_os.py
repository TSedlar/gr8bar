import tools


def get_volume_level():
    '''
    Gets the current volume level
    '''
    txt = tools.term('amixer sget DAC1 | egrep -o "[0-9]+%" | head -1')
    txt = txt.replace('%', '')
    return int(txt)


def set_volume(percent):
    '''
    Sets the volume level to the given percent
    :param percent: The volume percent to set to
    '''
    return tools.term('amixer -q sset DAC1 %s%%' % (percent))


def increment_volume(percent):
    '''
    Increments the volume level by the given percent
    :param percent: The amount of percent to increment by
    '''
    return tools.term('amixer -q sset DAC1 %s%%+' % (percent))


def decrement_volume(percent):
    '''
    Decrements the volume level by the given percent
    :param percent: The amount of percent to decrement by
    '''
    return tools.term('amixer -q sset DAC1 %s%%-' % (percent))


def toggle_volume():
    '''
    Toggles the volume (mute/unmute)
    '''
    return tools.term('amixer -q sset DAC1 toggle')
