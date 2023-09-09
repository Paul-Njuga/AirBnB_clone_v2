#!/usr/bin/python3
"""1-pack_web_static module"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates .tgz archive from web_static dir
    Returns: Archive path, otherwise False
    """
    fmt = datetime.now().strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")
    local(f"tar -cvzf versions/web_static_{fmt}.tgz web_static")

    try:
        return (f"versions/web_static_{fmt}.tgz")
    except Exception as e:
        return None
