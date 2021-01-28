import pia_controller


if __name__ == '__main__':
    print('This script will automatically connect and disconnect from the PIA VPN.')
    print('This will interfere with your internet connection.')
    input('Press return to continue. ')

    print()
    print('Test 1: connect/disconnect cycles.')
    print('A) Connecting...')
    pia_controller.connect()
    print('B) Disconnecting...')
    pia_controller.disconnect()
    print('C) Connecting...')
    pia_controller.connect()
    print('D) Disconnecting...')
    pia_controller.disconnect()
    print('Done.')

    print()
    print('Test 2: "get" commands.')
    print('A) Connection state:', pia_controller.get_connection_state())
    print('B) Debug logging:', pia_controller.get_debug_logging())
    print('C) Port forward:', pia_controller.get_port_forward())
    print('D) Current region:', pia_controller.get_current_region())
    print('E) All regions:', len(pia_controller.get_all_regions()))
    print('F) VPN IP:', pia_controller.get_vpn_ip())
    print('Done.')

    print()
    print('Test 3: "monitor" commands.')
    print('A) Connection state...')
    pia_controller.monitor_connection_state(timeout=1)
    print('B) Debug logging...')
    pia_controller.monitor_debug_logging(timeout=1)
    print('C) Port forward...')
    pia_controller.monitor_port_forward(timeout=1)
    print('D) Region...')
    pia_controller.monitor_region(timeout=1)
    print('E) VPN IP...')
    pia_controller.monitor_vpn_ip(timeout=1)
    print('Done.')

    print()
    print('Test 4: setting and cycling region.')
    print('A) Setting region to auto...')
    pia_controller.set_region(region='auto')
    print('B) Cycling region with no exclusions...')
    pia_controller.cycle_region()
    print('Done.')

    print()
    print('Test 5: disconnecting and waiting on disconnection.')
    pia_controller.disconnect()
    pia_controller.wait_for_state(state='Disconnected')
    print('Done.')
    print()
