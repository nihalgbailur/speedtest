import speedtest
test = speedtest.Speedtest()
print("loading server list...")

test.get_servers()
print("choosing best server....")
best = test.get_best_server()
print(f"Found: {best['host']} located in {best['country']}")



print("download test...")
download_result = test.download()


print("upload test...")
upload_result = test.upload()


ping_results = test.results.ping


print(f"Download speed : {download_result /1024 /1024 :.2f} Mbits/s")
print(f"upload speed : {upload_result /1024 /1024 :.2f} Mbits/s")
print(f"ping : {ping_results}")
