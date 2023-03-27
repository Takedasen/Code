import speedtest as st

    #! Set Best Server
server = st.Speedtest()
server.get_best_server()

    #! Test Download Speed
down = server.download()
down = down / 1000000
print(f"Down Speed: {down} Mb/s")

    #! Test Upload Speed
up = server.upload()
up = up / 1000000
print(f"Up Speed: {up} Mb/s")

    #! Test Ping
ping = server.results.ping
print(f"Ping: {ping}")