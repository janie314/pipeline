require "thor"
require_relative "../lib/imports/networkworld"
require_relative "../lib/consts"

class Pipeline < Thor
  no_commands do
    def self.exit_on_failure?
      true
    end
  end

  desc "start", "Starts the pipeline"
  def start
    NetworkWorld.new.run
  end

  desc "version", "Prints current version"
  def version
    puts VERSION
  end
end

Pipeline.start(ARGV)
