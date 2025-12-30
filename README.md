# CompleteLogManagement
Demo of Log Management

sudo tee /etc/yum.repos.d/nginx.repo <<EOF  
[nginx-stable]  
name=nginx stable repo  
baseurl=https://nginx.org/packages/centos/\$releasever/\$basearch/  
gpgcheck=1  
enabled=1  
gpgkey=https://nginx.org/keys/nginx_signing.key  
module_hotfixes=true  
EOF