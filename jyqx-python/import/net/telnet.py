# telnet.py: ftpd support _code_

SUCCESS = 1
BAD_ADDRESS = 0
CONN_REFUSED = -1
UNREACHABLE = -2

# This file holds the approved telnet sites.
APPROVED_SITES = "/adm/etc/approved_sites"
BANNED_SITES = "/adm/etc/banned_sites"

# These are the files that are permitted to perform telnet operations
# without any checks (assumed to have predefined address targets).
APPROVED_TELNET = ["/adm/daemons/network/telnetd", "/obj/tools/webster"]
