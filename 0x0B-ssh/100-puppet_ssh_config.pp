#!/usr/bin/env bash
# Client configuration file (w/ Puppet)
file { '/etc/ssh/ssh_config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => @("EOF"),
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
    | EOF
}
