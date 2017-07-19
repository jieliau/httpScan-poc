#/usr/bin/python

import nmap, os
from netaddr import IPNetwork

def main():
    try:
        subnet = raw_input("Please input the IP subnet: ")
        mask = raw_input("Please input the subnetmask: ")
        ipRange = subnet+"/"+mask
        print "The result fo scanning port 80 for "+ipRange+":"

        nm = nmap.PortScanner()
        for loop in IPNetwork(ipRange):
            ip = str(loop)
            nm.scan(ip, '80')
            try:
                result = nm[ip].tcp(80)
                if result['state'] == "open":
                    print loop, ":", result['product']
                    content = ip+": "+result['product']
                    ipWebServerList = open('./result_'+subnet+'.txt', 'a+')
                    ipWebServerList.write(ip+": "+result['product']+"\n")
                    ipWebServerList.close()
                else:
                    print loop, ": N/A"
            except KeyError:
                print loop, ": N/A"
    except KeyboardInterrupt:
        print "Bye Bye"

if __name__ == '__main__':
    main()
