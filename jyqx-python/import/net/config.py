# modified by wind

try:
    from net import services
    SVC_TCP = None
except ImportError:
    SVC_TCP = True

# These are the primary and secondry hosts to use as boot servers
# for the DNS.  It is better to set to the primary to be a mud on
# the same continent.
# Elon (07-01-95) updated LISTNODES to current
# The TMI-2
MUDLIST_DNS = ["172.27.157.89", 4448]
# The Eastern Stories
MUDLIST_BAK = ["172.27.157.89", 4448]

LISTNODES = {
    "SILVERSAND_MUD": "202.96.140.58 4448",
}

# This is the default packet size of outgoing mail messages.  The ideal
# number is 512, maximum would be about 900, since 1024 is the maximum
# udp packet size.  Probably best kept at 512
MAIL_PACKET_SIZE = 512

# These macros are for the name service.  They determine how often the
# database is refreshed, how often other muds are checked, how often
# the sequence list is checked for timed out services, and how long a
# service is allowed to time out.
REFRESH_INTERVAL = 5*60
PING_INTERVAL = 30*60
SEQ_CLEAN_INTERVAL = 60*60
SERVICE_TIMEOUT = 30

# The number of muds that we initialy allocate space for.  This speeds
# up name lookup.
MUDS_ALLOC = 60

# This macro controls the level of tcp support used by the mud for
# services such as finger, tell and mail. Valid values are:
#  TCP_ALL   - all services available
#  TCP_ONLY  - only tcp services available
#  TCP_SOME  - some tcp services are available
#  TCP_NONE  - no tcp services available
TCP_SERVICE_LEVEL = "TCP_ALL"

# These are the prefered protocols used for certain services which can
# be done either way.  Mail should be left tcp, the others are up to
# the individual admin.  If the one you choose is not supported the
# other type _may_ be used depending on the service.
PREF_MAIL = SVC_TCP
PREF_FINGER = SVC_TCP
PREF_TELL = "SVC_UDP"

# These macros are used by the name server to keep a list of muds which
# do not support the DNS.
MUD_ADDRESSES = "/adm/etc/mud_addresses"
MUD_SERVICES = "/adm/etc/mud_services"
