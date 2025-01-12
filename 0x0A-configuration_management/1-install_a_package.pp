# Installs Flask 2.1.0 using pip3
# File: 1-install-flask.pp

package { 'python3-pip':
    ensure => present,
}

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Package['python3-pip'],
}
