main(){
curl 'https://www.ba9chich.com/sitemap.xml' -H "Accept: xml,*/*" -H "Accept-Language: en-US,en" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36" 2> /dev/null |grep "<loc>" |grep -v post |grep -v creators |sed 's/<loc>//g' |sed 's/<\/loc>//g' |sed 's/https:\/\/ba9chich.com\///g' |sed 's/\///g' |tail +8
}
main
