# This network header file contains the macros used by the DNS master
# daemons and its auxiliary daemons.

NETWORK_MASTER = None
try:
    from net import daemons
except ImportError:
    NETWORK_MASTER = True

AUX_PATH = "/adm/daemons/network/services/"

PING_Q = AUX_PATH + "ping_q"
PING_A = AUX_PATH + "ping_a"
MUDLIST_Q = AUX_PATH + "mudlist_q"
MUDLIST_A = AUX_PATH + "mudlist_a"
SUPPORT_Q = AUX_PATH + "support_q"
STARTUP = AUX_PATH + "startup"
SHUTDOWN = AUX_PATH + "shutdown"
GFINGER_Q = AUX_PATH + "gfinger_q"
GTELL = AUX_PATH + "gtell"
GWIZ = AUX_PATH + "gwizmsg"
GCHANNEL = AUX_PATH + "gchannel"
LOCATE_Q = AUX_PATH + "locate_q"
LOCATE_A = AUX_PATH + "locate_a"
MAIL_Q = AUX_PATH + "mail_q"
MAIL_A = AUX_PATH + "mail_a"
RWHO_Q = AUX_PATH + "rwho_q"

# The currently known types
DNS_STARTUP = "startup"
DNS_SHUTDOWN = "shutdown"
DNS_PING_Q = "ping_q"
DNS_PING_A = "ping_a"
DNS_SUPPORT_Q = "support_q"
DNS_SUPPORT_A = "support_a"
DNS_RWHO_Q = "rwho_q"
DNS_RWHO_A = "rwho_a"
DNS_MUDLIST_Q = "mudlist_q"
DNS_MUDLIST_A = "mudlist_a"
DNS_GFINGER_Q = "gfinger_q"
DNS_AFFIRMATION_A = "affirmation_a"
DNS_GFINGER_A = "gfinger_a"
DNS_GWIZMSG = "gwizmsg"
DNS_WARNING = "warning"
DNS_GTELL = "gtell"
DNS_GCHANNEL = "gchannel"
DNS_LOCATE_Q = "locate_q"
DNS_LOCATE_A = "locate_a"
DNS_MAIL_Q = "mail_q"
DNS_MAIL_A = "mail_a"

# This is the number of retrys we ping the mud for before we decide
# it has gone down.
MAX_RETRYS = 3
DNS_NO_CONTACT = "_dns_no_contact"
