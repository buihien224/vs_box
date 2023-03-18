"""Project for Mobile Engineer
MC-VS by BHLNK"""

import datetime
from datetime import datetime
import json
import os
import os.path
import random
import re
import shutil
import signal
import string
import subprocess
import sys
import threading
import time
import tkinter
import uuid
import webbrowser
from ctypes import windll
from datetime import date
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

import firebase_admin
import requests
from firebase_admin import credentials, db

import customtkinter

from Crypto.Cipher import AES
import base64
import mouse
import win32mica as mc

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

global trigger
global username
global ver
global break_signal
global download
download = False
username = False
trigger = False
break_signal = False


# --- classes ---


class Redirect:
    def __init__(self, widget, autoscroll=True):
        self.widget = widget
        self.autoscroll = autoscroll

    def write(self, text):
        self.widget.insert(tkinter.END, text)
        self.widget.see(tkinter.END)  # autoscroll

    def flush(self):
        pass


# --- functions ---



def check_free_space(path):
    try:
        stat = shutil.disk_usage(path)
        KB = 1024
        MB = 1024 * KB
        GB = 1024 * MB

        return round(stat.free / GB, 2)
    except:
        print("Fail to check free space")
        return False


def tk_clear(terminal):
    terminal.delete("1.0", tkinter.END)


def send_tk(text, terminal):
    terminal.insert(tkinter.END, text)


part_array = (
    "preloader1:preloader_raw",
    "preloader2:preloader_raw",
    "preloader_a:preloader_raw",
    "preloader_b:preloader_raw",
    "crclist:crclist",
    "sparsecrclist:sparsecrclist",
    "vbmeta_a:vbmeta",
    "vbmeta_b:vbmeta",
    "vbmeta_system_a:vbmeta_system",
    "vbmeta_system_b:vbmeta_system",
    "vbmeta_vendor_a:vbmeta_vendor",
    "vbmeta_vendor_b:vbmeta_vendor",
    "md1img_a:md1img",
    "md1img_b:md1img",
    "spmfw_a:spmfw",
    "spmfw_b:spmfw",
    "mcf_ota_a:mcf_ota",
    "mcf_ota_b:mcf_ota",
    "audio_dsp_a:audio_dsp",
    "audio_dsp_b:audio_dsp",
    "pi_img_a:pi_img",
    "pi_img_b:pi_img",
    "dpm_a:dpm",
    "dpm_b:dpm",
    "scp_a:scp",
    "scp_b:scp",
    "ccu_a:ccu",
    "ccu_b:ccu",
    "vcp_a:vcp",
    "vcp_b:vcp",
    "sspm_a:sspm",
    "sspm_b:sspm",
    "mcupm_a:mcupm",
    "mcupm_b:mcupm",
    "gpueb_a:gpueb",
    "gpueb_b:gpueb",
    "apusys_a:apusys",
    "apusys_b:apusys",
    "mvpu_algo_a:mvpu_algo",
    "mvpu_algo_b:mvpu_algo",
    "gz_a:gz",
    "gz_b:gz",
    "lk_a:lk",
    "lk_b:lk",
    "vendor_boot_a:vendor_boot",
    "vendor_boot_b:vendor_boot",
    "dtbo_a:dtbo",
    "dtbo_b:dtbo",
    "tee_a:tee",
    "tee_b:tee",
    "logo:logo",
    "super:bhlnk",
    "super:super",
    "super:dtbo1",
    "cust:cust",
    "rescue:rescue",
    "boot_a:boot",
    "boot_b:boot",
    "init_boot_a:init_boot",
    "init_boot_b:init_boot",
    "abl_a:abl",
    "abl_b:abl",
    "xbl_a:xbl",
    "xbl_b:xbl",
    "xbl_config_a:xbl_config",
    "xbl_config_b:xbl_config",
    "shrm_a:shrm",
    "shrm_b:shrm",
    "aop_a:aop",
    "aop_b:aop",
    "aop_config_a:aop_config",
    "aop_config_b:aop_config",
    "tz_a:tz",
    "tz_b:tz",
    "devcfg_a:devcfg",
    "devcfg_b:devcfg",
    "featenabler_a:featenabler",
    "featenabler_b:featenabler",
    "hyp_a:hyp",
    "hyp_b:hyp",
    "uefi_a:uefi",
    "uefi_b:uefi",
    "uefisecapp_a:uefisecapp",
    "uefisecapp_b:uefisecapp",
    "modem_a:modem",
    "modem_b:modem",
    "bluetooth_a:bluetooth",
    "bluetooth_b:bluetooth",
    "dsp_a:dsp",
    "dsp_b:dsp",
    "keymaster_a:keymaster",
    "keymaster_b:keymaster",
    "qupfw_a:qupfw",
    "qupfw_b:qupfw",
    "cpucp_a:cpucp",
    "cpucp_b:cpucp",
    "rtice_a:rtice",
    "rtice_b:rtice",
    "rescue:rescue",
    "gsort:gsort",
    "oem_misc1:oem_misc1",
    "storsec_a:storsec",
    "storsec_b:storsec",
    "xbl_ramdump_a:xbl_ramdump",
    "xbl_ramdump_b:xbl_ramdump",
    "imagefv_a:imagefv",
    "imagefv_b:imagefv",
    "recovery_a:recovery",
    "recovery_b:recovery",
    "vm-bootsys_a:vm-bootsys",
    "vm-bootsys_b:vm-bootsys",
    "cmnlib_a:cmnlib",
    "cmnlib_b:cmnlib",
    "cmnlib64_a:cmnlib64",
    "cmnlib64_b:cmnlib64",
    "cam_vpu1_a:cam_vpu1",
    "cam_vpu1_b:cam_vpu1",
    "cam_vpu2_a:cam_vpu2",
    "cam_vpu2_b:cam_vpu2",
    "cam_vpu3_a:cam_vpu3",
    "cam_vpu3_b:cam_vpu3",
    "mitee_a:mitee",
    "mitee_b:mitee",
    "xbl:xbl.elf",
    "xbl_config:xbl.elf",
    "abL:abl.elf",
    "tz:tz.mbn",
    "hyp:hyp.mbn",
    "devcfg:devcfg.mbn",
    "storsec:storsec.mbn",
    "bluetooth:BTFM.bin",
    "cmnlib:cmnlib.mbn",
    "cmnlib64:cmnlib64.mbn",
    "modem:NON-HLOS.bin",
    "dsp:dspso.bin",
    "keymaster:km4.mbn",
    "featenabler:featenabler.mbn",
    "misc:misc.img",
    "aop:aop.mbn",
    "qupfw:qupv3fw.elf",
    "imagefv:imagefv.elf",
    "uefisecapp:uefi_sec.mbn",
    "multiimgoem:multi_image.mbn",
    "vbmeta_system:vbmeta_system.img",
    "vbmeta:vbmeta.img",
    "cache:cache.img",
    "cmnlib64bak:cmnlib64.mbn",
    "cmnlibbak:cmnlib.mbn",
    "hypbak:hyp.mbn",
    "keymasterbak:km4.mbn",
    "tzbak:tz.mbn",
    "aopbak:aop.mbn",
    "xbl_configbak:xbl_config.elf",
    "qupfwbak:qupv3fw.elf",
    "ablbak:abl.elf",
    "devcfgbak:devcfg.mbn",
    "storsecbak:storsec.mbn",
    "xblbak:xbl.elf",
)

# setup variable
fastboot = resource_path("tools/fastboot.exe")
adb = resource_path("tools/adb.exe")

# Setup Firebase

sdk = {
    "type": "service_account",
    "project_id": "mcvs-debug",
    "private_key_id": "7196b8eaf635bb26bd9360a125e68289207b70de",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC9YU2NpVjcPp5z\n+2kVqxdHsVUSg4B9+x/wBmi+EX0v+GQmAQe9m9yXrvD9GwjpYmKxJr5vYNz5/jUB\nLIIvCEgN4scx5r+UdSPTnIjf3MnDaVFvtXGxupvKDI0t+U+zo52nMX0xzejjHFAh\neYJmaGZnRrqc7I81iHzixGEPpUSL+yTz/PqY4IE19tq1i2kEBpgOU8Z5q6ivpOdH\nA+U9OrkzLkIR3BpPpX19fERq6mFDtZdGJcqCPIWVlvEBjGc0iE0j6TQY+T2how3g\n3AqyMG6OHu5xL2mVhYD66856tgTUYzEWYrAUbfu/nVxAkeG60Z8M5p8tARm/p/9X\nCYszyovFAgMBAAECggEAB/h0bNyaZNPJSuc4N+CtQ96ezpE9vFjLsizAmF9OWYg5\nDtT9aUT3yPX2z7lua7sMVFBltJk0M7g30b1mZCDu0I/xKAI5Dxul4TmRXcPLah18\nEauLBgh/cqIcmna+nJPG4bjWW4Gwyv447JRSWBvpU3CSohlL3bfJcvHdhjXoMKdm\nNCCXwGACK5u0pBuChrCBNrcRby8o1rquPK1hv1KmsSChusIZsO19GPcYsJGnVuct\nv2M7JrKm1r5+7CwYQy5FUR0bpKV3CMYJ0fCusxMG9TofQTzuKpy26K8VNW3EnR9y\n+TPBTNKwWKuO/akaltVcgVFdn+a4BrGBuwDeZIWC8QKBgQDhV0YA2U0jp3s3+9VQ\naHYcwEz0cRu4Wh32XvMZiTnqxcqSLfB/+ue85Ia51uWZHQBOKeuhw4re93pBHDlp\nx5cqUJTVv6guybg7mF4Mo41Y7SGcE34dsmDs5y9PzEM/5ciNCxshroOBnX8vxTwu\n/n+O/qnjQSknQn2RmlAnoePXowKBgQDXJX9n+KnhmKaSJJAXPJ2XHVB44nslnjrM\nlYaFQqFeVPMzJ9IoSjXZB/GEI5RAAv53b9Nak/CDibqTpUvKNTtx56EKO01Sd6pN\nYSIhIsoJJFzzwgSCtwP61dGWE09PuLbz2rYdOITcCtglXjWx5JQnFt4PA/7htHHu\n/T0autpldwKBgBtUBj1cHSrRyPPFKt2RjaF3AN40SXRWGYQjh7/1EH0Ud7i6sYwT\n1b7myCAJm9ax2bOhCd6YZGMeCEmVLrFRb1fGZgZ2M+NYu2se02kc/KtoNsdC5eyc\nEX0pnGdFEnLRXz0bt7KiA3jYrPASL3ZTjwy8fcX9xQvp2GisGkR0MbmZAoGABfBK\nCQOrJMgC6QvLUmjg7LfpbbzKq2ons1f5Q5poO+NaZzIVMfmCbQA0IXKd9/pdLczP\nZ7OnsunNVZ/9bJJ1lppPLqoeY0VcVRB2UbXVH9V6H1xepYEJwhW+2EamLMwreKWz\n2zChMjW2a6mjD8sAb+fIr19r3K0PbApfcmpv9tcCgYEAv8QjrC1KiqnoKALLa8yO\nVjO0oYRrNoKZUD4NisjIwXtBzrhGaiPQ3RHuNYdTWKxvbKUtqmJWCp4tPdTceyLE\ndUFpEpaWl03laRmA7kWCSTvnRZfe4bkrbQ0ot0K7IMbe7okiIJBJaLNZvSlVn6+V\n3JFgDM2iW+Mcb7fxm+ke77g=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-10cm4@mcvs-debug.iam.gserviceaccount.com",
    "client_id": "100686756615157550541",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-10cm4%40mcvs-debug.iam.gserviceaccount.com"
}


