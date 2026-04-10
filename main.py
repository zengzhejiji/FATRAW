with open("aa.post",mode='rb+')as f:
    f.seek(0)
    data = f.read()
deata = data.rstrip(b'\x00')
try:
    sea = deata.split(b"|",1)
    FileName = sea[0].decode("utf-8",errors='replace')
    content = sea[1]
    FN_L = FileName.split(".",1)
except:
    FileName = b''
    content = b''
    FN_L = [b'',b'']
while True:
    u_i = input(">>>")
    if u_i == 'ff':
        try:
            print(FileName,"\n",content.decode("utf-8",errors='replace'))
        except:
            print(FileName,"\n",content)
    if u_i == 'fmin':
        try:
            print(FileName,"\n",content[:10].decode("utf-8",errors='replace'))
        except:
            print(FileName,"\n",content[:10])
    if u_i == 'ffb':
        print(FileName,"\n",content)
    if u_i == 'fminb':
        print(FileName,"\n",content[:10])
    if u_i == "copy":
        try:
            with open(FN_L[0]+"copy."+FN_L[1],mode='wb') as f:
                f.write(content)
        except:
            pass
    if u_i == "null":
        a = input("(Y/N)?")
        if a == "Y": 
            with open("aa.post",mode='wb')as f:
                f.write(b"\x00"*1024) 
            FileName = ''
            content = ''
        else:
            break
    if u_i == "import":
        import_file = input("import>>>")
        try:
            with open(import_file,mode='rb') as f:
                user_input = f.read()
            with open("aa.post",mode='rb+')as f:
                f.seek(0)
                if not len(user_input)+len(import_file.encode('utf-8'))+1 > 1024:
                    f.write(import_file.encode("utf-8")+b"|"+user_input)
                else:
                    print("xxx")
                f.truncate()
                f.seek(0)
                data = f.read()
                deata = data.rstrip(b'\x00')
                try:
                    sea = deata.split(b"|",1)
                    FileName =sea[0].decode("utf-8")
                    content = sea[1]
                except:
                    FileName = b''
                    content = b''
        except:
            pass
    if u_i == "exit":
        break
