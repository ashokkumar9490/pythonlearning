class DeviceError(Exception):
    """Base class is Exception"""

    def __init__(self, errno, msg):
        self.errno = errno
        self.errmsg = msg


try:
    raise DeviceError(1, 'Not Responding')
except DeviceError as de:
    print(f"DeviceError raised... Message -  {de.errmsg} Number - {de.errno}")
