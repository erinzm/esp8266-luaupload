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

from luaupload.eps8266 import ESP8266

esp = ESP8266()

@click.group()
def cli():
	pass

def telnetupload(url, file):

	try:
		f = open(file, 'r')
	except:
		click.echo("Could not open file {file}".format(file=file))
		raise

	ip, seperator, port = url.rpartition(':')
	if not seperator:
		port = 3232
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except:
		click.echo("Could not connect to socket")
		raise

	s.connect((ip, port))

	click.echo("Starting download to module...")
	s.send('file.remove("{file}")\n'.format(file=filename))
	click.echo('file.remove("{file}")'.format(file=filename))
	time.sleep(0.1)

	s.send('file.open("{file}", "w")\n'.format(file=filename))
	click.echo('file.open("{file}", "w")'.format(file=filename))
	s.send('file.writeline([[print(1)]])\n')
	click.echo('file.writeline([[print(1)]])')
	s.send('file.close()\n')
	click.echo('file.close()')
	time.sleep(0.1)

	s.send('file.open("{file}", "w+")\n'.format(file=filename))
	click.echo('file.open("{file}", "w+")'.format(file=filename))
	time.sleep(0.1)

	for line in f:
		s.send('file.writeline([[{line}]])\n'.format(line=line.strip()))
		click.echo('file.writeline([[{line}]])\n'.format(line=line.strip()))
		time.sleep(0.1)

	s.send('file.close()\n')

	s.close()
	f.close()


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

	try:
		s = serial.Serial(port, baud)
	except:
		click.echo("Could not open {port} at {baud}".format(port=port, baud=baud))
		raise

	for line in f:
		s.write(line)
		click.echo(line)
		time.sleep(0.1)

	s.write(line+'\n')

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

	esp.upload(f.readlines(), {'filename': filename},
		'serial', {'port': port, 'baud': baud})

if __name__ == '__main__':
	cli()
