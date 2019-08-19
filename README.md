# DNS Over HTTPS Proxy
By default, this Docker image runs the `doh-stub` script which listens for DNS queries and forwards them to a DOH server.
For more information, see [facebookexperimental/doh-proxy](https://github.com/facebookexperimental/doh-proxy).

## Example

### Configure the firewall to accept DNS queries from containers.

If using UFW, run
```
ufw allow in on docker0 to any port 53
```

### Start the container.

```
docker run \
    --detach \
    --publish 53:53/udp \
    --name doh-proxy \
    --restart always \
    v2net/doh-proxy \
        --listen-port 53 \
        --listen-address 0.0.0.0 \
        --domain 1.1.1.1 \
        --remote-address 1.1.1.1
```

### Configure container DNS
Specify the `--dns` option for containers,
or add the "dns" entry to the Docker daemon configuration file `/etc/docker/daemon.json`:
```JSON
{
    "dns": [
        "172.17.0.1"
    ]
}
```

### Configure Host DNS
Optionally, configure the host to use the container's DNS service. Be sure to make a backup of the original settings.

## Build
```
docker pull v2net/doh-proxy:build
docker create --name doh-proxy-build v2net/doh-proxy:build
docker cp doh-proxy-build:/root/source/ ./docker-doh-proxy
docker rm doh-proxy-build
docker build --tag v2net/doh-proxy ./docker-doh-proxy/
```
