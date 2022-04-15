# Installing puppet-lint package using Puppet
package { 'puppet-lint':
    ensure  => '2.5.0',
    provider    => 'gem',
}
