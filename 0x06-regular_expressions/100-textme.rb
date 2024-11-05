#!/usr/bin/env ruby

import ARGV

# Regular expression to extract sender, receiver, and flags from the input string
pattern = /(\+?\d+|\w+),(\+?\d+|\w+),(\w+)/

# Get the input from the command-line argument
input = ARGV[0]

# Check if the input matches the regular expression
if input =~ pattern
  sender = $1
  receiver = $2
  flags = $3
  puts "[#{sender}],[#{receiver}],[#{flags}]"
else
  puts "Invalid input format"
end
