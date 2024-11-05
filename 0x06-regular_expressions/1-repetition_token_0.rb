#!/usr/bin/env ruby

import ARGV

pattern = /hb(tt?n)+/
input = ARGV[0]

if input =~ pattern
  puts "Match found: #{input}"
else
  puts "No match found"
end
