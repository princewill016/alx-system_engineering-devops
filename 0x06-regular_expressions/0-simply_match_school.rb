#!/usr/bin/env ruby

import ARGV

pattern = /School/
input = ARGV[0]

if input =~ pattern
  puts input
end
