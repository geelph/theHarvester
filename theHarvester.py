#!/usr/bin/env python3

# Note: This script runs theHarvester
from platform import python_version
import sys
import asyncio

if python_version()[0:3] < '3.7':
    print('\033[93m[!] Make sure you have Python 3.7+ installed, quitting.\n\n \033[0m')
    sys.exit(1)

from theHarvester import __main__

if __name__ == '__main__':
    platform = sys.platform
    if platform == 'win32':
        # Required or things will break if trying to take screenshots
        import multiprocessing
        multiprocessing.freeze_support()
        asyncio.DefaultEventLoopPolicy = asyncio.WindowsSelectorEventLoopPolicy
    else:
        import uvloop
        uvloop.install()
        if platform == "linux":
            import aiomultiprocess
            # As we are not using Windows we can change the spawn method to fork for greater performance
            aiomultiprocess.set_context("fork")
    asyncio.run(__main__.entry_point())

# __main__
