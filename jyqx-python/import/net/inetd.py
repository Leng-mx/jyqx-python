# net_inetd.py: ftpd support _code_

# DNS_MASTER is not defined
# from net import daemons

# INETD_ADDRESS = -100
# INETD_PORT = -200

PENDING_CMD = 0
PENDING_CONNECT = 1
PENDING_DATA = 2

READ_SOCKET = 0
WRITE_SOCKET = 1
INETD_SERVICES = "/adm/etc/services"
# INETD_PORT = lambda x: DNS_MASTER.get_host_name(x) + " " + \
#                        str(DNS_MASTER.get_mudresource(x, "inetd"))

AWAITING_CONNECT_ACK = 0
AWAITING_SERVICE = 1
AWAITING_DATA = 2
