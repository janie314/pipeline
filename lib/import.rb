require "semantic_logger"
require "csv"

class Import
  def self.log = SemanticLogger["import"]

  def self.json(name, data)
    FileUtils.mkdir_p(File.join(__dir__, "../../data/imports"))
    File.write(File.join(__dir__, "../../data/imports", "#{name}.json"), data.to_json)
  end

  def self.csv(name, data)
    log.info "importing #{name} to csv"
    FileUtils.mkdir_p(File.join(__dir__, "../../data/imports"))
    csvpath = File.join(__dir__, "../data/imports", "#{name}.csv")
    CSV.open(csvpath, "w") do |csv|
      headers = data.first&.keys
      if headers.nil?
        log.warn "no data from #{name} query"
      else
        csv << headers
        data[1..].each do |row|
          csv << headers.map { |h| row[h] }
        end
      end
    end
    htmlpath = File.join(__dir__, "../data/imports", "#{name}.html")
    system "csvtotable", csvpath, htmlpath
  end
end
