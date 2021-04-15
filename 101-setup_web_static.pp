# sets up web servers for the deployment of web_static folder

exec { 'update':
  command => '/usr/bin/apt-get update',
} ->

package { 'nginx':
    ensure  => 'installed',
    name    => 'nginx',
    require => Exec['update'],
} ->

#service { 'nginx':
#  ensure     => running,
#  hasrestart => true,
#  require    => Package['nginx'],
#} ->

file { '/data':
  ensure  => 'directory'
} ->

file { '/data/web_static':
  ensure => 'directory'
} ->

file { '/data/web_static/releases':
  ensure => 'directory'
} ->

file { '/data/web_static/releases/test':
  ensure => 'directory'
} ->

file { '/data/web_static/shared':
  ensure => 'directory'
} ->

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "Holberton School Puppet\n"
} ->

exec { 'symbolic link':
    command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
    provider => 'shell',
    require  => File['/data/web_static/releases/test/'],
} ->

file_line { 'redirect_me':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'root /var/www/html;',
  line    => "\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/ ;\n\t}\n",
  require => Package['nginx'],
} ->

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
} ->

exec { 'nginx restart':
  path => '/etc/init.d/'
}