cred = credentials.Certificate(sdk)
firebase_admin.initialize_app(
    cred, {"databaseURL": "https://mcvs-debug-default-rtdb.firebaseio.com"}
)


def fkash(txt, variable, text_box, tag):
    text_box.configure(state="normal")
    variable.set(txt)
    text_box.configure(state="disabled", text_color=tag)


def local_patch():
    try:
        if (
            type_rom.get() == "MIUIVS"
            or type_rom.get() == "VIETSUB"
            or type_rom.get() == "NSP"
        ):
            filename = askopenfilename(filetypes=[("Check File", ".check")])
            file_path = os.path.dirname(filename)
        elif type_rom.get() == "STOCK":
            filename = askopenfilename(filetypes=[("Flash file", ".bat")])
            file_path = filename
            tk_clear(tk_textbox)
            print("Flash stock fastboot rom with : " + os.path.basename(filename))
            if "lock" in os.path.basename(filename):
                print(
                    "Caution !!! , You choose lock bootloader script but for safety we do not lock your bootloader"
                )
            else:
                if not "storage" in os.path.basename(filename):
                    print(
                        "Install Stock Rom will auto earse all your data. \nChoose flash_all_except_data_storage.bat file to control it !"
                    )
        if not " " in filename:
            fkash(filename, link, patch_r_box, "white")
            patch_r_box.configure(state="normal")
        else:
            fkash("Pick again, Path must not contain 'space' and 'special' ", link, patch_r_box, "white")
            send_tk(
                "Pick again, Path must not contain 'space' and 'special' character \n" + file_path + "\n", tk_textbox
            )
    except:
        fkash("Invaild patch \n", link, patch_r_box, "red")


def install_rom():
    global trigger
    codename = cn_device.get()
    # tk_clear(tk_textbox)
    flash_r.configure(state="disabled")

    if patch_r_box.get():
        print("\n➥ Using manual path ROM: Checking ...")
        filename = patch_r_box.get()
        if (
            type_rom.get() == "MIUIVS"
            or type_rom.get() == "VIETSUB"
            or type_rom.get() == "NSP"
        ):
            if not codename in patch_r_box.get():
                print(codename),
                print("↻ This rom not for your device, please try again")
                flash_r.configure(state="normal")
                return

        else:
            with open(patch_r_box.get()) as fl_script:
                if not codename in fl_script.read():
                    print("↻ This rom not for your device, please try again")
                    flash_r.configure(state="normal")
                    return

    else:
        print("\n➥ Using Downloaded ROM: Checking ...")
        typeofrom = type_rom.get()
        if type_rom.get() == "STOCK":
            sss = list_dsk.get() + typeofrom + "\\" + codename.upper() + "\\flash_all.bat"
            if os.path.isfile(sss):
                filename = sss
            else:
                filename = False
        else:
            sss = (
                list_dsk.get()
                + typeofrom
                + "\\"
                + codename.upper()
                + "\\firmware-update\\"
                + codename
                + ".check"
            )
            if not os.path.isfile(sss):
                filename = False
            else:
                filename = sss

    if filename:
        eny = False
        trigger = True
        if type_rom.get() == "STOCK":
            file_path = os.path.dirname(filename) + "/images"
        elif (
            type_rom.get() == "MIUIVS"
            or type_rom.get() == "VIETSUB"
            or type_rom.get() == "NSP"
        ):
            file_path = os.path.dirname(filename)

        if not (
            os.path.isfile(file_path + "/super.img")
            or os.path.isfile(file_path + "/bhlnk.img")
        ):
            if type_rom.get() == "MIUIVS" or type_rom.get() == "NSP":
                merge = (
                    "copy /b "
                    + file_path
                    + "/lust.img+"
                    + file_path
                    + "/gluttony.img+"
                    + file_path
                    + "/greed.img+"
                    + file_path
                    + "/sloth.img+"
                    + file_path
                    + "/wrath.img+"
                    + file_path
                    + "/envy.img+"
                    + file_path
                    + "/pride.img "
                    + file_path
                    + "/dtbo1.img"
                )
                merge = merge.replace("/", "\\").replace("\\b", "/b")
                print(
                    "It will take some time depending on the computer hardware ! Please be patient"
                )
                p = subprocess.Popen(
                    merge.split(),
                    stdout=subprocess.PIPE,
                    bufsize=1000,
                    text=True,
                    shell=True,
                )
                a = 1
                while p.poll() is None:
                    msg = p.stdout.readline().strip()
                    if msg:
                        tk_clear(tk_textbox)
                        print(
                            "It will take some time depending on the computer hardware ! Please be patient"
                        )
                        print("* processing : " + str(a) + "/10")
                        a = a + 1
                tk_clear(tk_textbox)
                if not os.path.isfile(file_path + "/dtbo1.img"):
                    print("✖ Process failed , Try again !")
                    flash_r.configure(state="normal")
                    return
                eny = True

            else:
                print("✖ Missing Super partition, Stop Flashing !")
                flash_r.configure(state="normal")
                return

        res = os.listdir(file_path)
        time.sleep(1)

        read_phone()

        srnl = serial

        if not type_rom.get() == "STOCK":
            if int(slot) > 1:
                send_tk("\n➥ set active slot : A\n", tk_textbox)
                subprocess.check_output(
                    (fastboot + " --set-active=a ").split(),
                    stderr=subprocess.PIPE,
                    bufsize=1000,
                    text=True,
                    shell=True,
                )
                time.sleep(1)
            if type_rom.get() == "MIUIVS" or type_rom.get() == "NSP":
                try:
                    if authen(srnl) < 1:
                        coin = check_coin(srnl)
                        if coin > 0:
                            coin_dir = db.reference("ROM/MIUIVS").child(serial)
                            try:
                                coin_dir.update({"coin": coin - 1})
                            except:
                                trigger = False
                                flash_r.configure(state="normal")
                                os.remove(file_path + "/dtbo1.img")
                                print_err()
                                return
                        else:
                            trigger = False
                            flash_r.configure(state="normal")
                            os.remove(file_path + "/dtbo1.img")
                            return
                except:
                    print_err()
                    trigger = False
                    flash_r.configure(state="normal")
                    os.remove(file_path + "/dtbo1.img")
                    return

            line = 0
            st = time.time()
            for img in range(0, len(res)):
                if (".img" in res[img]) or (".bin" in res[img]) or (".txt" in res[img]):
                    for i in range(0, len(part_array)):
                        part = part_array[i].split(":")[0]
                        file = file_path + "/" + res[img]
                        if res[img].split(".")[0] == part_array[i].split(":")[1]:
                            # if part in partt:
                            fkash("Flashing", flash, flashing, "yellow")
                            cmd = fastboot + " flash " + part + " " + file
                            p = subprocess.Popen(
                                cmd.split(),
                                stderr=subprocess.PIPE,
                                bufsize=1000,
                                text=True,
                                shell=True,
                            )
                            while p.poll() is None:
                                msg = p.stderr.readline().strip()
                                if msg:
                                    if (
                                        "FAILED (Error reading sparse file)" in msg
                                        or "FAILED (Write to device failed" in msg
                                    ):
                                        print(str(line) + ":  " + msg)
                                        print("\nStop: Error while flasing !")
                                        trigger = False
                                        flash_r.configure(state="normal")
                                        p.terminate()
                                        return
                                    if not (
                                        "No such partition" in msg
                                        or "partition does not exist" in msg
                                        or "fastboot: error: Command failed" in msg
                                    ):
                                        print(str(line) + ":  " + msg)
                                        line = line + 1
                            p.wait()
                            if eny and part == "super":
                                os.remove(file)
                            fkash("Done", flash, flashing, "#08a792")
            fkash("Done", flash, flashing, "#08a792")
            # get the end time
            et = time.time()
            # get the execution time
            elapsed_time = et - st
            print("Execution time:", round(elapsed_time, 2), "seconds")

            try:
                macup = db.reference("ROM/MIUIVS").child(serial)
                macup.update(
                    {"mac": (":".join(re.findall("..", "%012x" % uuid.getnode())))}
                )
            except:
                pass

        else:
            with open(patch_r_box.get()) as fl_script:
                for line in fl_script:
                    if line.startswith("fastboot %* "):
                        if (
                            not line.startswith("fastboot %* getvar")
                            and not line.startswith("fastboot %* reboot")
                            and not line.startswith("fastboot %* oem")
                        ):
                            fkash("Flashing", flash, flashing, "yellow")
                            cmd = (
                                fastboot
                                + " "
                                + line.split("|")[0]
                                .replace("%~dp0\images\\", file_path + "/")
                                .replace("%~dp0images\\", file_path + "/")
                                .replace("fastboot %* ", "")
                                .strip()
                            )
                            p = subprocess.Popen(
                                cmd.split(),
                                stderr=subprocess.PIPE,
                                bufsize=1000,
                                text=True,
                                shell=True,
                            )
                            while p.poll() is None:
                                msg = p.stderr.readline().strip()
                                if msg:
                                    print(msg)
                            fkash("Done", flash, flashing, "#08a792")
                fkash("Done", flash, flashing, "#08a792")

        if formatval.get() == 1:
            fmdat = fastboot + " erase userdata"
            dd = subprocess.Popen(
                fmdat.split(),
                stderr=subprocess.PIPE,
                bufsize=1000,
                text=True,
                shell=True,
            )
            while dd.poll() is None:
                msg = dd.stderr.readline().strip()
                if msg:
                    print(msg)
            fmdat = fastboot + " erase metadata"
            dd = subprocess.Popen(
                fmdat.split(),
                stderr=subprocess.PIPE,
                bufsize=1000,
                text=True,
                shell=True,
            )
            while dd.poll() is None:
                msg = dd.stderr.readline().strip()
                if msg:
                    print(msg)

        if magiskval.get() == 1:
            file = file_path + "/" + "magisk.img"
            file1 = file_path + "/" + "init_boot.img"
            print("\n➥ Rooting with Magisk boot ")
            if os.path.isfile(file):
                fkash("Flashing", flash, flashing, "yellow")
                if os.path.isfile(file1):
                    cmd = fastboot + " flash " + "init_boot " + file
                else :
                    cmd = fastboot + " flash " + "boot " + file
                p = subprocess.Popen(
                    cmd.split(),
                    stderr=subprocess.PIPE,
                    bufsize=1000,
                    text=True,
                    shell=True,
                )
                while p.poll() is None:
                    msg = p.stderr.readline().strip()
                    if msg:
                        print(msg)
                fkash("Done", flash, flashing, "#08a792")
            else:
                print("No Magisk boot found, report Dev !")

        if rebootval.get() == 1:
            print("")
            print("➥ Reboot device, enjoy your ROM \n")
            subprocess.Popen(
                (fastboot + " reboot").split(),
                stderr=subprocess.PIPE,
                bufsize=1000,
                text=True,
                shell=True,
            )

        if clearval.get() == 1:
            print("➾ Clear Download ROM to save your PC's storage")
            try:
                typeofrom = type_rom.get()
                dict_dl = list_dsk.get() + typeofrom + "/" + nameofdev.upper()
                if os.path.isdir(dict_dl):
                    shutil.rmtree(dict_dl)
            except:
                print("Skip clear manual path ROM !")

        trigger = False
        theard_check_device()
    else:
        print("✖ No Local ROM found")
        trigger = False

    flash_r.configure(state="normal")
    trigger = False


