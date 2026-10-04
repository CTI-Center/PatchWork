---
title: "OpenVPN support on private scanning"
source: https://gtidocs.virustotal.com/docs/private-scanning-openvpn
slug: private-scanning-openvpn
section: guides
group: "Private Scanning"
updatedAt: 2026-05-18T11:09:50.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [Private Scanning](README.md) › OpenVPN support on private scanning

---

# openvpn-support-on-private-scanning

> 🚧 CAPE-Only Network Features
>
> Custom network routes and OpenVPN configurations are strictly limited to the **CAPE sandbox** engine. Other analysis engines do not support these network customizations at this time.

To support the most accurate environment for malware detonation, the outgoing network sometimes needs to be configured for a specific country or network. In addition to our offered routing options, customers can upload their own OpenVPN configuration to route analysis traffic through their own OpenVPN service.

This guide explains how to configure a self-hosted OpenVPN server with a compatible client configuration, or how to use external VPN providers.

# example-of-client-configurations-accepted-by-private-scanning

```
# Specify that we are a client.
client

# Currently we only support TUN interface
dev tun

# Currently we only support UDP to encapsulate traffic
proto udp

# The hostname/IP and port of the server.
remote 1.2.3.4 1194

# Always try to resolve the hostname of the OpenVPN server.
resolv-retry infinite

# Most clients don't need to bind to a specific local port number.
nobind

# Try to preserve some state across restarts.
persist-key
persist-tun

# Select a cryptographic cipher.
cipher AES-256-GCM
auth SHA256
# Certificate Authority 
<ca>
<REDACTED CA CERTIFICATE CONTENT>
</ca>

# User certificate
<cert>
redacted_certificate_content
</cert>

# This is the client's private key
<key>
<REDACTED KEY CONTENT>
</key>
```

Some configurations may require an extra check with a username and password. These configurations typically come with an embedded CA certificate and a TLS authentication key, often because they use a different authentication method. In such cases, you can insert your username and password inline in the configuration as follows:

```
<auth-user-pass>
your_username
your_password
</auth-user-pass>
```

Configurations should be very similar to these examples, with all keys and certificates embedded in the configuration file itself.  While some options or modifications may work, most deviations such as custom route injection, pushed DNS servers, MTU resizing and others will result in connectivity failure.

# running-private-scans-through-a-openvpn

The easiest way is to configure the analysis in the web UI before sending your binary to be analyzed. You can do this from the Configure Scan button. Just select the "OpenVPN custom configuration" option in the Internet section, and you will immediately see a form to upload your .ovpn configuration file, as shown in the following screenshot. Please note that this form **accepts only** files with the .ovpn extension.

![](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_openvpnupload_20250305.png)

