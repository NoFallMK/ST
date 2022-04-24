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
define PNRV = Character ("Personne énervée", color ="#7B3A5F", callback=mid_beep)

define Misa = Character ("Misaki", color ="#1FA278", callback=high_beep)
define FNoeuds = Character ("Fille aux noeuds", color ="#1FA278", callback=high_beep)

define Sak = Character ("Sakuya", color ="#163D8A", callback=mid_beep)
define HNCH = Character ("Homme nonchalant", color ="#163D8A", callback=mid_beep)

define Ryo = Character ("Ryonosuke", color ="#00A2FF", callback=low_beep)
define HExc = Character ("Homme Excentrique", color ="#00A2FF", callback=low_beep)

define Dai = Character ("Daisuke", color ="#21ECDD", callback=low_beep)
define HMuscle = Character ("Homme Musclé", color ="#21ECDD", callback=low_beep)

define BAR = Character ("BARA", color ="#892DFF", callback=high_beep)
define Irin = Character ("Irina", color ="#892DFF", callback=high_beep)

define Irim = Character ("Irimi", color ="#FF2E00", callback=high_beep)
define FQ = Character ("Fille à queue de cheval", color ="#FF2E00", callback=high_beep)

define Sho = Character ("Shoko", color ="#FF8EE7", callback=high_beep)
define FRose = Character ("Jeune fille en rose", color ="#FF8EE7", callback=high_beep)

define Ha = Character ("Hana", color ="#FF9536", callback=high_beep)
define Lyc = Character ("Lycéenne", color ="#FF9536", callback=high_beep)

define Shiz = Character ("Shizuo", color ="#00606F", callback=low_beep)
define HBlond = Character ("Homme blond", color ="#00606F", callback=low_beep)

define Ken = Character ("Kenzo", color ="#A19DFF", callback=mid_beep)
define HRaf = Character ("Homme raffiné", color ="#A19DFF", callback=mid_beep)


label start:
    scene black with dissolve
    show text "SHOWTIME\n PROLOGUE" with Pause(1.5)
    scene black with dissolve

    Inc "Le saviez-vous ?"

    scene prologue
    with dissolve

    Inc " \"SHOWTIME\" est une émission de télé secrète où vous pouvez envoyer la personne que vous détestez le plus souffrir au cours d'un jeu de plateau mortel !"
    Inc "Et ce soir... c'est la première !"

    scene black
    with dissolve

    Inc "Comme j'ai hâte !"
    Inc "Hâte de te voir souffrir."

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

    Mero "Je suis allée au festival des cerisiers, c'était vraiment amusant même si je n'ai pas pu faire tout ce que je voulais."
    Mero "Mais bon, ça sera pour une prochaine fois !"

    hide meroko_yukata_deux
    with dissolve

    Narr "*tap tap*"

    show silhouette_un at rightish
    with dissolve

    Sil "Excusez-moi, Mademoiselle ?"

    show meroko_yukata_trois at left
    with dissolve

    Mero "Hm ?"
    Sil "Vous êtes bien Mademoiselle Tsukimori... n'est-ce pas ?"
    Mero "E-E-En effet ? Est-ce que... nous nous connaissons ?"
    Sil "Pardonnez-moi, je ne voulais pas vous effrayer, mais vous avez fait tomber votre porte-monnaie, je me suis permis de regarder dedans pour connaître votre nom..."

    hide meroko_yukata_trois at left
    show meroko_yukata_quatre at left

    play audio "audio/powerdown07.ogg"

    Mero "A-Ah ! Non c’est moi qui m’excuse, merci beaucoup ! Je ne m’étais même pas rendue compte qu’il était tomb--"

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
    Mero "(Quelqu’un m'a poussé violemment contre le sol... et je n'arrive plus à bouger... je suis... immobilisée...)"
    Mero "(J'ai mal... J'ai peur... je sens qu'on appuie sur mon dos... j'ai l'impression que je vais étouffée... )"

    scene prologuered
    with fade

    Mero "(Je relevais les yeux sur cette femme...)"
    Mero "(Elle... ne bouge pas ? Est-ce que...)"

    scene black
    with fade

    stop music fadeout 1

    Sil "Je suis désolée, mais vous avez été sélectionnée."
    Mero "(!!!!!!!!!)"