def theard_install_rom():
    f = threading.Thread(target=install_rom, daemon=True)
    f.start()


def online_check(namecode):
    tk_clear(tk_textbox)
    # getting rclone config pass
    os.environ["RCLONE_CONFIG_PASS"] = (
        db.reference("ROM/RCLONE").child("THISISNOTPASS").get()
    )

    global nameofdev
    global branchofrom
    global nameofdev_dev

    nameofdev = namecode
    branchofrom = "STABLE"

    if branchofrom == "BETA":
        nameofdev_dev = namecode + "pre"
    else:
        nameofdev_dev = namecode

    srnl = serial

    link.set("")
    rt = False
    pass_auth = False
    fkash("Running", flash, flashing, "yellow")
    if type_rom.get() == "MIUIVS" or type_rom.get() == "NSP":
        reset_mac = True
        try:
            if not namecode:
                mac_reg = (
                    ":".join(re.findall("..", "%012x" % uuid.getnode()))
                ).replace(":", "")
                namecode = (
                    db.reference("ROM/MACADD").child(mac_reg).child("device").get()
                )
                srnl = db.reference("ROM/MACADD").child(mac_reg).child("serial").get()
                nameofdev_dev = namecode

                if namecode:
                    reset_mac = False
        except:
            pass
        if namecode:
            if not username:
                test_auth = authen(srnl)
                coin = check_coin(srnl)
                if not test_auth == "error":
                    if test_auth == "False":
                        reg = register()
                        if reg:
                            pass_auth = True
                            dayrm = authen(srnl)
                            coin = check_coin(srnl)
                    else:
                        if test_auth >= 1:
                            pass_auth = True
                            dayrm = test_auth
                            print("➥ Remaining usage days : ", dayrm)
                            print("➥ Remaining coin : ", coin)
                            print("")
                        else:
                            print("➥ Remaining usage days : 0")
                            if coin < 1:
                                print("➥ Your subscription has expired, please renew !")
                                reg = register()
                                if reg:
                                    pass_auth = True
                                    dayrm = authen(srnl)
                                    coin = check_coin(srnl)
                            else:
                                print("➥ Remaining coin : ", coin)
                                print("")
                                pass_auth = True
            else:
                print("Login : " + username + "\n")
                pass_auth = True
                dayrm = "admin account"
                coin = "admin account"

            if pass_auth:
                if checkd == "adb":
                    vietsub = (
                        subprocess.check_output(
                            [adb, "shell", "getprop", "ro.bhlnk.vietsub"],
                            stderr=subprocess.STDOUT,
                            shell=True,
                        )
                        .decode("utf-8")
                        .rstrip()
                        .split("\n")[0]
                    )
                    try:
                        if vietsub:
                            full_build = (
                                subprocess.check_output(
                                    [
                                        adb,
                                        "shell",
                                        "getprop",
                                        "ro.system.build.version.incremental",
                                    ],
                                    stderr=subprocess.STDOUT,
                                    shell=True,
                                )
                                .decode("utf-8")
                                .rstrip()
                                .split("\n")[0]
                                .split(".VS")
                            )
                            miui_ver = full_build[0]
                            build_date = full_build[1]
                            print("➾ Check Rom infomation")
                            print("  ⋆ MIUI : " + miui_ver)
                            print("  ⋆ MIUIVS : " + vietsub)
                            print("  ⋆ Build Date : " + build_date)
                            print("")
                        else:
                            print("↻ We only support check rom detail in MIUIVS ")
                    except:
                        print("↻ Can't read ROM information, skip it !\n")

                print(
                    "➥ Search all "
                    + type_rom.get()
                    + " builds avalable for : "
                    + nameofdev_dev.upper()
                )
                
                report_link = list_sever.get() + ":/" + type_rom.get() + "/" + branchofrom + "/" + nameofdev_dev.upper()
                check_link = resource_path("tools/rclone.exe") + " lsjson " + report_link
                
                try:
                    get_stable = subprocess.check_output((check_link),text=True,shell=True)
                    #sort by date
                    json_list = json.loads(get_stable)
                    json_list.sort(key=lambda x: datetime.fromisoformat(x['ModTime'].replace('Z', '+00:00')))
                    pass_rom = True
                except:
                    pass_rom = False
                    
                addtodown = []
                addtosb = []
                addtodev = []
                if pass_rom:
                    try:
                        print("")
                        for rom in json_list:
                            if rom["Name"] :
                                max_value=rom["Name"]
                                addtodown.append(rom["Name"])
                                check_branch = len(rom["Name"].split("_")[2].split("."))
                                if check_branch == 6 :
                                    addtodev.append(rom["Name"])
                                    maxdv = rom["Name"]
                                else :
                                    addtosb.append(rom["Name"])
                                    maxsb = rom["Name"]
                                combobox1.configure(values=addtodown)
                        if max_value:
                            count=1
                            print("✦ STABLE build :")      
                            for sb in addtosb:
                                    if sb == maxsb :
                                        print("  " + str(count) + " : " + sb + "  (latest)") 
                                    else:
                                        print("  " + str(count) + " : " + sb) 
                                    count=count+1
                            print("")
                            count=1
                            print("✦ DEV build :")
                            for dv in addtodev:    
                                    if dv == maxdv :
                                        print("  " + str(count) + " : " + dv + "  (latest)") 
                                    else:
                                        print("  " + str(count) + " : " + dv) 
                                    count=count+1
                            combobox_var.set(max_value)
                        else :
                            print("  ✖ No build")
                            rt = "No build available"            
                    except:
                        report_mess = "Err. massage : " + report_link                      
                        print("  ✖ Error ! Report to admin : https://t.me/miuivs ")
                        print("  " + report_mess)
                        fkash("Error", flash, flashing, "pink")
                else:
                    print("  ✖ No build")
                    rt = "No build available"
                fkash("Done", flash, flashing, "#08a792") 
            else:
                print("   > Fail to Auth")
                fkash("Error", flash, flashing, "pink")
                return
        else:
            print_err()
    else:
        if namecode:
            print(
                "➥ Search all "
                + type_rom.get()
                + " builds avalable for : "
                + nameofdev_dev.upper()
            )
            
            report_link = list_sever.get() + ":/" + type_rom.get() + "/" + branchofrom + "/" + nameofdev_dev.upper()
            check_link = resource_path("tools/rclone.exe") + " lsjson " + report_link
            
            try:
                get_stable = subprocess.check_output((check_link),text=True,shell=True)
                #sort by date
                json_list = json.loads(get_stable)
                json_list.sort(key=lambda x: datetime.fromisoformat(x['ModTime'].replace('Z', '+00:00')))
                pass_rom = True
            except:
                pass_rom = False
                
            addtodown = []
            if pass_rom:
                try:
                    print("")
                    for rom in json_list:
                        if rom["Name"] :
                            max_value=rom["Name"]
                            addtodown.append(rom["Name"])
                            check_branch = len(rom["Name"].split("_")[2].split("."))
                            if check_branch == 6 :
                                addtodev.append(rom["Name"])
                                maxdv = rom["Name"]
                            else :
                                addtosb.append(rom["Name"])
                                maxsb = rom["Name"]
                            combobox1.configure(values=addtodown)
                            
                    if max_value:
                        count=1
                        print("✦ STABLE build :")      
                        for sb in addtosb:
                                if sb == maxsb :
                                    print("  " + str(count) + " : " + sb + "  (latest)") 
                                else:
                                    print("  " + str(count) + " : " + sb) 
                                count=count+1
                        print("")
                        count=1
                        print("✦ DEV build :")
                        for dv in addtodev:    
                                if dv == maxdv :
                                    print("  " + str(count) + " : " + dv + "  (latest)") 
                                else:
                                    print("  " + str(count) + " : " + dv) 
                                count=count+1
                        
                        combobox_var.set(max_value)
                    else :
                        print("  ✖ No build")
                        rt = "No build available"  
                except:
                    report_mess = "Err. massage : " + report_link                      
                    print("  ✖ Error ! Report to admin : https://t.me/miuivs ")
                    print("  " + report_mess)
                    fkash("Error", flash, flashing, "pink")
            else:
                print("  ✖ No build")
                rt = "No build available"
            fkash("Done", flash, flashing, "#08a792") 
        else:
            print_err()

    return rt


