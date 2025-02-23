require "thor"
require_relative "../lib/imports/networkworld"

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

  private

  def f
    puts "Pipeline started!"
  end
end

Pipeline.start(ARGV)
