from Crypto.Util.number import long_to_bytes, inverse
from gmpy2 import gcdext

def common_modules_attack(c1, c2, e1, e2, n):
    gcd, s1, s2 = gcdext(e1, e2)
    if s1 < 0:
        s1 = -s1
        c1 = inverse(c1, n)
    elif s2 < 0:
        s2 = -s2
        c2 = inverse(c2, n)
    v = pow(c1, s1, n)
    w = pow(c2, s2, n)
    x = (v * w) % n
    return x


e1 = 65537
e2 = 65521

n = 158307578375429142391814474806884486236362186916188452580137711655290101749246194796158132723192108831610021920979976831387798531310286521988621973910776725756124498277292094830880179737057636826926718870947402385998304759357604096043571760391265436342427330673679572532727716853811470803394787706010603830747

c1 = 147465654815005020063943150787541676244006907179548061733683379407115931956604160894199596187128857070739585522099795520030109295201146791378167977530770154086872347421667566213107792455663772279848013855378166127142983660396920011133029349489200452580907847840266595584254579298524777000061248118561875608240

c2 = 142713643080475406732653557020038566547302005567266455940547551173573770529850069157484999432568532977025654715928532390305041525635025949965799289602536953914794718670859158768092964083443092374251987427058692219234329521939404919423432910655508395090232621076454399975588453154238832799760275047924852124717

m = common_modules_attack(c1, c2, e1, e2, n)

print(long_to_bytes(m))