def theard_check_online(namecode):
    threading.Thread(target=online_check, args=[namecode], daemon=True).start()


def download_rom():
    try:
        btn2.configure(state="disabled")
        check_btn.configure(state="disabled")

        if combobox1.get():
            tk_clear(tk_textbox)
            typeofrom = type_rom.get()
            link_dl = (
                list_sever.get()
                + ":/"
                + typeofrom
                + "/"
                + branchofrom
                + "/"
                + nameofdev_dev.upper()
                + "/"
                + combobox1.get()
            )
            dict_dl = list_dsk.get() + typeofrom + "/" + nameofdev_dev.upper()
            file_dled = (
                list_dsk.get()
                + typeofrom
                + "/"
                + nameofdev_dev.upper()
                + "/"
                + combobox1.get()
            )
            dl_link = (
                resource_path("tools/rclone.exe") + " copy " + link_dl + " " + dict_dl + " -P"
            )

            sp = check_free_space(list_dsk.get().split("\\")[0] + "\\")
            print("Free space : ", sp, " GB")
            if sp > 20:
                try:
                    if os.path.isdir(dict_dl):
                        shutil.rmtree(dict_dl)
                except:
                    pass

                fkash("⇓ Downloading", flash, flashing, "yellow")
                print("⇓ Downloading .... ", combobox1.get())

                try:
                    download = subprocess.Popen(
                        dl_link.split(),
                        stdout=subprocess.PIPE,
                        bufsize=1,
                        universal_newlines=True,
                        text=True,
                        shell=True,
                    )
                    for line in download.stdout:
                        line = line.strip()
                        if line.startswith("*"):
                            percent = line.split(":")[1].split("%")[0]
                            tk_clear(tk_textbox)
                            sp = check_free_space(list_dsk.get().split("\\")[0] + "\\")
                            print("Free space : ", sp, " GB")
                            print("➥ File : ", combobox1.get())
                            print("⇓ Downloading : " + percent + "%")
                            time.sleep(1)
                except:
                    btn2.configure(state="normal")
                    check_btn.configure(state="normal")
                    print("✘ Download Error, redownload !")
                    print("")
                    fkash("Error", flash, flashing, "pink")
                    return

                fkash("⇓ Extracting", flash, flashing, "orange")
                print("⇓ Extracting .... ", combobox1.get())
                ext_link = (
                    resource_path("tools/7za1.exe")
                    + " x -sopg "
                    + file_dled
                    + " -o"
                    + dict_dl
                )
                try:
                    extr = subprocess.Popen(
                        ext_link.split(),
                        stdout=subprocess.PIPE,
                        bufsize=1,
                        universal_newlines=True,
                        text=True,
                        shell=True,
                    )
                    for line in extr.stdout:
                        line = line.strip()
                        if "%" in line:
                            tk_clear(tk_textbox)
                            percent = line.split("%")[0]
                            print("➥ File : ", combobox1.get())
                            print("⇓ Extracting : " + percent + "%")
                            time.sleep(1)

                except:
                    print("✘ Extraction Error, redownload !")
                    print("")
                    fkash("Error", flash, flashing, "pink")
                    return

                try:
                    if os.path.isfile(file_dled):
                        os.remove(file_dled)
                        fkash("Done", flash, flashing, "#08a792")
                except:
                    print("Failed to delete compressed file, skip it \n")

                if checkd == "fastboot":
                    print("➥ Fastboot mode detect, wait 5s before auto install")
                    flash_r.configure(state="disabled")
                    for x in range(5, 0, -1):
                        fkash(x, flash, flashing, "white")
                        time.sleep(1)
                    pre_flash()
                else:
                    print("➥ Download an Extract is Done !")
                    print("➥ Turn into fastboot mode then hit FLASH button to Install")
                    print("")

            else:
                print("✖ No enough storage, we need more than 20GB !")
                print("")
                fkash("Error", flash, flashing, "pink")

        btn2.configure(state="normal")
        check_btn.configure(state="normal")
    except:
        tk_clear(tk_textbox)
        print("➥ Nothing to download, Online Check first !")
        btn2.configure(state="normal")
        check_btn.configure(state="normal")


def theard_download_rom():
    threading.Thread(target=download_rom, daemon=True).start()


def print_err():
    flash_r.configure(state="normal")
    print("✖ Fail to connect Sever , check some reason below :")
    print("    ➤ Internet connection")
    print("    ➤ Correct Clock")
    print("    ➤ No device found")
    print("")
    fkash("Error", flash, flashing, "pink")


def authen(serial):
    try:
        databs = db.reference("ROM/MIUIVS").child(serial)
        is_bought = databs.child("bought").get()
        if is_bought == True:
            fulldate = databs.child("buy_date").get().split("/")
            dayf = fulldate[0]
            monf = fulldate[1]
            yaf = fulldate[2]
            expirefire = databs.child("expire").get()

            today = date.today()
            crtdatev = today.strftime("%d")
            crtmonthv = today.strftime("%m")
            crtyearv = "20" + today.strftime("%y")

            d1 = date(int(crtyearv), int(crtmonthv), int(crtdatev))
            d0 = date(int(yaf), int(monf), int(dayf))
            delta = d1 - d0
            usage = int(expirefire) - delta.days

            return int(usage)
        else:
            return False
    except:
        print_err()
        return "error"


def check_coin(serial):
    try:
        databs = db.reference("ROM/MIUIVS").child(serial)
        is_bought = databs.child("bought").get()
        if is_bought == True:
            coin = databs.child("coin").get()
            return int(coin)
        else:
            return 0
    except:
        return 0


def register():
    try:
        dialog = customtkinter.CTkInputDialog(
            master=None, text="Enter your Installation Key", title="Auth MIUIVS"
        )
        a = dialog.get_input()
        inputdia = True
    except:
        inputdia = False

    if inputdia and a:
        
        ho = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'
        la = b'\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f'
        
        ciphertext = base64.b64decode(a)
        cipher = AES.new(ho, AES.MODE_CBC, la)
        plaintext = cipher.decrypt(ciphertext)
        padding_len = plaintext[-1]
        plaintext = plaintext[:-padding_len]
        base64_string = plaintext.decode('utf-8')

        codedevice = base64_string.split(".")[0]
        datev = base64_string.split(".")[1]
        monthv = base64_string.split(".")[2]
        yearv = base64_string.split(".")[3]
        expire = base64_string.split(".")[4]
        keydevice = base64_string.split(".")[5]
        author = base64_string.split(".")[6]

        today = date.today()
        crtdatev = today.strftime("%d")
        crtmonthv = today.strftime("%m")
        crtyearv = "20" + today.strftime("%y")

        d1 = date(int(crtyearv), int(crtmonthv), int(crtdatev))
        d0 = date(int(yearv), int(monthv), int(datev))
        delta = d1 - d0
        usage = int(expire) - delta.days

        if usage < 1 and delta < 10:
            print("✖ Key expired, please renew \n")
            return False

        if not keydevice == serial:
            print("✖ This key not for your device, please try again")
            return False
        else:
            try:
                upload = db.reference("ROM/MIUIVS").child(serial)
                upload.update(
                    {
                        "bought": True,
                        "buy_date": crtdatev + "/" + crtmonthv + "/" + crtyearv,
                        "expire": expire,
                        "mac": (":".join(re.findall("..", "%012x" % uuid.getnode()))),
                        "author": author,
                        "device": codedevice,
                        "key": a,
                    }
                )
            except:
                pass

            try:
                upload1 = (
                    db.reference("ROM/KTV")
                    .child("log")
                    .child(username)
                    .child("registed")
                    .child(serial)
                )
                upload1.update(
                    {
                        "bought": True,
                        "buy_date": crtdatev + "/" + crtmonthv + "/" + crtyearv,
                        "expire": expire,
                        "mac": (":".join(re.findall("..", "%012x" % uuid.getnode()))),
                        "author": author,
                        "device": codedevice,
                        "key": a,
                    }
                )
            except:
                pass
            flash_r.configure(state="normal")
            return True

    else:
        flash_r.configure(state="normal")
        return False


