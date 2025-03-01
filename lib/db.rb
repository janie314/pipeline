class DB
  def initialize(path)
    @db = SQLite3::Database.new(path)
  end
end
