#!/usr/bin/python3
"""
    Fabric script that distributes an archive to my web servers
"""
from fabric.api import *
from fabric.operations import run, put, sudo
import os

# specifying the web servers to which the archive will be deployed.
env.hosts = ['54.89.32.136', '52.72.27.194']


def do_deploy(archive_path):
    """
        takes archive_path as an argument, which is the path to the archive to be deployed.
        checks if the specified archive_path exists and is a file.
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        #extracts the filename from the archive path
        archive = archive_path.split("/")[-1]
        path = "/data/web_static/releases"
        # The archive is uploaded to the /tmp/ directory on each server using Fabric's put function.
        put("{}".format(archive_path), "/tmp/{}".format(archive))
        # A folder is created within /data/web_static/releases to store the extracted files from the archive.
        folder = archive.split(".")
        # The archive is extracted into this folder.
        run("mkdir -p {}/{}/".format(path, folder[0]))
        new_archive = '.'.join(folder)
        run("tar -xzf /tmp/{} -C {}/{}/"
            .format(new_archive, path, folder[0]))
        # After extraction, the original archive file in /tmp/ is removed.
        run("rm /tmp/{}".format(archive))
        # Contents of the extracted web_static folder are moved to the appropriate release folder.
        run("mv {}/{}/web_static/* {}/{}/"
            .format(path, folder[0], path, folder[0]))
        # The web_static folder is removed from the release folder.
        run("rm -rf {}/{}/web_static".format(path, folder[0]))
        run("rm -rf /data/web_static/current")
        # A symbolic link (current) is created to point to the latest release folder.
        run("ln -sf {}/{} /data/web_static/current"
            .format(path, folder[0]))
        return True
    except:
        return False
