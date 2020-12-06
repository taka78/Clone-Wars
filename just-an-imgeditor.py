import os
import numpy as np
from PIL import Image
img = Image.open(open("jedi_council.jpg",'rb'))
resized_img = img.resize((round(img.size[0]*0.25), round(img.size[1]*0.25)))
resized_img.save('little_jedi_council_but_only_25%_powerfull.jpg')
###############################That's how it should be#####################################################
#wanted_quality = (10,30,50,75,90,95) #as percentage
#for i in wanted_quality:
#    saviour_kenobi = str(i)
#    resized_img.save('little_jedi_council_but_only_25%_powerfull_and_%'+ saviour_kenobi +'less_qualified.jpg', quality=i)
#print("All wanted qualities has been saved on the parent directory.")
###############################That's how it should be#####################################################
the_jedi_council = Image.open(open("little_jedi_council_but_only_25%_powerfull.jpg",'rb'))
jedi_masters_and_anakin = np.asarray(the_jedi_council)
[ahsoka, rex, cody] = np.linalg.svd(jedi_masters_and_anakin)
grand_army_of_the_republic = np.sum(rex) #that's kinda accurate
wanted_quality = (10,30,50,75,90,95) #as percentage
for i in wanted_quality:
    our_brothers_born_in_kamino = grand_army_of_the_republic*i/100
    a_million_more_on_the_way = 0
    saviour_kenobi = str(i)
    for t in range(rex.shape[0]):
        a_million_more_on_the_way += rex[t]
        if(a_million_more_on_the_way>our_brothers_born_in_kamino):
            print(t)
            break
    ampliutude_of_the_clone_wars = t
    jedi_generals = np.empty(jedi_masters_and_anakin.shape)
    saviour_kenobi = str(i)
    for k in range(ampliutude_of_the_clone_wars):
        jedi_generals += rex[k]*np.dot(np.array([ahsoka[:,k]]).T, np.array([cody[k,:]]))
    the_jedi_councily = Image.fromarray(jedi_generals)
    the_jedi_councily = the_jedi_councily.convert("L")
    LIST_OF_THE_ORDER66 = the_jedi_councily.save('jedi_council_but_only_25%_powerfull_and_%'+ saviour_kenobi +'corrupted.jpg')
