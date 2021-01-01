import psutil, platform, GPUtil, cpuinfo, os, sys, wmi, winreg, getpass
from tabulate import tabulate
from datetime import datetime


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def get_ram():
    # Memory Information
    svmem = psutil.virtual_memory()
    return f"RAM: {get_size(svmem.total)}"


def get_hd():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:

            continue
        return f"HD Total Size: {get_size(partition_usage.total)}"
        # print(f"  Used: {get_size(partition_usage.used)}")
        # print(f"  Free: {get_size(partition_usage.free)}")


def get_gpu():
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        return "GPU: {}".format(gpu_name)


def get_os():
    platform_details = platform.platform()
    if platform_details.__contains__("Windows-10"):
        key = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
        val = r"ReleaseID"

        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key) as key:
            releaseId = int(winreg.QueryValueEx(key, val)[0])

        platform_details = releaseId
        message = "Windows 10 {}".format(platform_details)
    else:
        message = platform_details
    return "OS: {}".format(message)


def get_cpu():
    return "CPU: {}".format(cpuinfo.get_cpu_info()['brand_raw'])


def get_motherboard_serial():
    os_type = sys.platform.lower()
    if "win" in os_type:
        command = "wmic bios get serialnumber"
    elif "linux" in os_type:
        command = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"
    elif "darwin" in os_type:
        command = "ioreg -l | grep IOPlatformSerialNumber"
    return "Motherboard Serial: " + os.popen(command).read().replace("\n", "").replace("	", "").replace(" ", "")

    # output machine serial code: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX


def get_dell_servicetag():
    computer = wmi.WMI()
    bios_info = computer.Win32_SystemEnclosure()
    for info in bios_info:
        return 'Dell Service Tag: ' + info.SerialNumber


# get windows key
def decode_key(rpk):
    rpkOffset = 52
    i = 28
    szPossibleChars = "BCDFGHJKMPQRTVWXY2346789"
    szProductKey = ""

    while i >= 0:
        dwAccumulator = 0
        j = 14
        while j >= 0:
            dwAccumulator = dwAccumulator * 256
            d = rpk[j + rpkOffset]
            if isinstance(d, str):
                d = ord(d)
            dwAccumulator = d + dwAccumulator
            rpk[j + rpkOffset] = int(dwAccumulator / 24) if int(dwAccumulator / 24) <= 255 else 255
            dwAccumulator = dwAccumulator % 24
            j = j - 1
        i = i - 1
        szProductKey = szPossibleChars[dwAccumulator] + szProductKey

        if ((29 - i) % 6) == 0 and i != -1:
            i = i - 1
            szProductKey = "-" + szProductKey
    return szProductKey


def get_key_from_reg_location(key, value='DigitalProductID'):
    arch_keys = [0, winreg.KEY_WOW64_32KEY, winreg.KEY_WOW64_64KEY]
    for arch in arch_keys:
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key, 0, winreg.KEY_READ | arch)
            value, type = winreg.QueryValueEx(key, value)
            # Return the first match
            return decode_key(list(value))
        except (FileNotFoundError, TypeError) as e:
            pass


def get_windows_product_key_from_reg():
    return get_key_from_reg_location('SOFTWARE\Microsoft\Windows NT\CurrentVersion')


def get_windows_product_key_from_wmi():
    w = wmi.WMI()
    try:
        product_key = w.softwarelicensingservice()[0].OA3xOriginalProductKey
        if product_key != '':
            return product_key
        else:
            return None
    except AttributeError:
        return None


def get_windows_key():
    if __name__ == '__main__':
        # print('Windows Key from WMI: %s' % get_windows_product_key_from_wmi())
        return 'Windows Key: %s' % get_windows_product_key_from_reg()


def write_to_file():

    with open('computer_info.txt', 'w+') as f:
        f.write(get_cpu() + "\n")
        f.write(get_ram() + "\n")
        f.write(get_hd() + "\n")
        f.write(get_os() + "\n")
        f.write(get_dell_servicetag() + "\n")
        f.write(get_windows_key() + "\n")
        f.write(get_gpu() + "\n")
        f.write(get_motherboard_serial() + "\n")


write_to_file()
print(get_cpu())
print(get_ram())
print(get_hd())
print(get_os())
print(get_dell_servicetag())
print(get_windows_key())
print(get_gpu())
print(get_motherboard_serial())

# user = getpass.getuser()
# print("User: " + user)


# This function is derived from https://gist.github.com/Spaceghost/877110
