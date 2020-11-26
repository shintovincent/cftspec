require 'json'

data = JSON.parse(File.read('output.json'))

describe aws_security_group(data['InstanceSecurityGroup']) do
  it { should exist }
end