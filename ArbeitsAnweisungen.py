anweisungen=[#("AnweisungID", (ArbeitsAnweisung,BackgroundImagePath,ShortDescription,Erstellt,LetzteAenderung,
             #       (SchrittNummer,ShortDescription,ReferenceLink,
             #               (NotizNummer,NotizText)))
             ("Anweisung1", ("Anweisung1","butterfly_transparent.png","Eine erste Anweisung","2023-05-12 10:30:34",None,
                             (1,"eine erste Schritt der ersten Anweisung",None,
                             (1,"DIE ANWEISUNG 1 Notiz 1"),
                             (2,"... 1 Notiz 2"),
                             (3,"... 1 Notiz 3")),
                             (2,"eine zweite Schritt der ersten Anweisung","praktikantin_am_paketieren.jpg"))),
             ("Anweisung2", ("Anweisung2","soccerball_transparent.png","Eine zweite Anweisung","2023-06-30 08:12:43",None,
                             (1,"eine erste Schritt der zweiten Anweisung",None,
                             (1,"DIE ANWEISUNG 2 Notiz 1"),
                             (2,"... 2 Notiz 2")))),
             (3, ("Anweisung3","fish_transparent.png","Eine dritte Anweisung","2023-07-21 14:47:44",None,
                             (1,"eine erste Schritt der dritten Anweisung",None,
                             (1,"DIE ANWEISUNG 3 Notiz")),
                             (2,"eine zweite Schritt der dritten Anweisung",None,
                             (1,"DIE ANWEISUNG 3 Notiz")),
                             (3,"eine zweite Schritt der dritten Anweisung","peketieren.png"),
                             (4,"eine dritte Schritt der dritten Anweisung",None,
                             (1,"DIE ANWEISUNG 3 Notiz")))),
             (4, ("Anweisung4","flower_transparent.png","Eine vierte Anweisung","2023-09-27 13:23:55",None,
                             (1,"eine erste Schritt der vierten Anweisung",None,
                             (1,"DIE ANWEISUNG 4 Notiz")))),
             (5, ("Anweisung5","basketball_transparent.png","Eine fünfte Anweisung","2024-02-04 16:22:25",None,
                             (1,"eine erste Schritt der fünften Anweisung",None,
                             (1,"DIE ANWEISUNG 5/1 Notiz 1"),
                             (2,"DIE ANWEISUNG 5/1 Notiz 2")),
                             (2,"eine zweite Schritt der fünften Anweisung",None,
                             (1,"DIE ANWEISUNG 5/2 Notiz 1")),
                             (3,"eine dritte Schritt der fünften Anweisung",None,
                             (1,"DIE ANWEISUNG 5/3 Notiz 1"),
                             (2,"DIE ANWEISUNG 5/3 Notiz 2"),
                             (3,"DIE ANWEISUNG 5/3 Notiz 3"),
                             (4,"DIE ANWEISUNG 5/3 Notiz 4")),
                             (1,"eine vierte Schritt der fünften Anweisung",None,
                             (1,"DIE ANWEISUNG 5/4 Notiz 1"),
                             (2,"DIE ANWEISUNG 5/4 Notiz 2"))))]

def get_anweisung(id):
    anweisung=None
    for item in anweisungen:
        if item[0]==id:
            anweisung=item[1]
    return anweisung
