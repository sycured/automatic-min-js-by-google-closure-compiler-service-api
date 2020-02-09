#!/usr/bin/env ruby
require "net/http"
preout = ARGV[0].split(".js")
out = [preout,"min.js"].join('.')
f = File.read(ARGV[0])
params = {'js_code' => f,
'compilation_level' => 'SIMPLE_OPTIMIZATIONS',
'output_format' => 'text',
'output_info' => 'compiled_code'}
reponse = Net::HTTP.post_form(URI.parse('http://closure-compiler.appspot.com/compile'),params)
File.open(out, 'w') do |k|
  k.write reponse.body
  k.close
end