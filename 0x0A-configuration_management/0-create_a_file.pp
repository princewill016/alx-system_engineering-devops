# Creates a file in /tmp with specific permissions and content
# File: 0-create-file.pp

file { '/tmp/school':
    ensure  => 'present',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
