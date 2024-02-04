# ftpd.h

import time


POS = 1
DATA = 2
user = 3
LOGGED_IN = 4
CWD = 5
LEN = 6
PARENT_FD = 7
DATA_FD = 8
DATA_ADDR = 9
LAST_DATA = 10
DATA_PORT = 11
FILE = 12
TYPE = 13
DOWNLOAD = 14
PATH = 15
APPEND = 16
CONNECTED = 17
USER_SITE = 18
STRING = 19
BINARY = 20
FROMNAME = 21
IDLE_SETTING = 22

FTP_TIME = lambda: "[%s] " % time.ctime()[4:15]
UNAME = lambda fd: socket_info[fd][user]
UCWD = lambda fd: socket_info[fd][CWD]
UTYPE = lambda fd: socket_info[fd][TYPE]
USITE = lambda fd: socket_info[fd][USER_SITE]
UPATH = lambda fd: socket_info[fd][PATH]
UDATA = lambda fd: socket_info[fd][DATA]

MAX_UNIQUE_TRIES = 10

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

SECS_IN_YEAR = 365 * 24 * 60 * 60

cmdtab = {
    "user": ["USER", 1, "<sp> username"],
    "pass": ["PASS", 1, "<sp> password"],
    "acct": ["ACCT", 0, "(specify account)"],
    "smnt": ["SMNT", 0, "(structure mount)"],
    "rein": ["REIN", 0, "(reinitialize server state)"],
    "quit": ["QUIT", 1, "(terminate service)"],
    "port": ["PORT", 1, "<sp> b0, b1, b2, b3, b4"],
    "pasv": ["PASV", 0, "(set server in passive mode)"],
    "type": ["TYPE", 1, "<sp> [ A | E | I | L ]"],
    "stru": ["STRU", 0, "(specify file structure)"],
    "mode": ["MODE", 0, "(specify transfer mode)"],
    "retr": ["RETR", 1, "<sp> file-name"],
    "stor": ["STOR", 1, "<sp> file-name"],
    "appe": ["APPE", 1, "<sp> file-name"],
    "mlfl": ["MLFL", 0, "(mail file)"],
    "mail": ["MAIL", 0, "(mail to user)"],
    "msnd": ["MSND", 0, "(mail send to terminal)"],
    "msom": ["MSOM", 0, "(mail send to terminal or mailbox)"],
    "msam": ["MSAM", 0, "(mail send to terminal and mailbox)"],
    "mrsq": ["MRSQ", 0, "(mail recipient scheme question)"],
    "mrcp": ["MRCP", 0, "(mail recipient)"],
    "allo": ["ALLO", 1, "allocate storage (vacuously)"],
    "rest": ["REST", 0, "(restart command)"],
    "rnfr": ["RNFR", 1, "<sp> file-name"],
    "rnto": ["RNTO", 1, "<sp> file-name"],
    "abor": ["ABOR", 1, "(abort operation)"],
    "dele": ["DELE", 1, "<sp> file-name"],
    "cwd" : ["CWD" , 1, "[ <sp> directory-name ]"],
    "xcwd": ["XCWD", 1, "[ <sp> directory-name ]"],
    "list": ["LIST", 1, "[ <sp> path-name ]"],
    "nlst": ["NLST", 1, "[ <sp> path-name ]"],
    "site": ["SITE", 1, "site-cmd [ <sp> arguments ]"],
    "syst": ["SYST", 1, "(get type of operating system)"],
    "stat": ["STAT", 1, "[ <sp> path-name ]"],
    "help": ["HELP", 1, "[ <sp> <string> ]"],
    "noop": ["NOOP", 1, ""],
    "mkd" : ["MKD" , 1, "<sp> path-name"],
    "xmkd": ["XMKD", 1, "<sp> path-name"],
    "rmd" : ["RMD" , 1, "<sp> path-name"],
    "xrmd": ["XRMD", 1, "<sp> path-name"],
    "pwd" : ["PWD" , 1, "(return current directory)"],
    "xpwd": ["XPWD", 1, "(return current directory)"],
    "cdup": ["CDUP", 1, "(change to parent directory)"],
    "xcup": ["XCUP", 1, "(change to parent directory)"],
    "stou": ["STOU", 1, "<sp> file-name"],
    "size": ["SIZE", 1, "<sp> path-name"],
    "mdtm": ["MDTM", 1, "<sp> path-name"]
}

sitecmdtab = {
    "idle" : ["USER",  1, "[ <sp> timeout ]"],
    "umask": ["UMASK", 0, "[ <sp> umask ]"],
    "chmod": ["CHMOD", 0, "<sp> path-name"],
    "time" : ["TIME",  1, "(return local time)"],
    "help" : ["HELP",  1, "[ <sp> <string> ]"]
}
def PERMISSION_DENIED550(S):
    return socket_write(fd, "550 Permission denied to %s.\n" % S)

def PERMISSION_DENIED553(S):
    return socket_write(fd, "553 Permission denied to %s.\n" % S)

# these flags determine read level access
VALID_READ = 0              # rely on valid_read()
RESTRICTED_READ = 1         # ditto, but limited to public dirs
WRITE_LIMIT_READ = 2        # access limited by write access

# these flags determine write level access
VALID_WRITE = 0             # rely on valid_write()
RESTRICTED_WRITE = 1        # ditto, but limited to public dirs
READ_ONLY = 2               # no write access, at all
