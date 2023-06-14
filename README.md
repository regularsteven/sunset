# sunset
take photos during the day, take more photos towards the sunset 


# install
this must run on a lagacy system with raspi-still working

sudo apt-get update

sudo apt install git

git clone git@github.com:regularsteven/sunset.git

sudo -H apt install python3-picamera
sudo -H apt install sched
sudo -H apt install time

sudo apt-get install imagemagick -y



# running 
ssh steven@sunset.local
cd /home/steven/sunset/
nohup python3 ~/sunset/snapper.py &
ps -ef | grep python3
kill task 