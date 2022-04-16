# Turns off pass auth and uses pub key in school file
file_line { 'set password auth to no':
ensure  => 'present',
path    => '/etc/ssh/ssh_config',
line    => '    PasswordAuthentification no',
}
file_line { 'Specify Identity the file':
ensure  => 'present',
path    => '/etc/ssh/ssh_config',
line    => '    IdentityFile ~/.ssh/school',
}
