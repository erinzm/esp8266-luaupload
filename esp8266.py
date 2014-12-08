import serial
import socket

import click

class ESP8266:
	def connect(self, protocol, commsoptions):
		if protocol == 'serial':
			# Create serial connection
			try:
				this.connection = serial.Serial(commsoptions.port, commsoptions.baud)
			except:
				click.echo("Could not open serial port {port} at {baud}"
					.format(port=commsoptions.port, baud = commsoptions.baud))
				raise

		elif protocol == 'telnet':
			# Create telnet connection
			try:
				this.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((commsoptions.ip, commsoptions.port))
			except:
				click.echo("Could not connect to {ip}:{port}"
					.format(ip=commsoptions.ip, port=commsoptions.port))
		else:
			click.echo("Invalid protocol.")
			raise ValueError


	def send(self, data):
		if this.protocol == 'serial':
			this.connection.write(data)
		elif this.protocol == 'telnet':
			this.connection.send(data)


	def upload(self, code, espoptions, protocol, commsoptions):
			s.write('file.remove("{file}")\n'.format(file=espoptions.filename))
			time.sleep(0.1)

			s.write('file.open("{file}", "w")\n'.format(file=espoptions.filename))
			s.write('file.writeline([[print(1)]])\n')
			s.write('file.close()\n')
			time.sleep(0.1)

			s.write('file.open("{file}", "w+")\n'.format(file=espoptions.filename))
			time.sleep(0.1)

			# Now read the data over
			for line in code.splitlines():
				s.write('file.writeline([[{line}]])\n'.format(line=line.strip()))
				time.sleep(0.25)

			s.write('file.close()\n')

	def run(self, data, protocol, commsoptions):
		for line in data.splitlines():
			self.send(line)
			time.sleep(0.15)
