with open("aa.post",mode='rb+')as f:
    f.seek(0)
    data = f.read()
deata = data.rstrip(b'\x00')
try:
    sea = deata.split(b"|",1)
    FileName = sea[0].decode("utf-8",errors='replace')
    content = sea[1]
except:
    FileName = b''
    content = b''
while True:
    u_i = input(">>>")
    if u_i == 'ff':
        print(FileName,"\n",content)
    if u_i == 'fmin':
        print(FileName,"\n",content[:10])
    if u_i == "copy":
        with open(FileName[:len(FileName)-4]+"copy.txt",mode='wb') as f:
            f.write(content)
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
        with open("test.txt",mode='rb') as f:
            user_input = f.read()
        with open("aa.post",mode='rb+')as f:
            f.seek(0)
            f.write(b"test.txt"+b"|"+user_input)
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
    if u_i == "exit":
        break
