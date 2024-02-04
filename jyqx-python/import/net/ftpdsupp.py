# ftpdsupp.py: ftpd support _code_

import os

def directory_exists(p):
    return os.path.isdir(p)

def file_exists(p):
    return os.path.isfile(p)

# debugging macros
DEBUG = True
TP_CRE = "eatdami"
DEBUG_SEND = DEBUG

def TP(STR):
    if DEBUG:
        print(STR)

def CHECK_LOGIN(fd, socket_info):
    if not socket_info[fd]['LOGGED_IN']:
        socket_write(fd, "530 Please login with USER and PASS.\n")
        return False
    return True

def CHECK_CMD(command, x):
    if len(command) == x:
        socket_write(fd, f"500 '{command[0]}': command not understood.\n")
        return False
    return True

def check_access(name):
    FTP_USERS = ["atu", "robin", "byp"]
    ANONYMOUS_FTP = False
    GUEST_WIZARD_FTP = False
    PDATA_DIR = "/path/to/pdata_dir"
    HOME_DIR = lambda name: f"/home/{name}" # replace with actual function

    if FTP_USERS and name not in FTP_USERS:
        return 0

    if ANONYMOUS_FTP and name == "anonymous":
        return 1

    if GUEST_WIZARD_FTP:
        file = PDATA_DIR + name[0] + "/" + name + ".o"
        return file_exists(file) and "wizard 1" in open(file).read()

    return directory_exists(HOME_DIR(name))

def check_password(name, plaintext):
    ANONYMOUS_FTP = False
    LOGIN_OB = "/path/to/login_ob" # replace with actual object

    if ANONYMOUS_FTP and name == "anonymous":
        if not plaintext or plaintext in ["none", "guest", "anon", "anonymous", "none@none"]:
            return 0
        else:
            return 1

    login_ob = LOGIN_OB() # replace with actual object creation

    login_ob.set("id", name)
    fancytext = login_ob.query("password")

    if not fancytext or not plaintext:
        return 0

    cpass = crypt.crypt(plaintext, fancytext)

    return cpass == fancytext

def dot_match(site, pattern, flag):
    j = len(pattern)
    if j != 4:
        return 0

def dot_match(site, pattern, flag):
    j = len(pattern)
    while j > 0:
        j -= 1
        if flag:
            # match any octect
            if pattern[j] == "*":
                continue
        else:
            # be strict (last octect only)
            if j == 3 and pattern[3] == "*":
                continue

        # component doesn't match
        if site[j] != pattern[j]:
            return 0

    # by process of elimination...it must match
    return 1

def check_site(who, fd):
    wildcard_flag = False
    site = USITE

    # get site list (if any)
    if site and site != "" and os.path.isdir(HOME_DIR(who)) and os.path.isfile(HOME_DIR(who) + ".login"):
        arg = open(HOME_DIR(who) + ".login").read()
        if arg and len(arg):
            sites = arg.split("\n")
            sites = [s for s in sites if s.startswith("sitecheck ")]
            if sites:
                arg = sites[0][10:]

                # parse command line args
                arg = arg.replace(",", " ")
                sites = arg.lower().split()

                # check for options
                if sites[0][0] == '-':
                    # at the moment, we don't respect the presence of
                    # the -t (test) flag (ie allow the user to login
                    # anyways), and we don't respect the absense of the
                    # -d (destruct) flag, choosing to always drop the
                    # connection if the site check fails

                    if 'w' in sites[0]:
                        wildcard_flag = True

                # check list of accepted sites
                #   1) check for perfect match
                site = site.lower()
                if site in sites:
                    return 1

                #   2) check ip number (from ip name)
                if not re.match(r"\d+\.\d+\.\d+\.\d+", site):
                    site_num = socket.gethostbyname(socket.gethostname())
                    if site_num in sites:
                        return 1
                else:
                    site_num = site
                    site = None

# ftpdsupp.py: ftpd support _code_

import os
import re
import socket

def directory_exists(p):
    return os.path.isdir(p)

def file_exists(p):
    return os.path.isfile(p)

# debugging macros
DEBUG = True
TP_CRE = "eatdami"
DEBUG_SEND = DEBUG

def TP(STR):
    if DEBUG:
        print(STR)

def CHECK_LOGIN(fd, socket_info):
    if not socket_info[fd]['LOGGED_IN']:
        socket_write(fd, "530 Please login with USER and PASS.\n")
        return False
    return True

def CHECK_CMD(command, x):
    if len(command) == x:
        socket_write(fd, f"500 '{command[0]}': command not understood.\n")
        return False
    return True

def dot_match(site, pattern, flag):
    j = len(pattern)
    while j > 0:
        j -= 1
        if flag:
            # match any octect
            if pattern[j] == "*":
                continue
        else:
            # be strict (last octect only)
            if j == 3 and pattern[3] == "*":
                continue

        # component doesn't match
        if site[j] != pattern[j]:
            return 0

    # by process of elimination...it must match
    return 1

def check_site(who, fd):
    wildcard_flag = False
    site = USITE

    # get site list (if any)
    if site and site != "" and os.path.isdir(HOME_DIR(who)) and os.path.isfile(HOME_DIR(who) + ".login"):
        arg = open(HOME_DIR(who) + ".login").read()
        if arg and len(arg):
            sites = arg.split("\n")
            sites = [s for s in sites if s.startswith("sitecheck ")]
            if sites:
                arg = sites[0][10:]

                # parse command line args
                arg = arg.replace(",", " ")
                sites = arg.lower().split()

                # check for options
                if sites[0][0] == '-':
                    # at the moment, we don't respect the presence of
                    # the -t (test) flag (ie allow the user to login
                    # anyways), and we don't respect the absense of the
                    # -d (destruct) flag, choosing to always drop the
                    # connection if the site check fails

                    if 'w' in sites[0]:
                        wildcard_flag = True

                # check list of accepted sites
                #   1) check for perfect match
                site = site.lower()
                if site in sites:
                    return 1

                #   2) check ip number (from ip name)
                if not re.match(r"\d+\.\d+\.\d+\.\d+", site):
                    site_num = socket.gethostbyname(socket.gethostname())
                    if site_num in sites:
                        return 1
                else:
                    site_num = site
                    site = None

                # LAST: loop through wildcards in sites[]
                #   Note: sites[] is altered
                if '*' in arg:
                    # here's a quick filter :)
                    sites = [s for s in sites if "*" in s]
                    if sites:
                        # check site ip name;
                        # default only allows '*' as a prefix,
                        #   ie "*.domain.name"
                        if site:
                            l1 = len(site)
                            for i in range(len(sites)):
                                l2 = len(sites[i]) - 1
                                if l2 > 1 and l1 > l2 and sites[i][:2] == "*." and site[l1-l2:] == sites[i][1:]:
                                    return 1

                            if wildcard_flag:
                                # handle '*' as suffix
                                for i in range(len(sites)):
                                    l2 = len(sites[i]) - 2
                                    if l2 > 0 and l1 > l2 and sites[i][l2:] == ".*" and site[:l2] == sites[i][:l2]:
                                        return 1

                        # check site ip number
                        if site_num:
                            site_dots = site_num.split(".")
                            for i in range(len(sites)):
                                match_dots = sites[i].split(".")
                                if dot_match(site_dots, match_dots, wildcard_flag):
                                    return 1

                return 0

    return 1
