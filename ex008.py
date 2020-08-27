medida = float(input('Uma distância em metros: '))

km = medida / 1000  #quilometro
hm = medida / 100   #hectômetro
dam = medida / 10   #decametro
dm = medida * 10    #decimetro
cm = medida * 100   #centimetro
mm = medida * 1000  #milimetro
print('A medida de {}m corresponde a {:.0f}km , {:.0f}hm , {:.0f}dam , {:.0f}dm , {:.0f}cm e {:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))
