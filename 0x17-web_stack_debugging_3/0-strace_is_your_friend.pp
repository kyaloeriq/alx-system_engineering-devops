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

# Ensure the Apache configuration file exists and is correct
file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => file,
  content => template('apache2/000-default.conf.erb'),
  notify  => Service['apache2'],
}

# Ensure the site is enabled
exec { 'enable_site':
  command => '/usr/sbin/a2ensite 000-default.conf',
  unless  => '/usr/sbin/a2query -s 000-default.conf',
  notify  => Service['apache2'],
}

# Ensure Apache has correct permissions to its log directory
file { '/var/log/apache2':
  ensure => directory,
  owner  => 'root',
  group  => 'adm',
  mode   => '0755',
}
