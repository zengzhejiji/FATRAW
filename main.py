
with open("aa.post",mode='rb+')as f:
    f.seek(0)
    data = f.read()
deata = data.replace(b'\x00',b'')
rx =deata.decode('ascii')
sea = rx.find("|")
FileName = rx[:sea]
content = rx[sea+1:]
while True:
    u_i = input(">>>")
    if u_i == 'ff':
        print(FileName,"\n",content)
    if u_i == "copy":
        with open(FileName[:len(FileName)-4]+"copy.txt",mode='w',encoding='ascii') as f:
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
        with open("test.txt",encoding='ascii',mode='r') as f:
            user_input = f.read()
        with open("aa.post",mode='rb+')as f:
            f.seek(0)
            f.write(b"test.txt"+b"|"+user_input.encode('ascii'))
            f.seek(0)
            data = f.read()
            deata = data.replace(b'\x00',b'')
            rx =deata.decode('ascii')
            sea = rx.find("|")
            FileName = rx[:sea]
            content = rx[sea+1:]
    if u_i == "exit":
        break
