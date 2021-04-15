# sets up web servers for the deployment of web_static folder

exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
    ensure  => 'installed',
    name    => 'nginx',
    require => Exec['update'],
}

file { '/data/':
    ensure  => 'directory',
    group   => 'ubuntu',
    owner   => 'ubuntu',
    require => Package['nginx'],
}

file { '/data/web_static/':
    ensure  => 'directory',
    group   => 'ubuntu',
    owner   => 'ubuntu',
    require => File['/data/'],
}

file { '/data/web_static/releases/':
    ensure  => 'directory',
    group   => 'ubuntu',
    owner   => 'ubuntu',
    require => Package['nginx'],
}

file { '/data/web_static/shared/':
    ensure  => 'directory',
    group   => 'ubuntu',
    owner   => 'ubuntu',
    require => Package['nginx'],
}

file { '/data/web_static/releases/test/':
    ensure  => 'directory',
    group   => 'ubuntu',
    owner   => 'ubuntu',
    require => Package['nginx'],
}

file { '/data/web_static/releases/test/index.html':
    ensure  => 'file',
    group   => 'ubuntu',
    owner   => 'ubuntu',
    content => 'test wowww',
    require => File['/data/web_static/releases/test/'],
}

exec { 'symbolic link':
    command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
    provider => 'shell',
    require  => File['/data/web_static/releases/test/'],
}

exec { 'sed':
  command => "sed -i \
  '/^\tlisten 80 default_server;$/i location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  require => Package['nginx'],
}

service { 'nginx':
  ensure     => running,
  hasrestart => true,
  require    => Package['nginx'],
}
