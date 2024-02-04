# socket_errors.py: definitions for efun socket error return codes.

EESUCCESS = 1		# Call was successful
EESOCKET = -1		# Problem creating socket
EESETSOCKOPT = -2	# Problem with setsockopt
EENONBLOCK = -3		# Problem setting non-blocking mode
EENOSOCKS = -4		# No more available efun sockets
EEFDRANGE = -5		# Descriptor out of range
EEBADF = -6		# Descriptor is invalid
EESECURITY = -7		# Security violation attempted
EEISBOUND = -8		# Socket is already bound
EEADDRINUSE = -9	# Address already in use
EEBIND = -10		# Problem with bind
EEGETSOCKNAME = -11	# Problem with getsockname
EEMODENOTSUPP = -12	# Socket mode not supported
EENOADDR = -13		# Socket not bound to an address
EEISCONN = -14		# Socket is already connected
EELISTEN = -15		# Problem with listen
EENOTLISTN = -16	# Socket not listening
EEWOULDBLOCK = -17	# Operation would block
EEINTR = -18		# Interrupted system call
EEACCEPT = -19		# Problem with accept
EEISLISTEN = -20	# Socket is listening
EEBADADDR = -21		# Problem with address format
EEALREADY = -22		# Operation already in progress
EECONNREFUSED = -23	# Connection refused
EECONNECT = -24		# Problem with connect
EENOTCONN = -25		# Socket not connected
EETYPENOTSUPP = -26	# Object type not supported
EESENDTO = -27		# Problem with sendto
EESEND = -28		# Problem with send
EECALLBACK = -29	# Wait for callback
EESOCKRLSD = -30	# Socket already released
EESOCKNOTRLSD = -31	# Socket not released

ERROR_STRINGS = 32	# sizeof (error_strings)
