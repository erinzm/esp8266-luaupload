import time
import serial
import socket

import click

class ESP8266:
	def connect(self, protocol, commsoptions):
		if protocol == 'serial':
			# Create serial connection
			try:
				self.connection = serial.Serial(commsoptions['port'], commsoptions['baud'])
			except:
				click.echo("Could not open serial port {port} at {baud}"
					.format(port=commsoptions['port'], baud = commsoptions['baud']))
				raise

		elif protocol == 'telnet':
			# Create telnet connection
			try:
				self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((commsoptions['ip'], commsoptions['port']))
			except:
				click.echo("Could not connect to {ip}:{port}"
					.format(ip=commsoptions['ip'], port=commsoptions['port']))
		else:
			click.echo("Invalid protocol.")
			raise ValueError
		self.protocol = protocol


	def send(self, data):
		if self.protocol == 'serial':
			self.connection.write(data)
		elif self.protocol == 'telnet':
			self.connection.send(data)
		click.echo(data)


	def upload(self, data, espoptions={}):
			self.send('file.remove("{file}")\r\n'.format(file=espoptions['filename']))
			time.sleep(0.25)

			self.send('file.open("{file}", "w")\r\n'.format(file=espoptions['filename']))
			self.send('file.writeline([[print(1)]])\r\n')
			self.send('file.close()\r\n')
			time.sleep(0.25)

			self.send('file.open("{file}", "w+")\r\n'.format(file=espoptions['filename']))
			time.sleep(0.25)

			# Now read the data over
			for line in data.splitlines():
				self.send('file.writeline([[{line}]])\r\n'.format(line=line.strip()))
				time.sleep(0.25)

			self.send('file.close()\r\n')

	def run(self, data, espoptions = {}):
		for line in data.splitlines():
			self.send(line)
			time.sleep(0.15)
