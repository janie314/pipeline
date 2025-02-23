require "semantic_logger"
require "csv"

class Import
  def self.log = SemanticLogger["import"]

  def self.all(name, data)
    FileUtils.mkdir_p(File.join(__dir__, "../../data/imports", name))
    json(name, data)
    csv_and_html(name, data)
    markdown(name, data)
  end

  def self.json(name, data)
    log.info "importing #{name} into json"
    File.write(File.join(__dir__, "../../data/imports", name, "#{name}.json"), data.to_json)
  end

  def self.csv_and_html(name, data)
    log.info "importing #{name} into csv and HTML"
    csvpath = File.join(__dir__, "../data/imports", name, "#{name}.csv")
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
    htmlpath = File.join(__dir__, "../data/imports", name, "#{name}.html")
    system "csvtotable", "-o", csvpath, htmlpath
  end

  def self.markdown(name, data)
    log.info "importing #{name} into markdown"
    csvpath = File.join(__dir__, "../data/imports", name, "#{name}.csv")
    mdpath = File.join(__dir__, "../data/imports", name, "#{name}.md")
    md = IO.popen(["csv2md", csvpath]) do |io|
      io.read
    end
    File.write(mdpath, md)
  end
end
