import tools


def logout():
    '''
    Logs out of the current user
    '''
    return tools.term('pkill -u $USER')


def get_cpu_percent():
    '''
    Gets the current CPU percent
    '''
    return tools.term("vmstat 1 2 | tail -1 | awk '{print 100-$15}'")


def get_cpu_temp():
    '''
    Gets the current CPU temperature
    '''
    temp_str = tools.term('cat /sys/class/thermal/thermal_zone0/temp')
    return int((int(temp_str) if len(temp_str) else -1000) / 1000)


def get_mem_used():
    '''
    Gets the current amount of memory being used
    '''
    return tools.term("free -m | grep 'Mem:' | awk '{print $6}'")


def get_network_ssid():
    '''
    Gets the currently connected network SSID
    '''
    return tools.term('iwgetid -r')


def get_battery_capacity():
    '''
    Gets the current battery capacity
    '''
    cap_str = tools.term('cat /sys/class/power_supply/BAT0/capacity')
    return int(cap_str) if len(cap_str) else -1


def get_battery_state():
    '''
    Gets the battery state (Charging, Not Charging)
    '''
    return tools.term('cat /sys/class/power_supply/BAT0/status')


def get_active_window_name():
    '''
    Gets the active window name/title
    '''
    return tools.term('xdotool getwindowfocus getwindowname')


def get_workspace():
    '''
    Gets the current workspace number
    '''
    return tools.term('xprop -root _NET_CURRENT_DESKTOP | grep -o "[0-9]*"')


def get_user():
    '''
    Gets the currently logged in user's username
    '''
    return tools.term('id -u -n')
