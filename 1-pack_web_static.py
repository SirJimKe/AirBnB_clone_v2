#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder."""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Packs the contents of the web_static folder into a .tgz archive."""
    if not os.path.exists("versions"):
        os.makedirs("versions")

    now = datetime.utcnow()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month,
                                                       now.day, now.hour,
                                                       now.minute, now.second)

    local("tar -cvzf versions/{} web_static".format(archive_name))

    archive_path = "versions/{}".format(archive_name)
    return archive_path if os.path.exists(archive_path) else None
