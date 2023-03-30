consonnants = "bcdfghjklmnpqrstvwxz"
vowels = "aeiouy"
alphabet = consonnants + vowels

reversed_cons = consonnants[::-1]
reversed_vow = vowels[::-1]

text = " Freeman and slave, patrician and plebeian, lord and serf, guild-master and journeyman, in a word, oppressor and oppressed, stood in constant opposition to one another, carried on an uninterrupted, now hidden, now open fight, a fight that each time ended, either in a revolutionary reconstitution of society at large, or in the common ruin of the contending classes. In the earlier epochs of history, we find almost everywhere a complicated arrangement of society into various orders, a manifold gradation of social rank. In ancient Rome we have patricians, knights, plebeians, slaves; in the Middle Ages, feudal lords, vassals, guild-masters, journeymen, apprentices, serfs; in almost all of these classes, again, subordinate gradations. The modern bourgeois society that has sprouted from the ruins of feudal society has not done away with class antagonisms. It has but established new classes, new conditions of oppression, new forms of struggle in place of the old ones. Our epoch, the epoch of the bourgeoisie, possesses, however, this distinct feature: it has simplified class antagonisms. Society as a whole is more and more splitting up into two great hostile camps, into two great classes directly facing each other — Bourgeoisie and Proletariat. From the serfs of the Middle Ages sprang the chartered burghers of the earliest towns. From these burgesses the first elements of the bourgeoisie were developed. The discovery of America, the rounding of the Cape, opened up fresh ground for the rising bourgeoisie. The East-Indian and Chinese markets, the colonisation of America, trade with the colonies, the increase in the means of exchange and in commodities generally, gave to commerce, to navigation, to industry, an impulse never before known, and thereby, to the revolutionary element in the tottering feudal society, a rapid development. The feudal system of industry, in which industrial production was monopolised by closed guilds, now no longer sufficed for the growing wants of the new markets. The manufacturing system took its place. The guild-masters were pushed on one side by the manufacturing middle class; division of labour between the different corporate guilds vanished in the face of division of labour in each single workshop. Meantime the markets kept ever growing, the demand ever rising. Even manufacturer no longer sufficed. Thereupon, steam and machinery revolutionised industrial production. The place of manufacture was taken by the giant, Modern Industry; the place of the industrial middle class by industrial millionaires, the leaders of the whole industrial armies, the modern bourgeois. Modern industry has established the world market, for which the discovery of America paved the way. This market has given an immense development to commerce, to navigation, to communication by land. This development has, in its turn, reacted on the extension of industry; and in proportion as industry, commerce, navigation, railways extended, in the same proportion the bourgeoisie developed, increased its capital, and pushed into the background every class handed down from the Middle Ages. We see, therefore, how the modern bourgeoisie is itself the product of a long course of development, of a series of revolutions in the modes of production and of exchange. Each step in the development of the bourgeoisie was accompanied by a corresponding political advance of that class. An oppressed class under the sway of the feudal nobility, an armed and self-governing association in the medieval commune: here independent urban republic (as in Italy and Germany); there taxable “third estate” of the monarchy (as in France); afterwards, in the period of manufacturing proper, serving either the semi-feudal or the absolute monarchy as a counterpoise against the nobility, and, in fact, cornerstone of the great monarchies in general, the bourgeoisie has at last, since the establishment of Modern Industry and of the world market, conquered for itself, in the modern representative State, exclusive political sway. The executive of the modern state is but a committee for managing the common affairs of the whole bourgeoisie. The bourgeoisie, historically, has played a most revolutionary part. The bourgeoisie, wherever it has got the upper hand, has put an end to all feudal, patriarchal, idyllic relations. It has pitilessly torn asunder the motley feudal ties that bound man to his “natural superiors”, and has left remaining no other nexus between man and man than naked self-interest, than callous “cash payment”. It has drowned the most heavenly ecstasies of religious fervour, of chivalrous enthusiasm, of philistine sentimentalism, in the icy water of egotistical calculation. It has resolved personal worth into exchange value, and in place of the numberless indefeasible chartered freedoms, has set up that single, unconscionable freedom — Free Trade. In one word, for exploitation, veiled by religious and political illusions, it has substituted naked, shameless, direct, brutal exploitation. The bourgeoisie has stripped of its halo every occupation hitherto honoured and looked up to with reverent awe. It has converted the physician, the lawyer, the priest, the poet, the man of science, into its paid wage labourers. The bourgeoisie has torn away from the family its sentimental veil, and has reduced the family relation to a mere money relation. The bourgeoisie has disclosed how it came to pass that the brutal display of vigour in the Middle Ages, which reactionaries so much admire, found its fitting complement in the most slothful indolence. It has been the first to show what man’s activity can bring about. It has accomplished wonders far surpassing Egyptian pyramids, Roman aqueducts, and Gothic cathedrals; it has conducted expeditions that put in the shade all former Exoduses of nations and crusades."


# get a list of the couple of letters often found together in the text and their frequency of occurence
def get_pairs(text):
    pairs = {}
    for i in range(len(text)-1):
        pair = text[i:i+2]
        if pair in pairs:
            pairs[pair] += 1
        else:
            pairs[pair] = 1
    return pairs

a = get_pairs(text)

# delete the pairs that are not in the alphabet
b = {}
for i in a:
    if i[0] in alphabet and i[1] in alphabet:
        b[i] = a[i]

# sort the pairs by frequency of occurence
b = sorted(b.items(), key=lambda x: x[1], reverse=True)

already_in = []
frequent = []
# get only one pair for each letter
for i in b:
    if i[0][0] not in already_in:
        already_in.append(i[0][0])
        frequent.append(i)
        
# sort the pairs by the first letter of the pair
frequent = sorted(frequent, key=lambda x: x[0][0])

# get a list without the frequency of occurence
frequent = [i[0] for i in frequent]

print(frequent)

# get the two letters that are often found together with the first letter given
def get_2_letters(letter,frequent):
    for i in frequent:
        if letter in i:
            return i