def pre_flash():

    srnl = serial

    if checkd == "fastboot":
        if state1 == "yes":
            flash_r.configure(state="disabled")
            if type_rom.get() == "MIUIVS" or type_rom.get() == "NSP":

                if authen(srnl) == "error":
                    flash_r.configure(state="normal")
                    return
                else:
                    if authen(srnl) == False:
                        reg = register()
                        if reg == True:
                            theard_install_rom()
                        else:
                            flash_r.configure(state="normal")
                            return
                    else:
                        if authen(srnl) > 0 or check_coin(srnl) > 0:
                            theard_install_rom()
                        else:
                            reg = register()
                            if reg == True:
                                theard_install_rom()
                            else:
                                flash_r.configure(state="normal")
                                return
            else:
                theard_install_rom()
        else:
            tk_clear(tk_textbox)
            print("➥ Bootloader locked, unlock before flash anything !")
        flash_r.configure(state="normal")
    else:
        if checkd == "adb":
            if not lockstate == "locked":
                print("➥ Turn into fastboot mode then hit FLASH button to Install ツ")
            else:
                print("➥ Bootloader locked, unlock before flash anything !")


def theard_auth():
    threading.Thread(target=pre_flash, daemon=True).start()

def check_device():
    global codename
    global checkd
    global serial
    global slot
    global state1
    global lockstate
    letters = string.ascii_letters
    rdz = "".join(random.choice(letters) for i in range(8))
    while True:
        if trigger:
            break
        try:

            serial = (
                subprocess.check_output(
                    [adb, "devices"], stderr=subprocess.STDOUT, shell=True
                )
                .decode("utf-8")
                .rstrip()
                .split("\n")[1]
                .split("device")[0]
                .replace("\t", "")
            )
            codename = (
                subprocess.check_output(
                    [adb, "shell", "getprop", "ro.product.board"],
                    stderr=subprocess.STDOUT,
                    shell=True,
                )
                .decode("utf-8")
                .rstrip()
                .split("\n")[0]
            )
            if codename.endswith("in"):
                codename = codename.replace("in", "")
                
            lockstate = (
                subprocess.check_output(
                    [adb, "shell", "getprop", "ro.secureboot.lockstate"],
                    stderr=subprocess.STDOUT,
                    shell=True,
                )
                .decode("utf-8")
                .rstrip()
                .split("\n")[0]
            )
            if not lockstate == "locked":
                unl.set("unlocked: yes")
                state1 = "yes"
            else:
                unl.set("unlocked: no")
            state.set("ADB connected")
            state1 = "no"
            checkd = "adb"

        except:
            try:
                serial = (
                    subprocess.check_output(
                        [fastboot, "devices"], stderr=subprocess.STDOUT, shell=True
                    )
                    .decode("utf-8")
                    .rstrip()
                    .split("fastboot")[0]
                    .replace("\t", "")
                )
                if serial:
                    code1 = (
                        subprocess.check_output(
                            [fastboot, "getvar", "product"],
                            stderr=subprocess.STDOUT,
                            shell=True,
                        )
                        .splitlines()[0]
                        .decode("utf-8")
                    )
                    codename = str(code1).split("product: ")[1]
                    if codename.endswith("in"):
                        codename = codename.replace("in", "")

                    state_bl = (
                        subprocess.check_output(
                            [fastboot, "getvar", "unlocked"],
                            stderr=subprocess.STDOUT,
                            shell=True,
                        )
                        .splitlines()[0]
                        .decode("utf-8")
                    )
                    state1 = str(state_bl).split("unlocked: ")[1]
                    unl.set("unlocked: " + state1)

                    try:
                        code2 = (
                            subprocess.check_output(
                                [fastboot, "getvar", "slot-count"],
                                stderr=subprocess.STDOUT,
                                shell=True,
                            )
                            .splitlines()[0]
                            .decode("utf-8")
                        )
                        slot = str(code2).split("slot-count: ")[1]
                    except:
                        slot = 1

                    state.set("Fastboot connected")
                    checkd = "fastboot"
                else:
                    cn_device.set("No devices")
                    codename = ""
                    checkd = False
                    serial = ""
                    state.set("Plug in device !")
                    token.set("")
                    unl.set("")
            except:
                cn_device.set("No devices")
                codename = ""
                checkd = False
                serial = ""
                state.set("Plug in device !")
                token.set("")
                unl.set("")

        if checkd:
            cn_device.set(codename)
            token.set(rdz + "." + serial + "." + codename)


def theard_check_device():
    threading.Thread(target=check_device, daemon=True).start()


def read_phone():
    # tk_clear(tk_textbox)
    try:
        if checkd == "fastboot":
            for i in "product", "serialno", "unlocked", "slot-count", "current-slot":
                testabc = (
                    subprocess.check_output(
                        [fastboot, "getvar", i], stderr=subprocess.STDOUT, shell=True
                    )
                    .splitlines()[0]
                    .decode("utf-8")
                )
                temp = str(testabc).split(i + ": ")[1]
                txt = i + ": " + temp + "\n"
                send_tk(txt, tk_textbox)

        elif checkd == "adb":
            for i in (
                "product.brand",
                "product.device",
                "product.manufacturer",
                "product.name",
                "build.date",
                "build.fingerprint",
                "build.id",
                "build.version.incremental",
                "build.version.release",
                "build.version.sdk",
            ):
                props_c = "getprop ro.product." + i
                temp = (
                    subprocess.check_output(
                        [adb, "shell", "getprop", props_c],
                        stderr=subprocess.STDOUT,
                        shell=True,
                    )
                    .decode("utf-8")
                    .rstrip()
                    .split("\n")[0]
                )
                txt = i + ": " + temp + "\n"
                send_tk(txt, tk_textbox)
        else:
            send_tk("Connect Device first <3", tk_textbox)
            cn_device.set("No devices")
    except:
        send_tk("Connect Device first <3", tk_textbox)
        cn_device.set("No devices")


def reboot_n():
    global trigger
    trigger = True
    time.sleep(1)
    if checkd == "fastboot":
        subprocess.Popen(
            (fastboot + " reboot").split(),
            stderr=subprocess.PIPE,
            bufsize=1000,
            text=True,
            shell=True,
        )
    elif checkd == "adb":
        send_tk
        subprocess.run(
            [adb, "shell", "reboot", "bootloader"], stderr=subprocess.STDOUT, shell=True
        )
    trigger = False
    theard_check_device()


def t_reboot_n():
    threading.Thread(target=reboot_n, daemon=True).start()


def reboot_bln():
    global trigger
    trigger = True
    time.sleep(1)
    if checkd == "fastboot":
        subprocess.Popen(
            (fastboot + " reboot bootloader").split(),
            stderr=subprocess.PIPE,
            bufsize=1000,
            text=True,
            shell=True,
        )
    elif checkd == "adb":
        subprocess.run(
            [adb, "shell", "reboot", "bootloader"], stderr=subprocess.STDOUT, shell=True
        )
    trigger = False
    theard_check_device()


def t_reboot_bln():
    print("Reboot : Fastboot")
    threading.Thread(target=reboot_bln, daemon=True).start()


def reboot_rcn():
    global trigger
    trigger = True
    time.sleep(1)
    if checkd == "fastboot":
        subprocess.Popen(
            (fastboot + " reboot recovery").split(),
            stderr=subprocess.PIPE,
            bufsize=1000,
            text=True,
            shell=True,
        )
    elif checkd == "adb":
        subprocess.run(
            [adb, "shell", "reboot", "reboot"], stderr=subprocess.STDOUT, shell=True
        )
    trigger = False
    theard_check_device()


def t_reboot_rcn():
    print("Reboot : System")
    threading.Thread(target=reboot_rcn, daemon=True).start()


def local_pick():
    try:
        filename = askopenfilename(filetypes=[("Check File", ".img .bin")])

        fkash(filename, part, part_r_box, "white")
        send_tk("☞ Pick : \n" + filename + "\n", tk_textbox)
    except:
        fkash("✖ Invaild patch \n", part, part_r_box, "red")


def theard_local_pick():
    threading.Thread(target=local_pick, daemon=True).start()


def flash_boot(partti):
    if checkd == "fastboot":
        if part_r_box.get():
            slota = ab_1.get()
            fboot = subprocess.Popen(
                (fastboot + " flash " + partti + slota + part_r_box.get()).split(),
                stderr=subprocess.PIPE,
                bufsize=1000,
                text=True,
                shell=True,
            )
            while fboot.poll() is None:
                msg = fboot.stderr.readline().strip()
                if msg:
                    print(msg)
        else:
            print("↻ Emtpy input \n")
    else:
        print("✖ This function only work in Fastboot mode \n")


def theard_flash_boot(dRecieved):
    threading.Thread(target=flash_boot, args=[dRecieved], daemon=True).start()


def thear_flash_custom():
    cst_r_box.configure(state="disabled")
    parrr = cst_r_box.get()
    threading.Thread(target=flash_boot, args=[parrr], daemon=True).start()
    cst_r_box.configure(state="normal")


def action():
    if lst_action.get() == "Remove Module":
        tk_clear
        print("Run : " + "Remove Module")
        print("plug your phone and waiting ...")
        cnd =(adb + " wait-for-device shell magisk --remove-modules").split()
        
    elif lst_action.get() == "Magisk Boot":
        if patch_r_box.get():
            filename = patch_r_box.get()
            typeofrom = type_rom.get()
            sss = (
                list_dsk.get()
                + typeofrom
                + "\\"
                + codename.upper()
                + "\\firmware-update\\"
                + codename
                + ".check"
            )
            if not os.path.isfile(sss):
                filename = False
            else:
                filename = sss
                
            if filename: 
                file_path = os.path.dirname(filename)
                file = file_path + "/" + "magisk.img"
                file1 = file_path + "/" + "init_boot.img"
                print("\n➥ Rooting with Magisk boot ")
                if os.path.isfile(file):
                    fkash("Flashing", flash, flashing, "yellow")
                    if os.path.isfile(file1):
                        if checkd == "fastboot": 
                            cnd = fastboot + " flash " + "init_boot " + file
                        else:
                            cnd = "echo No action"
                    else :
                        if checkd == "fastboot": 
                            cnd = fastboot + " flash " + "boot " + file
                        else:
                            cnd = "echo No action"
        else:
            print("Patch ROM first")
            cnd = "echo No action"
    elif lst_action.get() == "Format Data":
        print("Your data cant be restore ! be carefull")
        print("➥ wait 10s before clean all data")
        for x in range(10, 0, -1):
            fkash(x, flash, flashing, "white")
            time.sleep(1)
        if checkd == "fastboot": 
            cnd = fastboot + " erase userdata"
        else:
            cnd = "echo No action"
    elif lst_action.get() == "Reboot":
        if checkd == "fastboot": 
            cnd = fastboot + " reboot"
        elif checkd == "adb" :
            cnd = adb + " reboot"
        else :
            cnd = "echo No action"
    else :
        cnd = "echo No action"
        
    fkash("Wating", flash, flashing, "yellow")
    p = subprocess.Popen(cnd,
        stderr=subprocess.PIPE,
        bufsize=1000,
        text=True,
        shell=True,
    )
    while p.poll() is None:
        msg = p.stderr.readline().strip()
        if msg:
            print(msg)
    fkash("Done", flash, flashing, "#08a792")
        
