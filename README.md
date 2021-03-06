kancolle_echor
=========================

Simple script that automate kancolle.

### Changes in ver. Taihou
1. New feature

	1. Automate 3-2-a battle. To use this, you have to supply some configs. 

		* ss_id: the ship ids of your submarine
		* ss_loc: the place to hold your submarine

		And create a file named counter to store 3-2-a battle count. Place your submarine at ss_loc
		and the script will change ships if the ship has too low life or in bad condition. Only when all of your
		ships in fleet 1 are in good condition will the script go to battle.

	2. Automate ship repair. First it will repair submarines, then prefer ships that can be repaired in shorter time.

2. Rewrite control logic for safety purpose. Now this script has almost the same api actions as the kcs flash client.

3. Now api call will retry for 10 times, if it still fails, script will restart in 60s.

4. The API_TOKEN file and log file are removed, change api_token in kancolle_echor.py.


### Requirement
The python script need python 2.7 and python requests lib, you can simply install it using:

```
>>> pip install requests
```

And the scheduler.bat is a windows batch script so you need to be under windows.

### How to use
1. First time config your host due to your server in kancolle_echor.py. Change value of **host** to your server ip address. This address won't change.

2. Every time before you use this script:

	1. Config your mission plan in kancolle_echor.py. Change value of **mission**. For example, 2:17,3:3,4:5 means fleet 2 set for mission 17, fleet 3 set for mission 3 and fleet 4 set for mission 5.

	2. Open the game page using a browser, place the api_token into the **api_token** file. Then don't kill the game page, just leave it there.

3. Run scheduler.bat to start the script.

4. Press ctrl+c to stop the script at any time you want.


### How to get the host address and api_token?
Before you run this script, you should open the game page using a browser. If you are using chrome or ie, press F12 at the game loading page and search for **api_token** in the source code part. You should see a url like:
```
http://your_host_ip_address/MainD2.swf?api_token=your_api_token&api_starttime=****
```
And then get the api_token and host ip.

### Attention
1. When the script is running, DON'T PLAY GAME ON GAME PAGE. If you do so, the game page may tell you network error occured.
2. After exiting the game page, refresh the game page.(this will cause the old api_token expired, so you should fill the api_token every time you run this script)
3. If you are running on windows xp or something older, remember to change line 5 of scheduler.bat to 
```
ping -n %SLEEP_TIME% 127.0.0.1 > nul
```
4. This script is used at your own risk. Contact me if you have any suggestion about the script itself.

