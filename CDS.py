import socket,sys,json,time,ssl

profile = json.loads(open("profile.json","rb").read())
TOKEN = profile["TOKEN"]
Cookie = profile["Cookie"]
Interval = profile["Interval"]
Status = profile["Status"]
apiIp = "discord.com"

while True:
    for StatNum in range(len(Status)):
        Stat = Status[str(StatNum+1)]
        sock = socket.socket()
        s = ssl.create_default_context().wrap_socket(sock,server_hostname="discord.com")
        s.connect((apiIp,443))
        head = "PATCH /api/v9/users/@me/settings HTTP/1.1\r\nHost: discord.com:443\r\n"
        body = '{"custom_status":{"text":"%s"}}'%(Stat)
        cookie = "Cookie: %s\r\n"%Cookie
        contentType = "Content-Type: application/json\r\nContent-Length: %s\r\n"%str(len(body))
        auth = "Authorization: "+TOKEN+"\r\n"
        data = head+auth+cookie+contentType+"\r\n"+body
        s.send(str.encode(data))
        result = 'Success' if s.recv(1024).decode().split(" ")[1] == "200" else "Failed"
        s.close()
        print("Custom Status [%s]: %s"%(result,Stat))
        time.sleep(int(Interval))