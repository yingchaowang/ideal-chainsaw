resource "digitalocean_droplet" "server4" {
    image = "ubuntu-14-04-x64"
    name = "server4"
    region = "sfo2"
    size = "1gb"
    ssh_keys = ["${digitalocean_ssh_key.default.id}"]
}
