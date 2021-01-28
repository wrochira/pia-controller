import os
import subprocess


CLI_PATH = 'C:/Program Files/Private Internet Access/piactl.exe' if os.name == 'nt' else 'piactl'


# Basic built-in functions
def connect():
    result = subprocess.run([ CLI_PATH, 'connect' ],
                            stdout=subprocess.PIPE)
    output = result.stdout.decode().strip()
    return output

def disconnect():
    result = subprocess.run([ CLI_PATH, 'disconnect' ],
                            stdout=subprocess.PIPE)
    output = result.stdout.decode().strip()
    return output

def get_connection_state():
    result = subprocess.run([ CLI_PATH, 'get', 'connectionstate' ],
                            stdout=subprocess.PIPE)
    output = result.stdout.decode().strip()
    return output

def get_debug_logging():
    result = subprocess.run([ CLI_PATH, 'get', 'debuglogging' ],
                            stdout=subprocess.PIPE)
    output = result.stdout.decode().strip()
    return output

def get_port_forward():
    result = subprocess.run([ CLI_PATH, 'get', 'portforward' ],
                            stdout=subprocess.PIPE)
    output = result.stdout.decode().strip()
    return output

def get_current_region():
    result = subprocess.run([ CLI_PATH, 'get', 'region' ],
                            stdout=subprocess.PIPE)
    output = result.stdout.decode().strip()
    return output

def get_all_regions():
    regions = [ ]
    result = subprocess.run([ CLI_PATH, 'get', 'regions' ],
                            stdout=subprocess.PIPE)
    output = result.stdout.decode()
    for line in output.splitlines():
        region = line.strip()
        if len(region) > 0:
            regions.append(region)
    return regions

def get_vpn_ip():
    result = subprocess.run([ CLI_PATH, 'get', 'vpnip' ],
                            stdout=subprocess.PIPE)
    output = result.stdout.decode().strip()
    return output

def monitor_connection_state(timeout=None):
    try:
        result = subprocess.run([ CLI_PATH, 'monitor', 'connectionstate' ],
                                stdout=subprocess.PIPE,
                                timeout=timeout)
    except subprocess.TimeoutExpired:
        return None

    output = result.stdout.decode().strip()
    return output

def monitor_debug_logging(timeout=None):
    try:
        result = subprocess.run([ CLI_PATH, 'monitor', 'debuglogging' ],
                                stdout=subprocess.PIPE,
                                timeout=timeout)
    except subprocess.TimeoutExpired:
        return None

    output = result.stdout.decode().strip()
    return output

def monitor_port_forward(timeout=None):
    try:
        result = subprocess.run([ CLI_PATH, 'monitor', 'portforward' ],
                                stdout=subprocess.PIPE,
                                timeout=timeout)
    except subprocess.TimeoutExpired:
        return None

    output = result.stdout.decode().strip()
    return output

def monitor_region(timeout=None):
    try:
        result = subprocess.run([ CLI_PATH, 'monitor', 'region' ],
                                stdout=subprocess.PIPE,
                                timeout=timeout)
    except subprocess.TimeoutExpired:
        return None

    output = result.stdout.decode().strip()
    return output

def monitor_vpn_ip(timeout=None):
    try:
        result = subprocess.run([ CLI_PATH, 'monitor', 'vpnip' ],
                                stdout=subprocess.PIPE,
                                timeout=timeout)
    except subprocess.TimeoutExpired:
        return None

    output = result.stdout.decode().strip()
    return output

def reset_settings():
    result = subprocess.run([ CLI_PATH, 'resetsettings' ],
                            stdout=subprocess.PIPE)
    output = result.stdout.decode().strip()
    return output

def set_region(region='auto'):
    result = subprocess.run([ CLI_PATH, 'set', 'region', region ],
                            stdout=subprocess.PIPE)
    output = result.stdout.decode().strip()
    return output

# Custom functions
def cycle_region(current_region=None, all_regions=None, excluded_regions=None):
    if all_regions is None:
        all_regions = get_all_regions()
    if current_region is None:
        current_region = get_current_region()
    excluded_regions = set() if excluded_regions is None else set(excluded_regions)
    included_regions = [ x for x in all_regions if x not in excluded_regions ]
    current_region_index = all_regions.index(current_region)
    if current_region_index == len(included_regions) - 1:
        new_region = included_regions[0]
    else:
        new_region = included_regions[current_region_index+1]
    result = subprocess.run([ CLI_PATH, 'set', 'region', new_region ],
                            stdout=subprocess.PIPE)
    output = result.stdout.decode()
    if len(output.strip()) > 0:
        print('ERROR CHANGING REGIONS:', output)
    return new_region

def wait_for_state(state='Connected'):
    import time
    current_state = None
    while current_state != state:
        current_state = get_connection_state()
        time.sleep(1)
