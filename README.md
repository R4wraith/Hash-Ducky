# Hash-Ducky
A CLI tool to convert any hash to MD5 by using Virus-Total API.

![load](https://user-images.githubusercontent.com/89847158/157982254-1767fcd9-db2c-43d4-88fe-9658c6a6f017.PNG)
## Hash-Ducky
is a CLI tool that use Python <a href="https://www.geeksforgeeks.org/libraries-in-python/">library</a> called "VT-PY".
The <a href="https://virustotal.github.io/vt-py/"> vt-py </a> is a python custom-made by Virus-total.<br>
This library has been build for the new <a href="https://developers.virustotal.com/reference/overview">REST v3 api.</a><br>
This tool has been build for the purpose of converting malicious/not malicious hash to MD5 using VT.<br>
<br>
By uploading a file to Virus-Total , VT automated calculate popular hashes such as MD5/SHA1/SHA526 etc.
By using this tool you can generate an 100% fully automated requests to VT api and recived the vt.object File that contains the MD5 etc.   
This tools has been build for the purpose of learning and exploring the vt-py module and has been found pretty much requested along many communities.

# Installation :

<details><summary>Installation command - </summary>
<p>

#### in cmd opened in CWD where requirements.txt is located 

   
     pip install -r requirements.txt
    

</p>
</details>

| Files | Description |
| --- | --- |
| `vt-test.py` | Main script |
| `requirements.txt` | requirements libraries to **Install that is required** for script to run |
| `hash-ducky-output-md5-date.txt` | The output file from the hash-convert job |

# How its work?
The script architecture is very simple. after installing all the requirements copy and paste the vt-test.py file to and folder at your machine.
##### Importent note - The script need to be editied before use and you should provied your api-key from VT.
to insert your api-key open the vt-test.py file with any text ediot (I highly recommend Sublime-Text) and navigate to line <b>46</b><br>
![test2](https://user-images.githubusercontent.com/89847158/157985412-3cf0a85b-0799-4f3e-9fb8-191b1d702a4a.PNG)
> change the argument provided for **vt.Clinet** to your api key and save the file.  

#### Open cmd in folder scripy is located and run the scripy usinh py vt-test.py

![original_api](https://user-images.githubusercontent.com/89847158/157990806-ee0d725e-3099-45a6-a1dd-d7f07acd2bb0.PNG)

after quick and cool inspection the script will load and ask you is you want to use the original API provided.

**If you alredy put the api key in the scripy just type yes. otherwise type no and the script will then ask for your api key.**
> when type yes or the api key the vt-Client will load your api to local client variable at local machine. your **API WILL STAY SAFE AND LOCALY SAVED ONLY.**

![defualt apy](https://user-images.githubusercontent.com/89847158/157990849-eb2f2e0f-33ef-4afd-a8d6-d316c8498c49.PNG)


#### The next step of the script will be to open a gui check box for you choosing your text file that includes the hashes you need to convert.
![checkbox](https://user-images.githubusercontent.com/89847158/157992856-2b27dfbc-ccfb-439d-954a-0a4b15858ba4.PNG)

The file you provide must be:
```
.txt file.
can include any kind of hash you desire to convert.
must be by order - each hash need to be in line by his own.
no empty lines
```

#### When loaded the script will open the txt file in backround
he will verify the hashes, copy them for local use to memory (by list them in local list structure)
the script then will put to output :
```
number of hashes found
estimated time for request.
any error while processing.
progress of work
```
**Due to the virus-total api docs, there is a limit of api request per minute. this script will send a request every 8 secounds.
this will be ok only for paid registered users, you can change the request break. Contact me in my linkedin for any help regards that. **

![exmaple](https://user-images.githubusercontent.com/89847158/157993434-78ede0ff-ac47-4554-86d0-955e1d79b005.PNG)

#### When finished , the script will print the output file name and path and then will reload for next use.
![output](https://user-images.githubusercontent.com/89847158/157993860-8b830c5c-f81f-48c3-baed-cd11276b02fe.PNG)


output file should look like this : 
![output_hash](https://user-images.githubusercontent.com/89847158/157993880-20457888-a7bb-430f-829f-b354eb3237e6.PNG)

**if a file is not found in the VT-DB the original hash will be stored in the output log !!**


<br>
<br>
<br>




**Compatibility requirements:**

Python 3 and above
Virus-Total user (for Private API)
Internet connection.

**Copyright for the vt-py module is for Virus-Total. the script is build by me and free to use, feel free to share with credit to my github for more awesome tools!**


**Misc**

This is my first foray into creating a theme, so if you see something amiss, please feel free to [file an issue!](https://github.com/R4wraith/Hash-Ducky/issues) I'm sure there are things I missed.

Any relevant changes for each version are documented in the changelog. Please update and check the changelog before filing any issues, as they may have already been taken care of.

