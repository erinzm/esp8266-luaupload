## $ LuaUpload_
### A program to upload code to a ESP8266 running ZeroDay's Lua interpreter

[![Stories in Ready](https://badge.waffle.io/archimedespi/esp8266-luaupload.png?label=ready&title=Ready)](https://waffle.io/archimedespi/esp8266-luaupload) [![Issue Stats](http://issuestats.com/github/archimedespi/esp8266-luaupload/badge/issue)](http://issuestats.com/github/archimedespi/esp8266-luaupload)

#### usage

````
$ python luaupload.py --help
Usage: luaupload.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  run
  upload
````

````
Usage: luaupload.py run [OPTIONS] FILE

Options:
  -p, --port TEXT     Port to connect to
  -b, --baud INTEGER  Baudrate. Defaults to 9600.
  --help              Show this message and exit.
````

````
Usage: luaupload.py upload [OPTIONS] FILE

Options:
  -p, --port TEXT     Port to connect to
  -b, --baud INTEGER  Baudrate. Defaults to 9600.
  --help              Show this message and exit.
````

#### lunning the program
On Linux/Mac/*nix, you should install dependencies:
`pip install click pyserial`.
You don't need to do this for the windows release since all the dependencies are bundled into `luaupload.exe`

Get the code with `git clone https://github.com/ArchimedesPi/esp8266-luaupload` or [download a ZIP](https://github.com/ArchimedesPi/esp8266-luaupload/archive/master.zip), or, on Windows, get [a binary](https://github.com/ArchimedesPi/esp8266-luaupload/releases)

Run it on Windows with `luaupload.exe`.
Run it on Linux with `./luaupload.py`.

#### license

GPL, of course.

````
LuaUpload - program to upload Lua scripts to a ESP8266
Copyright (C) 2014 Liam Marshall

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
````
