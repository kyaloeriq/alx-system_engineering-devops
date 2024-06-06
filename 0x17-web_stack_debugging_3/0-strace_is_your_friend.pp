# Ensure the Apache package is installed and the service is running
package { 'apache2':
  ensure => installed,
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/var/www/html/index.html'],
}

# Ensure the web root directory exists
file { '/var/www/html':
  ensure => directory,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

# Ensure the index.html file exists with appropriate content and permissions
file { '/var/www/html/index.html':
  ensure  => file,
  content => '<html><body><h1>It works!</h1></body></html>',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  require => File['/var/www/html'],
}
