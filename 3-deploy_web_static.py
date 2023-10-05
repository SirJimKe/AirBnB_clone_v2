#!/usr/bin/python3
"""
Creates and distributes an archive to your web servers using the function deploy
"""

from fabric.api import env, local, run
from datetime import datetime
import os

env.hosts = ['ubuntu@54.236.45.64', 'ubuntu@54.84.213.70']

def do_pack():
    """Packs the contents of the web_static folder into a .tgz archive."""
    now = datetime.utcnow()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month,
                                                       now.day, now.hour,
                                                       now.minute, now.second)
    local("mkdir -p versions")
    result = local("tar -czvf versions/{} web_static".format(archive_name))
    if result.failed:
        return None
    return "versions/{}".format(archive_name)

def do_deploy(archive_path):
    """Deploys the archive to the web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        archive_filename = os.path.basename(archive_path)
        folder_name = archive_filename.replace('.tgz', '')

        run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_filename, folder_name))

        run('rm /tmp/{}'.format(archive_filename))

        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(folder_name, folder_name))

        run('rm -rf /data/web_static/current')

        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(folder_name))

        return True

    except Exception as e:
        return False

def deploy():
    """Creates and distributes the archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

if __name__ == "__main__":
    deploy()
