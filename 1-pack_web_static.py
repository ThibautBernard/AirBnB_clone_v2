#!/usr/bin/python3
"""
    pack webstatic module fabric
"""
import time
# from fabric.context_managers import cd
from fabric.api import local
from fabric.api import get
from fabric.api import put
from fabric.api import reboot
from fabric.api import run
from fabric.api import sudo
import os.path


def do_pack():
    """ pack my static"""
    try:
        if not os.path.exists('versions'):
            l = local("mkdir -p versions")
        n = "versions/web_static_{}.tgz".\
            format(time.strftime("%Y%m%d%H%M%S", time.gmtime()))
        o = local("tar -cvzf {} web_static".format(n))
        # x = local("mv {} versions".format(n))
        # p = local("pwd {}".format(n))
        # return 'versions/{}'.format(n)
        return n
    except:
        return None
