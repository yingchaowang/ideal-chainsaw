# import my SSH key
resource "digitalocean_ssh_key" "default" {
    name = "tf xps13 bootcamp"
    public_key = "${file("/home/fdavis/.ssh/tf_rsa.pub")}"
}
