#!/usr/bin/env ruby

import ARGV

# Regular expression to match the given test cases
pattern = /hb(tt?n)+/

# Get the input from the command line argument
input = ARGV[0]

# Check if the input matches the regular expression
if input =~ pattern
  puts "Match found: #{input}"
else
  puts "No match found"
end
