resource "digitalocean_droplet" "server2" {
    image = "ubuntu-14-04-x64"
    name = "server2"
    region = "sfo2"
    size = "1gb"
    ssh_keys = ["${digitalocean_ssh_key.default.id}"]
}
