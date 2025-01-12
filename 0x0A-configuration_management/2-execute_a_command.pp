# Kills process named killmenow using pkill command
# File: 2-kill-process.pp

exec { 'killmenow':
    command => 'pkill killmenow',
    path    => '/usr/bin:/bin',
    onlyif  => 'pgrep killmenow',
}
