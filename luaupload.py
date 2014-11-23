#!/usr/bin/env python

import sys
import click
import time

import serial

@click.command()
@click.argument('file')
@click.option('-p', '--port')
@click.option('-b', '--baud', default=9600)
@click.option('-r', '--raw', is_flag=True)
def upload_file_serial(file, port, baud, verbose):
	filename = file

	try:
		f = open(file, 'r')
	except:
		echo "Could not open file {file}".format(file = file)

	try:
		s = serial.Serial(port, baud)
	except:
		echo "Could not open {port} at {baud}".format(port, baud)
		sys.exit(1)
	echo("Starting download to module...")
	s.write('file.remove("{file}")'.format(filename))
	echo('file.remove("{file}")'.format(filename))
	s.write('file.open("{file}", "w")'.format(filename))
	echo('file.open("{file}", "w")'.format(filename))

	for line in f:
		s.write('file.writeline([[{line}]])'.format(line))
		echo('file.writeline([[{line}]])'.format(line))

	s.write('file.close()')
	echo('file.close()')

	s.close()

	echo("Done downloading to module.")