label premierrepas:
    scene black with dissolve
    show text "SHOWTIME\n CHAPITRE ZÉRO" with Pause(1.5)
    scene black with dissolve

    scene black
    Mero "(...)"
    Mero "(Qu’est-ce qui m’arrive...)"
    Mero "(Ah... Je me sens encore toute raplapla...)"
    Mero "(Je crois que je me suis endormie...)"
    Mero "Hm ?"
    Mero "(J’ouvris doucement les yeux... et...)"

    scene salle_a_manger

    show akihiro02 at right
    with dissolve
    HCharmant "Bonjour Princesse ~ ."
    show meroko02 at left
    Mero "(!!!!!!!!!!!!!)"
    hide akihiro02
    hide meroko02
    show meroko03 with dissolve
    Mero "(Je n’ai pas pu m’empêcher de sursauter.)"
    Mero "(C’est dire... que je ne m’attendais pas à ça !)"
    hide meroko03
    show meroko18
    Mero "(Il... est plutôt charmant ce jeune homme en tout cas.)"
    hide meroko18
    show meroko08
    Mero "(Enfin bon, c’est looooooin d’être le plus important...)"
    hide meroko08

    show meroko23 with dissolve
    Mero "(Une montre me serre autour de mon poignet.)"
    Mero "(Autour de moi... il y a de la nourriture partout sur une table ainsi qu’un lustre au-dessus.)"
    Mero "(Il y a environ... une quinzaine de personnes.)"
    Mero "(Je reconnais quelques célébrités, comme BARA, une célèbre actrice, mais pas plus...)"
    Mero "(Je peux voir deux écrans...  ainsi que deux portes aussi...)"
    hide meroko23

    #show Kaede
    FVerte "Hehe ~ ! Notre belle aux bois dormant s’est enfin réveillée ~ !"
    #hide Kaede
    show akihiro04 at rightish
    HCharmant "Est-ce que tu vas bien ? Je suis désolé si je t’ai fais peur..."
    show meroko01 at left
    Mero "O-Oh ! Non non, ce n’est rien ! Je vais bien je crois, mais... qu’est-ce qui se passe au juste ?"
    hide akihiro04
    show akihiro03 at rightish
    HCharmant "..."
    hide akihiro03
    Mero "(J’essayais alors de retirer cette montre, mais un homme posa sa main sur la mienne pour m’arrêter.)"
    HRouge "Ne perd pas de temps avec ça très chère, on a tous essayé de le retirer, il n’y a pas moyen... sauf si tu veux te porter volontaire pour te couper le bras ?"
    hide meroko01
    show meroko05 at left
    Mero "Non merci, ça va aller !"
    hide meroko05

    HRouge "Autrement... "
    HRouge "Enchanté ! Je m’appelle Akamaru Kobayashi, mime de profession. J’imagine que comme tout le monde tu n’as aucun souvenir qui pourrait nous aider ?"

    show meroko14 at left
    Mero "(Personne... n’a de souvenirs ? C’est terrible...)"
    hide meroko14
    show meroko24 at left
    Mero "Eh bien, enchantée ? Je m’appelle Meroko Tsukimori, je suis violoniste."
    hide meroko24
    show meroko14 at left
    Mero "Et malheureusement... je ne sais pas non plus ce que nous faisons tous ici... ni pourquoi mais--"
    hide meroko14

    PNRV "Roh allez fais chier ! T’as dormi aussi longtemps pour quoi sérieux ?!"
    show meroko34-1 at left
    Mero "J-J’aimerais bien le savoir moi aussi ?!"
    Mero "Et je n’avais pas terminé de toute façon..."
    hide meroko34-1
    PNRV "Tsss..."

    show meroko29 with dissolve
    Mero "Mon dernier souvenir..."
    Mero "Je rentrais chez moi après être allée à un festival..."
    Mero "Une femme m’a interpellé pour me rendre mon porte-monnaie"
    Mero "Puis quelqu’un d’autre m’a... écrasée contre le sol..."
    Mero "Ensuite.., cette femme m’a dit :"
    Mero "«Je suis désolée mais vous avez été sélectionnée»."
    Mero "Et.. c’est tout. Je suis désolée, ça ne doit probablement pas être grand chose."
    Mero "Je ne la connaissais pas du tout."
    hide meroko29
    show meroko42 at left
    Mero "(Raconter tout ça... me donne des frissons dans le dos.)"
    hide meroko42 at left
    FVerte "Tout va bien, tout va bien !"
    show meroko24 at left
    Mero "(Cette fille en vert s’est mise à me tapoter l’épaule.) "
    Mero "M-Merci..."
    hide meroko24

    FNoeuds "C’est mieux que rien ~ ."
    HNCH "Ah bah c’est sûr que comparer à l’autre-là ! Haha !"
    show meroko45 at left
    show akihiro03 at right
    HCharmant "..."
    hide akihiro03
    Mero "Comment ça ?"
    HNCH "Bah c’est qu’il a perdu quasi toute sa mémoire le pelo !"
    HNCH "Il se rappelle même pas de son nom !"
    hide meroko45
    show meroko27 at left
    Mero "Q-Quoi ?!"
    Mero "(C’est affreux...)"
    hide meroko27
    HExc "Haha..."
    HNCH "Ugh. Tu rigoles de ma blague j’espère..."
    HExc "Moi, je n’y crois toujours pas. J’ignore qui vous êtes pour la plupart mais vous... Et peut-être Mademoiselle Tsukimori…"
    HExc "Quelque chose me dit que vous êtes peut-être complices."

    show meroko06 at left
    Mero "Quoi..."
    Mero "(Mais qu’est-ce qu’il raconte... ?! Je viens à peine de me réveiller ?!)"
    hide meroko06

    HExc "De plus, jeune homme, vous avez pleuré lorsque, ce qui semblerait être notre ravisseur, s’est présenté sur cet écran..."
    show akihiro03 at left
    HCharmant "Je ne peux malheureusement pas l'expliquer..."
    hide akihiro03 at left
    HMuscle "Tsss. Lâche-leur la grappe sérieux. Pour le moment, on est tous dans la même merde alors pas besoin d’empirer les choses avec des théories à la noix."
    FNoeuds "En voilà une chose intelligente ~ ."
    HMuscle "..."
    Mero "(Le grand blond se contenta de lancer un regard noir à la demoiselle à nœuds... qui s’est mise à glousser.)"

    BAR "Écoutez-moi, je pense que les souvenirs de Mademoiselle Tsukimori confirment ma théorie."
    BAR "Je pense que nous sommes piégées par une émission. Voyez-vous, nous sommes plusieurs à être célèbre, et il y a des caméras d’ailleurs ~ "
    BAR "Ils ont dû sélectionner des personnes ordinaires comme la plupart d’entre vous pour pimenter tout ça."
    HRaf "Pas besoin de se prendre autant la tête à imaginer des choses dramatiques !"
    HRaf "De toute façon, l’homme de tout à l’heure devrait se manifester de nouveau, maintenant que Tsukimori s’est réveillée."
    PNRV "Z’êtes sérieux ?! La blondasse vient de dire qu’elle s’est faite putain d’agressée, kidnappée, et..."
    PNRV "ON DOIT PAS SE PRENDRE LA TÊTE ??? "
    PNRV "Y en a un qui est totalement amnésique en plus ??!!"
    FQ "Morgan..."
    HMuscle "Je m’en occupe pas deux fois."
    Morg "Quoi ENCORE ?! Vous êtes tous tarés sérieux ! ALLO ON EST DANS LA MERDE !!"
    FRose "sniff.."
    Morg "Si ça se trouve on fait partie d’un trafic d’humain chelou MAIS BON !"
    Morg "«Pas besoin de se prendre autant la tête» HEIN !"
    Lyc "LA FERME !!"
    Lyc "T’es vraiment usante tu sais ?! Y a que toi qui craint ici !"
    Morg "Mais t’es qui toi ?!"
    FRose "H-Hana s’il te plaît... c-c’est pas grave !"
    Ha "On en a tous marre de toi ! Va crever dans ton coin sérieux !"
    Morg "C’est plutôt toi qui va crever avec mon poing dans ta gueule de salope !"
    Ha "ESSAIE POUR VOIR !!"

    FNoeuds "AHAHAHAHAHAHHAHAHAHAH !!!"
    show meroko27 at left
    Mero "(La demoiselle aux nœuds s’est mise à rire... telle une sorcière, figeant tout le monde sur place, comme si elle avait jeté un sort)"
    hide meroko27
    FNoeuds "Vous faites exactement ce que notre ravisseur veut."
    FNoeuds "Vous êtes vraiment bêtes. C’est dingue !"
    HRouge "Et comment est-ce que vous savez ce que veulent nos ravisseurs, au juste ?"
    HRouge "C’est étrange tout de même, c’est comme si... vous aviez réponse à tout."
    FNoeuds "Et pourtant ~ ."
    FNoeuds "Ce n’est que du bon sens. "
    FNoeuds "Mais j’imagine que ce n’est pas à la portée de tout le monde."
    HNCH "Oh ça va tête de nœud !"

    show meroko17 at left
    Mero "..."
    hide meroko17
    HBlond "Certes, tu as raison Misaki, patati, patata..."
    HBlond "Mais tu pourrais ne pas rigoler comme ça la prochaine fois, j’ai mal aux oreilles maintenant..."
    FNoeuds "Oooh ~ comme c’est dommage !"
    HBlond "..."
    HBlond "Enfin bref ! Je propose que l’on se présente tous envers notre belle aux bois dormant adorée ! "

    show meroko06 at left
    Mero "B-Bonne idée !"
    hide meroko06 with dissolve

#ici commence le choix des présentations
#on veut que les choix amènent sur une section précise du script
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

        "Homme musclé"
        jump Daisuke

        "Fille à queue de cheval"
        jump Irimi

        "Jeune fille en rose"
        jump Shoko

        "Homme blond"
        jump Shizuo

        "Homme raffiné"
        jump Kenzo

        "Hana"
        jump Hana


return
