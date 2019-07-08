'''
Created on Sep 13, 2018

@author: Kassen Qian
'''
import random 

def hair_plain():
    #     123456789012345678    #counting characters
    s = r" |||||||||||||||| "
    return s;
def hair_pointy():
    #     123456789012345678    #counting characters
    s = r" /\/\/\/\/\/\/\/\ "
    return s;
def hair_long():
    #     123456789012345678    #counting characters
    s = r" |||||||||||||||| " + "\n"
    s+= r" |||||||||||||||| " + "\n"
    s+= r" |||||||||||||||| "
    return s; 

def eyes_forward():
    #     123456789012345678    #counting characters
    s = r"  _____    _____  " + "\n"
    s+= r" /     \  /     \ " + "\n"
    s+= r"    O   ||   O    " + "\n"
    s+= r" \_____/  \_____/ "
    return s; 

def eyes_narrow():
    #     123456789012345678    #counting characters
    s = r"  _____    _____  " + "\n"
    s+= r" /     \  /     \ " + "\n"
    s+= r"   ---  ||  ---   " + "\n"
    s+= r" \_____/  \_____/ "
    return s; 
def eyes_plus():
    #     123456789012345678    #counting characters
    s = r"  _____    _____  " + "\n"
    s+= r" /     \  /     \ " + "\n"
    s+= r"   +++  ||  +++   " + "\n"
    s+= r" \_____/  \_____/ "
    return s; 

def nose_lefttriangle():
    #    123456789012345678    #counting characters
    s = r" |              | " + "\n"
    s+= r" |      /       | " + "\n"
    s+= r" |     /__      | "
    return s;
def nose_righttriangle():
    #     123456789012345678    #counting characters
    s = r" |              | " + "\n"
    s+= r" |       \      | " + "\n"
    s+= r" |      __\     | "
    return s;
def nose_big():
    #     123456789012345678    #counting characters
    s = r" |              | " + "\n"
    s+= r" |     |  |     | " + "\n"
    s+= r" |     |__|     | "
    return s;

def mouth_blankdimples():
    #    123456789012345678    #counting characters
    s = r" |   ( ____ )   | "
    return s;
def mouth_smile():
    #     123456789012345678    #counting characters
    s = r" |    \____/    | "
    return s;
def mouth_open():
    #     123456789012345678    #counting characters
    s = r" |    _______   | " + "\n"
    s+= r" |   |_______|  | " 
    return s;

def chin_plain():
    #    123456789012345678    #counting characters
    s = r" |              | " + "\n"
    s+= r" +--------------+ "
    return s;

def selfie_band():
    #    123456789012345678    #counting characters
    s = " +--------------+ " + "\n"
    s+= " |kkq        kkq| " + "\n"
    s+= " +--------------+ "
    return s;

def head_blankdimple():
    """
    Print a head that is staring at you,
    With wide eyes and blank dimples
    """
    print(hair_plain())
    print(eyes_forward())
    print(nose_lefttriangle())
    print(mouth_blankdimples())
    print(chin_plain())
def head_with_blankdimple(mouthfunc):
    """
    Print a head that is surprised,
    With pointy hair, forward eyes, right nose, and open mouth
    """
    print(hair_pointy())
    print(eyes_forward())
    print(nose_righttriangle())
    print(mouthfunc())
    print(chin_plain())
    
def head_surprised():
    """
    Print a head that is surprised,
    With pointy hair, forward eyes, right nose, and open mouth
    """
    print(hair_pointy())
    print(eyes_forward())
    print(nose_righttriangle())
    print(mouth_open())
    print(chin_plain())
def head_with_surprise(mouthfunc):
    """
    Print a head that is surprised,
    With pointy hair, forward eyes, right nose, and open mouth
    """
    print(hair_pointy())
    print(eyes_forward())
    print(nose_righttriangle())
    print(mouthfunc())
    print(chin_plain())
    
def head_smile():
    """
    Print a head that's smiling,
    With long hair, forward eyes, left nose, and a mouth smiling
    """
    print(hair_long())
    print(eyes_forward())
    print(nose_lefttriangle())
    print(mouth_smile())
    print(chin_plain())
    
def head_with_smile(mouthfunc):
    """
    Print a head that's smiling,
    With long hair, forward eyes, left nose, and a mouth specified by mouthfunc
    """
    print(hair_long())
    print(eyes_forward())
    print(nose_lefttriangle())
    print(mouthfunc())
    print(chin_plain())
    
def selfie(hairfunc, mouthfunc):
    print(hairfunc())
    print(eyes_forward())
    print(nose_lefttriangle())
    print(mouthfunc())
    print(chin_plain())
    print(selfie_band())
    
def random_head():
    x = random.randint(1,3)
    if x == 1:
        head_surprised()
    elif x == 2:
        head_blankdimple()
    else:
        head_with_smile(mouth_smile)

def totem_fixed():
    """
    Print the same totem pole with three
    heads, one blankdimple, one with smile, one that is surprised
    """
    head_blankdimple()
    head_with_smile(mouth_smile)
    head_surprised()

def totem_selfie():
    """
    Print a totem pole with three
    heads, one with pointy hair and a smile, one with long hair and blank dimples, one with plain hair
    and an open mouth. Each head should have a selfie band below the chin.
    """
    selfie(hair_pointy,mouth_smile);
    selfie(hair_long,mouth_blankdimples);
    selfie(hair_plain,mouth_open);
    


def totem_random():
    """
    Print a totem pole with three
    random heads.
    """
    random_head()
    random_head()
    random_head()



if __name__ == '__main__':
    print("\nfixed totem\n")
    totem_fixed()
    
    print("\nself totem\n")
    totem_selfie()
    
    print("\nrandom totem\n")
    totem_random()