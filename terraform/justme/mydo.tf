resource "digitalocean_droplet" "mydo" {
    image = "ubuntu-14-04-x64"
    name = "mydo"
    region = "sfo2"
    size = "2gb"
    ssh_keys = ["${digitalocean_ssh_key.default.id}"]
}
