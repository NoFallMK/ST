# Hold at black for a bit.
define fadehold = Fade(0.5, 1.0, 0.5)

image splash = "splash.png"

label splashscreen:
    scene black
    with Pause(2)

    play sound "audio/ting02.ogg"

    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(2)

    return
    with fade

init python:
    def low_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/low_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def mid_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/mid_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def high_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/high_beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

transform farleft:
    xalign -0.2 yalign 1.0
transform farright:
    xalign 1.2 yalign 1.0
transform leftish:
    xalign 0.3 yalign 1.0
transform rightish:
    xalign 0.7 yalign 1.0


define Narr = Character ("", callback=mid_beep)
define Inc = Character ("???", color ="#8cc6ff", callback=high_beep)
define Sil = Character ("????", color = "#f0f8ff", callback=high_beep)

define Mero = Character ("Meroko", color ="#36c6ff", callback=high_beep)

define Aki = Character ("Akihiro", color ="#F24687", callback=mid_beep)
define HCharmant = Character ("Homme charmant", color ="#F24687", callback=mid_beep)

define Kae = Character ("Kaede", color ="#0FEA5C", callback=high_beep)
define FVerte = Character ("Fille de vert", color ="#0FEA5C", callback=high_beep)

define Aka = Character ("Akamaru", color ="#EA0F0F", callback=low_beep)
define HRouge = Character ("Homme en rouge", color ="#EA0F0F", callback=low_beep)

define Morg = Character ("Morgan", color ="#7B3A5F", callback=mid_beep)
define PNRV = Character ("Personne ??nerv??e", color ="#7B3A5F", callback=mid_beep)

define Misa = Character ("Misaki", color ="#1FA278", callback=high_beep)
define FNoeuds = Character ("Fille aux noeuds", color ="#1FA278", callback=high_beep)

define Sak = Character ("Sakuya", color ="#163D8A", callback=mid_beep)
define HNCH = Character ("Homme nonchalant", color ="#163D8A", callback=mid_beep)

define Ryo = Character ("Ryonosuke", color ="#00A2FF", callback=low_beep)
define HExc = Character ("Homme Excentrique", color ="#00A2FF", callback=low_beep)

define Dai = Character ("Daisuke", color ="#21ECDD", callback=low_beep)
define HMuscle = Character ("Homme Muscl??", color ="#21ECDD", callback=low_beep)

define BAR = Character ("BARA", color ="#892DFF", callback=high_beep)
define Irin = Character ("Irina", color ="#892DFF", callback=high_beep)

define Irim = Character ("Irimi", color ="#FF2E00", callback=high_beep)
define FQ = Character ("Fille ?? queue de cheval", color ="#FF2E00", callback=high_beep)

define Sho = Character ("Shoko", color ="#FF8EE7", callback=high_beep)
define FRose = Character ("Jeune fille en rose", color ="#FF8EE7", callback=high_beep)

define Ha = Character ("Hana", color ="#FF9536", callback=high_beep)
define Lyc = Character ("Lyc??enne", color ="#FF9536", callback=high_beep)

define Shiz = Character ("Shizuo", color ="#00606F", callback=low_beep)
define HBlond = Character ("Homme blond", color ="#00606F", callback=low_beep)

define Ken = Character ("Kenzo", color ="#A19DFF", callback=mid_beep)
define HRaf = Character ("Homme raffin??", color ="#A19DFF", callback=mid_beep)


label start:
    scene black with dissolve
    show text "SHOWTIME\n PROLOGUE" with Pause(1.5)
    scene black with dissolve

    Inc "Le saviez-vous ?"

    scene prologue
    with dissolve

    Inc " \"SHOWTIME\" est une ??mission de t??l?? secr??te o?? vous pouvez envoyer la personne que vous d??testez le plus souffrir au cours d'un jeu de plateau mortel !"
    Inc "Et ce soir... c'est la premi??re !"

    scene black
    with dissolve

    Inc "Comme j'ai h??te !"
    Inc "H??te de te voir souffrir."

    play audio "audio/female-evil-laugh.wav"
    stop audio

    scene black
    with fadehold


