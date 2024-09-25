"""MAC"""
import re
def mac_address_validate(mac):
    """valitare mac address"""
    pattern1 = r'^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}$'
    pattern2 = r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$'
    pattern3 = r'^([0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4}$'
    if re.match(pattern1, mac):
        return "VALID 1"
    if re.match(pattern2, mac):
        return "VALID 2"
    if re.match(pattern3, mac):
        return "VALID 3"
    return "ERROR"

def main(mac):
    """main"""
    print(mac_address_validate(mac))
main(input())
