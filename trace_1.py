import subprocess
import re

def traceroute(hostname):
    '''
    input: hostname/ip
    return: list ip hop
    '''
    traceroute = subprocess.Popen(["tracert", '-d',hostname],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    ipList = []
    for line in iter(traceroute.stdout.readline,b""):
        line = line.decode("UTF-8")
        line = line.strip()

        if len(line) > 0 and line[0].isdigit():
            IPs = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)

            if len(IPs) > 0:
                print(line)
                ipList.append(IPs[0])
            else:
                print(line)

    return ipList