#!/usr/bin/env ruby

import ARGV

# Regular expression to match a 10-digit phone number
pattern = /^\d{10}$/

# Get the input from the command-line argument
input = ARGV[0]

# Check if the input matches the regular expression
if input =~ pattern
  puts "#{input}"
else
  puts ""
end
