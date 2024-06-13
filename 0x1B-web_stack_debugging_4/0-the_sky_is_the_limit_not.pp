class nginx_optimization {

  # Ensure the Nginx package is installed
  package { 'nginx':
    ensure => installed,
  }

  # Ensure the Nginx service is running and enabled
  service { 'nginx':
    ensure     => running,
    enable     => true,
    subscribe  => File['/etc/nginx/nginx.conf'],
  }

  # Configure Nginx with optimized settings
  file { '/etc/nginx/nginx.conf':
    ensure  => file,
    content => "
user www-data;
worker_processes auto;
pid /run/nginx.pid;

events {
    worker_connections 1024;
    multi_accept on;
}

http {
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # Logging
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    # Gzip Settings
    gzip on;
    gzip_disable 'msie6';
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_buffers 16 8k;
    gzip_http_version 1.1;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}
    ",
    notify  => Service['nginx'],
  }

  # Ensure that the necessary directory exists
  file { '/etc/nginx/conf.d/':
    ensure => directory,
  }

  # Add any additional configuration settings
  file { '/etc/nginx/conf.d/optimization.conf':
    ensure  => file,
    content => "
# Buffer and Timeout Settings
client_body_buffer_size 16K;
client_max_body_size 8M;
client_header_buffer_size 1k;
large_client_header_buffers 4 16k;
send_timeout 30;
server_names_hash_bucket_size 64;

# Connection Settings
keepalive_timeout 65;
keepalive_requests 100;
    ",
    notify  => Service['nginx'],
  }

}

# Include the nginx_optimization class in the main manifest
include nginx_optimization
