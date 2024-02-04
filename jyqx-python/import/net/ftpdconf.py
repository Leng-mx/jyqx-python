# ftpdconf.py: ftpd configuration

# The following defines are in globals.py which is included automatically.
# import uid        # gets define for ROOT_UID on tmi-2
# import config

import socket # various socket defines from tmi-2

# standard defines.

# FTPD_PORT port number on which the ftp daemon will listen.  On a UNIX
# system the user should type: ftp tmi.lp.mud.org 5554
# (depending on the hostname of the MUD and the port # set below).
FTPD_PORT = 5143

# time in seconds that an ftp connection should be idle before it times out;
# this is used as the default for all connections--see MAX_FTPD_IDLE
FTPD_TIMEOUT = 1800

# this is the maximum idle value that can be set with the SITE IDLE command;
# note that when a user logs into ftp, they are assigned the value in
# FTPD_TIMEOUT and may manually adjust it up to the limit of MAX_FTPD_IDLE
MAX_FTPD_IDLE = 7200

# HOME_DIR: given a username give the home directory path
HOME_DIR = lambda name: user_cwd(name) # on TMI-2

# If this is defined, it should point to a file that should be
# displayed upon every successful login.
LOGIN_MSG = "/adm/etc/ftpd_welcome"

# the name of the MUD
THE_MUD_NAME = "ÏÀ¿ÍÐÐ"

# Maximum number of simultaneous ftp users.
FTPD_MAX_USERS = 4

# the version # of the driver (__VERSION__ on MudOS muds)
THE_VERSION = __VERSION__

# Set this to be the size of each outgoing block of data during
# file transfers.  This hasn't been tested with any value other
# than 1024, so its generally good to leave this alone.
BLOCK_SIZE = 1024

# who to send bug reports to
FTP_BUGS_EMAIL = "robocoder@tmi-2 or annihilator@es2"

# misc support defines.

# define this to allow "anonymous" ftp logins
ANONYMOUS_FTP = False

# define this to allow guest wizards (without home directories) to login
GUEST_WIZARD_FTP = False

# define this to support advisory file locking
FILE_LOCKING = False

# define this to support individual site checking (from .login file)
CHECK_SITE = False

# define this to support .message files sent to user when they "cd"
MESSAGE_FILES = True

# these flags determine read level access (values are intentionally unique...
# and are manually generated, so don't change them)
VALID_READ = 0              # rely on valid_read()
RESTRICTED_READ = 1         # ditto, but limited to public dirs
WRITE_LIMIT_READ = 2        # access limited by write access

# define as (ie set to) one of the flags above
READ_LEVEL = RESTRICTED_READ

# these flags determine write level access (values are intentionally unique...
# and are manually generated, so don't change them)
VALID_WRITE = 0             # rely on valid_write()
RESTRICTED_WRITE = 1        # ditto, but limited to public dirs
READ_ONLY = 2               # no write access, at all

# define as (ie set to) one of the flags above
WRITE_LEVEL = RESTRICTED_WRITE

# define the following public dirs that you'll limit access to
# for RESTRICTED_READ and/or RESTRICTED_WRITE; undefine any for which
# the directory doesn't exist on your system
PUB_DIR = "/open/"
FTP_DIR = "/ftp/"

# define this array as the only set of users permitted to use ftp
# Example:
#   FTP_USERS = ["dsn"]
FTP_USERS = ["atu", "robin", "byp"]

# debugging defines.

# define DEBUG to enable debugging info
DEBUG = True

# player to whom to "tell" debugging info
TP_CRE = "eatdami"

# log file defines.

# undefine this to disable all logging
LOGGING = True

if LOGGING:
    # define this to log all connections
    LOG_CONNECT = True
    # define this to determine where to log all file xfers
    LOG_FILE = "FTPD"
    # define this to put a time stamp before all log entries
    LOG_TIME = True
    # define this to log cd's, time stamp, and file size commands
    LOG_CD_SIZE = True
    # define this to log failed connections
    LOG_NO_CONNECT = True
else:
    LOG_CONNECT = False
    LOG_FILE = None
    LOG_CD_SIZE = False
    LOG_TIME = False
    LOG_NO_CONNECT = False

# consistency checks

# restricting ftp to a limited number of users and having anon ftp
# at the same time is pointless
if 'ANONYMOUS_FTP' in globals() and 'FTP_USERS' in globals():
    del ANONYMOUS_FTP

# server should restrict anonymous ftp by using a restricted directory
if 'ANONYMOUS_FTP' in globals() and 'FTP_DIR' not in globals():
    del ANONYMOUS_FTP

# guest wizards, if permitted to login, need some place to go
if 'GUEST_WIZARD_FTP' in globals() and 'PUB_DIR' not in globals():
    PUB_DIR = "/"
