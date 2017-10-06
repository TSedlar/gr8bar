import tools


def get_volume_level():
    '''
    Gets the current volume level
    '''
    return tools.term("awk -F'[][]' '/dB/ { print $2 }' <(amixer sget DAC1)")


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
