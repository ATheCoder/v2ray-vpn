This is a repository for showing how you can integrate [tun2socks](https://github.com/xjasonlyu/tun2socks) with a V2Ray proxy in order to achieve
a complete rerouting of the traffic into the proxy. This is very useful for developers/software engineers who deal with a lot of software that lack a
proxy configuration setting and refuse to work with the OS level proxy settings.

### MacOS

#### Download the V2Ray client

First you need to download the [V2Ray Client](https://github.com/v2fly/v2ray-core) and configure it. You can also use any of the V2Ray clients that contain a GUI such as [V2RayN](https://github.com/2dust/v2rayN).

An important note here is that you have to make sure that your v2ray client accepts UDP traffic on its listening *socks* proxy server.

#### Download Tun2Socks

You have to download **Tun2Socks** from its GitHub repository's release page.

First you have to give executation permissions to the binary file using:

```
sudo chmod a+x ./tun2socks
```

Then you can run `tun2socks` like so (note that you should change `1081` to the local port that your *v2ray* client is listening to):

```
sudo ./tun2socks -device utun123 -proxy socks5://127.0.0.1:1081 -interface en5 -tcp-auto-tuning -tcp-rcvbuf 4m -tcp-sndbuf 4m
```


#### Configure the TunDevice and routing table

After you run **Tun2Socks** you have to change MacOS's routing table to make sure that all traffic gets routed into the new *Tun* device.

You can do this by running the `scripts/macos/add-routes.sh` script.

```
sudo bash ./scripts/macos/add-routes.sh
```

*Note that this settings are not persistant and you need to run this script everytime you restart your system*

#### Cleanup

If you want to change your routing table to what it was before so that you can use your Internet connection without the traffic going through v2ray you can run the `./scripts/macos/del-routes.sh` script.

```
sudo bash ./scripts/macos/del-routes.sh
```