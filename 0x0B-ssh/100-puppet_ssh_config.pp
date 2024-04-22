#!/usr/bin/env bash
# Client configuration file (w/ Puppet)
file { '/root/.ssh/config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
