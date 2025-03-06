# Fixing Nginx to handle high number of requests
# Increases the ULIMIT for the Nginx process

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && service nginx restart',
  path    => '/usr/local/bin/:/bin/:/usr/bin/'
}
