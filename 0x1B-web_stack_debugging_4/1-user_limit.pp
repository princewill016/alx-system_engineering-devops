# Increase user limits for the holberton user
# Fixes "Too many open files" error by increasing hard and soft file limits

exec { 'change-os-configuration-for-holberton-user':
  command => 'sed -i "/holberton hard/c\holberton hard nofile 50000" /etc/security/limits.conf && sed -i "/holberton soft/c\holberton soft nofile 50000" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/:/usr/bin/'
}
