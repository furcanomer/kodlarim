def kontrol(note):
    if (note < 0 or note > 100):
        print("Hatalı veri. Tekrar yazınız.")
        return True
    else:
        return False
    
def ortalama(vize,final):
    return vize*0.4+final*0.6

while (True):
    vize = float(input("Vize: "))
    if (kontrol(vize)):
        continue
    else:
        break

while (True):
    final = float(input("final: "))
    if (kontrol(final)):
        continue
    else:
        break

ort = ortalama(vize,final)

print("Ortalamanız: " + str(ort))

if (ort >= 50):
    print("geçtiniz")

else:
    print("kaldınız")