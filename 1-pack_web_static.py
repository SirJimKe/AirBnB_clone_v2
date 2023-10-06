#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder."""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Creates a .tgz archive from the contents of the web_static folder."""
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_name = "web_static_{}.tgz".format(timestamp)

        local("tar -cvzf versions/{} web_static".format(archive_name))

        archive_path = "versions/{}".format(archive_name)
        if os.path.exists(archive_path):
            return archive_path
        else:
            return None

    except Exception as e:
        print("An error occurred: {}".format(e))
        return None
