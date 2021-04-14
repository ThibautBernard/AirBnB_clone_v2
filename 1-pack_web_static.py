#!/usr/bin/python3
"""
    pack webstatic
"""
import time
from fabric.context_managers import cd
from fabric.api import local
from fabric.api import get
from fabric.api import put
from fabric.api import reboot
from fabric.api import run
from fabric.api import sudo


def do_pack():
    try:
        n = "web_static_{}.tgz".\
          format(time.strftime("%Y%m%d%H%M%S", time.gmtime()))
        l = local("mkdir -p versions")
        o = local("tar -cvzf {} web_static".format(n))
        x = local("mv {} versions".format(n))
        p = local("pwd {}".format(n))
        return p
    except:
        return None
