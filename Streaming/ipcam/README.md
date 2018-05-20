Repositorio Original:
```
wget https://github.com/nickoala/ipcam/archive/master.zip
unzip master.zip
mv ipcam-master ipcam
```

Inside `ipcam/scripts`, there are some shell scripts. They mostly enhance the
usability of `upnpc` and provide more readable output:

- `pf`: create and delete port-forwards to local Raspberry Pi
- `lspf`: List all port-forwards to local Raspberry Pi
- `ipaddr`: Extract all relevant IP addresses

Use `chmod` to make them executable, then move them to `/usr/local/bin`, so
they can be executed like normal Linux commands:

```
cd ipcam/scripts
chmod +x *
sudo cp * /usr/local/bin
```

## Run the bot

```
python3 ~/ipcam/ipcam.py <token>
```

- On startup, it starts mjpg_streamer. No router port is open yet, so the video
  stream is not accessible from outside.
- On receiving `/open`, it opens a port (default: 54321) through the router and
  text you the URL.
- On receiving `/close`, it closes the port on the router, so the video stream
  is no longer accessible from outside.

![](https://github.com/nickoala/ipcam/blob/master/images/ipcam.png?raw=true)

## Bonus

As a bonus, I also have a script,
[whatsmyip.py](https://github.com/nickoala/ipcam/blob/master/whatsmyip.py), a
pure IP-reporting Telegram Bot. Send it any messages, it answers with its public
IP address. If you have any servers running at home, this can be a handy tool.
