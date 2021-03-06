import socket,sys,json,time,ssl

profile = json.loads(open("profile.json","rb").read())
TOKEN = profile["TOKEN"]
Interval = profile["Interval"]
Status = profile["Status"]
apiIp = "discord.com"

def jslen(string):
    return int(len(string.encode(encoding='utf_16_le'))/2)

while True:
    for StatNum in range(len(Status)):
        Stat = Status[str(StatNum+1)]
        sock = socket.socket()
        s = ssl.create_default_context().wrap_socket(sock,server_hostname="discord.com")
        s.connect((apiIp,443))
        head = "PATCH /api/v9/users/@me/settings HTTP/1.1\r\nHost: discord.com:443\r\n"
        body = '{"custom_status":{"text":"%s","emoji_name":"%s"}}'%(Stat["text"],Stat["emoji_name"])
        contentType = "Content-Type: application/json\r\nContent-Length: %s\r\n"%str(jslen(body)+2)
        auth = "Authorization: "+TOKEN+"\r\n"
        data = head+auth+contentType+"\r\n"+body
        s.send(str.encode(data))
        result = "Success" if s.recv(1024).decode().split(" ")[1] == "200" else s.recv(1024).decode()
        s.close()
        print("Custom Status [%s]: %s%s"%(result,Stat["emoji_name"],Stat["text"]))
        time.sleep(int(Interval))
