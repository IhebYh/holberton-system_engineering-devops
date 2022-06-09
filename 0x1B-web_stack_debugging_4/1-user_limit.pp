# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.
exec {'hard':
  path     => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
  command  => "sudo sed -i 's/holberton hard nofile 5/holberton hard nofile 65536/g' /etc/security/limits.conf; /sbin/sysctl -p",
  provider => 'shell',
}
exec {'soft':
  path     => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
  command  => "sudo sed -i 's/holberton soft nofile 5/holberton soft nofile 65536/g' /etc/security/limits.conf; /sbin/sysctl -p",
  provider => 'shell',
}
