# Turns off pass auth and uses pub key in school file
file_line { 'set password auth to no':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentification no',
  replace => true
}

file_line { 'Specify Identity the file':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  replace => true
}
