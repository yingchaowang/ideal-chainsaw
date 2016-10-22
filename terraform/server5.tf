resource "digitalocean_droplet" "server5" {
    image = "ubuntu-14-04-x64"
    name = "server5"
    region = "sfo2"
    size = "1gb"
    ssh_keys = ["${digitalocean_ssh_key.default.id}"]
}
