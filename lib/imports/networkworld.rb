require "http"
require "nokogiri"
require "json"
require_relative "../import"

class NetworkWorld
  def self.log = SemanticLogger["NetworkWorld"]

  def self.run
    log.info "running NetworkWorld query"
    res = `curl -s 'https://nitter.net/search?f=tweets&q=networkworld' --compressed -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: none' -H 'Sec-Fetch-User: ?1' -H 'Priority: u=0, i' -H 'TE: trailers'`
    html = Nokogiri::HTML.parse(res)
    data = []
    html.css(".tweet-content, .tweet-date > a").each_slice(2) do |date, tweet|
      data.push({
        datetime: DateTime.parse(date[:title]),
        tweet: tweet.text
      })
    end
    Import.all("networkworld", data)
    data
  end
end