def theard_action():
    threading.Thread(target=action, daemon=True).start()

def CloseWindow(self):
    self.quit()


###### UI


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "sweetkind"
)  # Themes: blue (default), dark-blue, green
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
# app.resizable(False, False)
# app.maxsize(960,500)


# frame left up
frame = customtkinter.CTkFrame(master=app, width=280, height=400)
frame.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW", rowspan=2)

# frame right
frame1 = customtkinter.CTkFrame(master=app, width=250, height=490)
frame1.grid(row=0, column=1, padx=5, pady=5, sticky="NSEW", rowspan=2)

# frame right expan
frame3 = customtkinter.CTkFrame(master=app, width=250)
frame4 = customtkinter.CTkFrame(master=app, width=250)


app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame1.grid_rowconfigure(9, weight=1)
frame4.grid_columnconfigure(0, weight=1)
frame4.grid_rowconfigure(2, weight=1)

# Advanced Panel

noti = tkinter.StringVar()
noti.set("Advanced Panel")
notif = customtkinter.CTkEntry(
    master=frame3,
    width=203,
    height=25,
    border_width=2,
    corner_radius=10,
    textvariable=noti,
    state="disable",
    justify="center",
)
notif.grid(row=0, column=0, padx=12, pady=(10, 0), columnspan=4, sticky="swe")

list_device = customtkinter.StringVar()  # set initial value

combobox = customtkinter.CTkComboBox(
    master=frame3,
    width=140,
    values=[
    ],
    variable=list_device,
)
combobox.grid(row=1, column=0, padx=(10, 2), pady=(5, 0), columnspan=3, sticky="we")

list_device.set("BHLNK")

check_btn = customtkinter.CTkButton(
    master=frame3,
    width=22,
    height=30,
    border_width=0,
    corner_radius=8,
    text="CHECK",
    command=lambda: theard_check_online(combobox.get()),
)
check_btn.grid(row=1, column=3, padx=(2, 10), pady=(5, 0), sticky="we")


patch_r_label = customtkinter.CTkButton(
    master=frame3,
    width=20,
    height=32,
    border_width=0,
    corner_radius=8,
    text="Pick",
    command=theard_local_pick,
)
patch_r_label.grid(row=2, column=0, padx=(10, 2), pady=(5, 0), sticky="we")

part = tkinter.StringVar()
part_r_box = customtkinter.CTkEntry(
    master=frame3,
    width=155,
    height=30,
    border_width=2,
    corner_radius=10,
    textvariable=part,
)
part_r_box.grid(row=2, column=1, padx=(2, 10), pady=(5, 0), columnspan=3, sticky="we")


ab_var = customtkinter.StringVar(value="off")

ab_1 = customtkinter.CTkSwitch(
    master=frame3, text="both slot (AB)", variable=ab_var, onvalue="_ab ", offvalue=" "
)
ab_1.grid(row=3, column=0, padx=(10, 2), pady=(5, 0), columnspan=2, sticky="we")

vboot = customtkinter.CTkButton(
    master=frame3,
    width=15,
    height=32,
    border_width=0,
    corner_radius=8,
    text="vendor boot",
    command=lambda: theard_flash_boot("vendor_boot"),
)
vboot.grid(row=4, column=0, padx=(10, 2), pady=(5, 0), columnspan=2, sticky="we")

boot = customtkinter.CTkButton(
    master=frame3,
    width=15,
    height=32,
    border_width=0,
    corner_radius=8,
    text="boot",
    command=lambda: theard_flash_boot("boot"),
)
boot.grid(row=4, column=2, padx=(0, 0), pady=(5, 0), columnspan=1, sticky="we")


boot = customtkinter.CTkButton(
    master=frame3,
    width=15,
    height=32,
    border_width=0,
    corner_radius=8,
    text="init_boot",
    command=lambda: theard_flash_boot("init_boot"),
)
boot.grid(row=4, column=3, padx=(2, 10), pady=(5, 0), columnspan=1, sticky="we")


cst_r_box = customtkinter.CTkEntry(
    master=frame3,
    width=15,
    height=30,
    border_width=2,
    corner_radius=10,
    placeholder_text="partition",
)
cst_r_box.grid(row=5, column=0, padx=(10, 2), pady=(5, 10), columnspan=2, sticky="we")


eykh = customtkinter.CTkButton(
    master=frame3,
    width=15,
    height=32,
    border_width=0,
    corner_radius=8,
    text="FCP",
    command=thear_flash_custom,
)
eykh.grid(row=5, column=2, padx=(2, 10), pady=(5, 10), columnspan=2, sticky="we")


############################################################################
# ticket
ticketf = tkinter.StringVar()
ticketf.set("Account")
ticket = customtkinter.CTkEntry(
    master=frame4,
    height=25,
    border_width=2,
    corner_radius=10,
    textvariable=ticketf,
    state="disable",
    justify="center",
)
ticket.grid(row=0, column=0, padx=(12), pady=(10, 0), columnspan=4, sticky="swe")


ktv1 = tkinter.StringVar()
ktv1.set("KTV")
ktv = customtkinter.CTkEntry(
    master=frame4,
    height=20,
    width=50,
    border_width=2,
    corner_radius=10,
    textvariable=ktv1,
    state="disable",
    justify="center",
)
ktv.grid(row=1, column=0, padx=(10, 2), pady=(10, 0), sticky="swe")


ktv_g1 = tkinter.StringVar()
ktv_g = customtkinter.CTkEntry(
    master=frame4,
    height=20,
    width=140,
    border_width=2,
    corner_radius=10,
    textvariable=ktv_g1,
    justify="center",
)
ktv_g.grid(row=1, column=1, padx=(2, 10), pady=(10, 0), columnspan=3, sticky="we")


submit_data = customtkinter.CTkTextbox(master=frame4)
submit_data.grid(
    row=2, column=0, padx=12, pady=(5, 10), columnspan=4, rowspan=4, sticky="nswe"
)


postdata = customtkinter.CTkButton(
    master=frame4, width=10, text="Push", bg_color="#3d3d3d"
)
postdata.grid(row=5, column=3, pady=(0, 15), padx=(0, 2), sticky="sw")

getdata = customtkinter.CTkButton(
    master=frame4, width=10, text="Pull", bg_color="#3d3d3d"
)
getdata.grid(row=5, column=2, pady=(0, 15), sticky="se")


############################################################################
# Text box to display output
tk_textbox = tkinter.Text(frame, bd="0", fg="#FFFFFF", font=("", 9))
tk_textbox.grid(
    row=0, column=0, rowspan=10, columnspan=10, padx=10, pady=10, sticky="eswn"
)


def open_cmd():
    subprocess.call(
        "start cmd /K cd "
        + getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__))),
        shell=True,
    )


cmd = customtkinter.CTkButton(
    master=frame, fg_color=None, border_width=2, width=100, text="CMD", command=open_cmd
)
cmd.grid(row=10, column=1, padx=(1, 0), pady=(0, 10), sticky="w")

cn_device = tkinter.StringVar()
entry = customtkinter.CTkEntry(
    master=frame,
    width=100,
    height=25,
    border_width=2,
    corner_radius=10,
    textvariable=cn_device,
)
entry.grid(row=10, column=8, padx=2, pady=(0, 10), sticky="s")

flash = tkinter.StringVar()
flashing = customtkinter.CTkEntry(
    master=frame,
    width=100,
    height=25,
    border_width=2,
    corner_radius=10,
    textvariable=flash,
    state="disabled",
)
flashing.grid(row=10, column=9, padx=(0, 5), pady=(0, 10), sticky="s")


# Frame right
#################################################################################

Beta = tkinter.StringVar()
Beta.set("You're Alone, not Me !")
Betaf = customtkinter.CTkEntry(
    master=frame1,
    height=25,
    border_width=2,
    corner_radius=10,
    textvariable=Beta,
    state="disable",
    justify="center",
)
Betaf.grid(row=0, column=0, padx=12, pady=(10, 0), columnspan=4, sticky="nwe")


type_rom = customtkinter.CTkOptionMenu(
    master=frame1,
    values=["MIUIVS"],
)
type_rom.grid(row=1, column=0, columnspan=2, padx=(10, 2), pady=(5, 0), sticky="nwe")
type_rom.set("MIUIVS")  # set initial value


list_sever = customtkinter.StringVar()  # set initial value
sever = customtkinter.CTkComboBox(master=frame1, width=140, variable=list_sever)

sever.grid(row=1, column=2, columnspan=2, padx=(2, 10), pady=(5, 0), sticky="nwe")

patch_r_label = customtkinter.CTkButton(
    master=frame1,
    width=20,
    height=32,
    border_width=0,
    corner_radius=8,
    text="Patch",
    command=local_patch,
)
patch_r_label.grid(row=2, column=0, padx=(10, 2), pady=(5, 0), sticky="nwe")

