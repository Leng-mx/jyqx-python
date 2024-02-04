# net_macros.py: ftpd support _code_

# DNS_MASTER is not defined
# from net import daemons

# for converting hostnames in the host representation to the
# network representation and vice-versa
htonn = lambda x: str(x).lower().replace(" ", ".") if x else ""
nntoh = lambda x: str(x).capitalize().replace(".", " ") if x else ""

REMOTE_DIR = "/data/remote/"
# macros for getting resources
# Mud_name = lambda: DNS_MASTER.query_mud_name()
# mud_nname = lambda: htonn(Mud_name())
# mud_port = __PORT__
# udp_port = lambda: DNS_MASTER.query_udp_port()

# macros for the sequencer
# index_add = lambda x: DNS_MASTER.idx_request(x)
# index_call = lambda x, y: DNS_MASTER.idx_callback(x, y)

# for security checking
ROOT_UID = "root_uid"
ACCESS_CHECK = lambda x: not x or geteuid(x) == ROOT_UID

# for logging and stuff
# dns_log = lambda x, y: DNS_MASTER.aux_log(x, y)
# dns_warning = lambda x: DNS_MASTER.aux_warning(x)
