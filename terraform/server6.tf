resource "digitalocean_droplet" "server6" {
    image = "ubuntu-14-04-x64"
    name = "server6"
    region = "sfo2"
    size = "1gb"
    ssh_keys = ["${digitalocean_ssh_key.default.id}"]
}