onl_check = customtkinter.CTkButton(
    master=frame1,
    width=140,
    height=32,
    border_width=0,
    corner_radius=8,
    text="Online Check",
    command=lambda: theard_check_online(codename),
)
onl_check.grid(row=2, column=1, columnspan=3, padx=(2, 10), pady=(5, 0), sticky="nwe")


link = tkinter.StringVar()
patch_r_box = customtkinter.CTkEntry(
    master=frame1,
    width=205,
    height=30,
    border_width=2,
    corner_radius=10,
    textvariable=link,
)
patch_r_box.grid(row=3, column=0, columnspan=4, padx=12, pady=(5, 0), sticky="nwe")


formatval = tkinter.IntVar()
format = customtkinter.CTkCheckBox(
    master=frame1, text="Format Data", variable=formatval, onvalue=1, offvalue=0
)

clearval = tkinter.IntVar()
clearval.set(1)
clear = customtkinter.CTkCheckBox(
    master=frame1, text="Clear Download", variable=clearval, onvalue=1, offvalue=0
)

magiskval = tkinter.IntVar()
magiskval.set(0)
magisk = customtkinter.CTkCheckBox(
    master=frame1,
    text="Magisk Boot",
    variable=magiskval,
    onvalue=1,
    offvalue=0,
)

rebootval = tkinter.IntVar()
rebootval.set(1)
reboot = customtkinter.CTkCheckBox(
    master=frame1, text="Auto Reboot", variable=rebootval, onvalue=1, offvalue=0
)

lst_action = customtkinter.CTkOptionMenu(
    master=frame1,
    values=["Remove Module", "Format Data", "Magisk Boot", "Reboot"],
)
lst_action.set("Choose action")  # set initial value

action1 = customtkinter.CTkButton(master=frame1, text="Run", command=theard_action)


magisk.grid(row=4, column=0, columnspan=2, padx=(12, 2), pady=(5, 0), sticky="nwe")
format.grid(row=5, column=0, columnspan=2, padx=(12, 2), pady=(5, 0), sticky="nwe")
clear.grid(row=5, column=2, columnspan=2, padx=(2, 10), pady=(5, 0), sticky="nwe")
reboot.grid(row=4, column=2, columnspan=2, padx=(2, 10), pady=(5, 0), sticky="nwe")
lst_action.grid(row=6, column=0, columnspan=3, padx=(12, 2), pady=(5, 0), sticky="nwe")
action1.grid(row=6, column=3, padx=(2, 10), pady=(5, 0), sticky="nwe")

flash_r = customtkinter.CTkButton(
    master=frame1,
    width=200,
    height=32,
    border_width=0,
    corner_radius=8,
    text="FLASH",
    command=theard_auth,
)
flash_r.grid(row=7, column=0, columnspan=4, padx=12, pady=(5, 0), sticky="nwe")





############################################################################

unl = tkinter.StringVar()
unl1 = customtkinter.CTkEntry(
    master=frame1, height=25, border_width=2, corner_radius=10, textvariable=unl
)
unl1.grid(row=9, column=0, padx=(10, 2), pady=(50, 0), sticky="swe", columnspan=2)


state = tkinter.StringVar()
entry2 = customtkinter.CTkEntry(
    master=frame1, height=25, border_width=2, corner_radius=10, textvariable=state
)
entry2.grid(row=9, column=2, padx=(2, 10), pady=(50, 0), sticky="swe", columnspan=2)

token = tkinter.StringVar()
entry1 = customtkinter.CTkEntry(
    master=frame1, height=25, border_width=2, corner_radius=10, textvariable=token
)
entry1.grid(row=10, column=0, padx=(10, 10), pady=(5, 0), sticky="swe", columnspan=4)


############################################################################

combobox_var = customtkinter.StringVar(value="")  # set initial value

combobox1 = customtkinter.CTkComboBox(master=frame1, values=[], variable=combobox_var)
combobox1.grid(row=11, column=0, sticky="sew", padx=10, pady=(5, 0), columnspan=4)

btn2 = customtkinter.CTkButton(
    master=frame1,
    fg_color=None,
    border_width=2,
    width=100,
    text="Download",
    command=theard_download_rom,
)
btn2.grid(row=12, column=2, sticky="swe", padx=(2, 10), pady=(5, 0), columnspan=2)

list_dsk = customtkinter.StringVar()  # set initial value
ls_dsk = customtkinter.CTkComboBox(master=frame1, variable=list_dsk)

ls_dsk.grid(row=12, column=0, sticky="swe", padx=(10, 2), pady=(5, 0), columnspan=2)

btn = customtkinter.CTkButton(
    master=frame1, width=100, text="Recovery", command=t_reboot_rcn
)
btn.grid(row=13, column=2, sticky="swe", padx=(2, 10), pady=(5, 10), columnspan=2)
btn3 = customtkinter.CTkButton(
    master=frame1, width=100, text="Fastboot", command=t_reboot_bln
)
btn3.grid(row=13, column=0, sticky="swe", padx=(10, 2), pady=(5, 10), columnspan=2)
##############################################################################################





app.iconbitmap(resource_path("ico/client.ico"))
tk_textbox.configure(bg="#181b28")

old_stdout = sys.stdout
sys.stdout = Redirect(tk_textbox)

# - rest -


def update():
    print("Please wait a few seconds to load data from the internet <3")
    

    try:
        URL = "https://raw.githubusercontent.com/buihien224/toolbox_notification/main/initial"
        response = requests.get(URL)

        # update list device and sever

        Rclone_config = "https://raw.githubusercontent.com/buihien224/toolbox_notification/main/rclone_cf"
        Rclone_config_response = requests.get(Rclone_config)
        file_cf = resource_path("tools/rclone.conf")
        open(file_cf, "wb").write(Rclone_config_response.content)

        update_sever = db.reference("ROM/SETUP").child("sever_ls").get()
        update_dev = db.reference("ROM/SETUP").child("device_ls").get()

        drives = []
        get_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))).split(":")[0].upper()
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                print(letter)
                print(get_dir)
                if letter.upper() == str(get_dir) :
                    disk = letter.upper() + ":" + (getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))  + "\ROM\\").split(":")[1]
                else:
                    disk = letter.upper() + ":\Toolbox\ROM\\"
                    
                drives.append(disk)
            bitmask >>= 1

        tk_clear(tk_textbox)
        list_sever.set("sever1")
        print(
            response.content.decode("utf-8").replace("\\n", "\n").replace("\\t", "\t")
        )
        sever.configure(values=update_sever)
        combobox.configure(values=update_dev)
        ls_dsk.configure(values=drives)
        list_dsk.set(drives[0])

    except:
        tk_clear(tk_textbox)
        print("Hello, Be happy forever <3")
        sever.configure(values=["sever0", "sever1", "sever2"])
        list_sever.set("sever1")
        list_dsk.set(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))  + "\ROM\\")
        
    try:
        threading.Thread(target=check_device, daemon=True).start()
    except:
        pass
    


def theard_update():
    threading.Thread(target=update, daemon=True).start()
    


def start_MainUI(para, para1):
    login.destroy()
    if para1 == True:
        block_ip.mainloop()
    elif para1 == "Error":
        nocnt.mainloop()
    else :
        ver = para
        if ver:
            w = 1200  # width for the Tk root
            h = 600  # height for the Tk root
            ws = app.winfo_screenwidth()  # width of the screen
            hs = app.winfo_screenheight()  # height of the screen
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            app.geometry("%dx%d+%d+%d" % (w, h, x, y))
            app.title(" MIUIVS ToolBox 53 : Advanced")
            frame3.grid(row=0, column=2, padx=5, pady=5, sticky="NSEW")
            frame4.grid(row=1, column=2, padx=5, pady=5, sticky="NSEW")
            

        else:
            w = 876  # width for the Tk root
            h = 520  # height for the Tk root
            ws = app.winfo_screenwidth()  # width of the screen
            hs = app.winfo_screenheight()  # height of the screen
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            app.geometry("%dx%d+%d+%d" % (w, h, x, y))
            app.title("MIUIVS ToolBox 53 : User")
            
        app.configure(bg="#000000") # Please use BLACK as background color, otherwhise render issues might appear
        HWND=windll.user32.GetParent(app.winfo_id())
        mc.ApplyMica(HWND, ColorMode=mc.MICAMODE.DARK)
        
        app.after(1, theard_update)
        threading.Thread(target=app.mainloop(), daemon=True).start()
    
    

    # sys.stdout = old_stdout

global x1, y1


def standard_bind():
    login.bind("<B1-Motion>", lambda e: event(e, Mode=True))


def event(widget, Mode=False):
    global x1, y1
    if Mode:
        x1 = widget.x
        y1 = widget.y
    login.bind("<B1-Motion>", lambda e: event(e))
    login.geometry(
        "+%d+%d" % (mouse.get_position()[0] - x1, mouse.get_position()[1] - y1)
    )


login = customtkinter.CTk()  # create CTk window like you do with the Tk window
w = 400  # width for the Tk root
h = 240  # height for the Tk root
ws = login.winfo_screenwidth()  # width of the screen
hs = login.winfo_screenheight()  # height of the screen
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
login.geometry("%dx%d+%d+%d" % (w, h, x, y))
login.iconbitmap(resource_path("ico/key.ico"))
login.title("Initial Startup")
login.configure(bg="#000000") # Please use BLACK as background color, otherwhise render issues might appear
HWND=windll.user32.GetParent(login.winfo_id())
mc.ApplyMica(HWND, ColorMode=mc.MICAMODE.DARK)


def button_function():
    global username
    try:
        mac = ":".join(re.findall("..", "%012x" % uuid.getnode()))
        check_mac = db.reference("ROM/Block").child("MAC").child(mac).get()
    except:
        check_mac = "Error"
    
    if not ( user1_entry.get() or pass_entry.get() ) :
        start_MainUI(False, check_mac)
    else:
        try:
            acc = db.reference("ROM/KTV").child(user1_entry.get())
            psssw = acc.get()
        except:
            label.configure(text="Enter corect email and Pass !")
            return
        if str(psssw) == pass_entry.get():
            username = user1_entry.get()
            ktv_g1.set(username)
            start_MainUI(True, check_mac)
        else:
            label.configure(text="Wrong Password !")



