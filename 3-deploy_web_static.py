#!/usr/bin/python3
"""
    pack static content and deploy on server
"""
import time
from fabric.context_managers import cd
from fabric.api import local
from fabric.api import get
from fabric.api import put
from fabric.api import reboot
from fabric.api import run
from fabric.api import sudo
from fabric.api import env
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['34.75.49.246', '104.196.144.160']
path = do_pack()


def deploy():
    if path:
        return do_deploy(path)
    else:
        return False
