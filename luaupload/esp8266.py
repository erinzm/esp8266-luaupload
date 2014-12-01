import click

class ESP8266:
	def connect(protocol, commsoptions):
		if protocol == 'serial':
			# Create serial connection
			try:
				this.connection = serial.Serial(commsoptions.port, commsoptions.baud)
			except:
				click.echo("Could not open serial port {port} at {baud}"
					.format(port=commsoptions.port, baud = commsoptions.baud))
				raise

		elif protocol == 'telnet'
			# Create telnet connection
			


	def send(data):
		if this.protocol == 'serial':
			this.connection.write(data)
		elif this.protocol == 'telnet':
			this.connection.send(data)


	def upload(code, espoptions, protocol, commsoptions):
		if protocol == 'serial':

			# Try to connect to the serial port

			try:
				s = serial.Serial(commsoptions.port, commsoptions.baud)
			except:
				click.echo("Could not open serial port {port} at {baud}"
					.format(port=commsoptions.port, baud = commsoptions.baud))
				raise

			# Get a file set up

			click.echo("Starting download to module...")
			s.write('file.remove("{file}")\n'.format(file=espoptions.filename))
			click.echo('file.remove("{file}")'.format(file=espoptions.filename))
			time.sleep(0.1)

			s.write('file.open("{file}", "w")\n'.format(file=espoptions.filename))
			click.echo('file.open("{file}", "w")'.format(file=espoptions.filename))
			s.write('file.writeline([[print(1)]])\n')
			click.echo('file.writeline([[print(1)]])')
			s.write('file.close()\n')
			click.echo('file.close()')
			time.sleep(0.1)

			s.write('file.open("{file}", "w+")\n'.format(file=espoptions.filename))
			click.echo('file.open("{file}", "w+")'.format(file=espoptions.filename))
			time.sleep(0.1)

			# Now read the data over
			for line in code.splitlines():
				s.write('file.writeline([[{line}]])\n'.format(line=line.strip()))
				click.echo('file.writeline([[{line}]])'.format(line=line.strip()))
				time.sleep(0.25)

			s.write('file.close()\n')
			click.echo('file.close()')

			s.close()

			click.echo("Done downloading to module")
		elif protocol == 'telnet':



	def run(data, protocol, commsoptions):
		pass
