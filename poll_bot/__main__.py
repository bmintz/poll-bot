#!/usr/bin/env python3
# encoding: utf-8

from . import bot

import asyncio
import sys


def main(argv):
	try:
		bot.discordpw_api_token = argv[2]
		bot.run(argv[1])
	except:
		return 1
	else:
		return 0


sys.exit(main(sys.argv))
