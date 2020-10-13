### Example 1
Get a handle on the file and disk usage 
The _shutil_ module offers a number of high-level operations on files and collections of files. In particular, it provides functions that support file copying and removal. It comes under Python's standard utility modules. _disk_usage()_ method is used to get disk usage statistics of the given path. This method returns a named tuple with the attributes _total_, _used_, and _free_. The _total_ attribute represents the total amount of space, the _used_ attribute represents the amount of used space, and the _free_ attribute represents the amount of available space, in bytes.

_psutil_ (Python system and process utilities) is a cross-platform library for retrieving information on the processes currently running and system utilization (CPU, memory, disks, network, sensors) in Python. It's useful mainly for system monitoring, profiling, limiting process resources, and managing running processes. _cpu_percent()_ returns a float showing the current system-wide CPU use as a percentage. When the interval is 0.0 or None (default), the function compares process times to system CPU times elapsed since the last call, returning immediately (non-blocking). That means that the first time it's called it will return a meaningful 0.0 value. When the interval is > 0.0, the function compares process times to system CPU times elapsed before and after the interval (blocking).

**requests Module**
Requests is a Python module that you can use to send all kinds of HTTP requests. It's an easy-to-use library with a lot of features ranging from passing parameters in URLs to sending custom headers and SSL verification. You can add headers, form data, multi-part files, and parameters with simple Python dictionaries.You can then access the response data using the same request.

To use the requests module, you first need to install it. Use the following command to install the request module.  
```
#!/usr/bin/env python3  \
import shutil
import psutil
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage > 75
# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity(): 	   
    print("Everything ok")
else 
	print("Networks checks failed")


```
The network file created was

```
#!/usr/bin/env python3

import requests
import socket

def check_localhost():
    localhost  = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"

def check_connectivity():
    request = requests.get("http://www.google.com")
    k = request.status_code
    print(k)
    return k == 200


```

<!--stackedit_data:
eyJoaXN0b3J5IjpbODI0OTE2NjAxXX0=
-->