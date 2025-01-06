import os
import sys

#engineVer = 1.04
#toolsMajorVer = 0
#toolsMinorVer = 1
betaMajorVer = 2
betaMinorVer = 7
creator = "Adam1000"

def ClearScreen():
    os.system("cls" if os.name == "nt" else "clear")

def progress_bar(iteration, total, prefix="", suffix="", length=50, print_end="\r"):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = "#" * filled_length + "-" * (length - filled_length)
    sys.stdout.write(f"\r{prefix} [{bar}] {percent}% {suffix}",)
    sys.stdout.flush()
    if iteration == total:
        print(print_end)