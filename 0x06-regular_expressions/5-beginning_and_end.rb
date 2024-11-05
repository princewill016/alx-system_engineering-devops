#!/usr/bin/env ruby

import ARGV

# Regular expression to match a string that starts with 'h' and ends with 'n' with any single character in between
pattern = /^h.n$/

# Get the input from the command-line argument
input = ARGV[0]

# Check if the input matches the regular expression
if input =~ pattern
  puts "#{input}"
else
  puts ""
end