label kidnapping:
    play music "audio/bruitdefondnuit.ogg"
    scene prologue_kidnapping
    with dissolve

    Narr "*taptap*"

    show meroko_yukata
    with dissolve

    Mero "Vous vous demandez certainement ce que je fais au beau milieu de la nuit. Et bien... je rentre chez moi ~"

    hide meroko_yukata
    show meroko_yukata_deux

    Mero "Je suis all??e au festival des cerisiers, c'??tait vraiment amusant m??me si je n'ai pas pu faire tout ce que je voulais."
    Mero "Mais bon, ??a sera pour une prochaine fois !"

    hide meroko_yukata_deux
    with dissolve

    Narr "*tap tap*"

    show silhouette_un at rightish
    with dissolve

    Sil "Excusez-moi, Mademoiselle ?"

    show meroko_yukata_trois at left
    with dissolve

    Mero "Hm ?"
    Sil "Vous ??tes bien Mademoiselle Tsukimori... n'est-ce pas ?"
    Mero "E-E-En effet ? Est-ce que... nous nous connaissons ?"
    Sil "Pardonnez-moi, je ne voulais pas vous effrayer, mais vous avez fait tomber votre porte-monnaie, je me suis permis de regarder dedans pour conna??tre votre nom..."

    hide meroko_yukata_trois at left
    show meroko_yukata_quatre at left

    play audio "audio/powerdown07.ogg"

    Mero "A-Ah ! Non c???est moi qui m???excuse, merci beaucoup ! Je ne m?????tais m??me pas rendue compte qu???il ??tait tomb--"

    stop audio

    hide silhouette_un
    hide meroko_yukata_quatre

    stop music
    play audio "audio/249882__pfranzen__a-person-getting-knocked-down-on-their-ass.ogg"

    Narr "*PAM*"

    stop audio


    Mero "Argh..."

    play music "audio/bgm_maoudamashii_orchestra11.ogg"
    scene prologuehelp
    with vpunch

    Mero "(Qu'est-ce qui se passe... ?!)" with hpunch
    Mero "(Quelqu???un m'a pouss?? violemment contre le sol... et je n'arrive plus ?? bouger... je suis... immobilis??e...)"
    Mero "(J'ai mal... J'ai peur... je sens qu'on appuie sur mon dos... j'ai l'impression que je vais ??touff??e... )"

    scene prologuered
    with fade

    Mero "(Je relevais les yeux sur cette femme...)"
    Mero "(Elle... ne bouge pas ? Est-ce que...)"

    scene black
    with fade

    stop music fadeout 1

    Sil "Je suis d??sol??e, mais vous avez ??t?? s??lectionn??e."
    Mero "(!!!!!!!!!)"