def button_function1(event):
    global username
    try:
        mac = ":".join(re.findall("..", "%012x" % uuid.getnode()))
        check_mac = db.reference("ROM/Block").child("MAC").child(mac).get()
    except:
        check_mac = "Error"
    
    if not ( user1_entry.get() or pass_entry.get() ) :
        start_MainUI(False, check_mac)
    else:
        try:
            acc = db.reference("ROM/KTV").child(user1_entry.get())
            psssw = acc.get()
        except:
            label.configure(text="Enter corect email and Pass !")
            return
        if str(psssw) == pass_entry.get():
            username = user1_entry.get()
            ktv_g1.set(username)
            start_MainUI(True, check_mac)
        else:
            label.configure(text="Wrong Password !")


# Use CTkButton instead of tkinter Button
label = customtkinter.CTkLabel(
    master=login, text="Just click LOGIN to enter USER tool", width=120, height=25, corner_radius=8
)
label.place(relx=0.5, rely=0.23, anchor=tkinter.CENTER)

user1_entry_var = tkinter.StringVar()
user1_entry = customtkinter.CTkEntry(
    master=login,
    width=180,
    height=30,
    border_width=2,
    corner_radius=10,
    textvariable=user1_entry_var,
)
user1_entry.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)

pass_entry_var = tkinter.StringVar()
pass_entry = customtkinter.CTkEntry(
    master=login,
    width=180,
    height=30,
    border_width=2,
    corner_radius=10,
    textvariable=pass_entry_var,
    show="*",
)
pass_entry.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(
    master=login, text="LOGIN", command=button_function, border_width=1
)
button.place(relx=0.547, rely=0.65, anchor=customtkinter.CENTER)

# Bind the Enter Key to the window
login.bind("<Return>", button_function1)


block_ip = customtkinter.CTk()  # create CTk window like you do with the Tk window
w = 400  # width for the Tk root
h = 240  # height for the Tk root
ws = block_ip.winfo_screenwidth()  # width of the screen
hs = block_ip.winfo_screenheight()  # height of the screen
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
block_ip.geometry("%dx%d+%d+%d" % (w, h, x, y))
block_ip.title("Lack of Trust")
block_ip.iconbitmap(resource_path("ico/x.ico"))
block_ip.resizable(False, False)
block_ip.configure(bg="#000000") # Please use BLACK as background color, otherwhise render issues might appear
HWND=windll.user32.GetParent(block_ip.winfo_id())
mc.ApplyMica(HWND, ColorMode=mc.MICAMODE.DARK)

label = customtkinter.CTkLabel(
    master=block_ip,
    text="Your PC is Blocked by MIUIVS",
    width=120,
    height=25,
    corner_radius=8,
)
label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


nocnt = customtkinter.CTk()  # create CTk window like you do with the Tk window
w = 400  # width for the Tk root
h = 240  # height for the Tk root
ws = nocnt.winfo_screenwidth()  # width of the screen
hs = nocnt.winfo_screenheight()  # height of the screen
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
nocnt.geometry("%dx%d+%d+%d" % (w, h, x, y))
nocnt.title("Lack of internet")
nocnt.iconbitmap(resource_path("ico/x.ico"))
nocnt.resizable(False, False)
label = customtkinter.CTkLabel(
    master=nocnt,
    text="✖ Fail to connect Sever , check some reason below :\n     ➤ Internet connection\n     ➤ Correct Clock\n     ➤ No device found",
    width=120,
    height=25,
    corner_radius=8,
)
label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


def open_report():
    rp = customtkinter.CTkToplevel(app)
    rp.geometry("850x500")
    rp.title("Maybe you already know")
    rp.iconbitmap(resource_path("ico/ifo.ico"))
    rp.grid_columnconfigure(0, weight=1)
    rp.grid_columnconfigure(1, weight=1)
    rp.grid_rowconfigure(0, weight=1)
    rp.configure(bg="#000000") # Please use BLACK as background color, otherwhise render issues might appear
    HWND=windll.user32.GetParent(rp.winfo_id())
    mc.ApplyMica(HWND, ColorMode=mc.MICAMODE.DARK)

    # frame left
    framer = customtkinter.CTkFrame(master=rp)
    framer.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")
    framer.grid_columnconfigure(0, weight=1)
    framer.grid_rowconfigure(1, weight=1)

    vsub = customtkinter.CTkLabel(
        master=framer,
        text="VIETSUB",
        width=120,
        height=25,
        corner_radius=8,
        text_color="white",
    )
    vsub.grid(row=0, column=0, padx=25, pady=(10, 0), columnspan=4, sticky="swe")

    vietsub_textbox = tkinter.Text(
        framer, bd="0", fg="#FFFFFF", bg="#181b28", font=("", 9)
    )
    vietsub_textbox.grid(row=1, column=0, padx=25, pady=(5, 5), sticky="eswn")

    # frame right
    framel = customtkinter.CTkFrame(master=rp)
    framel.grid(row=0, column=1, padx=5, pady=5, sticky="NSEW")
    framel.grid_columnconfigure(0, weight=1)
    framel.grid_rowconfigure(1, weight=1)

    miuivs = customtkinter.CTkLabel(
        master=framel,
        text="MIUIVS",
        width=120,
        height=25,
        corner_radius=8,
        text_color="white",
    )
    miuivs.grid(row=0, column=0, padx=25, pady=(10, 0), columnspan=4, sticky="swe")

    miuivs_textbox = tkinter.Text(
        framel, bd="0", fg="#FFFFFF", bg="#181b28", font=("", 9)
    )
    miuivs_textbox.grid(row=1, column=0, padx=25, pady=(5, 5), sticky="eswn")

    frameb = customtkinter.CTkFrame(master=rp)
    frameb.grid(row=1, column=0, padx=5, pady=5, sticky="NSEW", columnspan=2)
    frameb.grid_columnconfigure(0, weight=1)
    frameb.grid_columnconfigure(1, weight=1)
    frameb.grid_columnconfigure(2, weight=1)
    frameb.grid_columnconfigure(3, weight=1)
    frameb.grid_columnconfigure(4, weight=1)

    open_tele = customtkinter.CTkButton(
        master=frameb,
        command=lambda: webbrowser.open("https://t.me/miuivs"),
        text="Telegram",
    )
    open_tele.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")

    open_tele = customtkinter.CTkButton(
        master=frameb,
        command=lambda: webbrowser.open("https://t.me/bhlnk_real"),
        text="Chanel",
    )
    open_tele.grid(row=0, column=1, padx=5, pady=5, sticky="NSEW")

    open_tele = customtkinter.CTkButton(
        master=frameb,
        command=lambda: webbrowser.open("https://t.me/anti_tho_online"),
        text="CLI",
    )
    open_tele.grid(row=0, column=2, padx=5, pady=5, sticky="NSEW")

    open_tele = customtkinter.CTkButton(
        master=frameb,
        command=lambda: webbrowser.open("https://www.youtube.com/@LowTechTopic"),
        text="Youtube",
    )
    open_tele.grid(row=0, column=3, padx=5, pady=5, sticky="NSEW")

    open_tele = customtkinter.CTkButton(
        master=frameb,
        command=lambda: webbrowser.open("https://www.facebook.com/vietsubBHLNK"),
        text="Buy Key",
    )
    open_tele.grid(row=0, column=4, padx=5, pady=5, sticky="NSEW")

    try:
        URL = "https://raw.githubusercontent.com/buihien224/toolbox_notification/main/vietsub"
        vsubff = (
            requests.get(URL)
            .content.decode("utf-8")
            .replace("\\n", "\n")
            .replace("\\t", "\t")
        )
    except:
        vsubff = "Cant fetch data from sever"

    send_tk(vsubff, vietsub_textbox)

    try:
        URL = "https://raw.githubusercontent.com/buihien224/toolbox_notification/main/miuivs"
        miuivsff = (
            requests.get(URL)
            .content.decode("utf-8")
            .replace("\\n", "\n")
            .replace("\\t", "\t")
        )
    except:
        miuivsff = "Cant fetch data from sever"

    send_tk(miuivsff, miuivs_textbox)


report = customtkinter.CTkButton(
    master=frame,
    fg_color=None,
    border_width=2,
    width=100,
    text="Information",
    command=open_report,
)
report.grid(row=10, column=0, padx=(5, 0), pady=(0, 10), sticky="w")


def desoi():
    # subprocess.check_output([adb, 'kill-server'],stderr=subprocess.STDOUT, shell=True).decode("utf-8").rstrip()
    try:
        download.send_signal(signal.CTRL_BREAK_EVENT)
        download.kill()
    except:
        sys.exit(0)
    sys.exit(0)


cancel = customtkinter.CTkButton(
    master=login, text="X", command=desoi, border_width=1, width=10
)
cancel.place(relx=0.316, rely=0.65, anchor=customtkinter.CENTER)
nocnt.protocol("WM_DELETE_WINDOW", desoi)
block_ip.protocol("WM_DELETE_WINDOW", desoi)
app.protocol("WM_DELETE_WINDOW", desoi)
login.protocol("WM_DELETE_WINDOW", desoi)


def start_adb():
    subprocess.check_output(
        [adb, "kill-server"], stderr=subprocess.STDOUT, shell=True
    ).decode("utf-8").rstrip()
    subprocess.check_output(
        [adb, "start-server"], stderr=subprocess.STDOUT, shell=True
    ).decode("utf-8").rstrip()


if __name__ == "__main__":

    threading.Thread(target=login.mainloop(), daemon=True).start()
    threading.Thread(target=start_adb, daemon=True).start()
    
    