If you prefer to send your analysis with VPN capabilities using our [privscan.py](https://github.com/VirusTotal/support-tools/blob/master/api-v3-examples/python/privscan.py) script, you need to add the arguments `--internet internet_openvpn_custom --openvpn_config_path=/path/to/your_config.ovpn`.

# self-hosted-solutions

## installation-on-bare-metal-or-virtualized-systems

Below you can check a sample script to deploy OpenVPN in a VM or bare-metal server. This script requires minimal but important modifications like interface names, VPN subnet, etc…

The next script automates the basic setup of an OpenVPN server on a Linux system (tested on Ubuntu 24.04 LTS). It will:

1. Update the system.\
   2\. Install the required packages (OpenVPN, Easy-RSA).\
   3\. Generate the CA certificate and server key.\
   4\. Configure OpenVPN server settings.\
   5\. Enable IP forwarding.\
   6\. Create a sample client configuration.\
   7\. Show important connection details.

## **important-notes:**

1. This script is designed for a basic, single-server setup. It's not a production-ready solution.
2. Hardcoding passwords in scripts is highly discouraged for production environments. Consider using more secure methods like interactive prompts or configuration files outside the script for real deployments.\
   3\.  **Replace placeholders** (marked with <...>) with your actual values.\
   4\.  Run this script as root or with sudo.\
   5\.  This script assumes a relatively clean system. Existing OpenVPN installations might conflict.\
   6\.  For more advanced configurations (e.g., multiple clients, different encryption, firewall rules), refer to the official OpenVPN documentation.

```
#!/usr/bin/env bash

# Basic OpenVPN setup script

# --- CONFIGURATION ---
VPN_SERVER_IP="<YOUR_SERVER_PUBLIC_IP>" # Your server's public IP address
VPN_SUBNET="10.8.0.0" # VPN subnet (private IP range for clients)
VPN_NETMASK="255.255.255.0" # VPN subnet netmask
EASY_RSA_LOCATION="/etc/openvpn/easy-rsa" # Easy-RSA directory
CA_COUNTRY="US"
CA_PROVINCE="CA"
CA_CITY="SanFrancisco"
CA_ORG="MyOrganization"
CA_EMAIL="admin@example.com"
SERVER_NAME="vpn-server"
CLIENT_NAME="client1"
OPEN_VPN_PORT="1194"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

check_root() {
  if [[ $EUID -ne 0 ]]; then
    echo -e "${RED}This script must be run as root.${NC}"
    exit 1
  fi
}

update_system() {
  echo -e "${YELLOW}Updating system packages...${NC}"
  apt update && apt upgrade -y
}

install_openvpn() {
  echo -e "${YELLOW}Installing OpenVPN and Easy-RSA...${NC}"
  apt install -y openvpn easy-rsa
}

create_easy_rsa() {
  echo -e "${YELLOW}Setting up Easy-RSA...${NC}"
  mkdir -p "$EASY_RSA_LOCATION"
  cp -r /usr/share/easy-rsa/* "$EASY_RSA_LOCATION"
  cd "$EASY_RSA_LOCATION"
  ./easyrsa init-pki
}

generate_ca_server_key() {
  echo -e "${YELLOW}Generating CA certificate and server key...${NC}"
  cd "$EASY_RSA_LOCATION"

  # Create vars file for defaults
  cat <<EOF > vars
export EASYRSA_COUNTRY="$CA_COUNTRY"
export EASYRSA_PROVINCE="$CA_PROVINCE"
export EASYRSA_CITY="$CA_CITY"
export EASYRSA_ORG="$CA_ORG"
export EASYRSA_EMAIL="$CA_EMAIL"
export EASYRSA_OU="IT Department"
EOF

  source vars
  ./easyrsa build-ca nopass
  ./easyrsa gen-req $SERVER_NAME nopass
  ./easyrsa sign-req server $SERVER_NAME
  openssl dhparam -out pki/dh.pem 2048
}

configure_openvpn() {
  echo -e "${YELLOW}Configuring OpenVPN server...${NC}"
  cd "$EASY_RSA_LOCATION"

  # Copy keys to OpenVPN directory
  cp pki/ca.crt /etc/openvpn/
  cp pki/issued/$SERVER_NAME.crt /etc/openvpn/
  cp pki/private/$SERVER_NAME.key /etc/openvpn/
  cp pki/dh.pem /etc/openvpn/

  # Create server.conf
  cat <<EOF > /etc/openvpn/server.conf
port $OPEN_VPN_PORT
proto udp
dev tun
ca ca.crt
cert $SERVER_NAME.crt
key $SERVER_NAME.key
dh dh.pem
server $VPN_SUBNET $VPN_NETMASK
ifconfig-pool-persist ipp.txt
push "redirect-gateway def1 bypass-dhcp"
keepalive 10 120
cipher AES-256-CBC
user nobody
group nogroup
persist-key
persist-tun
status openvpn-status.log
log-append  openvpn.log
verb 3
explicit-exit-notify 1
EOF

  # Enable IP forwarding
  echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf
  sysctl -p

  # Configure NAT (masquerade) for the VPN subnet
  iptables -t nat -A POSTROUTING -s "$VPN_SUBNET/$VPN_NETMASK" -o $(ip route get 8.8.8.8 | awk '{print $5;exit}') -j MASQUERADE
  iptables -I FORWARD 1 -s "$VPN_SUBNET/$VPN_NETMASK" -j ACCEPT
  iptables -I FORWARD 1 -d "$VPN_SUBNET/$VPN_NETMASK" -j ACCEPT
  dpkg -s iptables-persistent > /dev/null 2>&1 || apt install -y iptables-persistent
  netfilter-persistent save
}

create_client_config() {
  echo -e "${YELLOW}Creating client configuration...${NC}"
  cd "$EASY_RSA_LOCATION"

  ./easyrsa gen-req $CLIENT_NAME nopass
  ./easyrsa sign-req client $CLIENT_NAME

  # Create client config file
  cat <<EOF > /etc/openvpn/$CLIENT_NAME.ovpn
client
dev tun
proto udp
remote $VPN_SERVER_IP $OPEN_VPN_PORT
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
cipher AES-256-CBC
verb 3
<ca>
$(cat pki/ca.crt)
</ca>
<cert>
$(cat pki/issued/$CLIENT_NAME.crt)
</cert>
<key>
$(cat pki/private/$CLIENT_NAME.key)
</key>
EOF

  # Copy client config to home directory (or other accessible location)
  cp /etc/openvpn/$CLIENT_NAME.ovpn ~/$CLIENT_NAME.ovpn
  echo -e "${GREEN}Client configuration file created: ~/$CLIENT_NAME.ovpn${NC}"
  echo -e "${YELLOW}Transfer this file securely to your device.${NC}"

}

start_openvpn() {
  echo -e "${YELLOW}Starting OpenVPN server...${NC}"
  systemctl start openvpn@server
  systemctl enable openvpn@server
}

check_root
update_system
install_openvpn
create_easy_rsa
generate_ca_server_key
configure_openvpn
create_client_config
start_openvpn

exit 0
```

## **how-to-use-the-script**

* **Download the script:** Save the code above to a file (e.g., openvpn\_setup.sh).

* **Make it executable:** chmod +x openvpn\_setup.sh

* **Edit the script:** **Crucially,** open the script in a text editor and **replace the placeholder values** with your actual server information. Pay *very* close attention to the IP address or domain.

* **Run the script:** sudo ./openvpn\_setup.sh

* **Follow the instructions:** After the script completes, carefully follow the instructions it displays for connecting to the VPN.

* **Important Post-Script Steps:**

* **Firewall Configuration:** You **must** configure your server's firewall to allow UDP traffic on the port you specified (default 1194). The exact commands will depend on your firewall (e.g., ufw, iptables).

* **Client Configuration Transfer:** Securely transfer the client1.ovpn file to your client device. Do *not* email it without encryption. Use scp, sftp, or a secure file transfer service.

* **Client Installation:** Install an OpenVPN client on your device to test.

* **Import Configuration:** Import the client1.ovpn file into the OpenVPN client.

* **Connect:** Connect to the VPN!

# third-party-providers

## nordvpn

You can download the openvpn configuration files from *Manual Setup*.

![](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_nordvpnmanualsetup_20250305.png)

At this point, you can choose your exit country. By default, it recommends a server near your IP location, but you can choose any other. Once you have selected the country, copy your username and password from the *Service credentials*.

![](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_nordvpnservicecredentials_20250305.png)

After these steps, you can download your OpenVPN configuration file. Both UDP and TCP versions work, but we recommend using UDP.

![](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_nordvpndowloadconfiguration_20250305.png)

After download the configuration you must edit it with a text editor and insert the values for user and password authentication replacing *auth-user-pass* value as you can see below:

Replace:

```
auth-user-pass
```

With:

```
<auth-user-pass>
replace_with_your_nordvpn_service_credential_user
replace_with_your_nordvpn_service_credential_password
</auth-user-pass>

```

At this point, you have a fully working VPN configuration to pass to private scanning.

## mullvad-vpn

Inside your Mullvad panel, go to OpenVPN configuration and download your desired country configuration using the *Linux* platform.

![](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_mullvadvpn_20250305.jpg)

At this moment, you have a zip file. Extract it, and now you will have the base configuration, user/password, CA certificate, and update-resolv binary.

You can omit the update-resolv-conf program, open the .ovpn configuration file, and edit the following lines:"

Replace the line:

```
auth-user-pass mullvad_userpass.txt
```

With the content of *mullvad\_userpass.txt,* like:

```
<auth-user-pass>
your_mullvad_id_user
your_mullvad_password
</auth-user-pass>

```

Also, you need to integrate the CA certificate inside the .ovpn configuration file in this way:\
Replace the line:

```
ca mullvad_ca.crt
```

With the content of *mullvad\_ca.crt,* it looks like:

```
<ca>
-----BEGIN CERTIFICATE-----
certificate content...
-----END CERTIFICATE-----
</ca>
```

Don't forget to put the content of the CA inside `<ca> </ca>` tags. In addition, you can ignore lines with `up/down` commands or remove them. They will be deleted before loading. Now you can use the .ovpn configuration file modified with private scanning.

## proton-vpn

You can download the OpenVPN configuration files from this area. From the downloads area, you can download all the configuration files you want by country by clicking the download button.

![](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_protonvpndownloadconfiguration_20250305.jpg)

Now go to *Account* and copy your OpenVPN username and password.

![](https://storage.googleapis.com/gtidocresources/guides/private-scanning/images/privatescanning_protonvpncredentials_20250305.png)

After download the desired country configuration you must edit it with a text editor and insert the values for user and password authentication replacing *auth-user-pass* value as you can see below:

Replace:

```
auth-user-pass
```

With:

```
<auth-user-pass>
replace_with_your_protonvpn_openvpn_username
replace_with_your_protonvpn_openvpn_password
</auth-user-pass>

```

At this point, you have a fully working VPN configuration to pass to private scanning.

---

← [Private Scanning](private-scanning.md) · [up](README.md) · [How to Explore Vulnerabilities](../10-vulnerability-intelligence/explore-vulnerabilities.md) →

*Archived from <https://gtidocs.virustotal.com/docs/private-scanning-openvpn>.*
