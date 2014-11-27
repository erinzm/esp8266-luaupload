## LuaUpload
### Awesome program to upload code to a ESP8266 running ZeroDay's Lua interpreter

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
