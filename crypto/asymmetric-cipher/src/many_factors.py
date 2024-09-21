from Crypto.Util.number import inverse, long_to_bytes

n = 22853745492099501680331664851090320356693194409008912025285744113835548896248217185831291330674631560895489397035632880512495471869393924928607517703027867997952256338572057344701745432226462452353867866296639971341288543996228186264749237402695216818617849365772782382922244491233481888238637900175603398017437566222189935795252157020184127789181937056800379848056404436489263973129205961926308919968863129747209990332443435222720181603813970833927388815341855668346125633604430285047377051152115484994149044131179539756676817864797135547696579371951953180363238381472700874666975466580602256195404619923451450273257882787750175913048168063212919624027302498230648845775927955852432398205465850252125246910345918941770675939776107116419037
c = 1357660325421905236173040941411359338802736250800006453031581109522066541737601274287649030380468751950238635436299480021037135774086215029644430055129816920963535754048879496768378328297643616038615858752932646595502076461279037451286883763676521826626519164192498162380913887982222099942381717597401448235443261041226997589294010823575492744373719750855298498634721551685392041038543683791451582869246173665336693939707987213605159100603271763053357945861234455083292258819529224561475560233877987367901524658639475366193596173475396592940122909195266605662802525380504108772561699333131036953048249731269239187358174358868432968163122096583278089556057323541680931742580937874598712243278738519121974022211539212142588629508573342020495
e = 65537

# from factordb
factors = [
    16969003,
    17009203,
    17027027,
    17045117,
    17137009,
    17151529,
    17495507,
    17685739,
    17933647,
    18206689,
    18230213,
    18505933,
    18613019,
    18868781,
    18901951,
    18947729,
    19022077,
    19148609,
    19574987,
    19803209,
    20590697,
    20690983,
    21425317,
    21499631,
    21580043,
    21622099,
    21707797,
    21781139,
    21792359,
    21982481,
    22101437,
    22367311,
    22374509,
    22407799,
    22491913,
    22537409,
    22542229,
    22550677,
    22733041,
    23033441,
    23049673,
    23083759,
    23179243,
    23342663,
    23563571,
    23611043,
    23869933,
    24027973,
    24089029,
    24436597,
    24454291,
    24468209,
    24848633,
    25564219,
    25888721,
    26055889,
    26119147,
    26839909,
    27152267,
    27304777,
    27316717,
    27491137,
    27647687,
    27801167,
    28082749,
    28103563,
    28151399,
    28620611,
    29035709,
    29738689,
    29891363,
    29979379,
    30007841,
    30013391,
    30049171,
    30162343,
    30419063,
    30461393,
    30625601,
    31004861,
    31108043,
    31123457,
    31269479,
    31384663,
    31387957,
    31390189,
    31469279,
    32307589,
    32432339,
    32514061,
    32628367,
    32687509,
    32703337,
    32709977,
    32715343,
    32737429,
    32831261,
    33388603,
    33418129,
    33472771,
]

phy = 1
for _ in factors:
    phy *= _ - 1

d = inverse(e, phy)
m = pow(c, d, n)
print(long_to_bytes(m))
