import os
import subprocess
import sys

def run_once(func):
    """
    Decorator để đảm bảo rằng hàm chỉ được chạy duy nhất một lần.
    """
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            func(*args, **kwargs)

    wrapper.has_run = False
    return wrapper

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def scan_devices():
    """
    Scan for ADB and Fastboot devices in real-time and return a list of their serial numbers.
    """
    adb_devices = set()
    fastboot_devices = set()
    fastboot = resource_path("bin/windown/fastboot.exe")
    adb = resource_path("bin/windown/adb.exe")

    while True:
        # Run ADB command to list devices
        adb_process = subprocess.Popen([adb, "devices"], stdout=subprocess.PIPE)
        for line in iter(adb_process.stdout.readline, b''):
            # Decode the byte string to a UTF-8 string
            line = line.decode("utf-8").strip()

            # Skip the header and blank lines
            if line.startswith("List of devices attached") or not line:
                continue

            # Extract the serial number
            serial_number = line.split("\t")[0]
            if serial_number not in adb_devices:
                adb_devices.add(serial_number)
                print(f"{serial_number} connected")

        # Run Fastboot command to list devices
        fastboot_process = subprocess.Popen([fastboot, "devices"], stdout=subprocess.PIPE)
        for line in iter(fastboot_process.stdout.readline, b''):
            # Decode the byte string to a UTF-8 string
            line = line.decode("utf-8").strip()

            # Skip the header and blank lines
            if line.startswith("List of devices attached") or not line:
                continue

            # Extract the serial number
            serial_number = line.split("\t")[0]
            if serial_number not in fastboot_devices:
                fastboot_devices.add(serial_number)
                print(f"{serial_number} connected")

        # Check if any devices have been disconnected
        disconnected_devices = adb_devices.union(fastboot_devices) - set(scan_devices_internal())
        if disconnected_devices:
            for serial_number in disconnected_devices:
                print(f"{serial_number} disconnected")
                adb_devices.discard(serial_number)
                fastboot_devices.discard(serial_number)

def scan_devices_internal():
    """
    Internal function to scan for ADB and Fastboot devices and return a list of their serial numbers.
    """
    adb_devices = set()
    fastboot_devices = set()
    fastboot = resource_path("bin/windown/fastboot.exe")
    adb = resource_path("bin/windown/adb.exe")

    # Run ADB command to list devices
    adb_process = subprocess.Popen([adb, "devices"], stdout=subprocess.PIPE)
    for line in iter(adb_process.stdout.readline, b''):
        # Decode the byte string to a UTF-8 string
        line = line.decode("utf-8").strip()

        # Skip the header and blank lines
        if line.startswith("List of devices attached") or not line:
            continue

        # Extract the serial number
        serial_number = line.split("\t")[0]
        adb_devices.add(serial_number)

    # Run Fastboot command to list devices
    fastboot_process = subprocess.Popen([fastboot, "devices"], stdout=subprocess.PIPE)
    for line in iter(fastboot_process.stdout.readline, b''):
        # Decode the byte string to a UTF-8 string
        line = line.decode("utf-8").strip()

        # Skip the header and blank lines
        if line.startswith("List of devices attached") or not line:
            continue

        # Extract the serial number
        serial_number = line.split("\t")[0]
        fastboot_devices.add(serial_number)

    return adb_devices.union(fastboot_devices)
    
    
