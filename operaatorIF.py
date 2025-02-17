#8 ulesanne 
import random

tooted = ["piim", "sai", "leib"]
hinnad = {toode: round(random.uniform(0.5, 5.0), 2) for toode in tooted}
kokku = 0

print("salam prohodite v poodi!")
for toode in tooted:
    if input(f"Kas soovite osta {toode}? (jah/ei): ").strip().lower() == "jah":
        kogus = int(input(f"mitu tk {toode} soovite?: "))
        hind = hinnad[toode] * kogus
        kokku += hind
        print(f"{toode.capitalize()}: {kogus} tk x {hinnad[toode]}€ = {hind:.2f}€")

print(f"Kokku: {kokku:.2f}€")

#14 ulesanne
inim = int(input("sisesta inimeste arv: "))
kohad = int(input("sisesta bussi kohtade arv: "))
bussid = inim // kohad
vbuss = inim % kohad
if vbuss:
    bussid += 1
print(f"vaja on {bussid} bussi, viimases bussis on {vbuss if vbuss else kohad} inimest")


#13 ulesanne
soo = input("sisesta sugu: ")
if soo == "n":
    print("sobid, pole piirangiud")
if soo == "m":
    vanus66 = int(input("sisesta vanus: "))
    if 16 <= vanus66 <= 18:
        print("sobid")
    else:
        print("ei sobi")

#12 ulesanne
hind = float(input("sisesta hind: "))
if hind < 10:
    soodustus1 = hind - (hind * 0.1)
    print(f"teil on soodustus 10% nyyd teie hind on {soodustus1}")
if hind > 10:
    soodustus2 = hind - (hind * 0.2)
    print(f"teil on soodustus 20% nyyd teie hind on {soodustus2}")
    

#11 ulesanne
#operatoor % kontrollib, kas arv jagub täpselt 10ga
synniaasta = int(input("aisesta sünniaasta: "))
vanus = 2025 - synniaasta
if vanus % 10 == 0:
    print("juubel")
else:
    print("pole juubel")

#10 ulesanne
arv1 = float(input("sisesta esimene arv: "))
tehe = input("sisesta tehe: ")
arv2 = float(input("sisesta teine arv: "))
if tehe == "+":
   print(f"vastus on {arv1 + arv2}")
elif tehe == "-":
   print(f"vastus on {arv1 - arv2}")
elif tehe == "*":
   print(f"vastus on {arv1 * arv2}")
elif tehe == "/":
   print(f"vastus on {arv1 / arv2}")
else:
   print("vale tehe")




#9 ulesanne
kulg1 = float(input("sisesta esimene külg: "))
kulg2 = float(input("sisesta teine külg: "))
if kulg1 == kulg2:
    print("ruut")
else:
    print("ristkulik")


#7 ulesanne
sugu = input("sisesta sugu (m/n): ")
pikkus = float(input("sisesta pikkus: "))
if sugu == "m":
        if pikkus < 1.70:
            print("lühike mees")
        elif pikkus <= 1.85:
            print("keskmine mees")
        else:
            print("pikk mees")
if sugu == "n":
        if pikkus < 1.60:
            print("lühike naine")
        elif pikkus <= 1.75:
            print("keskmine naine")
        else:
            print("pikk naine")

#6 ulesanne
pikkus = float(input("sisesta pikkus: "))
if pikkus > 1.6:
    print("sa oled pikk")
if pikkus < 1.6:
    print ("sa oled luhike")

#5 ulesanne
temperatuur = float (input("sisesta toatemperatuur: "))
if temperatuur < 18:
    print("soovitav toasoojus talvel")

#4 ulesanne
hind = float(input("sisesta hind: "))
if hind > 700:
    soodushind= hind - (hind * 0.3)
    print(f"teil on soodustus 30% nyyd teie hind on {soodushind}")

#3 ulesanne
laius = float(input("sisesta laius: "))
pikkus = float(input("sisesta pikkus: "))
pindala = laius * pikkus

print(f"pindala on {pindala} ruutmeetrit") 
remont = input("kas on vaja remonti teha? ")
if remont == "jah":
    print("tuleb remontida")
    rmhind = float(input("sisesta ruutmeetri hind: "))
    print(f"remont maksab {pindala * rmhind} eurot")
else: 
        print("ei ole vaja remonti teha")

#2 ulesanne
nimi1 = input("sisesta nimi: ")
nimi2 = input("sisesta nimi: ")
nimi3 = input("sisesta nimi: ")
nimed = {nimi1, nimi2, nimi3}

if all(nimi.isalpha() for nimi in nimed):
    if {"eldar", "adri", "nastja"} == nimed:
        print("super vy pinginaabrid")
else:
    print("oneet vy ne pinginaabrid")



#1 ulesanne
nimi = input("Sisesta nimi: ")
if nimi.isupper() and nimi == "JUKU":
    print("lähme kinno")
    vanus = input("Sisesta vanus: ")
    if vanus.isdigit():
        vanus = int(vanus)
        if vanus < 0 or vanus > 100:
            print("valed andmed")
        elif vanus < 6:
            print(f"tasuta pilet sest, oled {vanus} aastat vana")
        elif vanus <= 14:
            print(f"lastepilet sest, oled {vanus} aastat vana")
        elif vanus <= 65:
            print(f"täispilet sest, oled {vanus} aastat vana")
        else:
            print(f"sooduspilet sest, oled {vanus} aastat vana")
    else:
        print("valesti sisestatud vanus")
