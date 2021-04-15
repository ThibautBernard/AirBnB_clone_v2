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
    require => Package['nginx'],
}

file { '/data/web_static/':
    ensure  => 'directory',
    require => Package['nginx'],
}

file { '/data/web_static/releases/':
    ensure  => 'directory',
    require => Package['nginx'],
}

file { '/data/web_static/shared/':
    ensure  => 'directory',
    require => Package['nginx'],
}

file { '/data/web_static/releases/test/':
    ensure  => 'directory',
    require => Package['nginx'],
}

file { '/data/web_static/releases/test/index.html':
    ensure  => 'file',
    content => 'test wowww',
    require => File['/data/web_static/releases/test/'],
}

exec { 'symbolic link'
    command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
    provider => 'shell',
    require  => File['/data/web_static/releases/test/'],
}

exec { 'give owner'
    command  => 'chown -hR ubuntu:ubuntu /data',
    provider => 'shell',
    require  => File['/data/'],
}

file_line { 'redirect_me':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'root /var/www/html;',
  line    => '\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}\n',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
