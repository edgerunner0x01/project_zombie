main(){
eliminate=" <loc>https://ba9chich.com/register/</loc>|\
            <loc>https://ba9chich.com/about-us/</loc>|\
            <loc>https://ba9chich.com/privacy-policies/</loc>|\
            <loc>https://ba9chich.com/contact/</loc>|\
            <loc>https://ba9chich.com/terms-of-use/</loc>|\
            <loc>https://ba9chich.com/creator-verification-request/</loc>|\
            <loc>https://ba9chich.com/know-your-customer/</loc>" 
            


curl 'https://www.ba9chich.com/sitemap.xml' -H "Accept: xml,*/*" -H "Accept-Language: en-US,en" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36" 2> /dev/null |egrep -v "$eliminate" |grep "<loc>" |grep -v post |grep -v creators |sed 's/<loc>//g' |sed 's/<\/loc>//g' |sed 's/https:\/\/ba9chich.com\///g' |sed 's/\///g'  
}
main
