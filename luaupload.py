#!/usr/bin/env python
##
# LuaUpload - program to upload Lua scripts to a ESP8266
# Copyright (C) 2014 Liam Marshall
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import sys
import os
import time

import click

from luaupload.esp8266 import ESP8266

esp = ESP8266()


@click.group()
def cli():
	pass

@cli.command()
@click.argument('file')
@click.option('-u', '--url', required=True, help="URL to telnet to. <hostname>:<port>.")
def telnetupload(url, file):
	filename = os.path.split(file)[-1]

	try:
		f = open(file, 'r')
	except:
		click.echo("Could not open file {file}".format(file=file))
		raise

	ip, seperator, port = url.rpartition(':')
	if not seperator:
		port = 3232
	port = int(port)

	esp.connect('telnet', {'ip': ip, 'port': port})

	esp.upload(f.read(), {'filename': filename})


@cli.command()
@click.argument('file')
@click.option('-p', '--port', help="Port to connect to")
@click.option('-b', '--baud', default=9600, help="Baudrate. Defaults to 9600.")
def run(file, port, baud):
	try:
		f = open(file, 'r')
	except:
		click.echo("Could not open file {file}".format(file=file))
		raise

	esp.connect('serial', {'port': port, 'baud': baud})

	esp.run(f.read())

@cli.command()
@click.argument('file')
@click.option('-p', '--port', help="Port to connect to")
@click.option('-b', '--baud', default=9600, help="Baudrate. Defaults to 9600.")
def upload(file, port, baud):
	filename = os.path.split(file)[-1]

	try:
		f = open(file, 'r')
	except:
		click.echo("Could not open file {file}".format(file=file))
		raise

	esp.connect('serial', {'port': port, 'baud': baud})

	esp.upload(f.read(), {'filename': filename})

if __name__ == '__main__':
	cli()
