require 'json'

data = JSON.parse(File.read('output.json'))

describe aws_security_group(data['InstanceSecurityGroup']) do
  it { should exist }
  it { should allow_in(port: 22, ipv4_range: '103.99.206.132/32') }
end