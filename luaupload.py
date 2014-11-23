#!/usr/bin/env python

import sys
import click
import time

import serial

@click.command()
@click.argument('file')
@click.option('-p', '--port', help="Port to connect to")
@click.option('-b', '--baud', default=9600, help="Baudrate. Defaults to 9600.")
def upload_file_serial(file, port, baud):
	filename = file

	try:
		f = open(file, 'r')
	except:
		click.echo("Could not open file {file}".format(file))
		raise

	try:
		s = serial.Serial(port, baud)
	except:
		click.echo("Could not open {port} at {baud}".format(port, baud))
		raise

	click.echo("Starting download to module...")
	s.write('file.remove("{file}")'.format(filename))
	click.echo('file.remove("{file}")'.format(filename))
	s.write('file.open("{file}", "w")'.format(filename))
	click.echo('file.open("{file}", "w")'.format(filename))

	for line in f:
		s.write('file.writeline([[{line}]])'.format(line))
		click.echo('file.writeline([[{line}]])'.format(line))

	s.write('file.close()')
	click.echo('file.close()')

	s.close()

	click.echo("Done downloading to module.")

if __name__ == '__main__':
	upload_file_serial()