#!/usr/bin/python3
"""
    Fabric script that generates tgz archive from contents of web_static
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
        generates a .tgz archine from contents of web_static
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static"
              .format(file_name))

        # Check if the archive was created successfully
        if local("test -e {}".format(file_name), capture=True).succeeded:
            return file_name
    except:
        return None


'''

Function Execution:
When you call the do_pack function in your Python script or Fabric task, it executes a series of steps to create a compressed archive (.tgz) of the contents of the web_static folder.

Steps Performed:

It first ensures that a folder named versions exists in the current directory.
Then, it generates a timestamp using the current UTC time in the format %Y%m%d%H%M%S (Year, Month, Day, Hour, Minute, Second).
Next, it constructs the filename for the archive by concatenating "versions/web_static_" with the generated timestamp and ".tgz".
After that, it creates the archive using the tar command, compressing the contents of the web_static folder into the generated filename.
Finally, it checks if the archive was successfully created by using the test -e <archive_name> command and capturing the output.
Return Value:

If the archive creation process succeeds, the function returns the path to the generated archive (e.g., "versions/web_static_<timestamp>.tgz").
If any error occurs during the archive creation process, or if the archive does not exist after creation, the function returns None.
Execution Context:

The do_pack function runs in the local context, meaning it executes on the machine where the Fabric script is invoked.
When you run the Fabric script, it executes locally on your development machine or wherever you initiate the script. The local function from Fabric executes shell commands on the local machine.
'''

