# Puppet manifest to fix the Apache 500 error
# This script addresses the issue found by using strace

# Fix the typo in the PHP file extension in the WordPress configuration
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/usr/bin:/bin',
  onlyif  => 'test -f /var/www/html/wp-settings.php && grep -q "phpp" /var/www/html/wp-settings.php',
}
