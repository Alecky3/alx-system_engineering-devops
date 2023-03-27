# sets a set of command to connect to server without typing a password

exec { 'ssh -F 2-ssh_config ubuntu@18.209.223.27':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}
