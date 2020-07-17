clear
blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'
sleep 1
echo
echo $green"Proses install agak lama cuy, tergantung jaringan Lu...."
sleep 3
echo
echo "10%"
pkg install ruby
gem install lolcat
sleep 1
echo "30%"
pip2 install requests
echo "50%"
pip2 install mechanize
echo "70%"
pip2 install requirements
echo "100%"
sleep 1