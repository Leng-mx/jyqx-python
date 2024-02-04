# net_services.py: ftpd support _code_

# These are the protocol types for the services
SVC_UNKNOWN = 0
SVC_KNOWN = 1
SVC_TCP = 2
SVC_NO_TCP = 4
SVC_UDP = 8
SVC_NO_UDP = 16

# These macros control which ports the services run on.
SRVC_PORT_INETD = lambda x: x + 5
SRVC_PORT_UDP = lambda x: x + 4

# These are the levels of tcp support available
TCP_NONE = "none"
TCP_SOME = "some"
TCP_ALL = "all"
TCP_ONLY = "only"
