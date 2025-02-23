def import_to_json(name)
  FileUtils.mkdir_p(File.join(__dir__, "../../data/imports"))
  File.write(File.join(__dir__, "../../data/imports", "#{name}.json"), data.to_json)
end
