# Using Puppet to install flask from pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
# Add environment path for flask executable
file { '/etc/profile.d/flask.sh':
  ensure  => present,
  content => "export PATH=$PATH:/usr/local/bin\n",
  mode    => '0644',
}
