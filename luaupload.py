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
	s.write('file.remove("{file}")\r\n'.format(file=filename))
	click.echo('file.remove("{file}")'.format(file=filename))
	time.sleep(0.1)

	s.write('file.open("{file}", "w")\r\n'.format(file=filename))
	click.echo('file.open("{file}", "w")'.format(file=filename))
	s.write('file.writeline([[print(1)]])\r\n')
	click.echo('file.writeline([[print(1)]])')
	s.write('file.close()\r\n')
	click.echo('file.close()')
	time.sleep(0.1)

	s.write('file.open("{file}", "w+")\r\n'.format(file=filename))
	click.echo('file.open("{file}", "w+")'.format(file=filename))
	time.sleep(0.1)

	for line in f:
		if line.strip() != "":
			s.write('file.writeline([[{line}]])\r\n'.format(line=line.strip()))
			click.echo('file.writeline([[{line}]])'.format(line=line.strip()))
			time.sleep(0.25)

	s.write('file.close()\r\n')
	click.echo('file.close()')

	s.close()
	f.close()

	click.echo("Done downloading to module.")

if __name__ == '__main__':
	upload_file_serial()