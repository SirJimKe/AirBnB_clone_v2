#!/usr/bin/python3
"""
Distributes an archive to your web servers using the function do_deploy
"""

from fabric.api import env, run, put
import os

env.hosts = ['ubuntu@54.236.45.64', 'ubuntu@54.84.213.70']

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
