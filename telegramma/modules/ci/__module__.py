#
# Copyright (C) 2022 Sebastiano Barezzi
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

from telegramma.api import Module, assert_min_api_version

assert_min_api_version(2)

from telegram import BotCommand
from telegram.ext import CommandHandler

from telegramma.modules.ci.main import (
	ci,
)
from telegramma.modules.ci.types.queue import ci_task

class CIModule(Module):
	NAME = "ci"
	VERSION = "1.0"
	HANDLERS = [
		CommandHandler(["ci"], ci),
	]
	COMMANDS = [
		BotCommand("ci", "Start a CI job"),
	]
	TASKS = [
		ci_task,
	]

module = CIModule()
