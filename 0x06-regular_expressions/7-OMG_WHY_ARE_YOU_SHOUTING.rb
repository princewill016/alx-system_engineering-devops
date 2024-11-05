#!/usr/bin/env ruby

import ARGV

# Regular expression to match only capital letters
pattern = /[A-Z]+/

# Get the input from the command-line argument
input = ARGV[0]

# Find all matches in the input string
matches = input.scan(pattern)

# Print the matched capital letter strings
if matches.length > 0
  puts matches.join("")
end
