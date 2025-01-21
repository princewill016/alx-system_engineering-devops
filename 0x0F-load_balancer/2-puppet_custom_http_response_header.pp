# Configures Nginx to include custom HTTP header X-Served-By

exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file_line { 'add_header':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'server {',
  line    => "\tadd_header X-Served-By \"${hostname}\";",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