label premierrepas:
    scene black with dissolve
    show text "SHOWTIME\n CHAPITRE Z??RO" with Pause(1.5)
    scene black with dissolve

    scene black
    Mero "(...)"
    Mero "(Qu???est-ce qui m???arrive...)"
    Mero "(Ah... Je me sens encore toute raplapla...)"
    Mero "(Je crois que je me suis endormie...)"
    Mero "Hm ?"
    Mero "(J???ouvris doucement les yeux... et...)"

    scene salle_a_manger

    show akihiro02 at right
    with dissolve
    HCharmant "Bonjour Princesse ~ ."
    show meroko02 at left
    Mero "(!!!!!!!!!!!!!)"
    hide akihiro02
    hide meroko02
    show meroko03 with dissolve
    Mero "(Je n???ai pas pu m???emp??cher de sursauter.)"
    Mero "(C???est dire... que je ne m???attendais pas ?? ??a !)"
    hide meroko03
    show meroko18
    Mero "(Il... est plut??t charmant ce jeune homme en tout cas.)"
    hide meroko18
    show meroko08
    Mero "(Enfin bon, c???est looooooin d?????tre le plus important...)"
    hide meroko08

    show meroko23 with dissolve
    Mero "(Une montre me serre autour de mon poignet.)"
    Mero "(Autour de moi... il y a de la nourriture partout sur une table ainsi qu???un lustre au-dessus.)"
    Mero "(Il y a environ... une quinzaine de personnes.)"
    Mero "(Je reconnais quelques c??l??brit??s, comme BARA, une c??l??bre actrice, mais pas plus...)"
    Mero "(Je peux voir deux ??crans...  ainsi que deux portes aussi...)"
    hide meroko23

    #show Kaede
    FVerte "Hehe ~ ! Notre belle aux bois dormant s???est enfin r??veill??e ~ !"
    #hide Kaede
    show akihiro04 at rightish
    HCharmant "Est-ce que tu vas bien ? Je suis d??sol?? si je t???ai fais peur..."
    show meroko01 at left
    Mero "O-Oh ! Non non, ce n???est rien ! Je vais bien je crois, mais... qu???est-ce qui se passe au juste ?"
    hide akihiro04
    show akihiro03 at rightish
    HCharmant "..."
    hide akihiro03
    Mero "(J???essayais alors de retirer cette montre, mais un homme posa sa main sur la mienne pour m???arr??ter.)"
    HRouge "Ne perd pas de temps avec ??a tr??s ch??re, on a tous essay?? de le retirer, il n???y a pas moyen... sauf si tu veux te porter volontaire pour te couper le bras ?"
    hide meroko01
    show meroko05 at left
    Mero "Non merci, ??a va aller !"
    hide meroko05

    HRouge "Autrement... "
    HRouge "Enchant?? ! Je m???appelle Akamaru Kobayashi, mime de profession. J???imagine que comme tout le monde tu n???as aucun souvenir qui pourrait nous aider ?"

    show meroko14 at left
    Mero "(Personne... n???a de souvenirs ? C???est terrible...)"
    hide meroko14
    show meroko24 at left
    Mero "Eh bien, enchant??e ? Je m???appelle Meroko Tsukimori, je suis violoniste."
    hide meroko24
    show meroko14 at left
    Mero "Et malheureusement... je ne sais pas non plus ce que nous faisons tous ici... ni pourquoi mais--"
    hide meroko14

    PNRV "Roh allez fais chier ! T???as dormi aussi longtemps pour quoi s??rieux ?!"
    show meroko34-1 at left
    Mero "J-J???aimerais bien le savoir moi aussi ?!"
    Mero "Et je n???avais pas termin?? de toute fa??on..."
    hide meroko34-1
    PNRV "Tsss..."

    show meroko29 with dissolve
    Mero "Mon dernier souvenir..."
    Mero "Je rentrais chez moi apr??s ??tre all??e ?? un festival..."
    Mero "Une femme m???a interpell?? pour me rendre mon porte-monnaie"
    Mero "Puis quelqu???un d???autre m???a... ??cras??e contre le sol..."
    Mero "Ensuite.., cette femme m???a dit :"
    Mero "??Je suis d??sol??e mais vous avez ??t?? s??lectionn??e??."
    Mero "Et.. c???est tout. Je suis d??sol??e, ??a ne doit probablement pas ??tre grand chose."
    Mero "Je ne la connaissais pas du tout."
    hide meroko29
    show meroko42 at left
    Mero "(Raconter tout ??a... me donne des frissons dans le dos.)"
    hide meroko42 at left
    FVerte "Tout va bien, tout va bien !"
    show meroko24 at left
    Mero "(Cette fille en vert s???est mise ?? me tapoter l?????paule.) "
    Mero "M-Merci..."
    hide meroko24

    FNoeuds "C???est mieux que rien ~ ."
    HNCH "Ah bah c???est s??r que comparer ?? l???autre-l?? ! Haha !"
    show meroko45 at left
    show akihiro03 at right
    HCharmant "..."
    hide akihiro03
    Mero "Comment ??a ?"
    HNCH "Bah c???est qu???il a perdu quasi toute sa m??moire le pelo !"
    HNCH "Il se rappelle m??me pas de son nom !"
    hide meroko45
    show meroko27 at left
    Mero "Q-Quoi ?!"
    Mero "(C???est affreux...)"
    hide meroko27
    HExc "Haha..."
    HNCH "Ugh. Tu rigoles de ma blague j???esp??re..."
    HExc "Moi, je n???y crois toujours pas. J???ignore qui vous ??tes pour la plupart mais vous... Et peut-??tre Mademoiselle Tsukimori???"
    HExc "Quelque chose me dit que vous ??tes peut-??tre complices."

    show meroko06 at left
    Mero "Quoi..."
    Mero "(Mais qu???est-ce qu???il raconte... ?! Je viens ?? peine de me r??veiller ?!)"
    hide meroko06

    HExc "De plus, jeune homme, vous avez pleur?? lorsque, ce qui semblerait ??tre notre ravisseur, s???est pr??sent?? sur cet ??cran..."
    show akihiro03 at left
    HCharmant "Je ne peux malheureusement pas l'expliquer..."
    hide akihiro03 at left
    HMuscle "Tsss. L??che-leur la grappe s??rieux. Pour le moment, on est tous dans la m??me merde alors pas besoin d???empirer les choses avec des th??ories ?? la noix."
    FNoeuds "En voil?? une chose intelligente ~ ."
    HMuscle "..."
    Mero "(Le grand blond se contenta de lancer un regard noir ?? la demoiselle ?? n??uds... qui s???est mise ?? glousser.)"

    BAR "??coutez-moi, je pense que les souvenirs de Mademoiselle Tsukimori confirment ma th??orie."
    BAR "Je pense que nous sommes pi??g??es par une ??mission. Voyez-vous, nous sommes plusieurs ?? ??tre c??l??bre, et il y a des cam??ras d???ailleurs ~ "
    BAR "Ils ont d?? s??lectionner des personnes ordinaires comme la plupart d???entre vous pour pimenter tout ??a."
    HRaf "Pas besoin de se prendre autant la t??te ?? imaginer des choses dramatiques !"
    HRaf "De toute fa??on, l???homme de tout ?? l???heure devrait se manifester de nouveau, maintenant que Tsukimori s???est r??veill??e."
    PNRV "Z?????tes s??rieux ?! La blondasse vient de dire qu???elle s???est faite putain d???agress??e, kidnapp??e, et..."
    PNRV "ON DOIT PAS SE PRENDRE LA T??TE ??? "
    PNRV "Y en a un qui est totalement amn??sique en plus ??!!"
    FQ "Morgan..."
    HMuscle "Je m???en occupe pas deux fois."
    Morg "Quoi ENCORE ?! Vous ??tes tous tar??s s??rieux ! ALLO ON EST DANS LA MERDE !!"
    FRose "sniff.."
    Morg "Si ??a se trouve on fait partie d???un trafic d???humain chelou MAIS BON !"
    Morg "??Pas besoin de se prendre autant la t??te?? HEIN !"
    Lyc "LA FERME !!"
    Lyc "T???es vraiment usante tu sais ?! Y a que toi qui craint ici !"
    Morg "Mais t???es qui toi ?!"
    FRose "H-Hana s???il te pla??t... c-c???est pas grave !"
    Ha "On en a tous marre de toi ! Va crever dans ton coin s??rieux !"
    Morg "C???est plut??t toi qui va crever avec mon poing dans ta gueule de salope !"
    Ha "ESSAIE POUR VOIR !!"

    FNoeuds "AHAHAHAHAHAHHAHAHAHAH !!!"
    show meroko27 at left
    Mero "(La demoiselle aux n??uds s???est mise ?? rire... telle une sorci??re, figeant tout le monde sur place, comme si elle avait jet?? un sort)"
    hide meroko27
    FNoeuds "Vous faites exactement ce que notre ravisseur veut."
    FNoeuds "Vous ??tes vraiment b??tes. C???est dingue !"
    HRouge "Et comment est-ce que vous savez ce que veulent nos ravisseurs, au juste ?"
    HRouge "C???est ??trange tout de m??me, c???est comme si... vous aviez r??ponse ?? tout."
    FNoeuds "Et pourtant ~ ."
    FNoeuds "Ce n???est que du bon sens. "
    FNoeuds "Mais j???imagine que ce n???est pas ?? la port??e de tout le monde."
    HNCH "Oh ??a va t??te de n??ud !"

    show meroko17 at left
    Mero "..."
    hide meroko17
    HBlond "Certes, tu as raison Misaki, patati, patata..."
    HBlond "Mais tu pourrais ne pas rigoler comme ??a la prochaine fois, j???ai mal aux oreilles maintenant..."
    FNoeuds "Oooh ~ comme c???est dommage !"
    HBlond "..."
    HBlond "Enfin bref ! Je propose que l???on se pr??sente tous envers notre belle aux bois dormant ador??e ! "

    show meroko06 at left
    Mero "B-Bonne id??e !"
    hide meroko06 with dissolve

#ici commence le choix des pr??sentations
#on veut que les choix am??nent sur une section pr??cise du script
    menu:
        Mero "Qui devrais-je aller voir ?"
        "Homme Charmant"
        jump Akihiro

        "Fille de vert"
        jump Kaede

        "Homme en rouge"
        jump Akamaru

        "Morgan"
        jump Morgan

        "Homme nonchalant"
        jump Sakuya

        "Homme muscl??"
        jump Daisuke

        "Fille ?? queue de cheval"
        jump Irimi

        "Jeune fille en rose"
        jump Shoko

        "Homme blond"
        jump Shizuo

        "Homme raffin??"
        jump Kenzo

        "Hana"
        jump Hana


return
