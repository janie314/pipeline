require "peppermint/rake"
require_relative "lib/imports/networkworld"
require_relative "lib/consts"

desc "Starts the pipeline"
task :start do
  SemanticLogger.add_appender(io: $stdout, formatter: :color)
  NetworkWorld.run
end

desc "Prints current version"
task :version do
  puts VERSION
end
