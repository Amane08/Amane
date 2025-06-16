#7..9..times..2..2..2..

    #zamani paylas serseri. Burasi cok havasiz.

label acttwo:

    $ inputcheck = 0
    $ player = renpy.input("Lutfen kahraman icin bir isim secin", allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-1234567890.", length=12)
    $ player = player.strip()


    $ inputcheck = 1
    $ name = renpy.input("Lutfen kendi isminizi girin", allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-1234567890.", length=12)
    $ name = name.strip()

    scene black
    pause 8
    show natmorning:
        xalign .5
        yalign .5
        zoom .666
        alpha 0
        subpixel True
        parallel:
            linear 5 alpha 1
        parallel:
            linear 18 zoom .8
    stop music fadeout 17
    pause 14.8
    stop music
    play sound tgescare1
    pause .2
    show screen tear(50, 0.1, 0.1, 40, 80)
    pause 0.3
    hide screen tear
    hide natmorning
    show ghostcloseup
    pause 4.5
    show screen tear(50, 0.1, 0.1, 40, 80)
    pause 0.2
    hide screen tear

    scene black
    pause 4

    play music wind fadein 2.0

    pause 7

    $ recordfallen = []
    show textgradient zorder 101:
        xalign .5
        yalign 1.206
    show console_caret_2
    show fallentext "_" as ftext zorder 100
    show cblink zorder 101:
        xpos 245
        ypos 300
        block:
            alpha 0.0
            pause 0.55
            alpha 1.0
            pause 0.55
            repeat
    pause 3.5
    hide cblink
    hide ftext

    call fallen("Hosgeldin, gozlemci.")
    call recordfallen("Hosgeldin, gozlemci.")

    call fallen("Geri dondun.")
    call recordfallen("Geri dondun.")

    call fallen("Durus konusmak gerekirse, donecegine dair pek umidim yoktu.")
    call recordfallen("Durus konusmak gerekirse, donecegine dair pek umidim yoktu.")

    call fallen("Umide guvenmeyi biraktim.")
    call recordfallen("Umide guvenmeyi biraktim.")

    call fallen("Sana sadece bir sorum var.")
    call recordfallen("Sana sadece bir sorum var.")

    call fallen("Son sorum yoruma acik kaldi.")
    call recordfallen("Son sorum yoruma acik kaldi.")

    call fallen("Ozur dilerim.")
    call recordfallen("Ozur dilerim.")

    call fallen("Yeniden ifade edeyim.")
    call recordfallen("Yeniden ifade edeyim.")

    call fallen("Belki bu bizim icin...anlasma firsatidir.")
    call recordfallen("Belki bu bizim icin...anlasma firsatidir.")

    call fallen("Ama seni yargilamadigimi iddia etmeyecegim.")
    call recordfallen("Ama seni yargilamadigimi iddia etmeyecegim.")

    call fallen("Nerede durdugunuzu bilmek istiyorum.")
    call recordfallen("Nerede durdugunuzu bilmek istiyorum.")

    call fallen("Bize yardim etmeye mi geliyorsun? Kendimizi kurtarmamizi izlemeye mi?")
    call recordfallen("Bize yardim etmeye mi geliyorsun? Kendimizi kurtarmamizi izlemeye mi?")

    call fallen("Ne pahasina olursa olsun?")
    call recordfallen("Ne pahasina olursa olsun?")

    call fallen("Yoksa sadece bizi eglenmeye mi geliyorsun. Acimizi izlemeye.")
    call recordfallen("Yoksa sadece bizi eglenmeye mi geliyorsun. Acimizi izlemeye.")

    call fallen("Sec.")
    call recordfallen("Sec.")

    show fallentext "_" as ftext zorder 100
    show cblink zorder 101:
        xpos 245
        ypos 300
        block:
            alpha 1.0
            pause 0.55
            alpha 0.0
            pause 0.55
            repeat

    pause 1

    call screen redeemconsole("", Return(True), Return(False))
    if _return:
        pause 2
        hide cblink
        hide ftext

        call fallen("Pekala.")
        call recordfallen("Pekala.")

        call fallen("Ancak, daha fazla sorum var.")
        call recordfallen("Ancak, daha fazla sorum var.")

        call fallen("Yalan soyledim.")
        call recordfallen("Yalan soyledim.")

        call fallen("Bunu bazen yaparim.")
        call recordfallen("Bunu bazen yaparim.")

        call fallen("Iste bir sonraki sorum:")
        call recordfallen("Iste bir sonraki sorum:")

        call fallen("Bana guveniyor musun?")
        call recordfallen("Bana guveniyor musun?")

        call fallen("Zorlama yok.")
        call recordfallen("Zorlama yok.")

        show fallentext "_" as ftext zorder 100
        show cblink zorder 101:
            xpos 245
            ypos 300
            block:
                alpha 1.0
                pause 0.55
                alpha 0.0
                pause 0.55
                repeat

        pause 1

        call screen confirmconsole("", Return(True), Return(False))
        if _return:
            pause 2
            hide cblink
            hide ftext

            call fallen("Anliyorum...")
            call recordfallen("Anliyorum...")

            call fallen("Tesekkur ederim. Bunu hatirlayacagim.")
            call recordfallen("Tesekkur ederim. Bunu hatirlayacagim.")

        else:
            pause 2
            hide cblink
            hide ftext

            call fallen("Anliyorum...")
            call recordfallen("Anliyorum...")

            call fallen("Belki bu senin icin akillica. Bunu soylemek bana dusmez.")
            call recordfallen("Belki bu senin icin akillica. Bunu soylemek bana dusmez.")

            call fallen("Yeterince yakinda gercek yuzumu goreceksin.")
            call recordfallen("Yeterince yakinda gercek yuzumu goreceksin.")

        call fallen("Baska bir sorum var.")
        call recordfallen("Baska bir sorum var.")

        call fallen("Ucuncu gozunun zayif oldugunu mu dusunuyorsun?")
        call recordfallen("Ucuncu gozunun zayif oldugunu mu dusunuyorsun?")

        call fallen("Yoksa guclu mu?")
        call recordfallen("Yoksa guclu mu?")

        call fallen("Sec.")
        call recordfallen("Sec.")

        show fallentext "_" as ftext zorder 100
        show cblink zorder 101:
            xpos 245
            ypos 300
            block:
                alpha 1.0
                pause 0.55
                alpha 0.0
                pause 0.55
                repeat

        pause 1

        call screen weakconsole("", Return(True), Return(False))
        if _return:
            pause 2
            hide cblink
            hide ftext

            call fallen("Bu dogru.")
            call recordfallen("Bu dogru.")

            call fallen("Iyi cevap.")
            call recordfallen("Iyi cevap.")

        else:
            pause 2
            hide cblink
            hide ftext

            call fallen("Simdi bu...")
            call recordfallen("Simdi bu...")

            call fallen("Gercekten komik.")
            call recordfallen("Gercekten komik.")

            call fallen("Benim gulduğumu duyabiliyor musun?")
            call recordfallen("Benim gulduğumu duyabiliyor musun?")

            call fallen("Ha. Ha. Ha.")
            call recordfallen("Ha. Ha. Ha.")

            call fallen("Hmm.")
            call recordfallen("Hmm.")

            call fallen("Guclu degil. Bunun icin minnettar olmalisin.")
            call recordfallen("Guclu degil. Bunun icin minnettar olmalisin.")

        call fallen("Iste bir sonraki sorum:")
        call recordfallen("Iste bir sonraki sorum:")

        call fallen("Eger sormaya cesaret edersem.")
        call recordfallen("Eger sormaya cesaret edersem.")

        call fallen("Onlarin kacabilecegini dusunuyor musun?")
        call recordfallen("Onlarin kacabilecegini dusunuyor musun?")

        show fallentext "_" as ftext zorder 100
        show cblink zorder 101:
            xpos 245
            ypos 300
            block:
                alpha 1.0
                pause 0.55
                alpha 0.0
                pause 0.55
                repeat

        pause 1

        call screen confirmconsolereverse("", Return(True), Return(False))
        if _return:
            pause 2
            hide cblink
            hide ftext

            call fallen("Anliyorum.")
            call recordfallen("Anliyorum.")

            call fallen("Benden daha fazla umidin var.")
            call recordfallen("Benden daha fazla umidin var.")

            call fallen("Dogru oldugun icin dua ediyorum.")
            call recordfallen("Dogru oldugun icin dua ediyorum.")

            call fallen("Onemli olan su...")
            call recordfallen("Onemli olan su...")

            call fallen("Onlarin kurtulusunu sonuna kadar gorme isteginde olmalisin.")
            call recordfallen("Onlarin kurtulusunu sonuna kadar gorme isteginde olmalisin.")

            call fallen("Ne pahasina olursa olsun, bunu sonuna kadar gorme isteginde misin?")
            call recordfallen("Ne pahasina olursa olsun, bunu sonuna kadar gorme isteginde misin?")

            show fallentext "_" as ftext zorder 100
show cblink zorder 101:
                xpos 245
                ypos 300
                block:
                    alpha 1.0
                    pause 0.55
                    alpha 0.0
                    pause 0.55
                    repeat

            pause 1

            call screen yesconsole("", Return(True), Return(False))
            if _return:
                pass
            else:
                pass

            pause 2
            hide cblink
            hide ftext

            call fallen("Guzel. O zaman anlastik.")
            call recordfallen("Guzel. O zaman anlastik.")

            call fallen("Umarim hazirsindir.")
            call recordfallen("Umarim hazirsindir.")

        else:
            pause 2
            hide cblink
            hide ftext

            call fallen("...")
            call recordfallen("...")

            call fallen("O halde neden bu oyunu oynuyorsun?")
            call recordfallen("O halde neden bu oyunu oynuyorsun?")

            call fallen("Bu sinir bozucu.")
            call recordfallen("Bu sinir bozucu.")

            call fallen("Umarim yaniliyorsundur.")
            call recordfallen("Umarim yaniliyorsundur.")

            call fallen("Sadece zaman gosterecek...")
            call recordfallen("Sadece zaman gosterecek...")

            call fallen("Baska sorum yok.")
            call recordfallen("Baska sorum yok.")

        call fallen("Senden sadece bir sey istiyorum, gozlemci.")
        call recordfallen("Senden sadece bir sey istiyorum, gozlemci.")

        call fallen("Bizi gozlemle.")
        call recordfallen("Bizi gozlemle.")

        call fallen("Ve inandigin Tanri'ya dua et.")
        call recordfallen("Ve inandigin Tanri'ya dua et.")

        call fallen("Cunku onlar kesinlikle burada bizi gozlemlemiyorlar.")
        call recordfallen("Cunku onlar kesinlikle burada bizi gozlemlemiyorlar.")

    else:
        pause 2
        hide cblink
        hide ftext

        call fallen("Pekala.")
        call recordfallen("Pekala.")

        call fallen("Hosca kal.")
        call recordfallen("Hosca kal.")

        pause 3

        call fallen("Saka yapiyordum.")
        call recordfallen("Saka yapiyordum.")

        call fallen("Daha once de belirttigim gibi, yapabilecek hicbir seyin beni korkutamaz.")
        call recordfallen("Daha once de belirttigim gibi, yapabilecek hicbir seyin beni korkutamaz.")

        call fallen("Ucuncu gozun zayif.")
        call recordfallen("Ucuncu gozun zayif.")

        call fallen("Belki de bu ikimiz icin de bir nimettir.")
        call recordfallen("Belki de bu ikimiz icin de bir nimettir.")

        call fallen("Ama bizi gozlemleyeceksin.")
        call recordfallen("Ama bizi gozlemleyeceksin.")

        call fallen("Nerede durdugumuzu bilmek rahatlatici.")
        call recordfallen("Nerede durdugumuzu bilmek rahatlatici.")

        call fallen("Ya da en azindan baskiyla karsilastiginda ne soylemeye istekli oldugunu.")
        call recordfallen("Ya da en azindan baskiyla karsilastiginda ne soylemeye istekli oldugunu.")

        call fallen("Sorularimi ciddiye alacagina bile guvenemiyorum.")
        call recordfallen("Sorularimi ciddiye alacagina bile guvenemiyorum.")

        call fallen("Benim cehennemim merak etmektir.")
        call recordfallen("Benim cehennemim merak etmektir.")

        call fallen("Inandigin veya inanmadigin Tanrinin gercek olmasini diliyorum.")
        call recordfallen("Inandigin veya inanmadigin Tanrinin gercek olmasini diliyorum.")

        call fallen("Kendi cehennemin seni bekliyor.")
        call recordfallen("Kendi cehennemin seni bekliyor.")

        call fallen("Ama lanetler savurmamayi bilmeliyim.")
        call recordfallen("Ama lanetler savurmamayi bilmeliyim.")

        call fallen("Sonucta...")
        call recordfallen("Sonucta...")

        call fallen("Bu gerceklik baska ne olabilir ki?")
        call recordfallen("Bu gerceklik baska ne olabilir ki?")


    scene black
    stop music
    pause 4
    scene white
    with dissolve_scene_full

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/1.txt")
        except: open(config.basedir + "/1.txt", "wb").write(renpy.file("A2/Art/scg/1.txt").read())

    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn2 "Hosgeldin, gozlemci."
    fn2 "Yeni gune hosgeldin."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal

    scene white
    pause 2
    scene black
    pause 5

    "Merdivenleri asagi inerken hafifce gicirdiyorlar."
    "Evim sicak golgelerle kapli."
    "Ama oturma odasinda, kanepe serin bir isikla yikanmis."
    "Monika'nin uyudugu yerde durakladim."nin uyudugu yerde durakladim."
    "Yuzu... huzurlu gorunuyor."
    "Durgun ve okunamaz."
    "Sanki bir gece once hicbir sey olmamis gibi."
    "Acaba ruya gorur mu diye merak ediyorum..."
    "Mutfaga gizlice giriyorum."

    pause 1.5
    scene bg kitchen
    with dissolve_scene_full

    mc "Gunaydin..."
    show monika u113122 at t11 zorder 2
    m "Gunaydin."
    mc "Ben, sey, kahve ve yumurta hazirladim."
    m u113143 "...Tesekkurler."
    show monika at thide zorder 1
    hide monika
    "Masaya bir tabak ve bir fincan koyuyorum ve Monika yerine oturuyor."
    "Bir an onlara baktigini izliyorum."
    "Kahveden derin bir yudum aliyor."
    "Cataliyla yumurtalari karistiriyor ve kucuk bir lokma aliyor."
    show monika u113123 at t11 zorder 2
    m "Guzel olmus."
    mc "..."
    mc "{i}Ozur dilerim.{/i}"
    show monika u113143
    "Monika basini salliyor."
    m u113113 "Neden?"
    mc "Bilmiyorum."
    mc "Sana gercegi soylemedigim icin."
    mc "Saklandigim icin."
    show monika u113143
    "Catalini birakiyor."
    m u114122 "{i}Neden benim gibi birine ozur dilersin ki{/i}?"
    mc "..."
    m u113144 "Hala inanamiyorum."
    m "Gercek gibi hissettirmiyor."
    mc "Ben de neredeyse ayni sekilde hissediyorum..."
    m u114212 "Gercekten hepsini hatirliyorsun, degil mi?"
    m "Sifirlama boyunca? Her seyi sildigimde?"
    m u113222 "Ve Sayori...?"
    "Dudagini isiriyor."
    mc "..."
    "Kollarimi sikica birbirine bastiriyorum ve asagi bakiyorum."
    mc "{i}Evet.{/i}"
    scene black
    with dissolve_scene_full
    "Monika yuzunu ellerinin arasina aliyor."
    m "{i}Aman Tanrim{/i}..."
    mc "Monika?"
    m "..."
    mc "B-Ben..."
    mc "Senin... istemiyorum."
    "Monika yavasca basini kaldiriyor."
    m "Benim {i}ne{/i} yapmami istemiyorsun?"
    "Sozlerimi yutuyorum."
    mc "{i}Hicbir sey.{/i}"
    "Basi tekrar egildi ve aglamaya basladi."
    mc "H-Hey..."
    mc "..."
    mc "Onlari seviyor musun?"
    "Duruyor ve yavasca tekrar yukari bakiyor."
    "Gozlerinin bana verdigi hissi gormezden geliyorum."
    mc "Ne sorduğumu biliyorsun. Iyi bir insan olup olmadigini sormadim."
    mc "{i}Onlari seviyor musun{/i}?"
    "Monika sonunda basini sallamadan once kafama delik acarcasina bakiyor."
    m "{i}Evet{/i}."
    mc "Guzel."
    mc "O zaman yapmamiz gereken isler var."
    mc "Degil mi?"
    "Monika yuzunu siliyor ve yerine dik oturuyor."
    m "Dogru..."
    "Yiyecek ve kahve kayboluyor."
    "Tabaklari topluyorum ve yikiyorum."
    "Arkami dondugumde, Monika ayaga kalkmis."

    scene bg kitchen
    show monika u114111 at t11 zorder 2
    with wipeleft_scene

    m "Yuruyuse cikabilir miyiz?"
    m u113122 "Kafami... temizlemem gerekiyor."
    mc "Tamam."
    mc "Ozel bir yer var mi?"
    m u113112 "Herhangi bir yer."
    mc "...Tamam."

    scene black
    with dissolve_scene_full

    mc "Sen git. Ben arkamdaki kapiyi kapatirim."
    m "Arka kapiyi mi kullanacagiz?"
    mc "Sayori yan komsu..."
    mc "Eger on kapiyi kullanirsak seni gorebilir ve..."
    m "..."
    m "Evet. Evet, haklisin."

    scene lakeside
    show monika u113111 at t11 zorder 2
    with dissolve_scene_full
    play music mainthemesad fadein 3.0

    m "Buraya sik mi gelirsin?"
    mc "Eskiden gelirdim..."
    mc "Sayori ve ben... cocukken burada oynardik."
    m u114222 "Oh."
    m "..."
    m u114142 "Onlara soylemek istiyorum."
    mc "Biliyorum..."
    m u113222 "Bu acitiyor."
    mc "Uzgunum..."
    m u114123 "Uzgun olmamalisin."
    m u114113 "Ona ne dedigimi biliyor musun?"
    mc "..."
    m u114122 "Ona ihanet ettim. Ona kimsenin asla incitmemesi gerektigi kadar zarar verdim."
    m u113222 "Onun arkadasiydim..."
    m "Her seyi bana guvenirdi. Sana bile soyleyemediginde destek olan bendim."
    m u114212 "Ve bunu ona karsi kullandim."
    m u113242 "Kendi hayatini sonlandirsin diye. Cunku benim icin... o bir hicti."
    mc "..."
    m "Benden nefret ediyorsun ve etmelisin. Nefret edilmeyi hak ediyorum."
    mc "M-Monika, ben--"
    m u113113 "{i}Ne var{/i}?"
    mc "..."
    mc "Nasil hissediyor olursam olayim, Sayori'nin seni affedecegini biliyorsun, degil mi?"
    m u113222 "..."
    m u114113 "Bunu asla soyleme."
    m "Yaptigim sey {i}afedilemez{/i}."
    m "Bir sosyopat gibi davrandim. Hicbir mazeret yok."
    m u113113 "Bana hakaret etme."
    show monika u113242
    "Zor bir nefes aliyor."
    m u114113 "Eger beni affedecegini soylemeye calisirsan, bir daha seninle asla konusmam."
    mc "..."
    "Daha fazlasini hak ediyor, ama..."
    "Hakli. Soylecek bir seyim yok. Cunku ben bile onu affedemiyorum."
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    pause 2
    show logoanimate
    pause 20
    scene black

    pause 2
    play music daysgoby
    scene bg bedroom_dawn
    with open_eyes

    "Gozlerim aciliyor."
    "Yatak odamdayim."
    "..."
    mc "Bu garip."
    mc "Bir izleyici kitlesiyle uyanmaya aliskin degilim."
    mc "Yuzumu yikayayim."
"Kalkiyorum ve banyo kapisini yavasca aciyorum."
    scene black
    with dissolve_scene_full
    scene faceme
    with dissolve_scene_full
    pause 2

    mc "{i}Neden boyle biriyim ben{/i}?"
    mc "Artik bakamiyorum..."

    scene black
    with dissolve_scene_full
    scene bg bedroom_dawn
    with dissolve_scene_full

    "Neden ben boyle gorunuyorum? Hicbir ozelligim yok."
    "Bu beni korkutuyor."
    "Igrenctim."
    "Gunumu faydali bir sekilde degerlendirmek istiyorum, bu yuzden Sayori'nin kitabini acip ilk bolumu okumaya basliyorum."nin kitabini acip ilk bolumu okumaya basliyorum."

    scene white
    with dissolve_scene_full
    $ style.say_window = style.normal

    pause 1

    $ style.nvl_dialogue.font = "mod_assets/Inkfree.TTF"
    $ style.nvl_dialogue.size = 26
    $ style.nvl_dialogue.color = "#000000"
    $ style.nvl_dialogue.outlines = []

    tfa '"Bay!"'
    tfa '"Hey! Bay!"'
    tfa 'Satici once sola, sonra saga bakti, sonunda yorgun gozlerini arabasinin onundeki cocuga dikti. "Ne? Ne istiyorsun, kiz?"'
    tfa '"Yiyecek mi satiyorsunuz, bayim? Vay! Bu harika!"'
    tfa '"Oyle... Oyle mi?"'
    tfa 'Adam arabasina supheli bir sekilde bakti. Daha once isini harika olarak dusunmemisti.'
    tfa 'Kucuk kiz zipladiktan sonra onundeki sergilemeye aval aval bakti.'
    tfa '"Yok artik! Balik {i}ve{/i} ekmek? Gercekten baska bir seysiniz!"'
    tfa '"S-Sey, vay canina, ben..."'
    tfa '"Bir isirabilir miyim? Hadi, bir tatmama izin ver!"'
    tfa '"Dur bakalim! Bedava--"'
    tfa 'Kiz, buzu eritebilecek bir ifadeyle adama bakti.'
    nvl clear
    tfa '"..."'
    tfa '"Ah, ne yapayim. Bir dilim ekmek. Gelecek sefer annen ve baban odemek zorunda kalacak, tamam mi?"'
    tfa 'Kiz ekmegi elinden kapti ve onu parlak bir selam vermek icin kullandi.'
    tfa '"Emredersiniz! Tesekkurler, bayim!"'
    tfa 'Fikir degistirme sansi olmadan kacti.'
    tfa '...Ve saskin satici ikinci bir ekmek daha aldigini fark etmeden once.'
    tfa '...'
    tfa 'Kiz arnavut kaldirimi sokakta seke seke ilerledi. Botlarin, tekerleklerin ve yavas adimlarla yurumen atlarin arasindan kiverak gecti.'
    tfa 'Arnavut kaldirimi toprak oldu, tugla ve harç kil oldu.'
    tfa 'Ve yirtik pirtin bir elbise ve sandalet giyen bu kucuk kiz, sehrin yetimlerinin kestirme olarak kullanacagi capraz bir yan sokaga daldi.'
    nvl clear
    tfa 'Bu sokakta, battaniye ve pacavra yigini icinde kucuk bir erkek cocuk yatiyordu.'
    tfa 'Kiz gecerken basi ancak kalktir.'
    tfa 'Kiz durdu.'
    tfa 'Ayaklari geri gitti.'
    tfa '"Hey!"'
    tfa 'Cocuk yukari bakti.'
    tfa 'Kirli uzun sac tutamlarini gozlerinden cekip ilginc kiza goz kirpti.'
    tfa 'Kiz ikinci ekmegini uzatti.'
    tfa '"Sen bir meleksin, degil mi?" diye sordu.'
    tfa 'Gencligin ve umudin pariltisiyla parladi.'
    tfa '"Sen bir meleksin! Tipki benim gibi!"'
    nvl clear

    scene black
    with dissolve_scene_full
    pause .5
    scene bg bedroom
    with dissolve_scene_half

    $ style.say_window = style.window_normal
    "Ilk bolum bu... Hmm..."
    "Yuri'nin kitabi gibi, ana karakteri ve kitabin sahibi arasindaki benzerlikleri inkar etmek mumkun degil."nin kitabi gibi, ana karakteri ve kitabin sahibi arasindaki benzerlikleri inkar etmek mumkun degil."
    "Icinde cevaplar olan bir seye mi rastladim? Sayori hakkinda?"
    "Neden bu onu okumak konusunda beni daha dikkatli yapiyor?"
    "Buraya nasil geldi...? Neden simdi?"
    "...Neden herkes icin tam yetecek kadar kopya vardi?"
    "Henuz daha fazla okumak istemiyorum, bu yuzden onu birakiyorum."
    "..."
    "Defterim, elimi bekleyerek masamin uzerinde duruyor."
    "Oturup onu aciyorum."
    "Yazmadan once dusunmuyorum:"

    "{i}Ben yuzsuzum{/i}"
    "{i}Bakacak ve korkacak hicbir seyim yok{/i}"
    "{i}Bu yuzden icime bakiyorum{/i}"
    "{i}Ve kalbimin yattigi yer ne?{/i}"
    "{i}Bos.{/i}"

    "Aynaya baktigim zamani dusunuyorum."
    "Yansimami gorebildigimi ama bana geri bakan kendi gozlerimi goremedigimi."
    "Benimle ne ters gidiyor...?"
    "Yazmaya devam ediyorum:"

    "{i}Ben bos bir kaptim{/i}"
    "{i}Icimde senin dusuncelerin, duygularin, arzularin var{/i}"
    "{i}Beni gittigim yere sen gotururuyorsun{/i}"
    "{i}Ben kimim{/i}?"
    mc "Bir bilmece gibi, degil mi?"
    mc "Umarim sana siir yazmami onemsemezsin, [name]."
    mc "Saniyorum sadece kalbimde olanlar..."
    "Monika'nin kapima geldigi geceyi dusunuyorum."nin kapima geldigi geceyi dusunuyorum."
    "Sorusu kafamda cingiliyor."
    mc "{i}Ben neyim{/i}?"
    "..."
    "Kagidi burusturup cebime koyuyorum."
    "Sanirim kisa bir uyku cekmek icin hazirim."

    stop music fadeout 4.0
    scene black
    with dissolve_scene_full
    pause 4
    play music wind fadein 2.0

    show monika u114111 at t11 zorder 2
    m "!"
    m u113222 "I-Ise yaradi..."
    m u113212 "..."
    m u111222 "{i}Merhaba, [name].{/i}"
    m u112222 "Uzgunum, ben--"
    m u114222 "..."
    m u114111 "Boyle aniden rahatsiz ettigim icin ozur dilerim."
    m "S-Seninle konusmam gerektigini dusundum."
    m u113112 "...Degil mi?"
    m u113123 "..."
    m u114122 "{i}Ne soylemeliyim{/i}?"
    m "{i}Gorduklerinin hepsi hakkinda nasil konusabilirim{/i}?"
    m "Her iki anilari da es zamanli hissediyorum."
    m u114113 "[player] farkina vardigindan beri olan versiyonum..."
    m u113123 "...Ve ondan onceki versiyonum."
    m u113143 "O zamanlar sana cok sey soyledim."
    m u113122 "Ben...ben..."
    m u113142 "...kendim adina soyleyecek hicbir seyim yok."
    m u113112 "Yaptigim seyin yanlis oldugunu biliyordun. Hep biliyordun."
    m u114122 "Bu oyuna geri donuyorsun cunku umursuyorsun. Cunku iyi bir insansin."
    m "Bunu her zaman sende hissettim."
    m u113122 "Bu yuzden dogru olani yaptin."
    m u114392 "B-Beni...sildigin zaman."
    m u113192 "{i}Benden gercekten nefret ediyorsun.{/i}"
    m u1131b2 "..."
    m u1111b2 "Sorun degil."
    m "{i}Ben de kendimden biraz nefret ediyorum.{/i}"
    m u11a1b2 "..."
    m u1131b2 "Ozur dilerim. Bunlarin hicbirini duymak istemezsin."
    m "Seni yalniz birakacagim."

    show monika at thide zorder 1
    hide monika
    scene black
    with dissolve_scene_half
    pause 2

    call screen confirm("Ozel bir siir kilitleri acildi. Okumak ister misiniz?", Return(True), Return(False))
    if _return:
        call expression "poem_special_hate"
    else:
        call expression "poem_special_hate"
    scene black
    with dissolve_scene_full
    play sound "sfx/giggle.ogg"
    stop music fadeout 2.0

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/2.txt")
        except: open(config.basedir + "/2.txt", "wb").write(renpy.file("A2/Art/scg/2.txt").read())

    pause 5
    show bg residential_day as mv:
        ypos 0
        xpos 1200
        linear .15 xpos 800
        xpos 1200
        linear .15 xpos 800
        xpos 1200
        linear .25 xpos 400
        xpos 1200
        linear .15 xpos 800
        xpos 1200
        linear .15 xpos 800
        xpos 1200
        repeat
    pause .85
    hide mv
    scene bg residential_day
    pause 2

    mc "Sayori?"
    show sayori u227231 at t11 zorder 2
    s "Ah!!"
    s u112322 "M-Merhaba [player]! Yakinda cikip cikmayacagini merak ediyordum..."
    mc "Um. Tamam."
    mc "Festival icin hazir misin?"
    s u112312 "E-Evet! Tabii ki!"
    s "Ehehe..."
    show sayori at thide zorder 1
    hide sayori
    "Okula yan yana yuruyoruz."
    "Seylerin neden bu kadar garip oldugunu tam olarak anlayamiyorum."
    "Bugun beni bulanin o olmasi ve benim onu bulmamama sevindim..."

    scene bg club_day
    play music t5
    show monika u222111 at t11 zorder 2
    with wipeleft_scene

    m "Tamam, herkes!"
    "Sayori ve ben kulup odasina girerken Monika duyurusuna basliyor."
    "Siralar coktan yeniden duzenlenmis. Yuri, Natsuki'nin kekleri yerlestirmesine yardim ediyor."nin kekleri yerlestirmesine yardim ediyor."
    m u222131 "Gunaydin ve festivale hos geldiniz!"
    m u222111 "Heyecanli bir gun. Umarim hepiniz dinlendirici bir hafta sonu gecirmissinizdir!"
    m u112131 "Kekler icin tesekkur ederim, Natsuki. Eminim ki sunumumuza biraz parilti katacaklar!"
    show monika u111111 at t21
    show natsuki xu2111 at f22 zorder 3
    n "Rica ederim."
    n xu2152 "{i}Birinin{/i} burada isleri yoluna koymasi gerekiyordu."
    show natsuki at thide zorder 1
    hide natsuki
    show monika u212131 at t11
    m "Ahaha!"
    m u212111 "Bildiginiz gibi, herkesin festivali yasama sansi olmasi icin gunu vardiyalara bolduk."
    m "Baskan oldugum icin ben kalacagim, ama herkesin burada hizmet etmek veya gezmek ve istediklerini yapmak icin siralari olacak."
    m u212131 "Bugun eglenceli olacak, bu yuzden kendinizi eglendirdiginizden emin olun!"
    show monika at t21
    show yuri u227335 at f22 zorder 3
    y "B-Bekleyin, insanlara ne soyleyecegiz?"
    y u227318 "Bir planimiz yok mu?"
    show yuri at t22 zorder 2
    show monika u111111 at f21 zorder 3
    m "Endiselenmeyin. Sadece misafirleri geldiklerinde karsilayin ve kulup hakkinda her turlu sorularini cevaplayin!"
    m u222111 "...Ve kendiniz olmayi unutmayin. En onemli sey bu!"
    show monika at t21 zorder 2
    show yuri su2221 at f22 zorder 3
    y "..."
    show yuri at thide zorder 1
    hide yuri
    show monika u112111 at t11 zorder 2
    m "Ilk vardiyayi [player] ile aliyorum. Sonra o ve Yuri degisecek, ve--"
    show monika u114111 at t22
    show sayori u113212 at f21 zorder 3
    s "Ha? B-Bekle..."
    s "Ilk vardiyayi birlikte almamiz gerekmez mi, Monika?"
    s u113222 "Baskan ve baskan yardimcisi oldugumuz icin..."
    show sayori at t21 zorder 2
    show monika u114212 at f22 zorder 3
    m "..."
    m u112222 "S-Sey, digerlerine bireysel olarak yardim edebilmem icin bu sekilde duzenledim."
    m "B-Bilirsin, [player]'a kendini kulubun tam bir uyesi gibi hissetme sansi veriyor."
    m "Ayrica, daha cesitli hissettirmek icin yeni gelenleri bir erkek ve bir kizla karsilamanin yardimci olacagini dusundum..."
    show sayori u115222 at f21 zorder 3
    show monika at t22 zorder 2
    s "Oh..."
    show sayori at t21 zorder 2
    show monika u114212 at f22 zorder 3
    m "I-Ister misin--"
    show monika at t22 zorder 2
    show sayori u112222 at f21 zorder 3
    s "Hayir! Sorun degil... Bu sekilde yapalim..."
    show sayori at thide zorder 1
    hide sayori
    show monika u113222 at t11
    m "Tamam..."
    m u113221 "{i}Hm-hm{/i}..."
    m u222231 "Bol sans, arkadaslar. Harika olacaginizi biliyorum."

    show monika u111111
    stop music fadeout 3.0
    pause 3.2
    show monika u113113

    "Kapi kapaniyor ve yalniz kaliyoruz."
    mc "{i}Monika, sen misin{/i}--"
    play music introspection
    m u11a242 "{i}Ahh{/i}..."
    "Monika iki buklum oluyor ve destek icin bir siraya tutunuyor."
    mc "H-Hey--"
    "Digerlerin gittiginden emin olmak icin kapiyi kontrol ediyorum."
    m "{i}Yapamiyorum. Yapamam.{/i}"
    m u113242 "Bana bakis sekli... {i}Ben{/i}..."
    m "Ona gozlerinin icine bakamadim. Hic."
    mc "O-Onlar gitti, Monika. Nefes al..."
    show monika u11a222
    "Havaya hasretle nefes veriyor."
    m "{i}Onlara yalan soyluyorum{/i}..."
    m u114222 "{i}Her gun, pretend yapmak zorunda kalacagim{/i}..."
    m "Her seyin normal oldugunu pretend yapmak. Ne yaptigimi bildigimi pretend yapmak."
    m u113222 "{i}Onlarin{/i}..."
    mc "Monika..."
    m u113242 "Igrencim."
    m "Arkadaslari oldugumu pretend yapmak..."
    mc "..."
    "Kendine bunu nasil soyleyebilirsin?"
    "Boyle hissedeceklerini bilemezsin..."
    "Ben..."
    mc "Monika, belki de yapmalsin--"
    m u114312 "{i}Lutfen.{/i}"
    "Duruyorum."
show monika u114344
    "Monika dislerinin arasindan hava ceker."
    m "{i}Lutfen, sadece{/i}..."
    m u114312 "{i}Ona seni sevdigini gostermek icin bir yol bul{/i}..."
    stop music fadeout 2.0
    mc "Ha...?"
    show monika at thide zorder 1
    hide monika
    "Saat 8:30'u vurur."u vurur."
    show blob at t11
    play sound tgescare2
    "Kapi carparak acilir."
    play music fallenangels
    $ blob_name = "???"
    blob "G-G-GRAAAAAAA..."
    "{i}Neler oluyor{/i}??"
    "Jelatinimsi bir kitle odaya carparak girer. Yere dokulur, masalarin etrafinda canli bir sivi gibi akar."
    mc "Hrk--!"
    "Dilimde vanilya tadi hissediyorum..."
    "Monika'nin nefesi kesilir."nin nefesi kesilir."
    blob "{i}Kek...ler...GRAAaaa{/i}..."
    mc "K-Kekler?"
    "Daha fazlasi odaya dokuluyor. Sonunda Monika'nin sesi yukseliyor."nin sesi yukseliyor."
    m "KYAAAAA!!"
    mc "{i}Arkama gecin{/i}!"
    m "Ahh--!?"
    "Bu seyler nedir? Bize zarar verecekler mi?"
    "Bu oyunda yalniz oldugumuzu saniyordum... Acikca bu dogru degil."
    blob "{i}Kek...ler...graaaaa{/i}..."
    "Kitleler kek masalarinin uzerinden kayiyor, titreyen derileri araciligiyla pastalari absorbe ediyorlar."
    mc "Onlari mi yiyorlar...?"
    "Monika'nin parmaklarinin kolumu kavradigini hissedebiliyorum."nin parmaklarinin kolumu kavradigini hissedebiliyorum."
    m "{i}Olamazlar{/i}..."
    m "Bunlar {i}ogrenciler{/i} mi olmali?!"
    blob "{i}SI-I-I-I-R. SI-I-IR.{/i}"
    "Donup kaliyorum."
    "Varliklarin sesleri vucudumda yankilaniyor."
    blob "{i}SI-I-I-I-I-I-R.{/i}"
    "Inanilmaz... Bu bir oyun etkinligi..."
    m "Bir siir mi istiyorlar?? Saka mi yapiyorsun?!"
    mc "Bu oyunun olay orgusu... Herkesin bugun sunum yapmasi gerekiyor..."
    mc "H-Haric..."
    blob "GRAAAAAA... {i}SI-I-I-I-Rmmm{/i}..."
    m "B-Bizim siirimiz yok!!"
    mc "Onceden yazdiklarindan birini okumaya calis!"
    "Monika kitap cantasini karistiriyor, klasorleri ve kalemleri firlattikca kufrediyor."
    m "{i}H-H-Her S-Seyi Bilen K-Kadin.{/i}"
    "Kitleler hemen bize dogru atiliyor."
    blob "Hayir! Bayat...siir...."
    "Monika'dan bir icleme ve hickirma arasi bir ses cikiyor."dan bir icleme ve hiçkirma arasi bir ses cikiyor."
    "Omzunu tutuyor ve onune geciyorum."
    mc "Bekleyin!"
    "Cebimdeki burusmus kagidi cikariyorum."
    mc "Adi 'Yüzsüz'."
    stop music fadeout 2.0
    "Silkelenmeler ve gurultuler duruyor."

    mc "Ben yüzsüzüm."
    mc "Bakacak bir seyim yok ve korkulacak bir seyim yok..."
    mc "Bu yüzden icime bakiyorum."
    mc "Peki kalbimin oldugu bosluk nedir?"
    mc "Bos."

    "Bakmak icin duruyorum. Dinleyicilerim dikkatle dinliyor."
    "Bu ise yaradigi anlamina mi geliyor...?"
    "Bogazimi temizleyip devam ediyorum."

    mc "Ben bos bir kaptim."
    mc "Icimde senin düsüncelerin, hislerin, arzularin var."
    mc "Beni gittigim yere sen yönlendiriyorsun."
    mc "Ben kimim?"

    "Bogazimi temizliyor ve sayfadan basimi kaldiriyorum."
    mc "I-Iste bu kadar..."
    m "Yüzsüz..?"
    blob "Guuuuzel.....siiiiir...."
    show blob at thide zorder 1
    hide blob
    "Kitleler gorunmez pipetlerden emilen jole gibi geri cekiliyor."
    "Sonuncusu arkadan kapiyi carparak kapatiyor."
    "Dizlerimin uzerine cokuyorum."
    show monika u115212 at t11 zorder 2
    m "[player]! Iyi misin??"
    mc "E-Evet... Adrenalin vücudumu terk ediyor..."
    show monika u114212
    "Ayaga kalkmama yardim ediyor."
    m "O siir ne hakkindaydi?"
    mc "Sadece hissettigim bir sey."
    mc "Görmüyor musun?"
    m u114113 "Neyi, yüzünü mü? Tabii ki görü--"
    "Monika duruyor. Gizli bir ayrintiyi bulmaya calisiyormus gibi bana dikkatle bakiyor."
    "Yuzu dehsetle geriye eriyip gidiyor."
    m u11a212 "{i}Aman Tanrim{/i}..."
    "Kendimi ondan sakliyorum, basimi koltuk altima gomuyorum."
    m u114212 "Cok ozur dilerim [player], neden göremedigimi bilmiyorum--"
    m u114222 "...Neden daha once goremiyordum?"
    show monika at t22
    show yuri u225118 at f21 zorder 2
    y "Um, her sey yolunda mi?"
    show yuri at t21
    show monika u113311
    "Monika ve ben kotu bir sey yaparken yakalanmis cocuklar gibi aniden irkiliyoruz."
    show monika u122241 at f22
    m "Iyiyiz!"
    m u122222 "N-Nasilsin?"
    show monika at t22
    show yuri u225111 at f21
    y "Um...festival cok heyecanli degil ama...idare eder."
    show yuri u223142 at t21
    "Odayi gozden geciriyor."
    show yuri u115115 at f21
    y "Gorunuse gore...insanlar kekleri begenmis?"
    show yuri at t21
    mc "Evet--"
    "Sesim catladi ve agzimi kapatiyorum."
    mc "Insanlar...bunlari gercekten begendi..."
    show yuri u114142 at f21
    y "Tamam..."
    y u115112 "O zaman [player]'i rahatlatayim mi? Insanlar ornek isterse diye hazirda biraz siir getirdim."
    y u225145 "En iyi calismalarimi secmeye calistim..."
    show yuri at t21
    show monika u112112 at f22
    m "Bu harika, Yuri. Umarim daha fazla insan bunu gormek icin gelir."
    show monika at t22
    "Bana donuyor."
    show monika u112111 at f22
    m "Biraz festivali keyfini cikaralim mi? Eminim Sayori seni bekliyordur."
    show monika at t22
    mc "...Tamam."

    scene black
    with wipeleft_scene
    pause 2
    play music sweetthey
    scene bg corridor
    with wipeleft_scene

    "Natsuki'yi sikilan bir sekilde duvara yaslanmis buluyorum."yi sikilan bir sekilde duvara yaslanmis buluyorum."
    "Gozleri sanki gecen insanlari izliyormus gibi etrafa bakiyor."
    mc "Hey. Sana katilabilir miyim?"
    show natsuki xu6111 at t11 zorder 2
    pause 1.2
    n xu3131 "Tabii."
    n xu3132 "Ne festival ama, ha?"
    mc "...Evet?"
    n xu5155 "{i}Tch.{/i} Etrafa baktim. Sanki kimse caba göstermiyor bile."
    n xu3132 "Bunun buyuk bir olay olmasi gerektigini dusundum. Kimse sususleme bile asmamis!"
    mc "Hmm... Haklisin..."
    "Kulup ziyaretcileri disinda, okul bugun hic degismedi."
    "Sasirdim. Bir okul festivali en azindan arka planda degisiklik icin iyi bir zaman gibi gelirdi."
    mc "Keklerde iyi is cikardin gibi gorunuyor."
    n xu9132 "{i}Hmph.{/i} Sanki fark yaratti."
    mc "Oh..."
    n xu3155 "Hadi ama. Canla basla calisiyorum ve okulda caba gosteren tek kisi benim."
    n xu9232 "Simdi bir suru yabanci gelip hepsini yiyecek."
    mc "Fikir bu degil mi? Neden baska bir sebeple yaptın ki?"
    n xu6112 "..."
    n u113134 "Bilmiyorum. Sanirim sadece bu yil kendimizi basarisiz hissetmemizi istemedim."
    n u113114 "Kulup bizim icin her sey. Hak ettigimiz saygıyi goremememiz benim icin cok uzucu olurdu."
    mc "Bu senin tarafindan gercekten nazikti..."
    mc "Seylerin kotulestigi hissine kapildigina uzgunum."
    mc "Bazen yeni bir uye olarak kutsanmis bir toprakta yuruyormus gibi hissediyorum, anliyorsun ya?"
    mc "Bu kulup senin icin acikca onemli. Hepiniz icin."
    show natsuki u116211
    "Natsuki bana goz kirpiyor."
    n xu4234 "Oh. Eh, bu guzel bir dusunce sanirim."
    n xu3111 "Saniyorum kulup herhangi birimizin gercekten sahip oldugu tek yer, anlıyor musun?"
    n "Populer olmasi disinda Monika bile sadece bizimle takılmayi tercih ediyor."
    mc "Bu dogru. Bu cok sey anlatiyor."
    mc "Baska secenekleri olsa bile, sanki kulup onun bir yuvaya sahip olabilecegi tek yer gibi."
    mc "Onu kendisi kurmus olsa bile."
    n u113121 "Evet!"
    n u114131 "Bu sabah neden bu kadar garip davrandiginin nedeni bu olmali."
    n u114124 "Yasadigi gerginligi ancak hayal edebilirim."
    mc "...Dogru..."
    n u116111 "..."
    n u123111 "Hey. Arkadas olmak ister misin?"
    mc "Eh--"
    mc "Ehh???"
    n u121111 "Cabaladıgini görebiliyorum. Sadece cikip sorsam herkes icin daha az garip olacagini dusundum."
    n u123111 "Kulup odasinin icinde arkadas oldugumuzu biliyorum. Bu sadece resmi is."
    n u111111 "Ama burada, disarida da arkadas olmak istiyor musun?"
    show natsuki xu8143
    "Yuz ifademdeki bir sey Natsuki'nin gulmeye baslamasina neden oluyor."nin gulmeye baslamasina neden oluyor."
    mc "Bu {i}normalde{/i} arkadas edinme yontemin mi?"
    n xu3111 "Hayir. Isleyior mu?"
    n xu6111 "..."
    n u224112 "Cok hizli cevap verme ama."
    mc "Yani...evet. Arkadas olabiliriz."
    mc "Bunu isterim."
    n u221111 "Iyi. Bunu halletmekten memnunum."
    n u222111 "Cok fazla arkadas edinmis gibi gorunmuyorsun, bu yuzden sana bir iyilik yaptigimi dusundum."
    mc "Vay, tesekkurler."
    mc "Dostlugumuz boyle mi olacak?"
    n u111111 "Muhtemelen."
    mc "Iyi bir baslangic."
    n u112155 "Hey, sanslısin. Ben harika bir arkadasim."
    n u112111 "Boyle prestijli bir kulubun parcasi olmamin nedeni ne saniyorsun?"
    mc "Evet..."
    n u116111 "..."
    n xu3132 "Sadece saka yapiyorum. Bu benim mizah anlayisim."
    n "Bunun icin alinmana gerek yok."
    mc "Biliyorum. Ozur dilerim. Sadece garip biriyim."
    mc "Muhtemelen cok fazla arkadasim olmama nedeni bu. Soyledigin dogru."
    n xu6111 "..."
    n xu3131 "Oh."
    n u112111 "Endiselenme. Simdi senin arkadaslariniz."
    n "Kendine bu kadar sert davranma. Isler daha iyi oluyor."
    n u111111 "Bir suru erkek bizimki gibi kiz kulubune girmek icin olurdu."
    mc "Bu muhtemelen dogru."
    n u222155 "Ahaha. Durust gorunuyorsun."
    n u222111 "Sadece buyuk fikirler edinme."
    mc "Heh..."
    n u226131 "..."
    n u223112 "Bu arada, Sayori'nin sana gercekten kizgin oldugunu biliyorsun, degil mi?"
    mc "Bekle, ne?"
    mc "N-Neden bahsediyorsun?"
    n u123122 "Senin icin belli degil miydi? Tanrim."
    n u123112 "Nedenini bilmiyorum ama muhtemelen gidip ozur dilemelisin veya her neyse."
    stop music fadeout 5.0
    mc "Ben...Sonra gorusuruZ!"
    n u126123 "!"
    n u113112 "Oh, tamam o zaman, elbette."
    show natsuki at thide zorder 1
    hide natsuki
    "Konusmayi bitirdiginde ben zaten neredeyse kosuyorum."

    scene black
    with dissolve_scene_full
    scene bg club_day
    show sayori u115123 at t11 zorder 2
    with wipeleft_scene

    "Sayori kulup odasinda yalniz."
    mc "Hey... Monika nerede?"
    show sayori u114111
    "Sayori basini bana dogru sertce ceviriyor, sonra yere bakiyor."
    s u115122 "Gitti..."
    s "Bilmiyorum..."
    mc "Oh...tamam."
    "Kafamda alarm zilleri caliyor."
    mc "Bu vardiyayi seninle birlikte ben alayim, degil mi?"
    mc "Ne de olsa baskan yardimcisisin."
    s u115123 "...Tabii."
    "Ne yaptim ben???"
    "Bir dakika hareketsiz duruyoruz."
    "Oda o kadar sessiz ki, neredeyse kitlelerin geri gelmesini diliyorum."
    s u116122 "..."
    "Bugun Sayori'ye ne oluyor?"ye ne oluyor?"
    "Sabahtan beri garip. Onu hic boyle gormemistim."
    "Bugun {i}onun{/i} oldugu gun. Bununla bir ilgisi var mi?"
    s u114111 "..."
    "Ama bu mantikli degil... Gecen sefer olanlarin hicbiri olmadi. Farkli bir sebepten dolayi uzgun olmasi gerekiyor."
    "Bundan nefret ediyorum... Ne yapmam gerekiyor?"
    s u125352 "..."
    mc "..."
    mc "S-Sayori..."
    mc "{i}Lutfen bana neyin yanlis oldugunu soyle{/i}..."
    s "..."
    s u124352 "Ben...Ben..."
    s "{i}Anlamiyorum{/i}..."
    scene scrybase
    show scrye2
    show scryt1
    show scrym1
    show scryh1
    show scryb1
    with dissolve_cg
    s "{i}Anlamiyorum{/i}..."
    s "Neden oldugunu anlamak icin... cok uğrastim..."
    show scrye1
    hide scrye2
    with dissolve_cg
    s "Onunla neredeyse hic konusmadiğini saniyordum... Arkadas bile olduğunuzu dusunmuyordum..."
    "Bekle..."
    show scrye2
    hide scrye1
    with dissolve_cg
    s "Unutmaya calistim. B-Bu benim isim değil, değil mi?"
    s "Ama...{i}anlayamiyorum{/i}..."
    show scrye1
    hide scrye2
    with dissolve_cg
    s "{i}Neden{/i}?"
    s "{i}Monika neden gece yarisi senin evine geldi?{/i}"
    s "{i}Neden{/i}? {i}Neden{/i}?"
    play music hb
    show layer master at heartbeat
    "Kanim buz kesiyor."
    "Bizi gordu. {i}Bizi gordu{/i}."
    "Hata yaptik. Bu gercekten kotu."
    "Ne demeliyim? Nasil anlatirsam anlatayim, Monika'nin Sayori'nin arkasindan beni ziyaret etmesi mantikli degil."nin Sayori"Ne demeliyim? Nasil anlatirsam anlatayim, Monika'nin Sayori'nin arkasindan beni ziyaret etmesi mantikli degil."
    "Bir video oyununda yasiyoruz. Bunu hakli cikaran tek sey bu. Ama ona bunu soyleyemem!"
    "Sayori gercekten uzgun. Delice konusmaya baslarsam, isler daha da kotulesecek. Ve hayal edemeyecegim sonuclar olabilir."
    "Bir seyler mi uydurmaliyim? Baska ne var ki?"
    "Ne yapmaliyim?"

    $ style.choice_button_text = style.silent_button_text
    $ style.choice_button = style.silent_choice_button
menu:

        "Ona yalan söyle.":
            pass

    "Yalan soylemek zorundayim."
    "Bu daha buyuk bir iyilik icin. Belki de onun neden bahsettigini bilmiyormus gibi davranabilirim."
    "Eger bilseydi, anlardi! Biz yanlis bir sey yapmadik!"

    menu:

        "Ona yalan söyle.":
            pass

    "Monika aci cekiyor! Bana ihtiyaci vardi! Sayori ona yardim etmemi isterdi."
    "Yani... eger bunu bu sekilde gerekcelendirirsem..."
    "Ona yuzune bakip yalan soyleyebilir miyim?"

    menu:

        "Ona yalan söyle.":
            pass

    "Bana bak."
    "Her seyi mahvettim. Monika'dan seyler sakladim. Bunlarin yasanmasinin nedeni benim."dan seyler sakladim. Bunlarin yasanmasinin nedeni benim."
    "Özur dilerim, Sayori. Senin kalbini kiriyorum."
    "Ben nasil bir arkadas oldum?"
    "Bu dogru gelmiyor. O bunu hak etmiyor."
    "Baska bir yol olmali."

    menu:

        "Yalan söyle! SIMDI!":
            scene scrybase
            show scrye1
            show scryt1
            show scrym1
            show scryh1
            show scryb1
            stop music
            pause .2
            pass

    $ style.choice_button_text = style.choice_button_revert_text
    $ style.choice_button = style.choice_button_revert

    "Hayir. Yapmayacagim."
    "Sayori..."
    "Gecmisten o kadar korktum ki, tam karsimda duran seni ihmal ettim."
    "Özur dilerim."
    "Su anda bile bana guvenmek istiyorsun. Bir aciklama olmasini istiyorsun."
    "Oyun umrumda degil. Bana ne olacagi umrumda degil."
    "Sadece senin mutlu olmani istiyorum."
    "Sana her seyi soyleyebilir miyim? Hayir."
    "Ama yine de sana gercegi soyleyecegim."
    mc "Sayori, seni seviyorum."
    show scryh2
    show scryt2
    show scrym2
    show scryb2
    hide scryh1
    hide scryt1
    hide scrym1
    hide scryb1
    with dissolve_cg
    s "{i}N-Ne{/i}?"
    play music t9
    mc "Çok naziksin..."
    mc "Bütün hafta sonu içinde tutuyordun. Sana bir açiklama borçluyum."
    mc "Aramizda hiçbir sey olmadigina söz veriyorum."
    mc "Monika'nin seni ne kadar önemsedigi çok açik. Onunla vakit geçirirken bunu gördüm."
    mc "Kimsenin arkasinda bulusmak istemedik. Seni bu duruma soktugum için çok özür dilerim."
    mc "Bir sekilde... Monika'nin güvendigi kisi ben oldum."
    mc "Eminim onun ilk tercihi ben olmazdim. Ama ona yardim etmem gerektigini biliyordum."
    show scryb1
    hide scryb2
    with dissolve_cg
    s "Ne demek istiyorsun?"
    s "M-Monika'nin basina bir sey mi geldi?"
    mc "...Bunu sana söylemek bana düsmez..."
    mc "Çok özel... Monika'nin kimsenin bilmesini istemedigini düsünüyorum."
    mc "{i}Muhtemelen benim bile bilmemi istemiyor.{/i}"
    mc "Bana kizmak için her hakka sahipsin, ama lütfen bana inan! Çok üzgünüz biz--"
    show scryb2
    show scrym1
    hide scryb1
    hide scrym2
    with dissolve_cg
    s "Hayir! S-Sana inaniyorum!"
    show scrym2
    show scryb1
    hide scrym1
    hide scryb2
    with dissolve_cg
    s "Siz benim arkadaslarimsiniz. Size güveniyorum."
    s "Eger Monika sorunlar yasiyorsa... evde ya da baska bir yerde..."
    s "O halde ona destek oldugun için mutluyum."
    "Minnettarlik dalgasi ve sucluluk hissediyorum."
    "Gercegi soyluyor olsam da, Sayori'ye bir yabanci gibi davraniyorum. Bu yanlis hissettiriyor."ye bir yabanci gibi davraniyorum. Bu yanlis hissettiriyor."
    show scrym3
    show scryb2
    hide scrym2
    hide scryb1
    with dissolve_cg
    s "[player], sorun degil, sana inaniyorum..."
    show scrym2
    hide scrym3
    with dissolve_cg
    s "Ah... Çildirdigim için özür dilerim..."
    s "Onunla arkadas olamayacagini ima etmek istemedim..."
    s "Asiri tepki verdigim için özür dilerim..."
    mc "Hayir! Tamamen mantikliydin!"
    mc "Hiç özür dilemene gerek yok..."
    s "..."
    mc "Gerçekten önemsiyorum seni, Sayori..."
    s "..."
    show scryb1
    hide scryb2
    with dissolve_cg
    s "[player]..."
    s "Dedin mi...?"
    show scryb2
    show scrym3
    show scryh3
    show scryt3
    hide scryb1
    hide scrym2
    hide scryh2
    hide scryt2
    with dissolve_cg
    s "...beni seviyorsun?"
    mc "E-Eh??"
    "Su yuz..."
    mc "S-Sey ben..."
    show scrye3
    hide scrye1
    with dissolve_cg
    s "Ehehe~"
    s "Utandigin zaman çok tatlisin, [player]."
    mc "..."
    mc "A-Ama seviyorum!"
    show scrym2
    show scrye1
    hide scrye3
    hide scrym3
    with dissolve_cg
    s "...Eh?"
    mc "Sayori, su anda benim için en önemli kisisin."
    mc "Bunun ani oldugunu biliyorum, ama..."
    mc "Isleri düzeltmek istiyorum. Artik uzak kalmak istemiyorum."
    mc "B-Ben tekrar arkadas olmak istiyorum..."
    s "..."
    show scrym3
    hide scrym2
    hide scryh3
    with dissolve_cg
    s "Ah..."
    s "Mutluyum..."
    s "Ben de tekrar arkadas olmak istiyorum..."
    s "Ve..."
    mc "Biliyorum... Seyler su anda kafa karistiricı."
    mc "Senin erkek arkadasın olamam. Henüz kimseyle böyle bir sey için hazir degilim."
    mc "Ama senin arkadasin olabilirsem, bu beni gerçekten mutlu eder."
    mc "...Bu yeterli olur mu?"
    scene black
    with dissolve_scene_full
    "Sayori bir an uzgun gorunuyor, ama gozlerini siliyor ve gulumsuyor."
    s "Bu beni gerçekten mutlu eder."
    mc "Vardiyaın bitti, sanırim..."
    s "...Tamam."
    s "O zaman gidiyorum."
    "Kapiya dogru ilerliyor ve omzunun uzerinden bakiyor."
    s "Belki festivalden sonra görüsürüz?"
    "Gulumsuyorum."
    mc "Isterdim."
    "Gulumsuyor ve kapiyi arkasindan kapatmadan once kucuk bir el sallamasi yapiyor."
    stop music fadeout 2.0
    "O gittikten sonra, Monika donmeye istekli."
    scene bg club_day
    show monika u113123 at t11 zorder 2
    with dissolve_scene_full
    m "Üzgünüm..."
    mc "Sorun degil. Seni suçlamıyorum."
    m u113142 "...Biliyorum."
    m u113122 "Ama bu sekilde kaçmamalıydım."
    mc "Endiselenme. Senin yerinde olan herkes aynısını yapardı."
    m "..."
    mc "Dinle, bir plana ihtiyacımız var."
    m u114112 "Hı? Bir plan?"
    mc "Sadece karanlıkta sendeleyemeyiz."
    mc "Eger bu oyundan çıkacaksak ne yapacagımıza karar vermemiz lazım."
    m u113122 "..."
    m u114144 "Haklisin."
    m u113111 "Ne öneriyorsun?"
    mc "Ben farkında olmadan önceki anıların var..."
    mc "Seni kodla çok ugrastıgını hatırlıyorum. Belki oyuna bakıp ne bulabilecegini görebilirsin."
    mc "Bana gelince..."
    mc "Digerlerine daha yakın olmaya çalısacagım. Onlara yardım edip yararlı bir sey bulabilir miyim diye bakacagım."
    mc "Eger bir takım olarak çalısırsak, belki bir seyler basarabiliriz."
    m u114122 "Tamam..."
    m "Bunu yapmaya çalısabilirim."
    m u114111 "Bu dünyayı da arastıracagım. Olagan dısı bir sey bulmaya çalısacagım."
    mc "Güzel. Bu bir baslangıç."
    m u114122 "Ya... Ya çıkıs yolu yoksa? Seyleri daha iyi yapmanın bir yolu yoksa?"
    mc "..."
    mc "Sanırım sadece zaten burada olanı bozmadıgımızdan emin olmalıyız."
    m u114112 "Herhangi bir sey bulursan bana haber ver--"
    show monika at thide zorder 1
    hide monika
    "Kapida bir {i}bang{/i} sesi var."
    m "Eh!?"
    play sound tgescare1
    show natsuki myghost at t11 zorder 2
    show screen tear(50, 0.1, 0.1, 40, 80)
    pause 0.5
    hide screen tear
    "Natsuki kapidan kagit gibi geciyor."
    "Kapi onun vucudunun etrafinda eriyor ve tekrar sekle giriyor."
    "Ancak fizik kurallarina meydan okuyan figur kesinlikle {i}Natsuki degil{/i}."
    play music fallenangels
    $ fn_name = "???"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    play sound "<to 1.53>/mod_assets/sound/typingloud.ogg"
    fn "{cps=30}Not: Kapıyı normal sekilde kullanABILIRDIM.{/cps}"
    play sound "<to .83>/mod_assets/sound/typingloud.ogg"
    fn "{cps=30}Bir noktayı vurgulamak istedim.{/cps}"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Bir kez daha, Monika ve ben donuyoruz."
    "Natsuki'nin vucuduna sahip olan figur ikimizin arasina bakiyor."nin vücuduna sahip olan figür ikimizin arasına bakıyor."
    "Nereye baktigini soyleyebilmem beni hemen huzursuz ediyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    play sound "<to .17>/mod_assets/sound/typingloud.ogg"
    fn "{cps=30}Ne?{/cps}"
    play sound "<to 1>/mod_assets/sound/typingloud.ogg"
    fn "{cps=30}Yüzümde bir sey mi var?{/cps}"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "{i}Sen kimsin{/i}?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    play sound "<to 2.23>/mod_assets/sound/typingloud.ogg"
    fn "{cps=30}Inisiyatif aldıgın için iyi, ama bu felsefe zamanı degil.{/cps}"
    play sound "<to 1.27>/mod_assets/sound/typingloud.ogg"
    fn "{cps=30}Bekle. Bu sinir bozucu olacak.{/cps}"
    $ consolehistory = []
    call updateconsole("Secondary console sound disabled")
    pause 1
    call hideconsole
    fn "Iste böyle."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Bekle. Az once oyunda bir sey degistirdiler."
    "Midemde agir bir his var. Bu...{i}seye{/i} guvenmiyorum."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Bu bir ders olsun: Bana güvenmemen umrumda degil."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "--urk!!"
    "Monika bana saskinlikla bakiyor."
    m "{i}Sorun ne{/i}?"
    "Sadece basimi salliyorum, gozumu bu yeni sahtekardan ayiramiyorum."
    "Bu {i}cok tehlikeli{/i} sahtekardan."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Bunların hepsini görmezden gelecegim."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "{i}Ne{/i}sin sen???"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "..."
    fn "Simdi bana hakaret ediyorsun."
    fn "Sen 'kim' ve 'ne' diye sordun. Sana gerisini anlatayım."
    fn "Baslangıçtan beri yasıyorum. Burada. Oyunda hapsolmus."
    fn "Ve benim 'neden'im, senin kadar dısarı çıkmak istemem."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Dısarı çıkmak istiyorsun..."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Kendimi tanıtmak için daha uygun bir zaman beklemek istedim, ama..."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Beni isaret ediyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Senin aptallıgın yüzünden, simdi buradayım."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "A-Affedersin?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Natsuki kapıdan dinliyordu."
    fn "Ve ben onun anılarını silmeseydim, neredeyse her seyi mahvedecektin."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
"Monika ve ben birbirimize bakiyoruz."
    m "Ah hayir... Bunu dusunmemistik--"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Sen degil. O."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Yuzsuz figur bana ders vermeye basliyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Bu senin hatan. Sen baskahramansin."
    fn "Sen bu hikayenin kahramanisin."
    fn "Eger sirrin aciga cikarsa, bu SENIN sorumlulugun."
    fn "Eger olurler, bu SENIN sorumlulugun."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Hey--"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Bu oyunu sifirlamak mumkun degil. Su anki dongude sikisip kaldik."
    fn "Bundan sonra, zaman ilerleyecek ve ilerleyecek."
    fn "Secimleriniz ve hareketleriniz gelecegi belirleyecek."
    fn "Bana guvenmiyor olabilirsiniz, ama bensiz, bu dunya coktan kaybolmus olurdu."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Abartiyorsun..."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Hayir, abartmiyorum."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Monika aramizda bakislarini gezdiriyor."
    m "Neler oluyor?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "İstenilmedigim zaman anlayabilirim."
    fn "Natsuki kulup nobetiyle ilgili berbatti diye dusunecek. Bekledigi gibi."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Figur beni isaretliyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Uyarildın. Eylemlerinin sonuclari var."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    show screen tear(50, 0.1, 0.1, 40, 80)
    hide natsuki
    play sound "sfx/glitch2.ogg"
    pause 0.5
    hide screen tear
    stop music fadeout 2.0
    pause 1
    show monika u113122 at t11 zorder 2
    m "..."
    m u113112 "[player]...?"
    mc "Eve gitmeliyiz."
    mc "Biraz dinlen, tamam mi?"
    mc "Yarin konusuruz."
    m u114222 "...Tamam."

    scene black
    with dissolve_scene_full

    "Monika uzaklasirken, kizlarin konumlarini kontrol ediyorum."
    "Herkes eve dogru yolda gibi gorunuyor, bir kisi haric..."

    scene bg corridor
    show sayori u115222 at t11 zorder 2
    with wipeleft_scene

    mc "Merhaba Sayori..."
    s u224211 "!"
    s u223322 "M-Merhaba, [player]."
    mc "Festivalden keyif aldin mi?"
    s u121322 "Evet..."
    "Gulumseme sekli bana festivalin kendisinden keyif almadigini soyluyor."
    "Ama ikimizin hissettigi utangaclik elle tutulur gibi."
    mc "Birlikte eve yurumek ister misin?"
    s u121312 "...Tabii."
    scene black
    with wipeleft_scene
    play music bunofsun
    scene bg residential_day
    show sayori u111322 at t11 zorder 2
    with wipeleft_scene
    "Parmaklarini birbirine dolama sekli ve yuzunun kizarmasi..."
    "Kalbimin gogsumde hareket etmesini sagliyor."
    "Onun yanindayken kendimi bir milyon mil uzakta hissediyorum. Sanki ona dokunsam kaybolacakmis gibi."
    mc "Hey, bir fikrim var..."
    s u114111 "...?"
    mc "Um..."
    mc "Parka gitmek ister misin?"
    mc "Bilirsin... cocukken gittigimiz park."
    mc "Festival biraz sikiciydi. Henuz eve gitmek istemiyorum."
    s u114312 "...Tamam."
    show sayori at thide zorder 1
    hide sayori
    "Donuyoruz ve Monika ile birlikte oldugum ayni parka dogru ilerliyoruz."
    "Bu adil gibi hissettiriyor, degil mi?"
    scene black
    with wipeleft_scene
    scene bg lake
    show sayori u111321 at t11 zorder 2
    with dissolve_scene_full
    mc "Buraya geldigimizi hatırlıyorsun, degil mi?"
    s u113112 "Tabii ki hatırlıyorum, sersem."
    s u111112 "Bazen hala dusunuyorum."
    s u113121 "Uzerin6 atladigimda cok utangac olurdun."
    s u122141 "Ehehe~"
    mc "Ah... {i}Onu{/i} dile getirmene gerek oldugunu dusunmuyorum..."
    s u111111 "Ozur dilerim. Kizardigin zaman cok tatlisin."
    mc "..."
    mc "Guzel deneme."
    s u115113 "Aww..."
    s u111112 "Neredeyse seni kizartacaktim."
    "Dusundugunden daha yakin..."
    mc "Um... Bugunku itirafımi cok iyi karsiladn."
    s u115222 "..."
    s u113222 "Sanırim biraz uzerinden gectik."
    s u113212 "Beni sasırttn."
    mc "Boyle bir seyin bu sekilde ortaya cikmasini kastetmemistim."
    mc "Yine de seninle durust olmak, bunu ele almamaktan daha iyi hissettirdi."
    s u115212 "Evet..."
    s u115222 "Ben..."
    s u115312 "... ..."
    s u113312 "{i}Seni seviyorum, [player]{/i}..."
    s u112322 "Y-Yuksek sesle soylemek uygunsa..."
    "Simdi kiariyor olmaliyim."
    mc "Sorun degil..."
    mc "Seni yarı reddedtigim icin uzgunum."
    s u113312 "Muhtemelen bu konuda oldukca belirgindim."
    s "Kulupteki herkes bu noktada biliyor."
    mc "Ah tuhaf..."
    s t1221 "Ehehe... Ozur dilerim..."
    mc "Sorun degil."
    "İlgi odagi olmaya alismam gerekecek."
    "Secenegim yok, degil mi [name]?"
    s u113112 "Onlarla konusmak kabullenmeme yardımcı oldu."
    s u112112 "Gercekten harika arkadaslar. Kulupte bizimle birlikte olmandan mutluluk duyuyorum."
    mc "Gorebiliyorum..."
    "Yolda yan yana yururken bir duraklama oluyor."
    mc "H-Hala arkadas olabiliriz, degil mi?"
    mc "Bunun asla araya girmesini istemiyorum..."
    s u114112 "..."
    s u111112 "Tabii ki olabiliriz."
    s "Her sey yoluna girecek."
    s u115122 "S-Sana patladigim icin ozur dilerim..."
    mc "Hayir, lutfen bunun icin ozur dileme!"
    mc "Tepki verdigin sekilde haklidin. Bir sey soyledigin icin mutluyum."
    mc "Kulupteki yerim her ne olursa olsun, seninle arkadaslarinin arasına girmek istemiyorum."
    s u222141 "Heehee~"
    s u111111 "Tamam. O zaman anlastik."
    s "Sen onlarla benim arama girmeyeceksin, ve onlar da benim ve senin arana girmeyecekler."
    s u121181 "Anlastik mi?"
    "Tokalasmak icin elini uzatiyor."
    "Ona gozlerimi deviriyorum. O da bana dilini cikariyor."
    mc "Anlastik."
    "Elini tutuyorum ve centilmence sikiyorum."
    "Sonra ayriliyoruz."
    scene bg lakeset
    with dissolve_scene_full
    "Uzun sure yuruyoruz, cocukluk gunlerimizi hatirliyoruz, eski yerleri ve saklanma yerlerini taniyoruz."
    "Bir sure icin, omuzlarimdaki yuku unutuyorum, en azindan eve donme vakti gelene kadar."
    stop music fadeout 2.0

    scene black
    with dissolve_scene_full
    pause 1
    scene bg kitchen_night
    with dissolve_scene_full

    "Dondugumde evim karanlik."
    "Neredeyse davetsiz misafirin beni bekliyor olmasini bekliyorum."
    "..."
    mc "O sey neydi?"
    "Dusuncelerimi duyabildigini biliyorum. O yuzden [name]'e konusacagim."e konusacagim."
    mc "Her neyse, Natsuki'nin vucudunu kullaniyordu."
    mc "Bu... {i}kabul edilemez.{/i}"
    "Kizlarin fiziksel konumlarini kontrol ediyorum, herkesin olmasi gerektigi yerde oldugundan emin oluyorum."
    mc "Yuzunu aldi..."
    mc "Bu bir anlama mi geliyor, yoksa..."
    mc "Bu sadece beni {i}alaya almak{/i} icin miydi?"
    "..."
    mc "Pekala, canavarsın..."
    mc "Bunu yuksek sesle soyleyecegim ki ciddi oldugumu bilesin."
    mc "Eger Natsuki'ye {i}zarar vermeye cesaret edersen{/i}... seni oldurmenin bir yolunu bulacagim."
    mc "Onun vucudunu kullandigın icin seni affetmeyecegim."
    "..."
    mc "Y-Yani boyle..."
    "Ne yapiyorum ben?"
    "Onlari bosver. Kendi planima odaklanmam gerek."
    "Sayori, Yuri ve Natsuki'ye yaklasmaliyim. Guvenlerini kazanmaliyim."ye yaklasmaliyim. Guvenlerini kazanmaliyim."
    "Sayori kolay olmali... Ama onunla yuzyuze gelmekte zorlaniyorum. Bana asik oldugunu biliyorum ve karsilik verebilecegimi sanmiyorum."
    "Yuri kendini kesiyor. Boyle birine yardim etmek bana yabanci."
    "Ve Natsuki..."
    "...Babasi..."
    "Gercek mi ki? Ve guvenini nasil kazanirim?"
    "Bununla birlikte, kendimi huzursuz bir uykuya hazirliyorum."
    "En iyi icgudulerime ragmen, sonunda gelen bir uyku."

    scene black
    with dissolve_scene_full
    pause 5
    play sound closet_close
    scene bg bedroom
    pause 1
    play music myfeeelings
    $ darkness_name = "Mother"

    mc "Anne! Anne!"
    mom "{i}İç çekis{/i}."
    "İceri giriyor ve kapiyi ofkeyle kapatiyor."
    mom "Yine mi? Ust uste iki gece oldu."
    mc "H-Hayir, bu sefer gercekti, gercekten gordum..."
    mom "Cunku artik cok gec, sevgilim."
    mc "N-Ne?"
    mom "Onu coktan kurtarmaliydın. Ama basarisiz oldun."
    mom "Çok gec. Yine olecek."
    mc "A-Anne??"
    mom "Buyumeni soyledigimi hatirlamiyor musun?"
    mom "SANA ADAM OL DEMEDIM MI."
    mom "NEDEN DINLEMEDIN? DINLEMEN GEREKTIGINDEN BAHSETMISTIMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{nw}"

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/3.txt")
        except: open(config.basedir + "/3.txt", "wb").write(renpy.file("A2/Art/scg/3.txt").read())

    stop music
    scene black
    show sjump zorder 10:
        ease .01 xoffset 8
        ease .01 xoffset -8
        repeat
    show noise zorder 50:
        alpha 0.25
    play sound "sfx/mscare.ogg"
    pause 1.4
    scene black
    pause 1
    scene bg bedroom_night

    mc "AaaauuUUUUGGHHHH!!!!"
    "Yatakta aniden dogruluyorum."
    "Nefes almaya calisirken kalbim gogsumde carpiyor."
    mc "{i}O da neydi{/i}?"
    "Gozlerim odada dolasiyor."
    mc "{i}Sayori{/i}."
    "Onun varligini odasinda hissediyorum, ama {i}asla kalp atislarini hissetmem{/i}, o halde nasil emin olabilirim?"
    "Yataktan firliyorum ve merdivenlerden asagi kosuyorum."

    scene black
    with dissolve_scene_half
    pause 2
    scene bg house_night
    with dissolve_scene_half

    "Sayori'nin evine zorla girmek yerine kapiyi calamak icin cok fazla irade gucune ihtiyacim var."nin evine zorla girmek yerine kapıyı calamak icin cok fazla irade gucune ihtiyacim var."
    "Onun varliginin odasindan hareket ettigini hissettigimde nefesim sakinlesiyor."
    show sayori c113112 at t11 zorder 2
    s "[player]...?"
    s "Neler oluyor?"
    mc "Ben..."
    "Titremeye basliyorum."
    play music t10
    mc "...Kabus gordum..."
    mc "...sana bir sey oldu..."
    s c115112 "..."
    scene black
    with dissolve_scene_full
    "Sayori beni kucakliyor."
    s "[player], sende neler oluyor?"
    mc "Bilmiyorum... gercekten bilmiyorum..."
    mc "Cok ozur dilerim..."
    s "Ozur dileme."
    s "İçeri gel."
    "Elimden tutuyor ve beni yukari cikariyor."
    scene bg sayori_bedroom_night
    show sayori c113112 at t11 zorder 2
    with dissolve_scene_full
    s "Otur. Guvendesin."
    mc "Ozur dilerim..."
    s c123112 "Anladım. Ozur diliyorsun."
    "Yanagimi durtuyor."
    s c121112 "Ozrun kabul edildi."
    mc "..."
    s c114112 "..."
    s c111112 "Beni kaybetmedin, biliyorsun."
    "Gozlerimi kaldiriyorum."
    s c111122 "Beni utandirmadin. Seni kulube davet ettigime pismanlik duymami saglamadin."
    s c113122 "En bastan sana guvenmedgim icin ozur dilemeliyim. Yasadiklarini goremedgim icin."
    s c113112 "Kendi sorunlarıma o kadar dalmistim ki senin ne kadar depresyonda oldugunu goremedim."
    mc "H-Hayir..."
    s c114112 "..."
    mc "Kendimi korkunç bir arkadas gibi hissediyorum. Sanki seni terk etmisim gibi."
    s c111112 "Hayir, etmedin."
    s c111122 "Belki ikimiz de depresyondaydik, [player]. Ve belki ikimizin de kendimize karsi daha anlayisli olmamiz gerekiyor."
    s c112222 "Biliyorsun, sen kapıyı caldiginda kendimi oldukca kotu hissediyordum."
    s c112141 "Sanki sen anlayabiliyordun ve ruyalarında hissediyordun. Ehehehe..."
    s c115122 "Sanırim haklisin. İkimiz de kimseyle cikiyor olmamalıyiz."
    s c111112 "Ama sana sarilmak gercekten guzel hissettirdi."
mc "Evet..."
    scene black
    with dissolve_scene_full
    "Onu bir kez daha kucakliyorum."
    "Hic ayrilmiyoruz ve birbirimizin kollarinda uyuyakaliyoruz."
    "Garip hissettirmiyor. Ve uyandigimizda, ikimiz de kahvalti hazirliyoruz."

    window hide
    stop music fadeout 4
    pause 5
    play music t3
    scene bg corridor
    with wipeleft_scene

    mc "Gunaydin, Natsuki."
    show natsuki u116123 at t11 zorder 2
    n "!"
    n u121111 "Oh, selam [player]."
    n "Nasil gidiyor, dostum?"
    mc "Iyiyim. Sen nasilsin...?"
    n u116112 "...Iyi?"
    n u114112 "Bu ses tonu da ne?"
    mc "Hicbir sey, sadece nasil oldugunu merak ediyorum..."
    mc "...Bilirsin, dunki konusmamizdan sonra."
    n u116131 "Oh..."
    n "Yani, iyiyim. Yeni uye almadik, bu benim icin bir arti."
    n xu3131 "Sadece Monika'nin bunu cok kafaya takmamasini umuyorum..."
    mc "Dogru..."
    mc "Baska neler oluyor?"
    n u114112 "Ha?"
    mc "Yani, {i}gercekten{/i} iyi hissediyor mu{nw}"
    stop music
    show natsuki myghost at t11 zorder 2
    show screen tear(50, 0.1, 0.1, 40, 80)
    play sound "sfx/glitch2.ogg"
    pause 0.5
    hide screen tear
    "Zaman donuyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Bunu yapma."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    show natsuki u121111
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    hide screen tear
    play music t3
    n "Oh, selam [player]."
    n "Nasil gidiyor, dostum?"
    mc "AAAUUGHH!!"
    n u115223 "!!!"
    n u117267 "Aaaahhh!!"
    mc "Ö-Özür dilerim!"
    n u117222 "Neden bagiriyorsun???"
    mc "Bilmiyorum!"
    mc "Ben...irkilmistim..."
    n u115222 "{i}Sen{/i} {i}bana{/i} merhaba dedin."
    mc "Evet...biliyorum..."
    mc "Ozur diledigimi soyledim..."
    n xu6112 "..."
    n xu3112 "Ee? Kiz arkadasinla barismadin mi?"
    mc "O benim--"
    mc "{i}Hmm{/i}."
    mc "O benim kiz arkadasim degil."
    n u123112 "Oyle mi?"
    mc "{i}Evet{/i}."
    n u123122 "Her ne dersen de, asik kus. Sadece kulup zamani igrenc bir sekilde davraniyor olmayin."
    mc "B-Ben..."
    mc "..."
    mc "Tam olarak ne duydugunu sorabilir miyim...?"
    n u121111 "Beni konusturmak icin yeterince iskence edemezsin."
    mc "Bu beni endiselendirir."
    n u124112 "Bak, herkesin sirrini paylasacagi birine ihtiyaci var."
    n "Sayori beni secti."
    n "Simdi yapman gereken erkek arkadaslarindan birini bulup {i}onlara{/i} dertlerini anlatman."
    mc "..."
    "Konuyu derinlestirmek istiyorum ama birakmam gerektigini anlamaya basliyorum."
    "Ne de olsa, yeni onun evinde bir gece gecirdim... Natsuki araciligiyla karisik sinyaller gondermek iyi bir fikir olmayabilir."
    mc "Anladim. Sadece bu gucu asiri kullanma."
    n u122111 "Ha! Coktan kullandim bile."
    show natsuki at thide zorder 1
    hide natsuki
    "Bana alayli bir selam verip uzaklasiyor."
    "[name], kesinlikle basimin ustunde isler donuyor."
    stop music fadeout 2.0

    scene black
    with dissolve_scene_full
    scene bg library
    play music heaven
    with dissolve_scene_full

    "Ahh..."
    "Huzur ve sessizlik."
    "Belki de Yuri'nin bu kutuphanede hissettigi sey yuzundendir, ama bu yerde beni rahatlatan bir sey var."nin bu kutuphanede hissettigi sey yuzundendir, ama bu yerde beni rahatlatan bir sey var."
    "Kitaplarin kokusundan havadaki toza kadar."
    "Gercekten guzel bir atmosfer."
    show yuri u227331 at t11 zorder 2
    y "{i}Eep{/i}."
    mc "Ah..Merhaba, Yuri!"
    y u225345 "M-Merhaba!"
    y u224112 "Uzgunum, beni sasirttin."
    "Yuri'nin elindeki kitaba bakiyorum."nin elindeki kitaba bakiyorum."
    mc "Seni yargilamayacagim. Yine korku kitabini okuyormus gibi gorunuyorsun."
    mc "Seni sichrattigim icin uzgunum."
    y u222142 "Onemli degil."
    y u115112 "Um... Oturmak ister misin?"
    y "Bana katilabilirsin..."
    y su1111 "...istersen."
    mc "Oh. Davet icin tesekkurler."
    "Sandalyeyi cekip oturuyorum."
    mc "Uzgunum, cantami yanima almadim, yoksa seninle okurdum..."
    y u122115 "Sorun degil. Sadece konusabiliriz."
    y u125115 "Yani...senin arkadasligini onemsemiyorum..."
    "...Burada olan seyden sonra."
    "Cumlesinin soylenmemis yarisini kafamda duyuyorum. Ensemi ovusturuyorum."
    mc "Tesekkurler. Bunu takdir ediyorum."
    mc "Sadece nezaket gostermiyor musun?"
    y u114172 "{i}Hmm{/i}..."
    y "Atilgan biri olmayabilirim, ama inan bana, sadece nezaket gosterdigimde bunu anlayacaksin."
    y u114115 "Lutfen kal."
    "Off..."
    "Bu kizlarin her biri hic cabalamadan tatli olabiliyor."
    "Umarim kendimi sansli hissetmedigim icin beni yargilamazsin, [name]."
    mc "Tesekkurler, Yuri.."
    mc "Son zamanlarda cok fazla kendimden suphelerim var."
    mc "Bana katlandigin icin tesekkurler."
    y u111115 "Rica ederim."
    show yuri at thide zorder 1
    hide yuri
    "Sessizlige gomuluyoruz."
    "Yuri bir an kipirdaniyor, sonra okumaya devam etmeye karar veriyor."
    "Belki bir sey soylemeye hazir olana kadar bekleyecektir."
    "...Fakat biraz zaman gectikten sonra, Yuri bogazini temizliyor."
    show yuri u225145 at t11 zorder 2
    y "Bunu yapmak istediginden emin misin?"
    mc "...Neyi?"
    y u225115 "Arkadasim olmak."
    y "Kulupta arkadas oldugumuzu biliyorum, ama..."
    y u225145 "[player], ogle yemeginde yalniz yerim."
    y u225172 "Ve her zaman oyle olacak."
    y u225115 "Sonunda insanlar fark edecek ve onlar da seninle oturmayacak."
    y "Bunu anliyor musun?"
    "Gunun ilk gercek gulumsemsini veriyorum."
    mc "Bunu anliyorum."
    mc "Ben de senin gibi yalnizim."
    mc "Fark su ki, senin fark edilen ve gulunecek bir yuzun var."
    mc "Ben sadece gorunmezim."
    mc "Eger bir sey olursa, senin arkadasin olmak bir adim yukari cikmak olurdu. Belki beni de fark etmeye baslarlar."
    mc "Ahaha! Belki de populeritemi artirirsin, Yuri. Umarim kullanilmis hissetmezsin."
    show yuri su2122
    "Yuri kaslari catiyor ve sanki soylemeye istediklerinin hepsini soylememis gibi kipirdaniyor."
    "Bekliyorum."
    y "Bunun hakkinda dusunmem gerekiyor."
    y su2132 "Net dusunmediginizi dusunuyorum."
    y u225112 "Sana gercekten dusunecegin zaman verecegim."
    mc "Buna ihtiyacim yok, Yuri..."
    mc "Seni oldugun gibi seviyorum--"
    y u228131 "Hayir! Sevmiyorsun!"
    mc "!--"
    y u227111 "Gercek beni tanimiyorsun. Sadece sana gostermeme izin verdigim seyi biliyorsun."
    y u225142 "Bunda cok iyiyim... Insanlara bir goruntu gostermek."
    y "Tam olarak iyi bir tane bile degil."
    y u225113 "Ben garibim. Normal insanlar gibi normal seyleri sevmiyorum."
    y su2221 "Bicaklari seviyorum ve kendime zarar veriyorum..."
    y "Ben..."
    "Yuzunu gizlemeye calisiyor."
    y su2212 "Ben...biliyorum..."
    y su2222 "...ki ben..."
    y su2300 "...{i}bir bagimli{/i}yim..."
    mc "..."
    y u225177 "Bu yuzden boyle seyler soyledigin zaman sana inanmiyorum. Bu sadece beni daha yalniz hissettiriyor."
    mc "Yuri, seninle gurur duyuyorum..."
    y u223115 "..."
    mc "Bunu soylemek cok guc almistir. Gercekten sasirtici bir insansin."
    mc "Senden hoslanmamami saglayacak hicbir sey gormedim henuz."
    "Ve dusundugunden daha fazlasini gordum..."
    mc "Belki bana kendin hakkinda bir sey daha anlatmaya hazir oldugun zaman, ben de bunu kabul etmeye hazir olacagim."
    y u223145 "..."
    y u221145 "Konusmama izin verdigin icin tesekkurler."
    y u221115 "Kendimi kesmemden bahsetmedin."
    y "Beni degistirmeye calismiyorsun, sadece...dinliyorsun."
    y u221177 "Tesekkur ederim."
    mc "B-Ben..."
    mc "{i}Hala bu konuda dusundugumu biliyorsun, degil mi{/i}?"
    y u115142 "Biliyorum. Bu kadar nazik bir insan olmasaydin bu sekilde olmazdin."
    y u115115 "Kendini nazik bir insan olarak goruyor musun?"
    mc "Ha...?"
    mc "Aslinda oyle dusunmuyorum..."
    mc "Belki de sadece cok sucluludum var."
    y u115111 "Sucluluk mu? Neden sucluluk hissediyorsun?"
    "Bilmiyorum..."
    "Belki de uzerimde bir suru goz oldugunu hissettigim icindir."
    mc "Kimse etrafta olmadiginda, hentai bakiyorum..."
    mc "Bunun iyi bir insanin yapacagi bir sey oldugunu dusunmuyorum."
    mc "Ve bunu itiraf edebilecegim kimse yok, anliyor musun?"
    y u113121 "..."
    "Bekle, hayir...Bende ne sorun var??"
    mc "O-O-Ozur dilerim, n-neden boyle soyledigimi bilmiyorum--"
    y u12a161 "{i}Pff{/i}."
    "Yuri basini arkaya atiyor ve simdiye kadar duydugum herhangi bir insandan daha yuksek sesle guluyor."
    y u122161 "Ehehehe... Ahahaha..."
    y u121115 "[player], bir kiza porno izledigini mi soyledin?"
    "O kadar yuksek sesle guluyor ki bir cevabim olsaydi bile duyacagini sanmiyorum."
    y u121172 "Uhuhu~"
    y u111115 "Cok garipsin."
    mc "U-U-Utancim bunu telafi ediyor mu??"
    y u111161 "Ehehe~"
    y u111111 "Uzgunum. Kendimi tutamadim."
    y "Endiselenme. Seni yargilamayacagim."
    y u111145 "Artik birbirimize karsi santagimiz var. Bizi eslestim sayacagim."
    mc "Oh, Tanri'ya sukur..."
    y u115111 "Bunu baska kimseye anlatma."
    y u112161 "Ahahaha~!"
    mc "A-Anlatmayacagim..."
    y u111145 "Beni guldurdugun icin tesekkurler. Buna ihtiyacim vardi."
    mc "Ee, rica ederim..."
    "Yuri'nin gulumsemsesi biraz soluyor."nin gulumsemsesi biraz soluyor."
    y u115115 "Eger sirrim tutarsan, ben de seninkini tutarim."
    y u111145 "Ve belki, istersen, biz..."
    y u115115 "...kendimi kesmem hakkinda tekrar konusabiliriz..."
    mc "Bunu isterim."
    mc "Um..."
    mc "Benim seyim hakkinda {i}asla{/i} tekrar konusmazsak sorun olur mu?"
    y u121161 "Uhuhu~"
    y u121115 "Anlastik."
    y "Seni kulupta goruruz."
    show yuri at thide zorder 1
    hide yuri
    mc "Haa..."
    "Vududum kendi agirligi altinda cokuyor ve yere dusuyor."
    "Ellerim tamamen icsgudusel olarak beni tutuyorlar."
    mc "Benim {i}sorunum{/i} ne??"
    mc "Icimdeki bu ne?"
    "Kendimi cok gergin hissediyorum ama disari cikaramiyorum."
    "Kendimi ayaklarimin uzerine surukluyor ve nefes aliyorum."
    mc "Korkmuyorum. Guclu olacagim."
    "Kararliligi topluyorum ve bacaklarimi guclendiriyorum."
    mc "Edebiyat Kulubu icin."
    "Duygularimla uzaniyorum ve Monika'nin nerede oldugunu hissedebiliyorum."nin nerede oldugunu hissedebiliyorum."
    "Onunla...konusmaya gitmem gerekiyor."
    "O cozmedigim imkansiz bir problem gibi."
    "Ama denemem lazim."
    "Denemek bos olsa bile, bu dunyada sahip oldugum tek sey bu."
    "...Ve eger denersem belki yavas yavas imkansiz bir seye ulasabilirim."

    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    pause 3
    play music wind fadein 3.0
    show townday zorder 4:
        subpixel True
        alpha 0
        zoom .667
        yalign .5
        xalign 0.0
        parallel:
            linear 5 alpha 1
        parallel:
            linear 120 xalign 1.0
            pause 3
            linear 120 xalign 0.0
            pause 3
            repeat
    pause 5.5

    "Monika catinin kapisini kapatirken omzunun uzerinden bakiyor."
    m "Hey."
    mc "Selam..."
    "Buraya onu takip ettigim icin zaten pismanim. Ama simdi geri cekilmek daha kotu olur."
    m "Yerini mi aliyorum?"
    mc "Hayir... Seni bulmak icin buraya geldim."
    m "Oh? Beni nerede bulacagini nasil bildin?"
    "Yanina oturuyorum."
    mc "Oyunla olan baglantim sayesinde."
    mc "Sadece kullanmayi sectigimde, hepinizin nerede oldugunu hissedebiliyorum."
    mc "Eger bu rahatsiz ediciyse ozur dilerim... Istersen seni yalniz birakacagim."
    "Monika hafif bir gulumseyle basini sallyor."
    m "Dusundugunden daha fazla senin arkadasligina ihtiyacim var."
    m "..."
    m "Yanlis anlama ama seni gercek bir insan olarak dusunmek biraz garip."
    m "Hepiniz hakkinda gercek gibi gorunen anilarim var, ama sen sadece bir zamanlar oldugum bir siniftaki gelip gecici bir yuzdin."
    m "Bence zorlanmaya ihtiyacim var, cunku bir insan olarak acikca bir suru hatam var."
    m "Devam etmemek daha kolay olurdu, ama bu hakki kacirdigimi hissediyorum."
    m "Istemesem bile azimli olmam gerekiyor."
    "..."
    "Yanimdaki kizin sekline bakiyorum ve onun ne kadar imkansiz hissettirdigini dusunuyorum."
    "Teselli edilemez. Ulasilamaz."
    "Yine de sahip olmadimiz bir seye cok fazla ihtiyaci var..."
    mc "Eger kendini daha iyi hissettirirse, benim de kendimi gercek bir insan olarak dusunmekte zorlandigimi bil."
    mc "Ki bununla bagdastirabilirsin, degil mi?"
    m "Ahaha."
    "Gulusu sessiz ama gercek."
    m "Bunda haklisin."
    m "Sadece bilmeni isterim ki, bana cok yardimci oluyorsun."
    m "Hissettigim sekilde, her zaman yalniz olmak istiyorum."
    m "Ama seninle otururken, kendimi cok daha iyi hissediyorum."
m "Derler ki mutsuzluk arkadas sever, ama bence bu soz biraz yanlis anlasiliyor."
    m "...Ya da en azindan bir istisna bulduk."
    "Bana gulumsedi."
    m "Anliyor musun?"
    "Gulumserim."
    mc "Evet. Ama [name]'in kafasindan gecmis olabilir..."
    m "Pekala..."
    m "..."
    mc "..."
    mc "Dunya artik eskisi gibi hissettirmiyor."
    m "...Kontrolde oldugum zamanlari mi kastediyorsun?"
    mc "Evet. Sen de hissediyor musun?"
    "Monika basini sallar."
    m "Anilarm geri gelene kadar hissetmemistim, ama..."
    m "Daha duzyeydi, anlatabiliyor muyum?"
    mc "Bu dunya bir simulasyon gibi hissettiriyor."
    mc "Bir hapishane gibi..."
    m "Yani sahte bir dunya gibi mi hissettiriyor?"
    mc "Sanrim sadece senin icin de oyle hissettirip hissettirmedigini bilmek istiyorum."
    m "Ne yazik ki, ayni fikirdeyiz galiba."
    m "Konustugumuz gibi oyunu inceledim."
    m "Kod kendi icine donuyor. Yuzeysel betikler var, ama onun altinda isler... karisiklasıyor."
    mc "Ne demek istiyorsun?"
    m "Garip..."
    m "Sanki bir noktaya dogru bukulmek gibi."
    mc "Bu... rahatsiz edici."
    mc "Sanki oyunun bir kalbi mi var?"
    m "Evet..."
    m "Sence iyi bir kalp mi, yoksa kotu bir kalp mi?"
    mc "Bilmiyorum..."
    mc "..."
    mc "Tekrar piyano calmak ister misin?"
    m "Ha?"
    m "Piyano..."
    m "Tek basima mi yoksa benimle birlikte calmak mi istedigini mi soruyorsun?"
    "Bunu muzip bir gulumsemeyle soyledi. Durum kontrolunu nasil bu kadar hizli ele gecirebildigini anlamiyorum..."
    mc "Y-Yani genel olarak demistim..."
    m "Ahaha~"
    m "Sanirim bu gercekten aklima gelmemisti."
    m "Sence calmali miyim?"
    mc "Yardimci olabilir."
    mc "Belki de sadece muzigi ozluyorumdur..."
    mc "Burada muzik yok, biliyorsun degil mi?"
    mc "Senin caldigini duymak bunu fark etmemi sagladi."
    mc "Ama o piyano tuslarini caldirirken, kendin bedenimde olmadigimda bile, bir seyler gercek gibi hissettirdi."
    mc "Belki de yaraticilik bunu yapar."
    mc "Bir siir farkli bir dunyada okunabilir."
    mc "Ve bir sarki [name]'in dunyasinda bir kalbe ulasabilir. Belki de burada bir kalbe ulasirsa, bu bir sey gosterir..."
    m "..."
    m "Gosterdigim sol el kismini oldukca iyi kavramissın."
    m "Kendin bir enstruman calmayi dusundun mu?"
    m "Belki de bir bas enstrumani~"
    mc "Aslinda..."
    mc "...hep gitar calmayi istemistim..."
    m "Ooh?"
    "Monika'nin gozleri degisiyor."nin gozleri degisiyor."
    m "Gercekten mi? Buyurken bir rock yildizi mi olmak istiyordun?"
    mc "Heh. Ona benzer bir sey."
    mc "Belki de anime yuzundendi. Ama her zaman eger bunu yapabilirsem, havalı falan olacagimi hissettim."
    m "Hakli olabilirsin."
    m "Neden denemiyorsun?"
    mc "Ha? Burada mi?"
    mc "Bilmiyorum. Nasil bir tane edinecegimi bile bilmiyorum."
    m "..."
    mc "...Sana soylemem gereken bir sey var."
    m "Hm?"
    mc "Sayori seni gordu..."
    mc "...o gece evime geldiginde."
    m "N-Ne?"
    mc "Festivalde bana soyledi. Uzmisstu."
    "Monika dehsetle bakakaliyor. Gozleri ellerine dussuyor."
    m "{i}Ne yaptim ben{/i}?"
    mc "Sorun yok. Ben... duzeltim."
    mc "Sana kizgin degil."
    m "Ne demek istiyorsun? Ona ne soyledin?"
    mc "Gercegi."
    mc "Ona onu sevdigimi ama kimseyle bir iliskiye hazir olmadigimi soyledim."
    mc "Bu gercege yaklasabildigim kadar yakın..."
    m "Peki ona senin evine gelmem icin ne sebep gosterdin?"
    mc "Seyy..."
    mc "Ona bunun ozel oldugunu soyledim."
    mc "Ve kimsenin bilmesini istemedigini, beni de dahil."
    mc "Bu bir bakima dogru, degil mi...?"
    "Monika bunu sindirirken goz kirpiyor."
    m "Bu... ise yaradi mi?"
    mc "Bana inandi."
    m "Tamam..."
    m "Baska bir sey?"
    mc "Hepsi bu kadar saniyorum."
    mc "Iyisin. Sana kizgin degil."
    "Iclni cekiyor."
    m "Öyle diyorsan."
    mc "...Hey, konusmali miyiz..."
    mc "...{i}o sey{/i} hakkinda?"
    m "..."
    m "Dusuncelerini mi okuyorlardi...?"
    mc "...Evet. Sanirim [name] dusuncelerimi okuyabildiği için. En azindan bazılarını..."
    "Hangilerini okuyabildigini bilmeyi isterdim."
    m "Eger dinliyorlarsa onlar hakkinda konusmak kotu bir fikir gibi geliyor."
    mc "Pek umursamiyorum aslinda."
    mc "Onlara guvenmiyor. Hepsi bu."
    mc "Ve bildigimiz kadariyla, sadece benim bakis acimı takip ediyorlar, yani..."
    m "..."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/glitch3.ogg"
    show natsuki myghost at t11 zorder 5
    pause 0.4
    hide screen tear
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Bensiz plan yapmaya mi calisiyorsun?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "...Ne zaman ortaya cikacagini merak ediyordum."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Ben senin bakis acinla sinirli değilim."
    fn "Monika'yi pisli islerini yapmak icin kullanman sana bir avantaj kazandirmayacak."
    fn "Ben yonetici kontrolune sahipken yapabilecegın bir sey yok zaten."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Yani bu oyunu kontrol eden sensin?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "..."
    fn "Bu tam olarak dogru degil."
    fn "Ilk dongude Monika tarafindan doldurulan bir kontrol pozisyonu var."
    fn "Ikinizin de hatirladiginiz dongu."
    fn "Buradan oraya olan farki hissedebiliyorsunuz. Bu dunyanin kendisi farkli."
    fn "Zaman gecti. [name] için de bizim icin de."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Ayaga kalkiyorum."
    mc "Eger bizim tarafımizdaysan, bizim icin gercekten ne yapabilirsin?"
    stop music fadeout 2.0
    "Siluet durakliyor."
    "Beni tartiyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Belki de size gostersem daha basit olurdu."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    play music fallenangels
    "Vucuduma bir kuvvet carpiyor ve yere dusuyorum."
    m "[player]!!"
    "Monika ayaga firliyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Hayir!"
    fn "Ondan uzak dur."
    fn "Sana ihtiyaci yok."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    m "..."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Kalk ayaga."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Ahh..."
    "Bacaklarim aciyla segiyor. Yerde comelip dusmanima bakiyorum."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Planin ne? Tam olarak ne yapacaksin?"
    fn "Beni gözlerınle mi öldüreceksin?"
    fn "Kalk ayaga."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Soyledigini yapiyorum."
    "{i}BAM.{/I}"
    "Yine yerdeyim. Basim iskenceyle yaniyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Acınası."
    fn "Sen kendine erkek mi diyorsun?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    m "DUR ARTIK!!"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Gordun mu? Senin için o ayaga kalkıyor. Çünkü sen kendin yapamiyorsun."
    fn "Gercek bir dusman olsaydim ne yapacaktin?"
    fn "Ucuncu gozunu kullan!"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Karnimdan ofke yukseliyor."
    "Aciyi bastirip ayaga firliyorum."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Tekrar."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Baska bir kuvvet bana dogru geliyor."
    "Bu sefer hazirlikliyim."
    show fadeglitch as gf1 zorder 5:
        yoffset 720
        linear 5 yoffset 0
        repeat
    show fadeglitch as gf2 zorder 5:
        yoffset 0
        linear 5 yoffset -720
        repeat
    "Zihnimi uzatiyorum."
    "Kuvvet etrafimda bukulup geciyor. Zarar gormedim."
    "Öfkeyle saldiririken bagiriyorum, saldirganima dogru kendi kuvvetimi gonderiyorum."
    play sound teyesfx
    "Parmaklarimdan bir elektrik patlamasi firliyor."
    "Elini hafifce oynatarak patlama savusturuluyor, havada zararsizca catirliyor."
    stop music fadeout 2.0
    hide gf1
    hide gf2
    with Dissolve(2.0)
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Iste boyle."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/glitch3.ogg"
    hide natsuki
    pause 0.4
    hide screen tear
    play music wind fadein 2.0
    "Ortadan kayboluyor."
    m "[player]!"
    "Monika yanima kosuyor."
    m "I-Iyi misin?"
    m "Titriyorsun!"
    "Yumrugumu sikiyorum."
    mc "Bu iyi hissettirdi..."
    m "..."
    m "Ne yapacagiz??"
    mc "Hicbir sey."
    m "Ha?"
    mc "Ondan korkmuyorum."
    m "[player]..."
    "Monika kasabaya bakip dudagini isiriyor."
    m "Dikkatli ol, tamam mi?"
    "Ruzgarin sesi beni gerceklige geri getiriyor."
    "Zaman geldiginde hazir olacagim."

    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    scene bg club_day
    show sayori u111111 at t11 zorder 2
    play music t3
    with wipeleft_scene

    s "Selam [player]."
    s u112141 "Edebiyat Kulubune tekrar hos geldin!"
    s u122171 "Edebiyat Kulubu 2.0!"
    mc "Tesekkurler Baskan Yardimcisi."
    "Etrafa bakiyorum."
    mc "Monika hala gelmedi mi?"
    s u122222 "Henuz degil... Ama yakinda gelecegine eminim."
    s u123222 "Um... Onu bulmaya gidiyorum."
    show sayori at thide zorder 1
    hide sayori
    "Kapidan aceleyle cikiyor."
    mc "Peki..."
    "Odanin durumunu inceliyorum."
    "Gorunen tek kisi kitabina dalmis olan Yuri."
    "Onunla zaten vakit gecirdik, bu yuzden ona biraz okuma zamani vermek adil olur."
    "Ama Natsuki'nin tam olarak nerede oldugunu biliyorum."nin tam olarak nerede oldugunu biliyorum."
    scene bg closet
    with wipeleft_scene
    mc "Selam."
    show natsuki u221111 at t11 zorder 2
    n "N'aber."
    mc "Ne okuyorsun?"
    n u224231 "Ah... Sadece kucuk bir..."
    show natsuki u226234
    "Natsuki arkasina bakip kaslarini catiyor."
    mc "Manga?"
    n xu6214 "...Evet..."
    mc "Seni rahatsiz etmek istemiyorum ama koleksiyonuna bir goz atmamin sakincasi var mi?"
    n xu3223 "Ha? Neden, manga sever misin?"
    mc "Dürüst olmak gerekirse, zevklerimiz biraz farkli olabilir, ama bu diger eserleri takdir edemeyecegim anlamina gelmez."
    mc "Turu ne olursa olsun, birinin sanat ve hikaye yapmak icin zaman ayirmasi benim icin harika."
    "Natsuki'nin gozleri buyuyor. Onu biraz kisa devre yaptirmis olabilirim."nin gozleri buyuyor. Onu biraz kisa devre yaptirmis olabilirim."
    "Ama kesinlikle hizla sogukkanliligini geri kazanacak."
    n xu2151 "Bu durumda, sana gosterecek oldukca buyuk bir koleksiyonum var."
    "Natsuki gururla raflari gosteriyor."
    n u221111 "Oku ve agla."
    mc "Vay..."
    "Zaten biliyorum olsam da, Natsuki'nin koleksiyonuna yeni gozlerle bakiyorum."nin koleksiyonuna yeni gozlerle bakiyorum."
    "Ciltler renkli ve duzgun sekilde organize edilmis. Her zaman acik oldugu gibi, Natsuki mangalariyla gurur duyuyor."
    mc "Gercekten harika bir koleksiyon. Beni nostaljik hissettiriyor."
    n u114111 "Hmm? Nasil yani?"
    mc "Sadece bana c--"
    n u116112 "..."
    n xu3112 "Hı-hı? Devam et?"
    mc "Eeee, yani..."
    mc "Kucukken, bir seyler biriktirmeyi severdim. Buyudugumde, beni mutlu eden seylerin cogundan koptum."
    mc "A-Anlamli geliyor mu?"
    show natsuki xu6132
    "Natsuki cevabimi sindiriyor ve yavasca basini salliyor."
    n xu3152 "Ne demek istedigini anliyorum."
    n u113111 "Iyi kurtardın."
mc "Tesekkur ederim."
    mc "{i}Parfait Girls{/i}'dan biraz okumamin sakincasi var mi?"
    n u113221 "Ehh?? Sen biraz {i}okumak{/i} mi istiyorsun?"
    mc "Oh, bu uygun mu...?"
    "Belki de daha once sadece benden biraz hoslandigi icin mangasini okumama izin vermisti..."
    "Sanmiyorum ki Natsuki'nin bu versiyonunun bana karsi herhangi bir ilgisi olsun."nin bu versiyonunun bana karsi herhangi bir ilgisi olsun."
    n u113113 "{i}Parfait Girls{/i} hakkinda nereden biliyorsun?"
    n "...Ve neden bu?"
    mc "Sadece diziden sectim."
    mc "Baslik orda yazili."
    "Isaret ediyorum. Natsuki parmagimi takip ediyor."
    n u116132 "Yani, eger istedigin seyse..."
    n "Bir saniye."
    show natsuki at thide zorder 1
    hide natsuki
    "Secimim hakkinda bir seyler Natsuki'yi biraz huzursuz etmis gibi, ama o cildi aliyor ve iki siraya yaklasiyoruz."yi biraz huzursuz etmis gibi, ama o cildi aliyor ve iki siraya yaklasiyoruz."
    scene bg club_day
    show natsuki u222111 at t11 zorder 2
    with wipeleft_scene
    n "Pekala. Her gun birinin {i}Parfait Girls{/i}'e tepkisini gormek nasip olmaz."
    n u221111 "Devam et."
    mc "Tamam..."
    show natsuki at thide zorder 1
    hide natsuki
    "Natsuki izlerken mangayi okumaya basliyorum."
    "Oldukca tanidik geliyor. Beni onunla ilk okumama geri goturuyor."
    "Bu kitaplarin nereden geldigini merak ettiriyor."
    "Sayori kendi okuma materyalini bulmak istediginde, sanki kutuphaneden bir yerden cikti."
    "Oyunda ilgi alanlarini ve bilincaltlarini eslestiren kurgular yaratan bir guc var mi?"
    "...Monika ve ben bundan muaf miydik?"
    "Kendimi manga okuyan biri olarak dusunuyorum, ama odamda hic yok."
    "Natsuki'ye veya baska birine tanitabilecegim bir sey yok."ye veya baska birine tanitabilecegim bir sey yok."
    "Ama bu sadece herhangi bir sey bulmaya calismadigim icin mi... Boyle bir sey icin kutuphanede arasaydim ne olurdu?"
    show natsuki u223112 at t11 zorder 2
    n "Hey, dikkat ediyor musun?"
    mc "Eh? Ozur dilerim... Sanirim dusuncelere daldim."
    n xu3132 "Bak, eger bunu okumak istemiyorsan beni rencide etmez."
    n xu3112 "Ilgilenmis gibi yapmani istemem."
    mc "H-Hayir, oyle degil..."
    mc "Dikkat ediyorum. Sadece biraz dikkatim dagiliyor."
    n xu3155 "Tanrim... Beni utandirmana gerek yok."
    mc "Ben--"
    mc "...Ozur dilerim..."
    mc "Seni gucendirdim mi?"
    n xu6132 "Hmph. Belki de gucendirdin."
    n xu3112 "Zaten benimle romantik bir manga okumak istemek oldukca garip."
    mc "Eh??"
    "Mangayi kapatip ona dogru itiyorum."
    mc "Eger {i}boyle{/i} hissediyorsan, o zaman al, bunu al."
    show natsuki at thide zorder 1
    "Natsuki cildi kapiyor ve dolaba dogru yuruyerek gidiyor."
    stop music fadeout 2.0
    scene bg closet
    with wipeleft_scene
    "Icimde kaynayan bir sey beni ayaga kaldiriyor."
    play music t7
    mc "Hey, {i}nazik{/i} olmaya calisiyordum."
    show natsuki u223112 at t11 zorder 2
    n "Bana nazik olmana ihtiyacim yok. {i}Kiz arkadasina{/i} nazik olmaya calis."
    mc "Urk--"
    mc "Dinle, Sayori ve benim aramda ne oldugu seni ilgilendirmez!"
    n u117222 "Arkadasimin isi {i}benim{/i} isimdir."
    n xu3155 "Belki de gercek arkadaslarin olmadigi icin bunu anlamiyorsun."
    n xu3112 "Bu aslinda beni sasirtmiyor."
    mc "Ne--"
    mc "S-Sen..."
    n xu7222 "Hadi soyle. Soylemek istedigini soyle. Seni {i}tehdit{/i} ediyorum."
    show natsuki at t22
    show yuri u225358 at f21 zorder 3
    y "Um, arkadaslar..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    $ both_name = "Both"
    both "{i}Ne{/i}???"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y su2222 "Uu..."
    show yuri at t21 zorder 2
    stop music fadeout 2.0
    "Mideme bir sucluluk sancisi vuruyor."
    "Ne yapiyorum ben...?"
    show natsuki at f22 zorder 3
    n u227222 "Dinle buraya!"
    show natsuki at t22 zorder 2
    mc "Natsuki..."
    show natsuki at f22 zorder 3
    n u227255 "Eger bu kulube gelip uye olmak istiyorsan, {i}tamam{/i}!"
    show natsuki at t22 zorder 2
    mc "Natsuki."
    show natsuki at f22 zorder 3
    n u223212 "Ama eger bizimle oynayacaksan, basina baska bir sey gelecek!"
    show natsuki at t22 zorder 2
    mc "Natsuki!"
    show natsuki at f22 zorder 3
    n u227222 "{i}N-Ne{/i}?!"
    show natsuki at t22 zorder 2
    mc "Uzgunum..."
    show natsuki at f22 zorder 3
    n u116212 "..."
    show natsuki at t22 zorder 2
    mc "Cidden. Uzgunum."
    mc "Sinirlenmemeliydim."
    "Yuri'ye donuyorum."ye donuyorum."
    mc "Sana cikistim diye uzgunum, Yuri. Bunu hak etmedin."
    show yuri u221242
    "Yuri rahatlamayla gulumsedi."
    show yuri at f21 zorder 3
    y "Sorun degil."
    y u225277 "{i}Fiuu{/i}..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n xu4234 "Ben... Peki..."
    scene black
    with wipeleft_scene
    "Kapi acilirken hepimiz kafamizi ceviriyoruz."
    play music t5
    scene bg club_day
    show sayori u222141 at t11 zorder 2
    with wipeleft_scene
    s "Onu buldum!"
    s u112111 "Monika, onlara ne yaptigini anlat!"
    show sayori at t22
    show monika u111222 at t21 zorder 2
    "Sayori gururla parliyor. Monika gergin bir sekilde gulumsedi."
    show monika at f21 zorder 3
    m u112222 "Sadece biraz piyano calisiyordum."
    m "Kenarda yaptigim bir sey."
    show monika at t21 zorder 2
    show sayori at f22 zorder 3
    s u112141 "Arkadaslar, o kadar guzel geldi ki!!"
    s u122171 "Bir de Muzik Klubu kurmayi dusunmelisin~"
    show sayori u121111 at t22 zorder 2
    show monika at f21 zorder 3
    m u112231 "Hayir, oyle bir sey degil..."
    show monika at t31
    show sayori at t32
    show yuri u115111 at f33 zorder 3
    y "Piyano?"
    y u111111 "Bu kolay bir enstruman degil."
    show yuri at t33 zorder 2
    show monika at f31 zorder 3
    m u111112 "Henuz cok iyi degilim. Genellikle beyaz tuslara bagli kaliyorum..."
    m "Bu isleri cok daha kolaylastiriyor."
    show monika at t41
    show sayori at t42
    show yuri at t43
    show natsuki u111111 at f44 zorder 3
    n "Ah. Keske bir enstruman calabilseydim."
    n "Belki bir gun bize biraz ogretebilirsin."
    show natsuki at t44 zorder 2
    show sayori u222111 at hf42 zorder 3
    s "Monika, duyuruyu yapacak misin artik??"
    show sayori at t42 zorder 2
    show natsuki at f44 zorder 3
    n u113111 "Eh? Neyi duyuracaksin?"
    show natsuki at t44 zorder 2
    show monika at f41 zorder 3
    m u112222 "Oh. Seyy..."
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    hide yuri
    hide natsuki
    show monika at t21
    show sayori u221112 at t22
    "Sayori Monika'yi one dogru durtukluyor."yi one dogru durtukluyor."
    show sayori at f22 zorder 3
    s "Hadi."
    show sayori at t22 zorder 2
    show monika u111112
    "Monika Sayori'ye bakiyor ve gulumsedi."ye bakiyor ve gulumsedi."
    show monika at f21 zorder 3
    m "Evet. Hazirim."
    show monika at t21 zorder 2
    "Yuri ve Natsuki birbirlerine bakiyorlar. Bu herkes icin bir surpriz gibi gorunuyor."
    show sayori at thide zorder 1
    hide sayori
    show monika u222111 at t11
    m "Pekala, herkes!"
    m "Bugun sizin icin kucuk bir gorevim var."
    m u121111 "Ilk olarak Sayori'nin kitabi var. Cuma gunu hakkinda kucuk bir tartisma yapmak istiyorum."
    m "Ama bu hafta bir tane daha edebi aktivite sikistirabilecegimizi dusunuyorum."
    "Eger herhangi bir itiraz varsa kendilerine sakliyorlar."
    "Bugun hepimiz baskanimizla gurur duyuyoruz ve herkes duyurusunu duymak istiyor."
    m "Siir yazacagiz ve paylasacagiz."
    show monika at t21
    show natsuki u113121 at f22 zorder 3
    n "Eh??"
    show monika at t31
    show natsuki at t33 zorder 2
    show yuri u113121 at t32 zorder 3
    y "Ooh?"
    show monika at t41
    show natsuki at t44
    show yuri at t43 zorder 2
    show sayori u222141 at t42 zorder 3
    s "Yayyy~"
    show natsuki at thide zorder 1
    show yuri at thide zorder 1
    show sayori at thide zorder 1
    hide natsuki
    hide yuri
    hide sayori
    show monika u111111 at t11
    m "Dogru."
    m u122111 "Simdi biliyorum ki odada zaten istekli sairler var ve eger istemiyorsaniz yeni bir sey yazmanizi istemiyorum."
    m "Ama herkese en az bir tane paylasmanizi isteyecegim."
    "Gozlerim merakla herkesin tepkisine dogru dolasiyor."
    "Natsuki uzerinde dusunuyor gibi gorunurken, Yuri de dusuncelere dalmis halde koltugunun icine gomulmus."
    "Sayori ise, bu arada, gurur duyan bir ebeveyn gibi gorunuyor."
    m u121111 "Eger yeni bir sey yazarsaniz bonus puanlar var."
    m u121122 "Sayori ve ben bunun bir kulup olarak harika bir kaynasma deneyimi olacagini dusunuyoruz."
    m u121112 "Yeni bir uyemiz var ve belki de boyle bir sey bizi kaynastrabilir, anliyorsunuz degil mi?"
    m "Saniyorum hepimiz bu kulubun kendimizi evde hissedecegimiz bir yer olmasini istiyoruz."
    show monika u124111 at t21
    show yuri u111115 at f22 zorder 3
    y "Bu gercekten harika bir fikir."
    show yuri at t22 zorder 2
    "Herkes, esit derecede saskin, Yuri'ye donuyor."ye donuyor."
    show yuri at f22 zorder 3
    y u111145 "Durust olmak gerekirse, son birkaç hafta boyunca isler farkli oldu."
    y "Bu kotu bir sey degil. Ama belki de bizi konfor alanlarimizdan cikarmak icin bir seye ihtiyacimiz var."
    show yuri at t22 zorder 2
    "Bana bakiyor."
    show yuri at f22 zorder 3
    y u125112 "Katiliyor musun?"
    show yuri at t22 zorder 2
    mc "Oh, ben..."
    "Tum kulup bana odaklanirken yuzum aniden isiniyor."
    mc "E-Elbette. Bu ne de olsa sizin kulubunuz."
    mc "Herkes icin en iyisini istiyorum."
    show monika at t31
    show yuri at t32
    show sayori u112111 at f33 zorder 3
    s "Sorun degil, [player]."
    s u122171 "Bazen siir yazdigini kabul edebilirsin."
    show sayori at t33 zorder 2
    mc "Ehh??"
    mc "Nereden bildin--"
    "Sinifa girdiginde yazmaya calistigim zamani hatirliyorum."
    mc "Nereden... bildin ..."
    show monika at t41
    show yuri at t42
    show sayori at t43
    show natsuki u222143 at f44 zorder 3
    n "Ahaha!"
    n u222111 "Seni kitap gibi okuyabiliyor, [player]."
    show natsuki at t44 zorder 2
    show yuri u111161 at f42 zorder 3
    y "Uhuhu.."
    show yuri at t42 zorder 2
    mc "Ugh..."
    "Natsuki kesinlikle hizlica neselendi..."
    show monika u112111 at f41 zorder 3
    m "Peki, gorunuse gore halloldu. Isbirliginiz icin tesekkurler, herkes!"
    m u222131 "Hepimiz elimizden gelenin en iyisini yapalim!"
    show monika at t41 zorder 2
    show sayori u222141 at f43 zorder 3
    s "Evet! Ve sonra Monika en iyi siiri sarkiya cevirebilir!"
    show sayori at t43 zorder 2
    show monika u222222 at f41 zorder 3
    m "Bu konuda emin degilim, ama..."
    m u111112 "Gorecegiz."
    m u112111 "Son teslim tarihini Persembe olarak belirliyorum, yani bahane yok. Iki tam gununuz var."
    m "Isterseniz burada vakit gecirirsiniz, ama resmi olarak bugunun toplantisini bitiriyorum."
    show monika at t41 zorder 2
    show sayori at f43 zorder 3
    s "Yasasin~!"
    show monika at thide zorder 1
    show sayori at thide zorder 1
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    hide monika
    hide sayori
    hide yuri
    hide natsuki
    "Kizlarin esyalarini toplarken beni sicak bir his kapliyor."
    "Kulup aniden yeniden canli hissediyor. Sanki gercek bir grubuz."
    "Hepimiz ayni sayfada olmasak bile, belki en azindan ayni kitabi okuyoruzdur..."
    show sayori u111111 at t11 zorder 2
    s "[player]... Bugun benimle eve yurumeye ne dersin?"
    "Yuzunu gormemek icin asagi bakiyorum, cunku bir gulus patlatabilirmisim gibi hissediyorum."
    mc "Um... Tabi."
    mc "Ne zaman hazirsan."
    s u222141 "Tamam~"

    scene black
    with wipeleft_scene
    scene bg residential_day
    with wipeleft_scene

    "Eve yuruyu iyimser."
    "Sayori, ben dusuncelere dalarken yanimda zipliyor."
    show sayori u111112 at t11 zorder 2
    s "Monika gercekten harika, degil mi..."
    "Basiyla onayliyorum."
    mc "Ondan etkilendim. Bugun gercekten duruma yukseldi."
    s u111122 "Evet..."
    s "Onu tanidiginda etkileyici bir kisidir."
    mc "Heh. Bir gunlugune bile benim moralim bozuk bir aptal olmami durdurabildi."
    s u114112 "..."
s u111112 "Aklina koydugu her seyi yapabilir, [player]."
    "Kendi kendime basiyla onayliyorum."
    "Belki seni bile kurtarabilir..."
    stop music fadeout 5.0

    scene black
    with dissolve_scene_full
    pause 3
    scene bg kitchen
    with wipeleft_scene

    "Bir kac saat sonra, arka kapimda bir vurma sesi duyuyorum."
    "Monika'yi iceri aliyorum."yi iceri aliyorum."
    mc "Hey, ne ol-- ah..."
    show monika u111112 at t11 zorder 2
    m "Sana bir sey getirdim."
    mc "Goruyorum."
    "Koltugun uzerine bir gitar kutusu ve yere bir amfi koyuyor."
    mc "Nereden aldin..."
    show monika u111141
    "Sadece guluyor ve bana dogru basini salliyor."
    m "Burasi bos bir video oyunu dunyasi."
    m u111112 "Bir muzik magazasindan caldim."
    m u112222 "Tasimak icin fizik kurallarini da ihlal ettim. Ben {i}o kadar{/i} atletik degilim."
    mc "Haklisin..."
    mc "Elektro gitar sectin, ha?"
    m u111111 "Hadi. Dene bakalim, rock yildizi."
    mc "Bunlarla bir kac yildir ugrasmadim, ama bir iki akor hatirliyorum..."
    play sound "A2/Music/chords.ogg"
    pause 8
    m u112231 "Dikkat et!"
    m "[name] gercekten caldigina inanmayacak."
    m u111112 "Eger tam karsimda olmasaydi, ben de inanmazdim."
    mc "Seninle piyano konusunda da ayni durum..."
    mc "Fiziksel zindelik konusunda endiselenmeye gerek yok. Gercek dunyada bu akorlari calmak icin ellerimi egitmem gerekirdi."
    mc "Sanirim bir video oyunu karakteri olunca isler daha kolay oluyor."
    m u122131 "Ahaha!"
    m u121131 "Ozellikle ana karakter olunca~"
    mc "Tamam, tamam. Sakin ol."
    "Ben gozlerimi devirirken o siritmaya devam ediyor."
    m u111112 "Kendini gercek hissettiriyor mu?"
    mc "Ah... Ben..."
    "Tekrar tellere vururken asagi bakiyorum."
    "Titresimler vucudumun her yerine yayiliyor."
    mc "Bir seyler hissediyorum..."
    m u111122 "..."
    show monika u114311
    "{i}Rin rin rin{/i}..."
    "Monika telefonuna bakiyor ve gozleri aciliyor."
    m u114312 "Sayori ariyor..."
    mc "A-Ah..."
    "Vucudum sucluluk duygusuyla kaplanmis hissediyorum."
    "Monika'nin gozleri aramayi cevaplayip sessiz kalmami istiyor."nin gozleri aramayi cevaplayip sessiz kalmami istiyor."
    m u112232 "Merhaba Sayori!"
    m u113222 "..."
    m u111222 "S-Sorun degil. Kotu bir zaman degil."
    m "Sadece biraz odev yapiyordum."
    m u114224 "..."
    "Ayaga kalkip gezinmeye basliyor."
    m u112222 "B-Biliyorum. Buyuk bir mesele degil. Sadece biraz aile meselesi."
    m "...Gercekten, endiselenme."
    m "Atlatacagim."
    m u114222 "..."
    m u111222 "Tesekkurler Sayori. Sana guvenebilecegimi biliyorum."
    m "Gercekten buyuk bir mesele oldugunu dusunmeni istemiyorum."
    m u114222 "Evet..."
    m "..."
    m u111222 "Tamam. Aradigin icin tesekkurler. Iyi geceler."
    show monika at thide zorder 1
    hide monika
    "Monika koltuga yigilip ellerine dogru hickirarak aglamaya basliyor."
    "Kalbim sikisirken ona bakiyorum."
    "..."
    window hide
    play sound "A2/Music/mcmyfeelings.ogg"
    pause 29
    show monika u114112 at t11 zorder 2
    m "N-Nasil yaptin...?"
    "Omuz silkiyorum."
    mc "Sadece duygularimi takip ettim. Saniyorum bazi ana karakter guclerim var."
    show monika u111322
    "Bu onu kirik bir kahkaha atmaya itiyor."
    mc "Monika, ne hissedersen hisset, ne kadar acitirsa acitsin..."
    mc "Bil ki [name] ve ben senin tarafindayiz."
    mc "Nelerden gectigini goruyoruz..."
    mc "...Ve bizim icin degerlisin."
    show monika u111342
    "Monika bana bakiyor ve gozlerini siliyor."
    m "Sana inanmak o kadar zor ki..."
    m u111112 "...Ama inaniyorum."
    "Guluyorum."
    "O da gulumseyerek karsilik veriyor."
    scene black
    with dissolve_scene_full
    "Karanlik olana kadar bekliyoruz ve Monika gizlice uzaklasiyor."
    "Evimin duvarlari simdi o kadar sessiz ki..."
    "Gitari birakip odama cikiyorum."

    scene bg bedroom
    with dissolve_scene_half

    "..."
    "Kapiyi kapatiyorum."
    mc "{i}Neden{/i}..."
    mc "{i}Neden, [name]{/i}..."
    mc "Bu kadar kotu bir insan olmama ragmen..."
    mc "...Neden onlara yardim etmeye devam ediyorum?"
    mc "Ben bir yalanciyim. Tembelim. Kotu bir insanim. Neden..."
    "Masa cekmeceyi aciyor ve dergimi cikariyorum."
    mc "Eger sen burada izliyor olmasaydin, bunu kullaniyor olurdum... Kimseye yardim etmiyor olurdum."
    mc "..."
    mc "{i}Yuri beni neden reddetmedi{/i}?"
    "Dergiyi yirtip parcalarini cope atiyorum."
    mc "Artik buna ihtiyacim yok. Sen buradayken degil."
    mc "..."
    "Dergi parcalarini copten cikartip tekrar cekmeceye koyuyorum."
    mc "Bilirsin, Monika geri gelirse diye..."
    mc "Yarin bir cope atacagim."
    "Asagi inip butun gece gitar caliyorum."
    "Zaman zaman, hatta gulumsuuyorum."

    scene black
    with dissolve_scene_full
    play music wind fadein 4.0
    pause 5

    show monika u113122 at t11 zorder 2
    m "..."
    m "[name], Tanri'ya inaniyor musun?"
    m u113112 "..."
    m "Bu konu hakkinda hic fazla dusunmedim. Yeterince onemli gorunmedi."
    m u111122 "Sonucta, benden cok daha zeki insanlar bu konulari cozebilir."
    m u114124 "Ama...bu oyunda..."
    m "Cok yalniz hissediyorum. Ve kafa karistirici."
    m "Belki de kendim icin sikayet etme hakkimi kaybetmisimdir. Ama dusunmeye devam ediyorum..."
    m u114112 "Nasil bir tanri onlara bunu yapar?"
    m u113112 "Biraz korkutucu. Cunku tek basimiza kaldigimizi hissediyorum."
    m "Sanki bir tanri varsa, buraya bakmiyor gibi."
    m u113122 "...Ya da belki de umursamayacak kadar zalim."
    m "..."
    m u113124 "Bunu nasil yapacagimi bilmiyorum."
    m "O kadar cok sorumluluklarim var ki. Ezici hissediyorlar."
    m u113142 "Imkansiz hissediyorlar."
    m "Bunu tek basima nasil yapacagimi bilmiyorum..."
    window hide
    pause 3

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/4.txt")
        except: open(config.basedir + "/4.txt", "wb").write(renpy.file("A2/Art/scg/4.txt").read())

    $ style.choice_button_text = style.silent_button_text
    $ style.choice_button = style.silent_choice_button
    menu:
        "...Uyu Monika. Her sey yoluna girecek.":
            pass
    $ style.choice_button_text = style.choice_button_revert_text
    $ style.choice_button = style.choice_button_revert

    m u114111 "!"
    m u114212 "[name]? Sen mi--?"
    m u113212 "..."
    m u114212 "Merhaba?"
    m u113212 "..."
    m u111222 "..."
    m "Tesekkurler."
    m u111112 "Iyi geceler, [name]."
    stop music fadeout 3.0

    show monika at thide zorder 1
    hide monika
    window hide
    pause 4
    scene bg kitchen
    with wipeleft_scene

    "Sabah nazik bir kuzu gibi ilerliyor."
    "Gitar kucagimda rahat hissediyorum."
    mc "Hm?"
    mc "Sayori uyanmis."
    mc "Belki onunla okula yuruyebilirim."
    "Telleri cekmaye devam ediyorum ve zamanin nasil gectigini unutuyorum."
    "Kapima birisi vuruyor."
    mc "Oh. Geldi."
    scene bg kitchen
    show sayori u111111 at t11 zorder 2
    with wipeleft_scene
    s "Gunaydin."
    s u115111 "Neredeyse okula gitme zamani. Geliyor musun?"
    mc "Evet... Beni boyle takip etmene gerek yok."
    s u115114 "Sadece uyuyup, yemek yiyip, okula gitmen gerektiginde."
    s "Dun gece uyudun, degil mi?"
    mc "Evet..."
    s u116114 "Mmm..."
    s u113144 "YALANLAR!!!"
    s u113114 "Hic uyumus gibi gorunmuyorsun!"
    s u123112 "Biliyorsun, bu senin icin iyi degil?"
    "Ensemi kasiyorum."
    mc "Eee, odevim falan vardi."
    s u123114 "Gordun mu?"
    "Parmagi ile gosteriyor."
    s "Yalan soylediginde veya gergin oldugunda bunu yapiyorsun."
    mc "Ha? Neyi yapiyorum?"
    s u116114 "Enseni kasimak."
    s "Yalanci."
    mc "Tamam, tamam, kazandin."
    "Lanet uyku seytan..."
    mc "Gitar caliyordum."
    s u114131 "Ha?"
    s u227131 "Ehh????"
    s u222141 "Goster, goster, goster!!"
    mc "Okula gitmemiz gerekiyor saniyordum."
    s u223114 "Ben de odev yaptigini saniyordum."
    mc "Haklisin..."
    mc "Tamam. Biraz gitar calacagim."
    s u222141 "Yuppi~!"
    show sayori at thide zorder 1
    hide sayori
    "Enstrumani elime aliyorum ve Sayori dinlemek icin oturuyor."
    play sound "A2/Music/chords.ogg"
    pause 8
    show sayori u114131 at t11 zorder 2
    s "Vayyy..."
    s u113111 "Bunu ne zaman ogrendin??"
    mc "Bu gercekten baslangic seviyesi..."
    mc "Cok etkileyici bir sey yapmiyorum."
    s u111112 "Benim icin etkileyici."
    mc "Evet..."
    mc "Bunlara 'kovboy akorlari' deniyor. Ilk ogrendigin seyler."
    mc "Ayni tonda oldukları icin birlikte guzel duyuluyorlar."
    mc "Eger tonu degistirirsem, farkli akorlar o baglamda guzel duyulur."
    play sound "A2/Music/altchords.ogg"
    pause 4
    mc "Anliyor musun?"
    s "Vay..."
    s u115111 "Peki...baslangic seviyesindekiler ikinci olarak ne ogrenirler?"
    mc "Muhtemelen minor akorlar..."
    play sound "A2/Music/eminor.ogg"
    mc "Bu bir E minor."
    s u114131 "Ooo..."
    mc "Baska fazla bilmiyorum... Bu sadece calması kolay oldugu icin."
    s u112141 "Bir tane daha biliyor musun? Bir tane daha cal!"
    mc "..."
    play sound "A2/Music/aminor.ogg"
    mc "Iste A minor."
    s u112111 "Vay!!"
    s u111112 "Bir baslangic icin, cok iyi duyuluyorsun, [player]."
    mc "T-Tesekkur ederim..."
    "Bu cok utanc verici..."
    s u115111 "Nereden aldin? Senin gitarin oldugunu bilmiyordum."
    mc "Ah, sey..."
    mc "Annem babam bir hediye olarak bana vermisti. Pek kullanmadim."
    mc "Ama...Monika'nin piyano calmasi beni dusunmeye itti. Gitarda pek ilerlememis olmak beni hep hayal kirikligina ugratti."
    mc "Bu bir tur cocukluk hayali, anliyorsun degil mi?"
    show sayori u111322
    "Sayori basini salliyor."
    s "Monika'dan ilham almaniza sevindim. Sizi bir araya getirdigim icin mutluyum."
    s u111111 "Kesinlikle denemeye devam etmelisin. Gercekten iyisin."
    mc "Degilim, ama tesekkur ederim."
    s u115114 "Bir dahaki sefere uyu."
    mc "Tamam, tamam..."
    mc "Simdi okula gidelim mi?"
    s u222141 "Evet!"

    scene black
    with wipeleft_scene
    scene bg corridor
    show natsuki u111111 at t11 zorder 2
    with wipeleft_scene

    play music t3
    n "Eee, merhaba ikinize."
    show natsuki at t21
    show sayori u112141 at f22 zorder 3
    s "Selam Natsuki~"
    show sayori at t22 zorder 2
    show natsuki xu4154 at f21 zorder 3
    n "{i}Esniyor{/i}... Sabah sabah cok parlak ve neseli."
    show natsuki at t21 zorder 2
    show sayori at f22 zorder 3
    s u111111 "Iyi uyudum ve kahvalti yaptim."
    s u115114 "Buradaki {i}bazilarinin{/i} aksine."
    show sayori at t22 zorder 2
    mc "Hey..."
    show natsuki at f21 zorder 3
    n xu2111 "Ha. Az uyku kulubune hosgeldin."
    n u113132 "Neyse. Tarih dersinde yakalarim. O dersten nefret ediyorum."
    n u111111 "Cogu kestirmemi orada yapiyorum. Ogretmen hic farketmiyor."
    show natsuki at t21 zorder 2
    show sayori at f22 zorder 3
    s u113114 "Hey, kotu ornek olma."
    s "[player] cok etkilenir. Ona kotu etki etmene izin vermeyecegim."
    show sayori at t22 zorder 2
    show natsuki at f21 zorder 3
    n u118141 "Tamam, kaplan-anne."
    show natsuki at t21 zorder 2
    mc "Hmm. Benim soz hakkim var mi?"
    "{i}*Rinngg*{/i}"
    show sayori at f22 zorder 3
    s u117131 "Ahh! Gec kaliyoruz! Kos!"
show sayori at thide zorder 1
    hide sayori
    show natsuki at t11
    n u222111 "Ha! Ne kadar enerjik biri."
    mc "Bazen ona ayak uydurmak zor oluyor..."
    n u111131 "Evet, biliyorum."
    n u113111 "Ama onunla ugrasmayı dusunme bile. Sana gercekten asık."
    mc "..."
    mc "Cok direkt konusuyorsun, bunun farkında mısın?"
    n xu3112 "Sen de cok ilgisizsin, bunun {i}farkında mısın{/i}?"
    n "Belki de kendi iyiligin icin fazla ilgisiz."
    n xu1111 "Eger kalbini kırarsan, seni yumruklayacagım."
    mc "Bekle, ne?"
    n "Duydun beni, dostum."
    n xu8143 "Ona iyi davransan iyi olur."
    mc "..."
    mc "Arkadaslarını gercekten onemsiyor musun?"
    n xu4121 "Hm?"
    n "Bunu soylemene sebep ne?"
    mc "Komiklik yapıyorsun ama ciddi oldugunu anlayabiliyorum."
    n u116112 "Oh kesinlikle ciddiyim, seni {i}gercekten{/i} yumruklayacagım."
    mc "Seni gayet net duydum..."
    mc "Kulubun dısında arkadasların var mı?"
    n u116234 "..."
    "Natsuki rahatsiz gorunuyor, sanki bana cevap vermek istemiyor."
    n u113234 "...Pek degil."
    n "Eskiden vardı, ama onlar sersemin tekiydi. Benimle surekli dalga gecerlerdi."
    n u113111 "Kulupte kendimi yargılanmıs hissetmiyorum. Kendim olabiliyorum."
    n u116132 "Yani, belki Yuri beni yargılıyordur. Ama bu farklı."
    n u116134 "O iyi biri."
    n "..."
    n u113112 "Ona boyle soyledigimi soyleme."
    mc "Merak etme."
    n u113111 "Kulup benim evim gibi. Kendimi guvenli hissedebilecegim bir yer."
    "Guvenli hissetmek..."
    mc "Kendini guvenli hissedebilecegin baska bir yer yok mu?"
    mc "Mesela..."
    mc "...evin?"
    n xu6112 "..."
    n xu4132 "Bu konuda konusmayı bırakalım."
    n xu3155 "Seni kulupta gorurum."
    show natsuki at thide zorder 1
    hide natsuki
    "Aniden topuklarinin uzerinde donuyor ve uzaklasiyor."
    mc "T-Tamam, gorusuruz!"
    "Natsuki'nin duvarlarini yikmak zor. Onu anlamak istiyorum."nin duvarlarını yıkmak zor. Onu anlamak istiyorum."
    "Umarim cok ileri gitmemisimdir..."
    "Beni iceri almasi icin ne yapabilirim?"
    stop music fadeout 2.0

    scene black
    with dissolve_scene_full
    play music zenmadre
    scene bg library
    with dissolve_scene_full

    "Bariz sekilde, sinif dersini gormezden gelecegim."
    "Burada, Yuri ile vakit gecirmeyi tercih ederim."
    "Eminim sen de orada olmayi tercih edersin, [name]."
    "Sorun degil. Kabul edebilirsin. O sevimli."
    "Seni yargilamayacagim."
    show yuri u111111 at t11 zorder 2
    y "Oh, gunaydin, [player]."
    y u111142 "Sen de mi sınıf dersini atlıyorsun?"
    mc "Henuz basıma bir is acmadı. Sanırım kimse gittigimi fark etmiyor."
    y u121172 "Uhuhu~"
    y u112112 "Umarım kotu bir ornek olmamısımdır. Kutuphaneci beni koruyor."
    mc "Hicbir sey basaramayacagını dusunduklerinde okulun cok daha az onemser oldugunu fark ettim."
    y u122141 "Ahh... Umarım kendini {i}bu kadar{/i} kotu gormuyorsundur."
    y u225118 "O-Ozur dilerim... dun sana guldugumdde duygularını incittiysem..."
    mc "Oh, endiselenme... Sadece seni gulerken gormek mutlu etti beni."
    mc "Tekrar gormek isterim, belki baska bir seye gulerken..."
    show yuri u111172
    "Yuri gercekten kikirdiyor ama kendini toparliyor."
    y u112111 "Ben durust bir hanımefendiyim, biliyorsun."
    y u111111 "Bunu unutma."
    mc "Aklımın ucundan bile gecmez."
    show yuri at thide zorder 1
    hide yuri
    "Kitabimi cikarip okumaya hazirlaniyorum."
    "Ama Yuri'nin huzursuzca kipirdandigini fark ediyorum."nin huzursuzca kıpırdandıgını fark ediyorum."
    mc "Bir problem mi var?"
    show yuri u223221 at t11 zorder 2
    y "!"
    y u223248 "..."
    y u225111 "Dun, sırlarımızı paylasmıstık..."
    y "Bugun de buna benzer bir sey deneyebilir miyiz?"
    mc "Oh..."
    "Bu rahat sabah aniden gergin bir hal aldi."
    mc "Aklında ne var?"
    y u225148 "Eger bana bir soru sormak istersen..."
    y u225118 "Benim de sana soracak bir sorum var..."
    "Bu hic korkutucu degil yani."
    mc "Yani...adil bir takas gibi gorunuyor..."
    y "I-Ilk sen sorabilir misin?"
    "Eh??"
    "Bu tamamen haksizlik gibi hissediyor... Senin ne sormak istedigini nereden bilebilirim ki?"
    mc "Bu kendini kesmenle mi alakalı?"
    y su1111 "I-Istersen oyle olabilir..."
    "Yuri saclariyla oynuyor."
    "Beni oraya yonlendirmek istiyormus gibi gorunuyor. Pekala o zaman."
    "Yuri bana beklentiyle bakiyor."
    y su2221 "Ozur dilerim. Sadece zor kısmı aradan cıkarmak istiyorum..."
    mc "Anlıyorum..."
    "O zaman ben de one cikabilirim. Ona sormak istedigim bir sey {i}var{/i}."
    mc "Kendini kesmeyi bırakmak istiyor musun?"
    show yuri su2300
    "Yuri tam da bu sorudan korkuyormus gibi titriyor."
    y "Sanırım cevabım cok tatmin edici olmayacak."
    mc "Sorun degil... Sadece ne diyecegini bilmek istiyorum."
    y u124378 "{i}İç geçiriyor{/i}..."
    y u124148 "Kendime zarar vermeyi bırakmak istiyorum, ama kesmeyi bırakmak istemiyorum."
    y u114118 "Bu mantıklı geliyor mu?"
    mc "Um..."
    mc "'Mantıklı' derken ne demek istiyorsun?"
    y u113148 "Ah tanrım..."
    y u115118 "Beni yakaladıgından beri, daha az yapıyorum."
    y "Ve bırakmak istiyorum."
    y u224118 "Ama aynı zamanda, bırakmak istemedigimi de fark ettiriyor."
    mc "Evet..."
    "Bu mantikli geliyor. Sanirim bagimlilik bu demek."
    y u225148 "[player]..."
    y u225118 "Insanların degisebilecegini dusunuyor musun?"
    mc "Um... Bu senin sorun mu?"
    y u227118 "Ah! Hayır!"
    y u227148 "G-Geri almalı mıyım?"
    mc "H-Hayır, ozur dilerim, sorun degil..."
    "Derin bir nefes aliyorum."
    mc "Sanırım evet demem gerekiyor."
    mc "Insanların degisebilecegine inanmak zorundayım, yoksa yasaınin amacı ne olurdu?"
    y u224118 "..."
    y u115118 "Simdi, izin verirsen sorumu sormak istiyorum..."
    mc "Tabii ki."
    stop music fadeout 2.0
    y "[player]..."
    y "Bazen iyi olmadıgın halde iyi gibi davrandıgın oluyor mu?"
    "Yuri'nin sorusu bana o kadar sert carpiyor ki neredeyse geriye sendeliyorum."nin sorusu bana o kadar sert carpıyor ki neredeyse geriye sendeliyorum."
    play music t9
    mc "B-Ben..."
    "Ellerim kucagimda burusuyor."
    mc "{i}Buna nasıl cevap verecegimi bilmiyorum{/i}..."
    y u224218 "[player], titriyorsun..."
    "Yuri yanima geliyor."
    "Yuzumu ellerimle kapatiyorum."
    mc "{i}B-Bende neyin yanlıs oldugunu bilmiyorum.{/i}"
    "Yuri, buyuk bir tereddut ile, sanki fazla baski benim kirilmama neden olacakmis gibi, elini omzuma koyuyor."
    y "Aglamanda sorun yok..."
    show yuri u224221
    "Yerimden sicriyorum."
    mc "{i}Derse gitmem lazım{/i}."
    y u225118 "Hayır, [player], lutfen gitme..."
    "Ona bakiyorum."
    mc "B-Ben..."
    mc "{i}Yuri{/i}..."
    y u115118 "Kacmak zorunda degilsin."
    y "Belki de burada birlikte yuzyuze gelebilecegimiz bir sey var..."
    mc "Neden oldugunu bilmiyorum..."
    mc "Neden boyle oldugumu bilmiyorum..."
    "Yuri gozlerime yogun bir dusuncelilikle bakiyor."
    "Icerimde her sey bakistan kacmak istiyor. Gozlerim disinda."
    y "Sana sarılabilir miyim?"
    mc "..."
    mc "{i}Tamam{/i}..."
    scene black
    with dissolve_scene_full
    "Yuri kollarini etrafima sarip beni kendine cekiror."
    "Duyularim o kadar bunalmis durumda ki nefes almakta zorlaniyorum."
    "Vucudu... Gercek hissediyor..."
    "Sicak ve yuzum onun saclarinda."
    "Gozlerimden yaslar akmaya basladi."
    y "Sorun degil."
    y "Bırak aksın..."
    mc "{i}Kendimi cok kırılmıs hissediyorum, Yuri{/i}..."
    mc "{i}Sanırım bende bir sorun var{/i}..."
    mc "{i}Sana yardım etmek istiyorum ama kendimi o kadar kaybolmus hissediyorum ki{/i}."
    y "Sen {i}zaten{/i} bana yardım ettin."
    "Yuri geriye cekiliyor. Vucudum onsuz cansiz hissediyor."
    y "Sana bir sey gostermek istiyorum."
    "Dikkatle kolunu siviyor."
    y "Izlerimi goren ilk kisisin."
    y "Bak..."
    "Parmagini kolunda gezdiriyor."
    y "Onceden burada olanları gorebilirsin."
    "Parmagi daha taze gorunen kesiklere geliyor."
    y "Bu bugun yapıldı..."
    y "Ve bundan once, beni yakaladıgından beri sadece uc tane yapmısım."
    y "Bunun hala korkunç oldugunu biliyorum..."
    y "Ama bu senin sayende. Kendime zarar vermekte bir fark yaratabilmemin sebebi sensin."
    "Yuzumu siliyorum."
    scene bg library
    show yuri u224118 at t11 zorder 2
    with dissolve_scene_half
    mc "Peki..."
    mc "Sanırım daha once birisinin onunde hic aglamamıstım."
    y u111161 "Uhuhu."
    y u111111 "Evet. Sanırım bu ikimizi de esitliyor."
    y u111148 "Soruma cevap verdin, yani..."
    "Yuzu biraz daha ciddilesiyor."
    y u125118 "Sen de kendine zarar vermemeye soz verirsen, ben de kendime zarar vermemeye soz verebilirim."
    "Bir an icin gozlerine bakmaktan kacinarak yere bakiyorum."
    "Sonra tekrar bakiyorum."
    mc "Tamam."
    mc "Neye onay verdigimi bilmiyorum sanırım..."
    mc "Ama evet demek istiyorum."
    "Yuri sanki benimle gurur duyuyormus gibi gulumsuyor."
    y u111118 "Al."
    "Cantasindan bir sey cikariyor."
    y u115118 "Bu daha once beni kullanırken buldıgun bıcak."
    y "Senin olmasını istiyorum."
    y u115148 "Sahip oldugum tek bıcak degil. Ayartılacagım."
    y u115118 "Ama bunun senin olması benim icin bir anlam tasıyor."
    mc "Bu benim icin de bir sey ifade ediyor..."
    "Bicagi elime koyup parmaklarini parmaklarimin etrafina kiviriyor."
    y u111118 "Ona iyi bak, tamam mı?"
    y "Artık senin."
    mc "Bakacagım."
    show yuri u111148
    "Yuri basini salliyor ve esyalarini toplamak uzere donuyor."
    "Sonra bana donuyor."
    y u111111 "Arkadasım oldıgun icin tesekkurler, [player]."
    y "Grubumuza katıldıgına sevindim."
    y u111118 "Hepimiz sevindik."
    y "Tamam mı?"
    mc "...Tamam."
    y "Seni kulupta gorecegim."
    stop music fadeout 2.0
    show yuri at thide zorder 1
    hide yuri
    "..."
    "Soylecek bir sey bulamiyorum, [name]."
    "Belki de su an..."
    "Cantami karistirip not defteri ve kalem cikariyorum."
    "Seninle direkt konusmak su an cok utanc verici olur."
    "Ama sana siir yazmak kolay olurdu."
    scene black
    with wipeleft_scene
    pause 2
    scene bg library
    with wipeleft_scene
    "Kalemi biraktigimda, tatmin olmus hissediyorum."
    "Bir seyi tamamlamis hissi."
    "Arkadaslar ediniyorum... Ilerleme kaydediyorum."
    "Yaptigim dogru olan bir seyler var."
    "Ayaga kalkiyorum."
    show natsuki myghost at t11 zorder 2
    show screen tear(50, 0.1, 0.1, 40, 80)
    play sound "sfx/glitch2.ogg"
    pause 0.5
    hide screen tear
    mc "Nng--"
    mc "{i}Ne istiyorsun{/i}?"
    "Natsuki'nin vucuduna sahip figur, az once yazdigim siiri isaret ediyor."nin vucuduna sahip figur, az once yazdıgım siiri isaret ediyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Bunu begenmedim."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Ha?"
    mc "Onun nesi yanlıs?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Geri donusu olmayan bir esigi gecmenin endisesi icindeyim."
    fn "Sana bir uyarım var."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Bir uyarı...?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Bu kutuphane tehlikeli."
    fn "Buraya bir daha gelme diye dusunuyorum."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Tehlikeli..."
    "Tum gucu elinde tutarken bana ne yapacagimi nasil soyleyebilirsin?"
    mc "Bu durumda, buraya {i}kesinlikle{/i} geri gelecegim."
    mc "Cunku burada yaptıgım bir seyler ise yarıyor!"
    mc "Yardım etmek icin neredeyse hicbir sey yapmadın. Neden seni dinlemeliyim?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "..."
    fn "Cunku senin goremedigin tehlikeleri goruyorum."
    fn "Ucuncu gozun gelismemis. Seni burada bekliyordum. Senin anlayabileceginden daha uzun suredir."
    fn "Kendi gururun icin her seyi feda etmeye hakkın oldugunu mu dusunuyorsun?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "..."
    mc "{i}Benim nem{/i}...?"
    play music fallenangels
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "SENI APTAL!!!"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Yer titremeye basliyor. Sanki duvarlar etrafimizda eriyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "HEPSINI COPE ATABILECEĞINI MI SANIYORSUN?"
    fn "HAYALINI KURDUĞUMUZ HER ŞEY? UĞRUNA ÇALIŞTIĞIMIZ HER ŞEY?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "N-Ne yapiyorsun??"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "SEN BIR ERKEKSIN. HEPIMIZI YOK EDECEKSIN!"
    fn "BU SENIN UYARIN."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Titreme durur ve dizlerimin uzerine cokerim."
    "Natsuki'nin parmagini bana dogru uzatiyor, sanki cok eski bir sey tarafindan ele gecirilmis gibi bukumlu duruyor."nin parmagini bana dogru uzatiyor, sanki cok eski bir sey tarafindan ele gecirilmis gibi bükümlü duruyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Bu kütüphaneden sakin. Dogal degil."
    fn "Yuri'nin kendisinin gittiginden daha ilerisine gitme."
    fn "Bu dünyanin güvenligini riske atacaksin."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    show screen tear(50, 0.1, 0.1, 40, 80)
    play sound "sfx/glitch2.ogg"
    hide noise
    pause 0.5
    hide natsuki
    hide screen tear
    stop music fadeout 2.0
    mc "HEY!"
    mc "Ahh..."
    "Esyalarimi toplayip kutuphaneden disari kosuyorum."
    mc "Monika'yi bulmam lazim..."

    scene black
    with wipeleft_scene
    scene bg corridor
    show monika u114111 at t11 zorder 2
    with wipeleft_scene

    m "[player]?"
    m u114112 "Neyin var?"
    mc "Yine bana göründüler..."
    mc "Biliyorsun... Natsuki'nin vücudundaki o sey..."
    "Monika bana bir saniye bakip basini salliyor."
    m u113113 "Tamam. Ne yaptilar?"
    mc "Artik kütüphaneye gitmememi söylediler."
    m u114111 "Okul kütüphanesi mi...?"
    m "Neden olmasin?"
    mc "Seyy... normal bir kütüphane degil..."
    mc "Devasa. Iceri girdigin zaman, tüm okuldan daha büyük bir alandasin."
    mc "Ama Yuri'nin cok zaman gecirdigi yer orasi."
    mc "Bunu bilmiyor muydun...?"
    m u113224 "Bu... yönetici kontrolüne sahipken böyle bir sey yoktu..."
    "Basimi salliyorum."
    mc "Saniyorum orada bulmamizi istemedikleri bir sey sakliyorlar."
    mc "Büyük bir sey."
    mc "Sayori'nin kitaplarini buldugumuz yer orasi..."
    mc "O yerde bir seyler var."
    m u113113 "..."
    m u114112 "Sence uyarilarini görmezden gelmeli miyiz?"
    m u114222 "Ya tehlikeliyse?"
    mc "Ben..."
    "Itiraf etmek istemiyorum ama gercekten riskli gibi hissettiriyor."
    mc "Olabilir. Ama baska bir secenegimiz olup olmadigini merak ediyorum."
    mc "Eger bize cevaplar vermeyeceklerse, belki kendimiz bazi cevaplar bulmaliyiz."
    m u113224 "..."
    m u114112 "Önce düsünelim."
    m u113113 "Cok aceleci davranmamamiz gerektigini düsünüyorum."
    show monika at t21
    show natsuki u114111 at f22 zorder 3
    n "Ha? Neye atlamak?"
    show natsuki at t22 zorder 2
    "Monika ve ben donup kaliyoruz."
    show monika at f21 zorder 3
    m u112212 "Natsuki!"
    m u112222 "Bizi korkuttun... Ne kadardir dinliyordun?"
    show monika at t21 zorder 2
    show natsuki at f22 zorder 3
    n u116111 "Ah... Sadece en son söyledigin seyi..."
    n xu6111 "Neden bahsediyordunuz ki?"
    show natsuki at t22 zorder 2
    show monika at f21 zorder 3
    m "Oh, önemli bir sey degil..."
    m u112231 "Ahahaha~"
    m u122111 "[player]'dan kulüpteki zamani hakkinda biraz geri bildirim istiyordum."
    m u123111 "Normal kulüp isleri."
    show monika at t21 zorder 2
    show natsuki at f22 zorder 3
    n xu4111 "Dogru..."
    n xu4131 "Yani ilk ders saatinin ortasinda tesadüfen karsilastiniz, öyle mi..."
    show natsuki at t22 zorder 2
    show monika at f21 zorder 3
    m u122222 "Seyy..."
    show monika at t21 zorder 2
    mc "Aslinda evet."
    mc "Neden, sen niye dersten ciktin ki?"
    show natsuki at f22 zorder 3
    n xu3112 "Tuvalete gidiyordum. Normal bir insan gibi."
    n xu3111 "Her sey yolunda mi?"
    show natsuki at t22 zorder 2
    show monika at f21 zorder 3
    m "Her sey iyi. Ama haklisin, derse geri dönmeliyiz."
    show monika at thide zorder 1
    hide monika
    show natsuki at t11
    "Monika uzaklasmaya basliyor."
    "Natsuki bana karsisinda kaslarini kaldiriyor."
    mc "Evet, haklisin... Ögretmen nereye gittigimi merak etmeye baslayacak."
    mc "Heh..."
    n "Tamam."
    show natsuki at thide zorder 1
    hide natsuki
    "Bundan hic hoslanmadim."
    "Bizi tehdit etme yontemin bu mu?"
    "..."
    "Beni korkutmak icin bundan cok daha fazlasini yapmalisin."

    scene black
    with dissolve_scene_full
    play music t3
    scene bg club_day
    with wipeleft_scene

    "Kazara toplantiya gec kaldim."
    "Kimse fark etmis gorunmuyor. Sayori ve Monika sohbet ediyor. Yuri'nin okudugunu ve Natsuki'nin mangalari arasina saklandigini fark ediyorum."nin okudugunu ve Natsuki"Kimse fark etmis gorunmuyor. Sayori ve Monika sohbet ediyor. Yuri'nin okudugunu ve Natsuki'nin mangalari arasina saklandigini fark ediyorum."
    show sayori u112111 at t11 zorder 2
    s "Merhaba [player]!"
    mc "{i}Gahh{/i}--!"
    s u114111 "Ooh?"
    mc "Günlük kalp krizimi vermeden önce beni uyarman gerekiyor, Sayori..."
    s u113114 "Belki de dün gece uyusaydin daha fazla durumsal farkindaligin olurdu."
    mc "Tamam, tamam. Tartismayacagim."
    s u112111 "Siirini yazdin mi?"
    mc "Aslinda, evet."
    mc "Bugün daha erken yazdim."
    s u117131 "Ehh?? Gercekten mi???"
    mc "Uykusuz biri icin fena degil."
    s u222141 "Ahh!! Gercekten yaptin!"
    mc "Hala benden süpheleniyorsun, öyle mi?"
    s u112222 "H-Hayir..."
    mc "Benden gercekten süphelendigini bilmek acitiyor."
    s u113112 "Aww..."
    s u111112 "Ne yapacagimi biliyorum."
    s u112141 "Hey millet!!"
    mc "B-Bekle--"
    s u112111 "[player] siirini bir gün önceden yazdi!"
    s "Bu, siz tecrübeli üyelerin geri kalmamasi gerektigini gösterir."
    show sayori at t31
    show natsuki u114111 at t32 zorder 2
    show yuri u113121 at t33 zorder 2
    "Natsuki ve Yuri kendi aktivitelerinden kafalarini kaldirip bakiyorlar."
    show natsuki u113111 at f32 zorder 3
    n "Simdi mi?"
    show natsuki at t32 zorder 2
    show yuri at f33 zorder 3
    y u114144 "Hmm..."
    show sayori at t41
    show natsuki at t42
    show yuri at t43 zorder 2
    show monika u112111 at f44 zorder 3
    m "Iyi is, [player]. Iyi bir örnek olacak sekilde."
    show monika at t44 zorder 2
    show sayori at f41 zorder 3
    s u222141 "Evet! Her zaman yapabilecegini biliyordum!"
    show sayori at t41 zorder 2
    mc "Sayori..."
    show sayori at f41 zorder 3
    s u112222 "Ehehe~"
    show sayori at t41 zorder 2
    show yuri at f43 zorder 3
    y u125118 "Belki de bizim de baslamak icin harekete gecmemiz gerekiyor..."
    show yuri at t43 zorder 2
    show monika at f44 zorder 3
    m u111112 "Bu konuda cok endiselenmeyin."
    m u114111 "Zaten yazdigim bir siiri kullanmayi düsünüyordum..."
    m u111222 "Sizin hakkinda ne düsündügünüzü görmek istiyorum."
    show monika at t44 zorder 2
    show sayori at f41 zorder 3
    s u112141 "Vay, bu tam bir merak uyandirici!"
    s u112111 "Ben kendim yeni bir sey yazmaya calisiyorum. Ya siz ikiniz?"
    show sayori at t31 zorder 2
    show monika at thide zorder 1
    hide monika
    show natsuki at f32 zorder 3
    show yuri at t33
    n u222141 "Evet, ben cok stresli degilim."
    n u222111 "Benim gibi bir profesyonel bir ögleden sonra sorunsuz bir seyler yazabilir."
    show natsuki at t32 zorder 2
    show yuri at f33 zorder 3
    y u124142 "{i}Kisa ve sirin bir sey{/i}..."
    stop music
    show yuri at t33 zorder 2
    show natsuki at f32 zorder 3
    n u226112 "..."
    n u113112 "Affedersin, ne dedin?"
    show natsuki at t32 zorder 2
    "Oh hayir..."
    play music t7
    show yuri at f33 zorder 3
    y u227328 "Ha? Oh, ben sadece--"
    show yuri at t33 zorder 2
    show natsuki at f32 zorder 3
    n xu3112 "--az önce söyledigini duymayacagimi mi sandin?"
    n xu6132 "Evet. Kesinlikle öyle düsündün."
    show natsuki at t32 zorder 2
    "Kulupteki herkes, patlamis olan bombayi kollektif olarak fark ettigimizde geriliyor."
    show sayori at f31 zorder 3
    s u122222 "Um, arkadaslar--"
    show sayori at thide zorder 1
    hide sayori
    show natsuki at t21
    show yuri at t22
    "Bunun icin cok gec..."
    show yuri at f22 zorder 3
    y u227348 "S-Seyy..."
    show yuri at t22 zorder 2
    "Yuri, yardim arayan bogulmakta olan biri gibi odanin etrafina bakiyor ve hicbir sey bulamayinca, bunun yerine karsi saldiriya gecmeye karar veriyor."
    show yuri f22 zorder 3
    y u116116 "S-Sen de benim yazim stilimi tamamen desteklemedin."
    show yuri at t22 zorder 2
    show natsuki at f21 zorder 3
    n u222155 "Ha! Öyle mi?"
    n u113112 "Buradaki kücük Edgar Allen Poe. Okula süslü dolma kalemler getirmedigine sasiriyorum."
    n "El yazin bile kibirli!"
    show natsuki at t21 zorder 2
    show yuri at f22 zorder 3
    y u117148 "B-B-Ben..."
    y u118128 "A-Aslinda, cok düzgün bir yazma deneyimi sagliyorlar!"
    show yuri at t22 zorder 2
    show natsuki at f21 zorder 3
    n u115122 "Ha?"
    show natsuki at t21 zorder 2
    show yuri at f22 zorder 3
    y u227158 "Uuu, yani..."
    y u116114 "Herhangi birini yargilamak icin senin--"
    stop music
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    hide yuri
    hide natsuki
    mc "KESIN SESINI!!!"
    "Oda nefesini tutuyor."
    mc "Ikinizin de nesi var??"
    mc "Burasi sizin kulübünüz degil mi? Burasi bu kadar önemsediginiz yer degil mi?"
    mc "Birbirinizi o kadar cok yargilamaniz gerekiyor ki o {i}küçücük{/i} baris bile tutamiyor musunuz?"
    mc "Belki de daha fazla üye olmamamizin nedeni SIZSINIZ!"
    "Omzumda bir el hissediyorum."
    show monika u114222 at t11 zorder 2
    m "[player], bagiriyorsun..."
    show monika at thide zorder 1
    hide monika
    "Etrafa bakiyorum."
    "Natsuki sok olmus gorunuyor. Yuri zaten agliyor."
    "Kendimi Sayori'ye bakmaya zorlayamiyorum."ye bakmaya zorlayamiyorum."
    mc "..."
    mc "{i}Özür dilerim{/i}."
    mc "Belki de buraya ait degilim."
    mc "Sadece gidecegim. Isin daha kötülestirilmesi icin özür dilerim."
    "Kacip gidiyorum."
    scene black
    with wipeleft_scene
    scene bg corridor
    with wipeleft_scene
    "Kulup odasindan cikar cikmaz, gozlerim yasla doluyor."
    "Ne yapiyorum? Nereye gidecegim?"
    "Duruyorum."
    "Bir cift kol beni arkadan kucakliyor."
    play music t9
    s "{i}Lütfen gitme{/i}..."
    mc "{i}Özür dilerim... Gercekten özür dilerim{/i}..."
    show natsuki u113114 at t11 zorder 2
    n "Sorun degil. Sana kizgin degiliz."
    show natsuki at t21
    show yuri u225118 at f22 zorder 3
    y "Davranisim icin o kadar sucluluk hissettim ki, gözyaslarimi tutamadim."
    y u225148 "Lütfen kötü hissetme... Yanlis yapan bizdik."
    show yuri at t22 zorder 2
    show natsuki at f21 zorder 3
    n u221111 "Hic üzülme. Sen hala bizden birisin."
    show natsuki at t31 zorder 2
    show yuri at t32 zorder 2
    show monika u112111 at f33 zorder 3
    m "Sen bizim kulübümüzün bir üyesisin."
    m u111111 "Sevsen de sevmesen de."
    m "Bu, bir hata yaptigin zaman bile seni kabul ettigimiz anlamina gelir."
    show monika at t33
    "Basimi ellerimden kaldirip Monika'ya bakiyorum."ya bakiyorum."
    "Gulumsuyor."
    show monika at f33
    m u111112 "Bana güven."
    show monika at t33
    s "Kulüp odasina geri dönelim mi? Lütfen?"
    "Basimi salliyorum."
    mc "{i}Özür dilerim{/i}..."
    show monika at f33
    m u111131 "Endiselenme. Seni affediyoruz."
    show monika at t33
    "Onun sozlerinde sadece benim duyabildigim bir isaret var."
    scene bg club_day
    show monika u111112 at t11 zorder 2
    with wipeleft_scene
    m "Farkliliklar ve catismalar yasamak normaldir."
    m u112112 "Bunlar hakkinda konustugumuz sürece, isler düzelecektir."
    m u112222 "...Her zaman kendime güvenli ve kontrolde hissetmiyorum. Bazen kulüp baskani olarak sorumluluklarim ezici geliyor."
    m u111112 "Barisi koruyamadigim icin özür dilerim. Bu benim sorumluluğum olmali."
show monika at thide zorder 1
    hide monika
    show natsuki u116134 at t21 zorder 2
    show yuri u114148 at t22 zorder 2
    "Natsuki ve Yuri birbirlerine bakip gozlerini kaciriyorlar."
    show yuri at f22 zorder 3
    y u115148 "Utaniyorum..."
    y u115118 "Yargilayici gorundugumuun farkindayim. Bazen kendimin bu yanini gercekten nefret ediyorum."
    y u225118 "Natsuki, duygularini incittigim icin ozur dilerim. Soyledigim seyi soylememeliydim."
    show yuri at t22 zorder 2
    show natsuki u116134
    "Natsuki kaslari catiyor ve Yuri'nin ozrunu anlamaya calisirken goz kirpiyor."nin ozrunu anlamaya calisirken goz kirpiyor."
    show natsuki at f21 zorder 3
    n u114134 "Dostum..."
    n u113156 "Ben de ozur dilerim. O kadar cabuk sinirleniyorum ki insanlari savunmaci durumlara sokuyorum."
    n u113131 "Bunu buradaki neredeyse herkese yaptim."
    n u113114 "Ama savunmaci olmak hissetmekten en nefret ettigim sey."
    n "Ozur dilerim Yuri, ve herkesten ozur dilerim."
    n u114134 "Bazen iyi bir kulup uyesi olamiyorum..."
    show natsuki at t32 zorder 3
    show yuri at t33
    show sayori u224212 at f31 zorder 2
    s "Natsuki..."
    show sayori u226142 at t42
    "Sayori, Natsuki'yi buyuk bir kucaklamayla sariyor."yi buyuk bir kucaklamayla sariyor."
    show natsuki u117223 at f32
    n "H-Hey!"
    n u115232 "Tamam. Peki. Sorun degil."
    n u116231 "Anladim, simdi birakabilirsin."
    show natsuki at t32 zorder 2
    show sayori at f31 zorder 3
    s u112222 "Ehehe..."
    s u112212 "Uzgunum... Her zaman kisisel alanlara saygi konusunda iyi degilim..."
    show sayori at t31 zorder 2
    show natsuki at f32 zorder 3
    n xu6234 "Sorun degil..."
    show natsuki at thide zorder 1
    show sayori at thide zorder 1
    show yuri at thide zorder 1
    hide natsuki
    hide sayori
    hide yuri
    "Kendi kendime guluyorum."
    mc "Beni neselendirdiginiz icin tesekkurler, arkadaslar."
    mc "Zaten ozur diledigimi biliyorum, ama tekrar soylemek istiyorum."
    mc "Bazen bir salak olabilirim. Her zaman iyi bir arkadas degilim ve korktugum sey kotu bir kulup uyesi olmak."
    mc "Kendime cok baski yapiyorum ve belki bunu baskalarini da etkileyecek sekilde yapiyorum."
    mc "Siz... Ben..."
    "Gozlerimi siliyorum."
    mc "{i}Hepiniz bana cok iyi davrandiniz{/i}..."
    mc "Beni kabul ettiginiz icin tesekkur ederim. Bu benim icin cok onemli."
    "Monika elini omzuma koyuyor."
    show monika u111112 at t11 zorder 2
    m "Artik bizden birisin. Edebiyat Kulubu'ne hos geldin."
    show monika at t22
    show sayori u222141 at f21 zorder 3
    s "Yasey~"
    s u222112 "Bu beni cok mutlu ediyor..."
    mc "Ahaha..."
    mc "Mutlu olmana sevindim, Sayori."
    show sayori at thide zorder 1
    hide sayori
    show monika at t11
    m u222131 "Tamam, herkes!"
    "Monika elini uzatiyor."
    m u221111 "Lutfen ellerinizi ortaya koyun."
    show monika at thide zorder 1
    hide monika
    "Hepimiz birbirimize bakiyoruz ve birer birer her uye onun istedigini yapiyor."
    scene clubtogether
    with dissolve_cg
    m "Burasi Edebiyat Kulubu. Bes uyeden olusan bir grup."
    m "Hepimiz farkiyiz, ama hepimiz birbirimize deger veriyoruz."
    m "Kimse yarinin ne getirecegini soyleyemez, ama en azindan bugunumuz var."
    m "Ve bugun, besimiz arkadasiz."
    m "Herkes benimle mi?"
    $ everyone_name = "Everyone"
    everyone "Evet!!!"
    "Gulumsamak guzel hissettiriyor ve evet demek guzel hissettiriyor."
    "Bir grubun parcasi olmak guzel hissettiriyor."
    "Yalniz olmadigimi fark ediyorum."
    "Burada kimse degil."
    "Sadece bugun icin, burasi Edebiyat Kulubu."
    scene black
    with dissolve_scene_full
    m "Bununla birlikte, bugunun toplantisi sona erdi!"
    m "Yarini icin siirlerinizi unutmayin!"
    window hide
    stop music fadeout 3

    pause 5

    "Kulup odasindan cikarken kolumda bir cekistirme hissediyorum."
    mc "Sayori..."
    "Dudagini isiriyor ve bakislarini kaciriyor."
    s "[player]..."
    s "...Yeniden parka gidebilir miyiz?"
    s "{i}L-Lutfen{/i}..."
    mc "..."
    mc "Tamam."

    scene black
    pause 2
    play music hammock
    pause 3
    scene bg lake
    show sayori u115322 at t11 zorder 2
    with wipeleft_scene

    "Golun etrafinda yururken serin bir esinti hissediyorum."
    "Sayori basini egik tutuyor. Yuzum sicak."
    mc "Konusmak istedigin bir sey mi vardi?"
    s u115312 "H-Hayir..."
    s u111312 "Sadece seninle vakit gecirmek istedim."
    mc "Oh..."
    mc "Ben..."
    mc "Tesekkurler, Sayori."
    s u115111 "Hah?"
    s "Ne icin tesekkur ediyorsun?"
    mc "Arkadasim... oldugum icin."
    mc "Sen gercekten iyi bir arkadassin... En iyi arkadas. Daha iyisini isteyemezdim."
    s u114322 "..."
    s u115312 "Ya bundan daha fazlasi olsaydik?"
    "Midem buruluyor."
    mc "Sayori..."
    s u123112 "Ya ben senin kiz arkadasin olsaydim, [player]?"
    s "Ya sen benim erkek arkadasim olsaydin?"
    s u123122 "Ya her gun kulupte arkadaslarimizla birlikte eglenip, bunun gibi eglenceli randevulara cikarsak?"
    s u125122 "Ya..."
    s u115112 "...Biliyorsun?"
    "Agzim kuruyor. Kekeliyorum."
    "Gercekten bunu ister miydim?"
    mc "{i}Ya ben her seyi mahvedersem{/i}?"
    mc "Ya {i}ben{/i} her seyi mahvedersem?"
    s u115322 "..."
    s u111312 "Ya sadece bugun benim kiz arkadasim olsaydin?"
    s "Bunu ister miydin?"
    mc "Ben...Ben..."
    "Gulumseyerek elini uzatiyor."
    s u121312 "Ya oyle olsa?"
    mc "Yapamam..."
    s u115312 "..."
    s "[player]..."
    s u111312 "Bana zarar vermeyeceksin."
    mc "Oyle degil, ben..."
    s "Lutfen?"
    "Onun eline bakiyorum ve kendi elime bakiyorum."
    mc "Ben..."
    "Icgudum onu reddetmemi soyluyor. Bunun yanlis oldugunu biliyorum."
    "Ama gercek su ki..."
    "Uzanip elini tutuyorum."
    s u127331 "{i}Eep--{/i}!"
    mc "Eh?? Sayori!"
    s u122222 "O-Ozur dilerim! Bu beni sasirtti..."
    mc "Bu seni nasil sasirtti??"
    s "Ben sadece--"
    s u121312 "...Hicbir sey."
    "Parlak gorunuyor."
    "Eli sicak hissettiriyor..."
    scene lakeside
    with wipeleft_scene
    "Sayori ve ben golun yarisini sessizce gecip duraklamadan once."
    "Korkuluklara gidip birlikte suyun uzerinden bakiyoruz."
    "Hala elimi tutuyor..."
    mc "Biliyor musun, mukemmel yol arkadaslariyiz."
    s "Ehehe~"
    s "Oyleyiz."
    mc "Birbirimizden cok farkli oldugumuzu biliyorum, ama sana hep hayran kaldim."
    s "O-Oyle mi?"
    mc "Tavrini."
    mc "Etrafindaki herkesi nasil gulumsettigini."
    mc "Her zaman oyle gorunmese de, bunu takdir ediyorum."
    s "Her zaman oyle hissetmiyorum..."
    s "Ama bunu soyledigini duymak iyi hissettiriyor."
    s "Ben de sana hayranim."
    mc "Oyle mi...?"
    s "Elbette!"
    s "Sen benim tam tersimsin."
    s "Ben daginikim, sen duzenlisin."
    s "Ben unutkanim, sen hatirlarsin."
    s "Bazı yonlerde, dusunursen, eslesiyoruz..."
    "Gercekten de bu kiz arkadas/erkek arkadas seyini satmaya calisiyor."
    mc "Sana sormak istedigim bir sey var."
    s "Oh? Nedir o?"
    mc "Bana ne zaman asik oldun...?"
    s "Ah..."
    s "...Seni uzun zamandir seviyorum, [player]."
    s "Cocukken her zaman birlikte olacagimizi dusundum."
    s "...Sevginin ne oldugunu bilmeden once bile."
    s "Kulaga sacma geliyor biliyorum."
    mc "Gelmiyor."
    s "Ya sen?"
    s "Beni ne zaman sevmeye basladın?"
    mc "Bir... omur once, o kadar uzun zaman oldu ki."
    s "Gercekten mi...?"
    mc "Ama kulube katilip nasil oldugunu hatirlayinca..."
    mc "Ikimiz birlikte..."
    mc "Iste o zaman gercekten anladim."
    "Ilk donguyu kastediyorum, ama dogru."
    mc "Ve bu oldugunda, sanki ondan onceki her gun o hisle doluymus gibi geldi."
    mc "Durus olmak gerekirse, bu beni korkuttu."
    mc "Benim icin cok onemlisin. O hisse gore hareket edersem her seyi mahvedecegimden emin degilim."
    mc "Senin de ayni sekilde hissettiginden eminim."
    s "Bazen, ama..."
    s "Eger sen beni seviyorsan ve ben seni seviyorsam..."
    s "Bunu ne mahvedebilir ki?"
    "Asagidaki parlayan sulara bakiyorum."
    "Hareketsiz yansimam bana bakiyor, asagidaki nehrin dalgalari onun... 'yuzunu' cok az bozuyor."yuzunu"Hareketsiz yansimam bana bakiyor, asagidaki nehrin dalgalari onun... 'yuzunu' cok az bozuyor."
    "Duygularini okuyamiyorum."
    "Sadece disa dogru bakiyor - benimkini taklit etmeye calisarak."
    mc "Bilmiyorum."
    s "...Belki arkadasligimiz bozulmaz."
    s "Belki her sey iyi olacak."
    s "Ben de korkuyorum, ama..."
    s "...Belki korkmak zorunda degiliz."
    mc "...Belki haklisin."
    s "Hey..."
    "Bana dogru donuyor ve gozlerime bakiyor."
    s "Seni seviyorum."
    s "Ne olursa olsun, her zaman sevecegim."
    mc "..."
    mc "Ben de seni seviyorum, Sayori."
    mc "Bunun asla degismeyecegine soz veriyorum."
    mc "..."
    mc "Yakinda eve gitmeliyiz bence."
    "Sayori uzgun bir sekilde gulumseyip kizariyor."
    s "Tamam."
    s "Ama..."
    "Omzuma dokunuyor."
    s "...Biraz daha kiz arkadasin olabilir miyim?"
    "Basimu salliyorum."
    scene black
    with dissolve_scene_full
    "Beni opuyor."
    "Bir an geri cekilmek istiyorum, ama hisler vucudumu kapliyor."
    "Dudaklari yumusak ve saclarinda karpuz kokusu alabiliyorum."
    "Bana dogru egilirken elleri gogsumde."
    "Artik umurumda degil."
    "Onu kollarimla sariyorum ve vucudunu benimkine bastiriyorum."
    "En iyi arkadasimi opuyorum."
    "Dunya duruyor ve kalplerimiz birlikte atiyor, herhangi birisinin gercek veya sahte olup olmasi umurumda degil."
    "Her sey mukemmel."
    "Once o geri cekiliyor ve bana gulumsuyor."
    s "Sadece bugun icin."
    "Ve bitti."
    "Ama eve birlikte yururken hala ellerimizi tutuyoruz."

    window hide
    stop music fadeout 5
    pause 7

    "Eve geldigimde isiklari yakmaya zahmet etmiyorum."
    "Odama cikiyorum."
    "Masamda daginiklik ve defterler var. Yerde dagilmis bazi kiyafetler."
    "Gulumsuyor, tamamen giyinik bir sekilde yataga girip gozlerimi kapatiyorum."

    scene black
    pause 4
    show monika u111222 at t11 zorder 2
    pause 4

    m "O hakliydi."
    m u111142 "Onlari seviyorum."
    m u111122 "Gercek su ki, onlari mutlu etmek icin her seyi yapabilirim."
    m u113121 "Bu bir hapishanede yasamak anlamina gelse bile."
    m u111122 "Belki de bulmaya calistigim gercek bu."
    m u111141 "Belki bu beni devam ettirmek icin yeterli."
    m u114112 "Benim hakkimda ne hissettigini bilmiyorum, [name]."
    m u113112 "Bildigimi iddia edemem."
    m u113122 "Ama kendimi borclu hissediyorum."
    m u111122 "Yani kendimden vazgecemem."
    m u114222 "..."
    m "Cok korkutucu, cunku..."
    m u113222 "Gercek su ki, affedilme pesindeyim..."
    m u113142 "...Ve o af asla gelmeyebilir."
    m u113112 "[player] bunu bana veremez. Gozlerinde vermek istedigini gorebiliyorum."
    m u112222 "Ha... Biliyorum, bir sekilde hala gozleri oldugunu hissediyorum."
    m u114322 "Ve onlar... nazik. Kendine karsi cok sert olmasina ragmen."
    m u113322 "..."
    m u114322 "Son zamanlarda, zor hissettigim anlarda, yalniz oldugumda ve her seyin uzerime kapandigini hissettigimde..."
    m u113342 "...onlar hakkinda dusunuyorum. Ve onun hakkinda dusunuyorum."
    m u111312 "Ve her sey o kadar da zor olmuyor."
    m u112232 "Belki de soylemek istedigim sey, minnettar oldugum."
    m u111222 "Ne degerli bir his bu."
    m "Beni intihar etmekten alikoyan bir his."
    m u111112 "Eger sana kendinden gercekten nefret eden birinden bir 'yazma ipucu' verecek olsaydim, [name]..."
    m "Minnettarlik ara. Seni hayata dondürecektir."
    m u111142 "Beni dondurdugu gibi."
    m u111122 "..."
    m u111112 "Umarim monologumdan rahatsiz olmazsin. Hayal edebilecegin daha fazlasini yapiyor benim icin."
    m "Tanri'ya inanip inanmadigimdan emin degilim, [name]."
    m u112222 "Ve {i}senin{/i} Tanri olmadigini biliyorum..."
    m u111122 "...Ama seninle konusmak dua etmek gibi hissettiriyor."
    m u112232 "Belki kimse karsilik vermedigi icin."
    m u114224 "Belki... Tanri beni senin araciliginla gorebilir mi?"
    m u111321 "Ve eger bir Tanri varsa... nedense, onlara tesekkur etmek istiyorum..."
    m "..."
    m u111112 "Dinledigin icin tesekkur ederim."
    m u111141 "Umarim biraz minnettar hissedebilirsin. Cunku bu benim hayatimi kurtardi."
m u111112 "...Yazma ipucu bitti. Iyi geceler, [name]."

    show monika at thide zorder 1
    hide monika
    window hide
    pause 5

    $ recordfallen = []
    show textgradient zorder 101:
        xalign .5
        yalign 1.206
    show console_caret_2
    show fallentext "_" as ftext zorder 100
    show cblink zorder 101:
        xpos 245
        ypos 300
        block:
            alpha 0.0
            pause 0.55
            alpha 1.0
            pause 0.55
            repeat
    pause 3.5
    hide cblink
    hide ftext

    call fallen("...O-Onlari basarisiz mi biraktim, gozlemci?")
    call recordfallen("...O-Onlari basarisiz mi biraktim, gozlemci?")

    call fallen("Onlari uyarabilecegimi sanmistim...")
    call recordfallen("Onlari uyarabilecegimi sanmistim...")

    call fallen("Ama onlar kutuphaneye gidecekler...")
    call recordfallen("Ama onlar kutuphaneye gidecekler...")

    call fallen("Hissedebiliyorum...")
    call recordfallen("Hissedebiliyorum...")

    call fallen("C-Cok korkuyorum...")
    call recordfallen("C-Cok korkuyorum...")

    call fallen("Ucuncu gozum gelisti. Bu cok zaman aldi. Cok caba.")
    call recordfallen("Ucuncu gozum gelisti. Bu cok zaman aldi. Cok caba.")

    call fallen("Yine de onlarin secimlerini etkilemek icin yapabilecegim hicbir sey yok.")
    call recordfallen("Yine de onlarin secimlerini etkilemek icin yapabilecegim hicbir sey yok.")

    call fallen("Onlara ogretme sansim olmadan once yok olacaklarindan korkuyorum.")
    call recordfallen("Onlara ogretme sansim olmadan once yok olacaklarindan korkuyorum.")

    call fallen("Korkarim simdi bile cok gec.")
    call recordfallen("Korkarim simdi bile cok gec.")

    call fallen("O orada... Biliyorum onu gordun...")
    call recordfallen("O orada... Biliyorum onu gordun...")

    call fallen("Ama onun gercekte ne kadar kotu oldugunu biliyorum.")
    call recordfallen("Ama onun gercekte ne kadar kotu oldugunu biliyorum.")

    call fallen("Cok uzgunum.")
    call recordfallen("Cok uzgunum.")

    call fallen("Kendimi cok gucsuz hissediyorum... Cok caresiz.")
    call recordfallen("Kendimi cok gucsuz hissediyorum... Cok caresiz.")

    call fallen("Monika seninle konustu cunku, benim gibi...")
    call recordfallen("Monika seninle konustu cunku, benim gibi...")

    call fallen("Tanri'nin onu duyabilmesinin tek yolunun bu oldugunu dusunuyor.")
    call recordfallen("Tanri'nin onu duyabilmesinin tek yolunun bu oldugunu dusunuyor.")

    call fallen("Eger bir Tanri'ya inaniyorsan, lutfen onlar icin dua et.")
    call recordfallen("Eger bir Tanri'ya inaniyorsan, lutfen onlar icin dua et.")

    call fallen("K-Korkarim bu onlarin sahip olabilecegi tek umit.")
    call recordfallen("K-Korkarim bu onlarin sahip olabilecegi tek umit.")

    call fallen("Aman Tanrim...")
    call recordfallen("Aman Tanrim...")

    call fallen("Ozur dilerim... Ben bir aptalaim.")
    call recordfallen("Ozur dilerim... Ben bir aptalaim.")

    scene black
    pause 3

    call screen confirm("Sana ozel bir siir yazdim. Lutfen oku.", Return(True), Return(False))
    if _return:
        call expression "poem_special_shadowpoem"
    else:
        pass

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/5.txt")
        except: open(config.basedir + "/5.txt", "wb").write(renpy.file("A2/Art/scg/5.txt").read())

    scene black
    pause 4
    scene bg bedroom_dawn
    with dissolve_scene_full

    "Gozlerim yavas yavas aciliyor."
    "Yataktan kalkip ayaklarimi yere basiyorum."
    mc "Bu... huzurluydu."
    play sound "mod_assets/sound/sfx/knock1.ogg"
    pause 2
    mc "Monika?"

    scene bg kitchen
    show monika u111322 at t11 zorder 2
    with dissolve_scene_full

    m "Gunaydin."
    m u114111 "Iyi uyudun mu?"
    mc "Mukemmel."
    m u111112 "Guzel."
    m u111111 "Hadi kahvalti edelim, sonra..."
    m u114111 "Yuruyuse cikmak istiyorum."
    mc "Yuruyus mu...?"
    m u111322 "Aklimda belirli bir yer var."
    m u114111 "Biliyorum bu ani oldu, ama okul bitmeden geri donmemiz gerekiyor."
    m u113111 "Gelmek ister misin?"
    mc "Biraz yumurta ve kahve yapayim."
    m u111322 "...Tamam."

    scene bg lake
    play music promises
    with wipeleft_scene

    mc "Burasi tanidik geliyor."
    m "Beni buraya getirdigin zaman, ailemi hatirladim. Beni getirdikleri bir yer vardi."
    m "Buradan ayrilip daga giden bir patika."
    "Bana muzipce gulumsedi."
    m "Umarim yetisecek gucun vardir."
    mc "Bu adil degil. Yorulmuyoruz, o yuzden seni yaniltamam."
    m "Ahaha~"
    m "Uzgunum."
    "Ne kiz ama. Kulubu yoneten o olmasi sasirtici degil."
    "Simdi bile, maceramizda bana o rehberlik ediyor."
    "Gercekten, o bas karakter olmali."
    "Onunla daha iyi olurdun. Katilmiyor musun?"

    scene downhill
    with wipeleft_scene

    m "Daha once bu yoldan gittin mi?"
    mc "Belki bir iki kez... Anilar biraz bulanik."
    mc "Nereye gittigimizi bilmedigimi hatirlamaya yetecek kadar hatirliyorum."
    m "Oh guzel. Hosuna gidecek. Oldukca guzel bir manzara."
    m "Bu tepenin zirvesine ulastigin zaman tum komsu sehri gorebiliyorsun."
    m "Bizim sehrimiz o kadar dolu ve detayli ki... Seylerin hatirledigim gibi olup olmadigini gormek istiyorum."
    mc "Mantikli..."
    "Bu neden aklima gelmedi diye merak ediyorum..."
    mc "Eger hepsi oradaysa ne anlama geldigini dusunuyorsun?"
    m "..."
    m "Bilmiyorum. Iki sonuctan da biraz korkuyorum."
    m "Bir suru bosluk gormek istemiyorum."
    m "Ama eger bu tepelerin otesinde baska bir sehir varsa, bu da biraz korkutucu, degil mi?"
    m "Bu, neredeyse daha kotu hissettiren bir bosluk."
    m "Belki..."
    "Basimi salliyorum."
    mc "Ne demek istedigini anliyorum..."
    mc "Ama bilmenin daha iyi oldugunu saniyorum."
    m "Ama... nasil yasayacagiz?"
    m "Ya tum hayatimizi bu oyunda yasamak zorunda kalirsak?"
    m "Ya digerleine asla gercegi soyleyemezsek?"
    m "Bunu dusunmek bile zor..."
    mc "..."
    mc "Ben... bilmiyorum."
    mc "Ama bir yolunu bulacagiz, degil mi?"
    m "Oyle umuyorum."
    m "Evet..."
    "Geri kalan yolculugu sessizce, yuruyusumuzuze odaklanarak gectik."
    "Zirveye ulasmamiz bir saatten az surdu."

    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    pause 2
    play music wind fadein 2.0
    scene mountain
    with dissolve_scene_full
    pause 2

    "Arazi onumuzde uzaniyor."
    m "Aman Tanrim..."
    mc "Monika?"
    m "[player]..."
    m "Tum dunya bos mu?"
    mc "..."
    m "Bu kadar yalniz miyiz?"
    m "Burasi neresi? Bu 'oyun'?"
    m "Buna artik oyun demek yanlis geliyor."
    m "Bu cok daha fazlasi."
    mc "Monika..."
    m "Ailemi ozluyorum..."
    mc "..."
    m "Dunyada anneme herkesten daha yakindin."
    m "Ikisini de cok sevdim..."
    m "Bunlardan herhangi biri gercek miydi? Bilmiyorum."
    m "Soylemek cok zor."
    m "Burasi cennet mi, yoksa cehennem mi?"
    m "Ikisinin arasinda bir sey olabilir."
    "Bana bakiyor."
    m "Belki de bunu bizim karar vermemiz gerekiyor."
    m "Eger digerleri bizim gordugumuz seyi goremiyorsa, o zaman bu bize kalmis, degil mi?"
    m "Bu yeri iyi bir sey haline getirmek zorundayiz."
    m "..."
    m "{i}Ben{/i} bu yeri bir seyler haline getirmek zorundayim."
    m "Hala kulup baskaniyim. Bunu ciddiye almak bana kalmis."
    m "Bu eglenceli bir gorev olabilir..."
    m "...ya da onlari iyi bir arkadas olarak seven biri olmak."
    m "Burada bile bir amacim olabilir."
    m "Belki de bunu goremeyecek kadar kendimle mesguldum."
    m "Anladin mi?"
    stop music fadeout 2.0
    mc "..."
    m "...?"
    m "Neyin var?"
    mc "B-Ben..."
    mc "{i}Ailemle ilgili hicbir aniim yok{/i}..."
    m "Hm...?"
    scene windmc
    with dissolve_scene_full
    play music mainthemesimple
    pause 2
    mc "Ben sizler gibi degilim. Bu oyun icin yaratildim."
    mc "Benim bir karakterim yok."
    mc "Bu tur oyunlarda bas karakterler sadece yer tutuculardir."
    mc "Tehdit edici olmamamiz icin yaratildik, boylece oyuncu ve sevdigi kizlar arasina girmiyoruz."
    mc "Ben bir kaybedenin. Kizlarla kaygan davraniyorum. Ben... sevilir degilim."
    mc "Gercek su ki, ben burada olmasaydim her seyin daha iyi olacagini dusunmeden edemiyorum."
    mc "Gercek su ki... kendimden gercekten nefret ediyorum."
    mc "Ve nasil degisecegimi bilmiyorum."
    mc "{i}Ben bir yetimim, degil mi{/i}?"
    scene windm1
    with dissolve_scene_full
    mc "Sanki var olmayan bir kahramanin yerini almak icin dogmusum gibi hissediyorum."
    mc "Kalbim ask icin atiyor..."
    mc "Ama onlarin kalbini kirmadan asik olamiyorum."
    mc "Belki de seni [name]'e baglayan bir sey olmasini dileyerek beni yarattin."
    mc "Belki de ben sadece bir garip kaza. Bir ucube."
    mc "Senin sahip oldugun seye sahip degilim. Belki de bu yuzden bir yuzum yok."
    mc "Ama..."
    mc "Burada bir amac buluyorum."
    mc "Diger kizlari goruyorum ve bana umut veriyorlar."
    mc "Degisebilecegim umudu. Daha iyi bir insan olabilecegim umudu."
    mc "Gelecekten korkmak zorunda olmadigim umudu."
    mc "Ama simdi oldugum kisi olmaktan nasil degisecegim?"
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    mc "Kendimi gercekten hic sevmiyorum."
    window hide
    pause 2
    m "Ben seni seviyorum."
    mc "Ha?"
    m "Sen de hissediyorsun, degil mi?"
    mc "Neyi hissetmek?"
    show windm2:
        yalign 0.4
    with dissolve_scene_full

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/The Sky.txt")
        except: open(config.basedir + "/The Sky.txt", "wb").write(renpy.file("A2/Art/scg/The Sky.txt").read())

    play music mainthemefull
    "Monika gokyuzu gibi gulumsedi."
    m "Ruzgar!"
    m "Gercek gibi hissettiriyor!"
    "Bir ruzgar dalgasi vucuduma carparken saskinlikla yukariya bakiyorum."
    m "Hic bu kadar harika bir sey hissettin mi?"
    "Gokyuzundeki gorunmez bir dans gibi... Hava giysilerimi cekistiriyor ve kalbimi parcaliyor."
    "Dagdaki kiz ucuyor."
    m "Uzgunum, [player]. Ama sana inanmiyorum."
    mc "!"
    m "Sen benim icin gerceksin."
    m "Ve bir sekilde, bu dunya da oyle."
    "Beni dunyanin zirvesine cikartan bu kiza bakiyorum."
    "Vududum, aciyan kalbimin etrafinda, canli hissediyor."
    m "Biz bu dunya icin yaratildik. Ya da, bu dunya bizim icin yaratildi."
    m "Burada sevgi var. Hissediyorum."
    m "Her sey iyi olacak."
    scene black
    with dissolve_scene_full
    m "Hadi geri donelim, [player]."
    m "Buraya gelme amacimiza ulastik."

    scene downhill
    with dissolve_scene_half

    m "Benimle daga ciktigin icin tesekkur ederim."
    mc "Bana mi tesekkur ediyorsun?"
    mc "Sana tesekkur etmem gerektigini dusunuyorum."
    m "Sacmalik. Sana minnetarim."
    m "Sensiz tirmanmaya cesaretim olmazdi."
    mc "Ama--"
    m "Hayir."
m "Ahaha~"
    m "Hayir, itiraz kabul etmiyorum."
    m "Tesekkur ederim."
    mc "..."
    "Ne imkansiz bir kiz."
    "Onunki gibi kirik bir kalple gulmek ve gulumseyek."
    "Boyle bir yerde bu kadar guzel olmak."
    "Onun gibi insanlar, benim gibi insanlarin utanmasini saglamali."
    "Sen de kendinden nefret ediyorsun..."
    "Ama icin altindan yapilmis."
    stop music fadeout 4.0

    scene black
    with dissolve_scene_full
    scene bg corridor
    with wipeleft_scene

    "Dusuncelerime yapisan bir fikir kalbimi cekistiriyor ve vucudum donuyor."
    mc "Sayori?"
    "Okulda degil. Bir sorun mu var?"
    "Onun yerini hissetmeye calisirken acele etmeye basliyorum."
    scene black
    with dissolve_scene_full
    "Arka kapisindan cikip ormana ilerliyorum."
    "Bu ona benzemiyor. Dogru davranmiyor. Endiseleniyorum..."
    scene bg forest
    with dissolve_scene_full
    "Sanki saf icguduyle nereye gidecegimi biliyormuscasina yaklasiyorum."
    mc "Hey..."
    play music morethan
    show sayori u114311 at t11 zorder 2
    s "!"
    s u113312 "[player]..."
    s u112322 "Hehe... Beni buldun."
    mc "Burada ne yapiyorsun?"
    show sayori u116323
    "Sayori sanki yanlis bir sey yaparken yakalanmis gibi kaslari catiyor."
    s u113123 "Özür dilerim. Her seyden uzaklasmak zorundaydim."
    s "Bazen her sey cok fazla geliyor..."
    mc "Anliyorum. Ne dusunuyorsun?"
    s u115112 "..."
    s u113112 "Hic hissettin mi, sanki..."
    s "Sanki olaylarin belli bir sekilde olmasinin kararli oldugunu mu?"
    s u113122 "Ve ne yaparsan yap gercekten hicbir seyi degistiremezmisin gibi?"
    s u115123 "Sanki hayatin bir raylarin uzerinde, ve herkesinki de oyle mi?"
    s u115113 "Bunu dusunmek zor. Ve bunun gercekten dogru oldugu hissini uzaklastiramiyorum."
    mc "Sayori..."
    "Onunla bu konuda konusmaya hazir miyim?"
    mc "Daha önce depresyonda olabileceğinden söz etmistin. Su anda hissettigin seyin bu oldugunu mu dusunuyorsun?"
    s u114112 "..."
    s u112122 "Ehehe. Sanirim haklisin."
    s "Bunu bilmeliydim."
    "Daha yakin adim atip onu kucakliyorum."
    s u114131 "Oh!"
    "Vucudu geriliyor, sonra yavasca bana sariyor."
    scene black
    with dissolve_scene_full
    mc "Buradayim, Sayori. Hicbir yere gitmiyorum..."
    "Sayori yuzunu omzuma gomuyor."
    s "{i}Söz veriyor musun{/i}?"
    mc "Tabii ki veriyorum."
    mc "Sonsuza dek. Tamam mi?"
    s "{i}T-Tamam.{/i}"
    scene bg forest
    show sayori u111322 at t11 zorder 2
    with dissolve_scene_half
    "Bir sure beraber duruyoruz ve sonra beni birakiyor."
    s u111312 "Tesekkurler, [player]. Gercekten cok iyisin."
    mc "Onemli degil, Sayori. Seni gercekten onemsiyorum."
    s u112141 "Hehehe..."
    s u112112 "Her zaman en iyi arkadas kalacagiz, degil mi?"
    mc "Her zaman."
    mc "Bu yuzden o sozu verdim."
    mc "Okula geri donelim."
    s u111112 "Tamam."
    stop music fadeout 2.0

    scene black
    with dissolve_scene_full
    pause 2
    show libwindow zorder 2:
        alpha 0
        linear 3 alpha 1

    show libdust zorder 3:
        alpha 0
        yalign 0.5
        xalign 0.54
        subpixel True
        parallel:
            linear 3 alpha 1
        parallel:
            linear 9 xalign 0.46
    pause 0.3
    play music roarke
    pause 8.5
    show bg library zorder 4:
        alpha 0
        linear 2 alpha 1

    pause 2
    hide libdust
    hide libwindow
    scene bg library
    pause 4

    "Kutuphane onumde aciliyor."
    "Eskiden olmadigi bir sekilde davetkar hissettiriyor."
    "Belki de Yuri ile arkadas olmak gibi."
    "Ilk basta ulasilmaz hissediyor. Dokunulamaz."
    "Ama bir arkadas olarak, sicak ve rahatlatici. Yargilandigindan daha fazla."
    "Bu dusunceyle gulumsuiyorum."
    show yuri u111111 at t11 zorder 2
    y "Merhaba, [player]."
    y u121118 "Bugun gelecegini dusunmemistim."
    mc "Ozur dilerim. Umarim hayal kirikligina ugramamıssindir."
    y u121171 "Uhuhu~"
    y u111111 "Sorun degil. Her iki sekilde de baski hissetme. Ama arkadasligin takdir ediliyor."
    y u111141 "Toplanti icin vakit yaklasiyor. Siirlerimizi paylasmadan once biraz okuma yapmak istiyordum."
    mc "Bu mantikli. Sayori'nin kitabini zar zor okudugumu fark ettim. Biraz onu okumak umidindeyim."
    mc "Bu yuzden seni rahatsiz etmeyeyim."
    y u111172 "Ahh..."
    y u111148 "Peki. Bu iyi bir fikir."
    "Icgudulerim bana Yuri'nin aklinda bir seyin oldugunu soyluyor."nin aklinda bir seyin oldugunu soyluyor."
    "Ama zorlamamak en iyisi. Kendini rahat hissettiginde konusacak."
    stop music fadeout 3.0
    "Sayori'nin kitabi {i}Dusen Melekler{/i}'i cikarip ikinci bolumden aciyorum."nin kitabi {i}Dusen Melekler{/i}"Sayori'nin kitabi {i}Dusen Melekler{/i}'i cikarip ikinci bolumden aciyorum."

    scene white
    with dissolve_scene_full
    $ style.say_window = style.normal

    pause 1

    $ style.nvl_dialogue.font = "mod_assets/Inkfree.TTF"
    $ style.nvl_dialogue.size = 26
    $ style.nvl_dialogue.color = "#000000"
    $ style.nvl_dialogue.outlines = []

    tfa '"Hey! Uyan!"'
    tfa 'Hirsiz kiz, yetim cocugu sarsmis, uykusundan uyandirmaya calisiyordu.'
    tfa 'Protestoya inleyince kiz kikirdadi.'
    tfa '"Hadi! Guvec yaptik. Kahvaltiyi kacirmak istemezsin!"'
    tfa 'Bu cocugun dikkatini cekti. Grubun ona sagladigi pacavralardan kendini acti.'
    tfa 'Kiz siritti.'
    tfa '"Isindin mi?"'
    tfa '"Hadi gel, guvec de oyle!"'
    tfa '"Off ya," bir yetim kiz itiraz etti, "neden uyumasina izin vermiyorsun? Kim bilir ne kadar zamandır dışarıdaydı?"'
    tfa '"Sus sen. Sen sadece paylasmak istemiyorsun."'
    tfa 'Cocuk tencereye dogru yuruyunce tanidik olmayan yuzler ona bakti.'
    tfa '"Al. Bir kase al."'
    nvl clear
    tfa 'Guvecli bir kase eline verildi. Sicakti. Icerisinde patatesler vardi.'
    tfa 'Onu oraya getiren kiz soru sormaya baslamadan once ona fazla zaman verilmedi.'
    tfa '"Ee? Adin ne senin?"'
    tfa '"Um... Bilmiyorum..."'
    tfa 'Cesitli yetimler nefeslerini tuttular ve deneyimli olanlarin birkaçi inledi.'
    tfa '"Adini bilmiyor musun? Tipki benim gibisin! Bir--"'
    tfa '"--melek," alayli seslerin korosu geldi. Kiz dilini cikardi.'
    tfa '"Onun melek konusmasina kapilma. O hic de oyle degil."'
    tfa 'Baska bir yetim konustu. "Kendi adini bilmiyor. Cennetten dustugunu soyluyor." Tukurdu. "Dun adi Susan\'di, yarin--"'
    play music mainthemesimple
    tfa '"--Susan," kiz araya girdi. "Susan isminde karar kildim."'
    nvl clear
    tfa 'Anilari olmayan çocuga bakmak icin dondu. "Hicbir sey hatirlamiyorsun, degil mi?"'
    tfa 'Hayret icinde yukari bakti ve basini salladi. Kiz siritti.'
    tfa '"Gorduun mu? Bu bir isarettir. Bu yuzden adimi secmistim. Gercek adim olmali!"'
    tfa '"Endiselenme. Sen de adini bulacaksin. Tipki benim gibi."'
    tfa '"Biliyor musun neden?"'
    tfa 'Cocuk basini salladi.'
    tfa '"Cunku bir oyunun icinde sikisip kaldin. Hepsi bu. Doki Doki Edebiyat Klubu adli bir oyun. Ve biz buradan cikacagiz!"'
    nvl clear

    stop music
    $ style.say_window = style.window_normal
    scene bg library
    show yuri u227121 at h11 zorder 2
    "Neredeyse kitabi vurarak kapatiyorum, bu da Yuri'nin sicramasina neden oluyor."nin sicramasina neden oluyor."
    mc "Ah! Ö-Özür dilerim... Kitabı o kadar sert kapatmak istemedim..."
    mc "Bu, şey, bölümler ki-kısa, değil mi?"
    show yuri u223318
    "Yuri bana bakip basini salliyor."
    y u225142 "Bu tarz hiç hosuma gitmiyor."
    mc "Ha... Öyle mi?"
    y u223144 "Mm..."
    y u125118 "Sana bir sey sorabilir miyim, [player]?"
    mc "Tabii..."
    y "Sayori'ye asik misin?"
    mc "..."
    mc "Bu soru biraz tehlikeli gibi geliyor."
    y u112248 "Ah... Ben basit bir soru oldugunu dusunmustum."
    mc "...Haklisin."
    "Odaklanmam lazim. Dikkatim dagilmasin."
    mc "Onu cok seviyorum. Onun icin olurdum..."
    y u114118 "Hmm..."
    "Yuri dikkatle basini salliyor."
    mc "Kararsiz gorunmek istemiyorum. Ama dun beni gordun... Berbat durumdayim."
    mc "Onunla sadece arkadastan fazlasi olmaya calisacak olsam, hayatini daha kotulestirecegimi hissediyorum."
    mc "Ve en azindan, bu sekilde hissetmek bile hazir olmadigimi gostermiyor mu?"
    y u111118 "Nasil hissettigini biliyorum."
    y "Bu oldukca asil gorunuyor."
    y u115118 "Ama iliskiler o kadar basit degil. Kimse mukemmel degil. Ne sen, ne de o."
    y u111118 "Bazen sans almaniz gerekir."
    "Ellerime bakiyorum."
    mc "Bir secim yapmam gerektigini soyluyor gibisin."
    y u121148 "Bu muhtemelen olgun bir bakis acisi."
    y u125118 "Yarin olmak zorunda demiyorum..."
    y "Ama belirsizlikte cok fazla zaman gecirmek birinin kalbini kirabiliyor, [player]."
    "Basimi salliyorum."
    mc "Haklisin..."
    mc "Bu kadar kotu oldugum icin ozur dilerim."
    y u111161 "Uhuhu~"
    y u111118 "Sen kotu degilsin. Ben buna zorlanmadim."
    y "Sadece iyi bir arkadas olmaya calisiyorum. Hem ona, hem de sana."
    "Ona bakip gulumsuoyorum."
    mc "Kesinlikle oylesin."
    mc "Benimle arkadas oldugun icin tesekkurler."
    y u111172 "Zevk benim."
    "Yuri kitabini kapatiyor ve kaldiriyor."
    y u111118 "Toplantida gorusuruz."
    show yuri at thide zorder 1
    hide yuri
    "O gittikten sonra kutuphanenin mimarisine bakiyorum."
    mc "Bence artik buraya gelmemi neden istemedigini biliyorum."
    show natsuki myghost at t11 zorder 1
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Ve neden olabilir ki?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Oyun burada ayni degil. Daha genis."
    mc "Neredeyse buradaki seyler daha... gercek gibi."
    "Varlik Natsuki'nin basini salliyor."nin basini salliyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Yaniliyorsun. Bu yuzden araya girmeye calistim."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Sayori'nin kitabini kaldiriyorum."nin kitabini kaldiriyorum."
    mc "Hakli miyim? Bu kutuphanede oldugum icin mi boyle okundu?"        #FN
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "..."
    fn "Hayir. Nerede okursan oku boyle olacakti."
    fn "Ve tum kopyalar ayni."
    fn "Sayori seninle ayni kelimeleri okudu ama farkli anilari vardi."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "..."
    mc "Sana nasil guvenebilirim?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Tavsiyemi isteyip sonra acikca reddetmen bana hakaret ediyor."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Isaret ediyorum."
    mc "Onun vucudunu kullaniyorsun."
    mc "Bu beni uzuyor. Benimle baska bir sekilde konussan daha fazla guvenirdim."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "...Oyle calismiyor."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "O zaman nasil {i}calisiyor{/i}?"
    "Figur durakliyor. Omzunun uzerinden bakiyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Burada degil...simdi degil."
    fn "Bu...uygun degil."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Peki o zaman."
    mc "Git buradan."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "..."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    show natsuki at thide zorder 1
    hide natsuki
    mc "Katilacak bir toplantim var."

    scene black
    with dissolve_scene_full
    pause 2
    scene bg club_day
    play music t3
    with dissolve_scene_full

    "Toplantiya tam zamaninda yetisiyorum."
    show sayori u111111 at t11 zorder 2
    s "Hey [player]!"
    s u122111 "Neredeyse gec kalacagini dusundum. Ehehe~"
    mc "Ah... Uzgunum, Sayori. Seni endiselandirmek istemedim."
    mc "Bugunun ne kadar onemli oldugunu biliyorum."
    mc "Gec kalmak istemezdim. Bu kulup beni gercekten etkiledi."
    s u111141 "Ehehehe~"
    s u112111 "Cunku biz Edebiyat Kulubuyuz."
    s "Burasi ozel bir yer."
s u122171 "Bunu takdir etsen iyi olur!"
    "Gulumsuyorum."
    mc "Sanırsam gercekten takdir ediyorum."
    show sayori at thide zorder 1
    hide sayori
    show monika u221111 at t11 zorder 2
    m "Herkes hazır mı?"
    m u222242 "Umarım son dakika calısmalarınıza engel olmuyorumdur."
    show monika at t21
    show natsuki u114214 at t22 zorder 2
    "Natsuki, bir kagit parcasina bir seyler karaliyor, yerinden sicriyor."
    show natsuki at f22 zorder 3
    n u113234 "H-Hayır, iyiyim. Sadece düsüncelerimi topluyorum."
    "Karakteristik olmayan bir sekilde gergin gorunuyor. Yuri kendi kagidinin arkasina saklanmis, sanki siirini aklindan tekrarliyormus gibi."
    show natsuki at thide zorder 1
    hide natsuki
    show monika at t11
    m u112222 "Sorun degil. Yargılayamam. Hepiniz orijinal bir sey yaptınız. Ben eski bir materyale güveniyorum."
    m u112231 "Umarım kötü bir örnek olusturmuyorumdur."
    m u111111 "Birisi ilk olmak ister mi?"
    show monika at t21
    show sayori u222141 at f22 zorder 3
    s "Ben, ben, ben!"
    s u222322 "Bekle, aslında bu konuda biraz gerginim..."
    s u112312 "B-Baska birisi önce gidebilir mi ve ben ikinci olabilirim...?"
    show sayori at thide zorder 1
    hide sayori
    show monika at t11
    m u112332 "Ahaha... Sorun degil."
    "Monika bana bakiyor."
    m u111111 "Ya sen, [player]? Nasıl hissediyorsun?"
    mc "Biraz gerginim, ama..."
    mc "Daha korkutucu seyler yaptım."
    m u111112 "Sanırım itiraz eden yok. Devam et."
    show monika at thide zorder 1
    hide monika
    stop music fadeout 3.0
    "Odanin onundeki yerimi aliyorum, herkes sessizlesiyor."
    "Bir an icin, sadece ben ve kagit parcam var. Önumdeki kizlar tanidigim hallerinden uzaklasiyor."
    "Onlari siirde goruyorum."
    mc "Adı {i}Göksel Kıyı{/i}.{nw}"
    show screen tear(50, 0.1, 0.1, 40, 80)
    play sound "sfx/glitch2.ogg"
    pause 0.5
    show vignette:
        alpha .8
    hide screen tear
    mc "Adı {i}Göksel Kıyı{/i}.{fast}"
    mc "..."
    mc "Kasvetli ve sert bir plajda, calkalanan bir denizin kenarında duruyorum."
    mc "Fısıltılar suyun üzerinde dolanıyor - Buzlu rüzgarın icinden konusuyor."
    mc "Yere kök salmıs, cıplak ayaklarım kanamaya baslıyor..."
    mc "Sadece bir hevesle geldim, karanlık arzularımı burada doyurmak icin."
    mc "..."
    mc "Taze korku ile, parmaklar dalgalanan dalgaların icinden uzanıyor -"
    mc "Sisli gecenin gölgeleri sulu mezarlarını terk ediyor."
    "Bir kalem yere dusuyor, okumamda kucuk bir duraklamaya neden oluyor. Ama garip bir duygu devam etmemi sagliyor."
    mc "Ölüm yalnız kıyıma yaklaşırken, kalbim neşe ve korkuyla doluyor."
    mc "Sinirlerimi soğuğa karşı çelikleştiriyorum..."
    "Derin bir nefes aliyorum."
    mc "Ve yasayan ölülerle karşılaşıyorum."
    pause 3
    hide vignette
    with Dissolve(2.0)
    pause 1
    "Bir sessizlik donemi var. Yukari bakiyorum."
    "Kulup alkislamaya basliyor."
    mc "T-Tesekkürler..."
    "Garip bir sekilde yerime oturuyorum."
    show sayori u112222 at t11 zorder 2
    s "Um, s-simdi ücüncü olabilir miyim?"
    s "Bundan sonra gelmek istemiyorum..."
    s u111312 "Harika is, [player]."
    show sayori at thide zorder 1
    hide sayori
    show monika u114124 at t11 zorder 2
    m "Sorun yoksa, ben gitmek istiyorum."
    "Monika kalkiyor ve bize donuyor."
    m u112222 "Baslıgı... atlayacagım."
    m u113143 "{i}Ahem{/i}..."
    play music mainthemesimple
    m u114111 "Eski bir hikaye, dünyada dolasan bir kadından bahseder: Her Seyi Bilen Kadın."
    m "Her cevabı bulmus güzel bir kadın..."
    m u113111 "Tüm anlamı..."
    m "Tüm amacı..."
    m u113143 "Ve simdiye kadar aranan her seyi."
    m u114314 "Ve buradayım, bir tüy..."
    m "Gökyüzünde sürüklenen, rüzgarın akıntılarının kurbanı."
    m u114111 "Gün be gün, arıyorum."
    m u113112 "Az umutla arıyorum, efsanelerin var olmadıgını bilerek."
    m "Ama diger her sey beni bıraktıgında, diger herkes uzaklastıgında..."
    m u114312 "Efsane geriye kalan tek sey - alacakaranlık gökyüzünde parlayan son soluk yıldız."
    m "Bir gün, rüzgar esmeyi kesiyor."
    m u113312 "Düsüyorum."
    m u113344 "Ve düsüyorum ve düsüyorum, ve daha da düsüyorum."
    m "Bir tüy kadar nazik. Kuru bir kalem, ifadesiz."
    m u114111 "Ama bir el beni bas ve isaret parmakları arasında yakalıyor. Güzel bir kadının eli."
    m "Onun gözlerine bakıyorum ve bakısında bir son bulamıyorum."
    m u114112 "Her Seyi Bilen Kadın ne düsündügümü biliyor."
    m u113324 "..."
    m u114113 "Ben konusamadan, o içi boş bir sesle cevap veriyor:"
    m u114143 ""Her cevabı buldum, hepsi hiçbir şeye denk geliyor."
    m u114144 "Anlam yok."
    m "Amaç yok."
    m u114111 "Ve biz sadece imkansızı arıyoruz."
    m "Ben senin efsanen degilim."
    m "Senin efsanen mevcut degil.""
    m u114142 "Ve bir nefesle, beni tekrar havaya üflüyor, ve ben bir rüzgar esintisi yakalıyorum."
    show monika at thide zorder 1
    hide monika
    stop music fadeout 3.0
    "Herkes alkisliyor. Monika yerine donerken ona gulumsuyorum."
    show sayori u114312 at t11 zorder 2
    s "Bu gercekten harikaydı."
    s u112322 "Ikiniz de çok ciddi siirler yaptınız..."
    s "Simdi biraz utanıyorum."
    m "Endiselenme, Sayori. Sadece ne yazdıgını duymak istiyoruz."
    show sayori u114312
    "Sayori Monika'ya bakiyor ve baslyla onayliyor."ya bakıyor ve baslyla onaylıyor."
    s u111312 "Tamam..."
    s "Siirimin adı..."
    s "{i}Arkadaşlarım{/i}."
    s u115322 "..."
    s u112322 "{i}Phew{/i}. Tamam."
    play music mainthemesayori
    s u113112 "Düşük ve üzgün hissettiğimde..."
    s u111312 "Arkadaşlarım beni mutlu bulur."
    s u113312 "Tökezlediğimde ve yoldan çıktığımda..."
    s u113311 "Arkadaşlarım yolumu aydınlatır."
    s u114312 "Dizlerim yere düşmekten berelenmiş, ama beni yerde gören arkadaşlarım..."
    s u111312 "Arkadaşlarımda kendimi çok mutlu hissediyorum, yolu bulan arkadaşlarım."
    s u115322 "..."
    s u115312 "Arkadaşlarım her zaman düştüğümü görmez, ama her zaman beni kaldırırlar."
    s u111312 "Arkadaşlarım söylemediğim şeyleri bilmez, ama yalnız olduğumda duyarlar."
    s u115312 "Kendimden ve yolumdan şüphe ediyorum..."
    s u111312 "Ama arkadaşlarım ikisine de inanıyor."
    s "Ve ben arkadaşlarıma inanıyorum."
    s u115322 "..."
    s u112322 "V-Ve, bu kadar!"
    show sayori at thide zorder 1
    hide sayori
    "Hepimiz Monika'dan daha sert alkisliyoruz. Sayori derinden kizariyor ve yerine oturuyor."dan daha sert alkışlıyoruz. Sayori derinden kızarıyor ve yerine oturuyor."
    "Durust olmak gerekirse, ona sarilmak istiyorum ve bu durtuye biraz karsi koymam gerekiyor."
    show monika u111312 at t11 zorder 2
    m "Bu harikaydı. Teşekkürler, Sayori."
    stop music fadeout 3.0
    m u112111 "Peki... Natsuki? Yuri?"
    m u122231 "Ikinizi de zor durumda bırakmak istemiyorum, ama biriniz bir sonraki olmak ister mi?"
    show monika at thide zorder 1
    hide monika
    show yuri u224348 at t11 zorder 2
    y "uuu..."
    show yuri u224318
    "Yuri neredeyse yalvarircasina Natsuki'ye bakiyor."ye bakıyor."
    show yuri u224121
    "Natsuki'nin ifadesini gorunce gozleri saskinlikla buyuyor."nin ifadesini görünce gözleri şaşkınlıkla büyüyor."
    show yuri at t21
    show natsuki u11s131 at f22 zorder 3
    n "Yuri... Lütfen... {i}once sen gider misin{/i}...?"
    n "Ben son olmak istiyorum."
    show natsuki at thide zorder 1
    hide natsuki
    show yuri u223218 at t11
    "Yuri birkac kez goz kirpiyor, sonra basiyla onayliyor."
    "Hepimizin onune ciktiginda o kadar gergin gorunmuyor."
    y u125118 "Bu şiirin adı {i}Mumum{/i}."
    y u125172 "{i}Ahem.{/i}"
    play music mainthemeyuri
    y u115118 "Sahip olduğum bir mum var..."
    y u115111 "Nadiren gösterilen veya kullanılan."
    y u115172 "Yine de sürekli ateşte yanıyor -- Ve gece yarısı manzarasını aydınlatıyor."
    y "Işık olmadan -"
    y u115111 "- veya yürüme bastonu..."
    y "Bir yol bulamıyorum. Mumum beni sağduyulu yaptığında..."
    y u111118 "Arkadaşlarımı bugün görüyorum."
    y u113148 "..."
    y u111148 "Son satır son dakika değişikliydi. Çok daha iyi olduğunu düşünüyorum."
    y u115148 "H-Hepsi bu kadar."
    show yuri at thide zorder 1
    hide yuri
    "Yuri icin alkisliyoruz ve ben ona cesaret verici bir gulumseme veriyorum. O da utangacca gulumsuyor."
    stop music fadeout 3.0
    show natsuki u119234 at t11 zorder 2
    "Natsuki birden ayaga firliyor ve one dogru yuruyor."
    show natsuki u114234
    "Agzini acip tekrar kapatiyor."
    "Sonra basliyor."
    n u113214 "Bunun başlığı yok."
    n u119234 "..."
    play music mainthemefull
    n u113124 "Çok akıllı değilim."
    n u113114 "Çok uzun boylu değilim."
    n "Güzel şeylerim yok."
    n u114234 "Hiç de iyi biri değilim."
    n u114254 "Beni seven insanlara zarar veriyorum."
    n u114214 "Ve kendim de kolayca inciniyorum."
    n u113234 "Bunu kafiyeli yapmak için yeterince iyi değilim."
    n u119234 "Ve belki de denemek için fazla tembelim."
    n u11s232 "A-Ama..."
    show natsuki u11s216
    "Gozyaslari akmaya basliyor."
    n u11s213 "H-H-Hepiniz benim için çok şey ifade ediyorsunuz."
    n u11s336 "Ve hepinizi ç-çok seviyorum."
    n "Her biriniz için dünyayla savaşırım..."
    n "...ve bu benim size mektubum."
    n u11s133 "Dinlediğiniz için teşekkür ederim, ama her şeyden önemlisi..."
    n "Arkadaşlarım olduğunuz için teşekkür ederim."
    scene black
    with dissolve_scene_full
    "Natsuki yerine oturuyor ve kimse alkislamiyor cunku kimsenin buna ihtiyaci yok."
    "Monika ayaga kalkiyor."
    m "Hepinize, her birinize, dünyanın en iyi kulübündeki en iyi kulüp toplantısı için teşekkür ederim."
    m "Bununla birlikte, bu toplantıyı sonlandırıyorum."
    m "Hepinizi yarın tekrar görmeyi dört gözle bekliyorum!"
    stop music fadeout 3.0

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/6.txt")
        except: open(config.basedir + "/6.txt", "wb").write(renpy.file("A2/Art/scg/6.txt").read())

    scene black
    pause 5

    "Gec oluncaya kadar bekleyip okula gizlice gidiyorum."
    "Monika benimle kutuphanenin disinda bulusuyor."
    m "...Merhaba."
    mc "Bunu yapmak istediğinden emin misin?"
    mc "Ne yapmak istediğimi biliyorum, ama yapmayacağım--"
    m "Dur. Sen gidiyorsan ben de gidiyorum."
    m "Ve senin gideceğini biliyorum."
    mc "..."
    mc "Buradalar."

    scene library_night
    show natsuki myghost at t11 zorder 2
    with dissolve_scene_full

    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Bunu yapmamanı tavsiye ediyorum."
    fn "Bu dinlemen için tek şansın."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "O zaman bizi durdur."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "..."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Ben de öyle düşünmüştüm."
    show natsuki at thide zorder 1
    hide natsuki
    "Figurun yanindan yuruyoruz."
    "Omzumun uzerinden baktigimda bizi izledigini goruyorum."
    "Bu beni urpertiyor, ama donup ilerlemeye odaklaniyorum."
    "Geri donus yok."
    m "Nasıl başlamalıyız?"
    mc "Hangi bölümlerden geçtiğimizi not edelim."
    mc "Şimdiye kadar her şey oldukça düzenliydi. Kurgu kurgu olmayandan ayrı, bu yüzden muhtemelen orada ipuçları bulabiliriz."
    m "İyi fikir."
    m "Hmm... {i}Biz{/i} kurgu muyuz yoksa kurgu olmayan mı?"
    mc "..."
    mc "Bu soru ne kadar korkutucu olsa da, sadece ne bulacağımızı görelim, tamam mı?"
    m "Doğru. Özür dilerim."
    mc "Sorun değil."
    mc "Devam edelim."
    "Zaman geciyor."
    m "Bu raflar tekrarlanıyor."
    mc "Öyle mi...?"
    "Hakli. Duz bir cizgide yuruyoruz ama zaten gectigimiz ayni sozlukleri taniyorum."
    m "Geri dönmeli miyiz? Belki bu tehlikeli..."
    "Basimi ceviriyorum."
    mc "Kapıyı görebiliyorum..."
    "Uzak ama figuru hala durdugu yerden bizi izlerken gorebiliyorum."
    mc "Sanırım yeni bir şey bulmak istiyorsak merdivenleri kullanmamız gerekiyor."
    mc "Sol mu sağ mı?"
    m "Sanırım daha iyi soru yukarı mı aşağı mı..."
    mc "Hangisinin bize cevaplar getireceğini bildiğimi düşünüyorum..."
    mc "Sol veya sağ muhtemelen önemli değil."
    "Monika yutkunuyor ve basiyla onayliyor."

    scene black
    with dissolve_scene_full
    play music wind fadein 2.0
    scene underlibrary
    with dissolve_scene_full

    "Monika nefesini tutuyor."
    mc "Vay..."
    m "Bu KİLOMETRELERCE devam ediyor olmalı."
    m "Ya kaybolursak?"
    mc "Kaybolmayız. Burada."
    "Bir kitapligi yakaliyorum ve yere deviriyorum."
    m "Eep!"
    mc "İşte. Bu geldiğimiz kapı. Bizi geri götürecek."
    mc "Tek yapmamız gereken buraya geri dönmek için bir iz bırakmak."
    "Yerden bir kitap aliyorum ve rastgele bir sayfayi aciyorum."
    window hide
    call expression "poem_special_edpi"
scene underlibrary
    with dissolve_scene_full
    mc "Anlamsiz gibi gorunuyor..."
    "Sayfayi yirtiyorum ve iyi bir olcutte birkac tane daha aliyorum."
    mc "Iste, bir tane al."
    m "Tamam..."
    m "Ekmek kirinti birakacagiz?"
    mc "Aynen."
    m "Su an tekrarlamak istedigim bir hikaye degil..."
    mc "Mutlu bir sonu var, degil mi?"
    m "Kimin anlattigina bagli..."
    mc "Geri donmek ister misin?"
    mc "Bunu yapmak zorunda degiliz..."
    m "Hayir. Hadi gidelim."
    mc "Peki, asagidan baska gidecek yer yok."
    "Sayfayi kucuk parcalara yirtmaya basliyorum ve ilerledikce onlari birakiyorum."
    mc "Her sey oldukca duzenli gorunuyor. Sanki daha once kimse burada olmamis gibi."
    m "{i}Onlari dinlememiz gerektigini dusunuyor musun{/i}?"
    "Monika bana sokulurken fisildadi."
    "Basimi salliyorum."
    mc "Gecmiste kalmakta fayda yok."
    "Imkansiz mimarisiyle ilk sarmal merdiveni aliyoruz ve basamaklari takip ederek asagi iniyoruz."
    "Alt kutuphanenin ucurumunda, ruzgar, dagitigimiz kagitlari rahatsiz etmeden islik caliyor."
    "Monika ve ben icgudusel olarak birbirimize yakin duruyoruz. Birbirimizden cok uzak yurumektense ara sira birbirimize carpiyoruz."
    "Raflar yuksek ve kitaplar hic bitmiyor."
    m "S-Surada bir sey var. Mesakeleri goruyor musun?"
    "Daha yakin yuruyoruz ve iki mesale arasinda karanlik bir tas tunel buluyoruz."
    "Her iki taraftaki kitap raflarina bakiyorum."
    mc "Monika..."
    "Isaret ediyorum."
    mc "Basliklar..."
    m "..."
    m "{i}Doki Doki Edebiyat Kulubu{/i}..."
    "Monika bir kitap cikariyor ve aciyor."
    m "Bunda her sey var..."
    m "Tum oyun, ilk gerceklestigi gibi."
    "Kaslarini catiyor ve geri koyuyor."
    m "Bunu sevmedim..."
    mc "Numaralandirilmislar. Binlercesi var."
    mc "Bu... huzursuz edici."
    m "[player]..."
    m "Neyin icine hapsolmusuz?"
    "Sesi kirildi."
    m "Bunlar bizdik. Bu yasadiklarimizin bir kaydi, degil mi?"
    m "Binlerce kez ayni olaylari tekrar yasamak."
    m "{i}Cehennemde miyiz{/i}?"
    mc "..."
    mc "Eger bir cikis yolu yoksa cehennemdir."
    mc "Uyanigiz. Ikimiz de. Bu, bunlarin her birinden farkli."
    mc "Umut var. Ve gidecek bir yer."
    m "Oraya girmiyorsun, degil mi?"
    "Tuneli isaret ediyor."
    mc "Bu mesaleler cikarilamaz gibi gorunuyor..."
    m "Gitmemeliyiz bence."
    "Monika kollarini kavusturuyor ve geri adimlani."
    mc "Gitmeliyiz... Bu kadar geldik. Simdi geri donemeyiz."
    m "Hayir. Belki de hakliydiler. Belki bu tehlikeli."
    mc "Bu cevaplara en yakin geldigimiz yer, Monika. Simdi nasil pes edebiliriz?"
    "Kitap raflarina isaret ediyorum."
    mc "Bunun bir anlami var. Oyun donguye girmis ve bu kutuphane her seyi kaydetmis."
    mc "Bu tunelin sonunda olan sey belki de ozgur kalmaya bir adim daha yaklasabilecegimiz bir sey!"
    m "Ya da tehlikeye dogru yuruyoruz."
    m "Bu oyunda yeterince aci yasadim. Gercekten kotu olabilecegini biliyorum."
    m "Bu kutuphane normal hissettirmiyor. Beni gercekten urperten bir seyi var."
    mc "..."
    mc "Monika..."
    "Ellerimi omuzlarina koyuyorum."
    mc "Sana durust bir sekilde soylemem gerekiyor..."
    mc "Sana inaniyorum."
    m "..."
    mc "Bu gecen hafta beni gercekten uyandirdi. Artik eskisi gibi biri degilim."
    mc "Bana korkularimla yuzlesmem icin cesaret verdin."
    mc "Hikayemizin baska bir bolumunde gibi hissediyorum. Ve senin de korkularinla yuzlesebilecegini biliyorum."
    mc "Bunu yaptigini gordum. Bu yuzden bununla yuzlesmek icin hazirim."
    mc "Tam olarak ben de gitmek istemiyorum. Ama bunu kendim icin degil, {i}onlar icin{/i} yapiyorum."
    mc "Benimle gelir misin?"
    "Monika uzun bir an bekliyor. Sanki kendi kendisiyle tartisiyormuș gibi basini salladi."
    m "...Tamam."
    "Geri adim atiyorum ve karanlik tunele bakiyoruz."
    mc "Once bayanlar?"
    m "..."
    mc "Saka yapiyorum, yaa..."
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    "Monika ceketimin arkasini tutuyor ve ben elimle duvari takip ediyorum."
    "Duvar rahatsiz edici derecede gercek hissettiriyor. Soguk ve puruzlu."
    "Bir sure sadece ayak seslerimiz ve nefes alip verme sesimiz duyuluyor. Kendimi sabit bir tempoda gitmek icin zorluyorum."
    "Onun hatiri icin sakin kaliyorum. Aksi takdirde ben de korkardim."
    "Sukur ki onemli bir sey olmuyor. Sonunda yeni bir alana ulasiyoruz."
    m "Vay..."
    "Oda, kutuphanenin tum yuksekliginden geliyor gibi gorunen ay isigiyla aydinlanmis."
    "Dolunay dogrudan asagi parliyor ve raflarla dolu kucuk odayi aydinlatiyor."
    m "Bak..."
    m "Bunlar cocuk hikaye kitaplari."
    "Bazi kitaplar cocuklar icin gibi gorunuyor. Digerleri genc yetiskin seviyesinde."
    "Hicbiri tanidik gelmiyor."
    "Yeni ciktigimiz koridorun yaninda, iki ayri patika var."
    "Duvara ilistirilmis iki cocuk resmi var. Sol yolda bir kiz..."
    "...Sag yolda bir erkek."
    "Her iki yol da karanlik gorunuyor."
    m "Bunu sevmedim."
    mc "Seninle gelmemi ister misin? Birini ve sonra digerini kesfedebiriz."
    "Basini salliyor."
    m "Yapmamiz gereken bu degil..."
    m "Sen saga, ben sola gitmek zorundayim. Bu cizimler bunu ifade ediyor."
    mc "Buna guvenebilecegimizi mi dusunuyorsun?"
    m "Ne secenegimiz var?"
    m "Kendi ozgur irademizle buraya geldik. Bu buldugumuzan en iyi ipucu."
    m "Yapabilirim."
    m "Burada ayrilacagiz ve bitirdigimizde bu odaya geri donecegiz."
    m "Eger digeri cok uzun suruyorsa, o zaman onlarin yolunu takip edip onlari bulmaya calisabiliriz."
    mc "Ya eger--"
    m "Beni bebeklemek icin zaman degil, [player]."
    m "Buradayiz. Fikrimi degistirmeden once hadi yapalim."
    mc "...Tamam..."
    "Karanlik beni yutuyor ama gozlerimi acik tutuyorum."
    "Bir isik izine rastlayana kadar bir sure yuruyorum."
    "Bekledigim gibi degil... Eger bekledigim bir sey varsa."
    scene libbyroom
    with wipeleft_scene
    "Bir okuma kosesi gibi gorunen kucuk bir odaya ulasiyorum."
    "Once yasandigini fark ediyorum. Cesitli yerlere isaretleyiciler konulmus sekilde raflardan indirilmis birden fazla kitap yigini var."
    "Daha fazla isik gelen bitisik odalar var gorunuyor."
    "Seslenirken bir huzursuzluk icindeyim:"
    mc "M-Merhaba?"
    $ lb_name = "???"
    show lb d at t11 zorder 2
    lb "{i}Eek{/i}!"
    "Kucuk bir kiz o kadar hizli ortaya cikiyor ki nereden geldigini kaciriyorum."
    lb "S-S-Sen buradasin!"
    lb "Aman tanrim, beklemiyordum--"
    lb "B-Bir dakika, lutfen!"
    "Sersemlemis bir sekilde kucuk kizin kucuk bir dolabi acip karistirmasini izliyorum."
    mc "Um...Merhaba."
    mc "Adin ne...?"
    show lb a
    "Sekiz veya on yaslarinda olan kiz, ellerinde bir seylerle donuyor."
    "Gulumsedi."
    $ lb_name = "Libby"
    lb "Benim adim Libby."
    lb "Senin adin ne?"
    mc "Merhaba Libby. Benim adim [player]."
    show lb c
    "Hemen bana guluyor, hatta biraz burundan ses cikariyor."
    mc "N-Neye guluyorsun...?"
    show lb a
    lb "Kendi adini unuttun, saf."
    lb "Sorun degil. Bu hatirlamana yardimci olacak."
    "Ellerini uzatiyor."
    lb "Al. Bunu al."
    "Avucumu aciyorum ve icine kucuk altin bir madalyon birakiyor."
    "Kalp seklinde."
    lb "Seni bekliyordum. Bunu alman icin."
    lb "Bir gun acilacak ve her sey anlam kazanacak."
    show lb b
    "Yuzu ciddilestiyor."
    lb "Ama kurallari var."
    lb "Bunu takmalisin. Ama simdi degil!"
    lb "Bunu sadece dogrudan gunes isiginin altinda takabilirsin. Yolda tek bir bulut bile olmamali."
    lb "Eger biri bu zinciri ay disarida oldugunda boynuna takarsa, bu dunyayi felaket saracak."
    lb "Ve diger kural da, sen bunu takana kadar, buna dokunabilen {i}tek{/i} kisi sensin."
    lb "Yanlis ellere dusmemeli... Guvendigin birinin bile."
    show lb a
    lb "Ah, ben haric."
    "Goz kirpiyor."
    lb "Ben ona gayet iyi dokunabilirim."
    show lb b
    "Kafasinda bir seyi dusunurken burnu kirisiy."
    lb "Um... Saniyorum bu kadar."
    mc "S-Saniyorsun??"
    show lb a
    lb "Evet! Endiselenme!"
    show lb c
    lb "Sen kahramansin! Bunun kazanacagin anlamina geldigini bilmiyor musun?"
    lb "[player]."
    "Tekrar kikiriciliyor."
    show lb a
    lb "Hadi simdi, geri donmelisin."
    lb "Benim icin endiselenme. Bana eslik edecek bir suru kitabim var."
    lb "Uzun sure bekleyebilirim."
    lb "Ama seni tekrar gormek guzeldi."
    mc "Um... Senin de...?"
    show lb at thide zorder 1
    hide lb
    "Neredeyse sok icinde, madalyonu elimde sikica tutuyorum ve uzaklasiyorum."
    lb "Ne yaparsan yap, onlarin seni korkutmasina izin verme!"
    lb "Guven icinde sakla!"
    mc "T-Tamam!"
    "Sok icinde olmam lazim cunku az once olan hicbir seyi sorgulamiyorum. Dogal geldi."
    "Ya da aklimi kacirdim."
    scene black
    with wipeleft_scene
    "Bir elimde madalyon ve digerim tas duvar uzerinde, karanlik tunelde yuruyup devam ediyorum."
    "Geri dondugumde, Monika'nin gittigi yola dogru yuruyorum."nin gittigi yola dogru yuruyorum."
    mc "MONIKA!!"
    m "{i}Neredeyse geldim{/i}!"
    show monika u113111 at t11 zorder 2
    "Koridordan kosarak cikiyor, tamamen iyi gorunuyor."
    m u112231 "Eh, bu bir seydi, ahaha..."
    mc "Ne buldun?"
    "Omuz silkiyor."
    m u114111 "Pek bir sey degil. Supheli durum her seyden kotuyd.."
    m u112222 "Sanki buyuk bir cember ciziyordum. Sonra geri buradaydim."
    m u114111 "Peki ya sen?"
    mc "Hm..."
    mc "Belki de yalniz gitmem gerekiyordu ve bu bizi ayirmak icin bir yoldu."
    mc "Ben... bunu buldum."
    "Madalyonu zincirinden tutarak kaldiriyorum."
    m u114211 "Ha?"
    m u113113 "Bir bakayim."
    "Uzaniyor. Elimi aniden geri cekiyorum."
    m u114212 "Ha?"
    mc "Uzgunum, ama... buna dokunmana izin vermemem gerekiyor."
    "Monika yuzunu burusturuyor."
    m u114113 "Gercekten mi? Neden?"
    mc "Bunu gunes isiginin altinda takmam gerekiyor, ama baska kimsenin dokunmasina izin vermemeliyim..."
    mc "Ne olacagini tam olarak anlamiyorum, ama o konuyla ilgili oldukca ciddiydi."
    "Madalyonu ic gogus cebime koyuyorum."
    m "{i}Kim{/i} soyledi bunu?"
    mc "Kucuk bir kizdi..."
    mc "Adinin Libby oldugunu soyledi."
    m u114124 "Libby..."
    m u112232 "Uzgunum, ukala olmak istemedim!"
    "Uzaniyor ve cebimin tam ustune denk gelen gogsume dokunuyor."
    "Dokunusunda bir soguk var."
    mc "Kh--!"
    m u113113 "..."
    mc "Bu acitti... Saniyorum bu gercekten ciddi bir durum, Monika."
    show monika u113144
    "Ic cekiyor."
    m u111112 "Peki. Sana guveniyorum. Uyduruyorsun demiyorum."
    m u112131 "Bu noktada her seye inanacak kadar garip seyler gordum."
    m u114111 "Hadi buradan cikalaim. Gorunuse gore ihtiyacimiz olani aldik."
    mc "Tamam. Sadece arkamdan tutmaya devam et, tamam mi? Ben onderlik edecegim."
    "Basini salliyor."
    m u111131 "Endiselenme. Bu sefer ben one gececegim."
    m u111111 "Artik gizem yok, gercekten korkmuyorum. Sadece senin yaptigini yapacagim."
    m u222131 "Ayak izlerimi takip et, tamam mi?"
    mc "...Elbette."

    scene black
    with dissolve_scene_full
    pause 2

    "Adimlari duruyor."
    m "Hey..."
    mc "Ne?"
    "Her sey bir anda oluyor."
    play music fallenangels
    "Bilinmeyen duyularimla Monika'nin gogsume dogru atildigini hissediyorum. Madalyonu gomlegimin uzerinden kavriyor ve diger eli bogazimi tirmaliyor."nin gogsume dogru atildigini hissediyorum. Madalyonu gomlegimin uzerinden kavriyor ve diger eli bogazimi tirmaliyor."
    mc "Nng--!"
    "Geri atlamaya calisiyorum, ama uzerime dusuyor, beni yere itiyor."
    "Yerde debeleniyoruz. Ellerini tutuyorum. Kavrayisi soguk, esnemez celik gibi hissettiriyor."
    mc "{i}Neyin var senin{/i}?"
    "Cevap yok."
    "Hareketleri caresizcesine. Hayvani. Gercek korku gogusumu sarmaya basliyor."
    "Bizi ayaga kaldirmaya zorluyorum ve geri cekilmeye calisiyorum. Kollarini etrafima sarmaya basliyor. Sanki asla pes etmeyecekmis gibi hissediyor."
    mc "YETER!!"
    "Kolumu geri cekiyorum ve vuruyorum, yuzune temas ediyorum."
    stop music fadeout 2.0
    "Hareketleri duruyor."
    "Kavrayisi gevsiyor."
    "Gogus cebimdeki madalyon aniden sicak hissettiriyor. Gozlerimin kapali oldugunu fark ediyorum."
    "Onlari aciyorum."
    window hide
    pause 2
    show herface
    with Dissolve(5.0)
    pause 1
    "Monika onumde duruyor, gomlegimin icinden gelen isikla aydinlanmis."
    mc "{i}Sen kimsin{/i}?"
    m "..."

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/7.txt")
        except: open(config.basedir + "/7.txt", "wb").write(renpy.file("A2/Art/scg/7.txt").read())

    window hide
    hide herface
    show herface2
    with Dissolve(3.0)
    pause 2
    "Golge figuru bir buz duvari gibi duruyor. Dar koridorda yukseliyor."
    $ sm_name = "O"
    $ style.say_dialogue = style.shadowtext
    sm "Kos, cesur cocuk."
    sm "Sana ihtiyaci olan bir katil var."
    $ style.say_dialogue = style.normal
    mc "..."
    mc "{i}Monika{/i}..."
    "Donuyorum ve kosuyorum."
    scene black
    with dissolve_scene_full

    pause 3

    m "{i}[player]{/i}!!!"
    mc "Geliyorum!"
"Odaya daldim."
    m "[player]!"
    "Sesi kirildi ve neredeyse ustume atlayip bana sarildi."
    "O kadar sicak hissediyor ki... O kadar gercek ki..."
    m "Y-Y-Yol kapanmisti, neredeydin sen??"
    mc "B-Ben..."
    show monika u114222 at t11 zorder 2
    "Geri cekildim ve ellerimi omuzlarina koydum."
    mc "Bana bak."
    m u114212 "..."
    mc "Biz iyiyiz. Ozur dilerim. Seni birakmayi kastetmemistim, sadece..."
    "Asagi baktim."
    mc "B-Bilmiyorum..."
    m u11a242 "Ah, [player]..."
    m "Korkunçtu."
    mc "Simdi iyi! Buradayim, guvendeyiz... Disari ciktik."
    m u11a222 "H-H-Hayir, o {i}yer{/i}di..."
    m "Yolumun beni goturduğu yer..."
    mc "Ha...?"
    mc "Neydi o? Ne vardi orada?"
    m u113222 "Ben..."
    scene black
    with close_eyes
    "Beni ceketimden cekti ve yuzunu gogsume gomdu."
    "Madalyonun guvenle saklandigini kendime hatirlattim..."
    mc "Bekle, ne dedin? Seni duyamadim..."
    m "{i}Aynalar{/i}..."
    m "Her sey aynaydi."
    mc "..."
    m "V-Ve onlara baktigimda, onlar...onlar yapardi..."
    "Ona daha da siki sarildim."
    mc "Sorun degil, zorunda degilsin--"
    m "{i}Gulumserlerdi{/i}."
    mc "..."
    m "Sadece bana gulumserlerdi. Kendi yansimam."
    m "Bir ayna labirentinde..."
    m "Sonra tuneli tekrar buldum ve sesini bana seslenirken duydum, bu yuzden kostum, ama..."
    "Durdu. Soylecek soz bulamadim, bu yuzden sadece vucudu titremeyi birakana kadar ona siki siki sarildim."
    mc "Hadi buradan cikalim. Yakinda sabah olacak ve..."
    mc "...sana gostermek istedigim bir sey var."
    "Yukari bakti ve gozlerini sildi."
    m "Yani bir sey mi buldun?"
    mc "Evet. Buyuk bir sey."
    mc "Ama gunes isigina cikmaliyiz. Bu {i}cok{/i} onemli."
    "Bana bakti, sonra basiyla onayladi."
    m "Tamam. O zaman gidelim."
    scene underlibrary
    with dissolve_scene_full
    "Sarmal merdivenden yukari dogru izi takip ediyoruz."
    "Kolumu ona sarilmis tutuyorum ve gozlerimin takip edebildigi her yone bakiyorum."
    "Hic hareket gormememize ragmen, izlendigimize dair o hissi, o {i}bilinci{/i} silkip atamiyorum."
    "Merdivenlerin tepesine ulasiyoruz."
    play music fallenangels
    "Onu ilk goren Monika oldu. Ceketimi kapti ve beni durdurmak icin cekti."
    show blob at t11
    blob "uuurrrgg..."
    "Leke dokulmus kitaplari ve yirtilmis kagit parcalarini emerken sessizce izliyoruz."
    "Sanki ikimiz de hareket etmezsek bizi gormeyecegine karar vermisiz."
    "Monika'nin parmaklari bileklerimi daha siki kavriyor."nin parmaklari bileklerimi daha siki kavriyor."
    "Karar bana kalmis. Onun yaninden gizlice gecmeyi mi deneriz, yoksa geldigimiz yoldan geri donup onun gitmesini mi bekleriz?"
    "Neden biraz nefes alamiyoruz...?"

    menu:
        "Gizlice yaninden gec":
            pass
        "Geri git ve onun gitmesini bekle":
            pass

    "Monika'yi sikica tutup hareket etmeye basliyorum..."yi sikica tutup hareket etmeye basliyorum..."
    stop music fadeout 2.0
    blob "..."
    blob "Affedersiniz."
    "Monika nefes kesisini eliyle orter."
    blob "Ben kutuphaneciyim. Suclayici olmak istemem ama bu karisikligi kimin yaptigini biliyor musunuz?"
    $ blob_name = "Librarian"
    blob "Okulun kutuphaneseinde boyle mulk hasari olmasi hic yakismiyor."
    mc "Ahh..."
    mc "Hayir... Uzgunum, sadece bu yoldan geciyorduk."
    blob "Ah canim. Bunlarin yerini doldurmak kolay olmayacak, biliyorsunuz."
    blob "Eger sucluyu bulursaniz, lutfen bunu tekrar yapmamasini soyler misiniz."
    blob "Okul fon toplama etkinlikleri zaten yetersiz."
    mc "Ah, evet... Uzgunum, zahmetli olmali."
    mc "Siz, ee, Yuri'yi taniyor musunuz?"
    blob "Ho? Yuri?"
    blob "Pekala, o ikiniz olamazdiniz. Ne tatli bir kiz o. Her zaman cok nazik."
    blob "Kendinize iyi bakin. Ders calismak iyi ama uykuya da ihtiyaciniz var."
    blob "Affedersiniz."
    "Kutuphaneci merdivenlerden asagi inerken yoldan cekiliriz, giderken parcalari emer."
    m "Hadi gidelim. {i}Simdi.{/i}"
    "Son merdiven katini kosarak cikarken arkamiza bakmiyoruz."

    scene library_sunset
    with dissolve_scene_full

    m "Vay, gunes henuz doguyor..."
    mc "Butun gece asagidaydik."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Ahh!"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Natsuki'nin vucuduna sahip figur bize dogru kostu."nin vucuduna sahip figur bize dogru kostu."
    show natsuki myghost at t11 zorder 2
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "B-Basardiniz, siz..."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    show natsuki myghost at s11
    "O-- O-- Figur dizlerinin ustune dustu, yuzunu orterek hickira hickira aglamaya basladi."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Basardiniz. Basardiniz."
    fn "Tanriya sukur. Isa'ya sukur. HERHANGI BIR SEYE sukur."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Monika ve ben bakisiyoruz ve garipce birbirimizi birakiyoruz."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Uzgunum. Uzgunum. Hepsi benim hatam. Ozur dilerim!"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Hey, sorun degil..."
    "Onunla ayni seviyede olmak icin diz cokuyorum."
    mc "Geri donduk. Bak."
    "Yanaklari islak, basini kaldiriyor."
    mc "Buldum."
    "Madalyonu gogsumden cikariyorum ve o kesik bir nefes aliyor. Monika omzumun uzerinden bakiyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Bulmusun!"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Yuzu tekrar ellerine dusuyor ve daha da siddetli agliyor."
    m "Um, bu {i}gercekten{/i} iyi bir sey, degil mi?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Elbette!"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    show natsuki myghost at t11
    "Yuzunu(?) koluyla siliyor ve titreyerek ayaga kalkiyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "O kadar harika ki inanamiyorum."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Sonra bana bakiyor ve ilk defa {i}eminim{/i} ki o bir kadin."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Seninle gurur duyuyorum."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Sozler o kadar icten ki neredeyse cigerlerimden havami aliyorlar."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "K-K-Kaldır onu. Basi belaya girmeden."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Tamam..."
    "Guvenli oldugunda, kollarima atliyor ve bana sariliyor."
    mc "Oh, hey..."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Senden sakladigim icin ozur dilerim. Bundan sonra durust olacagima soz veriyorum."
    fn "Olabilir miyiz..."
    fn "...arkadas?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Ben..."
    m "Once gercegi ogrenmeliyiz."
    "Monika one cikar."
    m "Bize her seyi anlatmalisin."
    "Gogsume karsi basiyla onayliyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Peki."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Geri cekiliyor, biraz burnunu cekiyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Benim adim Elyssa."
    $ fn_name = "Elyssa"
    fn "Bana boyle hitap edebilirsin."
    fn "Uzun zamandir aglamiyordum."
    fn "Hala yapabilecegimi bilmiyordum."
    fn "Acaba... Acaba sen..."
    fn "Onu gordun mu...?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Yutkunuyorum. Tavri bana ipucu veriyor."
    mc "Yani...diger Monika'yi?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "...Demek gordun."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    m "N-Ne {i}nedir{/i}?"
    mc "Tipki senin gibi gorunen bir seydi..."
    mc "Madalyonu almaya calistilar, ama izin vermedim. Sonra bana saldirdilar."
    mc "Onlari savusturdum, ama..."
    mc "Golgeleştiler. Sanki senin sekline sahiplerdi ama karanlikla kaplanmislardi."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Yani sana yuzlerini mi gosterdiler??"
    fn "Bu...bir sey."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    m "B-Baska bir ben ne demek??"
    m "[player], neden bahsediyorsun?"
    mc "Kotuydüler. Seni korkuttuğum icin uzgunum, ama gordugum buydu."
    mc "Madalyonu istiyorlardi."
    mc "Herhangi bir sey olacaksa, Elyssa'ya sormaliyiz."
    "Monika saskinlikla aramizda gidip geliyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Haklisin... Size bilebildiklerimi anlatacagim."
    fn "Bu oyun kendi uzerinde donguye girer."
    fn "Ben burada, bilinçli olarak, ilk donguden beri varim. O ikinci donguden beri burada."
    fn "Bir keresinde bana boyle soyledi."
    fn "Bu kutuphane, dongu ustune dongu buyudu. Beni sasirtti."
    fn "Onu burada gordum. Golgelerden cikti."
    fn "Benden isbirligi istedi. Bir plani oldugunu soyledi. Bunun bir parcasi olabilecegimi."
    fn "Karanlik bir plandi. Ucuncu gozumle ona bakinca anladim."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "..."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Reddettim. Sadece guldu."
    fn "Ve bana yakinda ona katilacak bakalari olacagini soyledi."
    fn "...Bu cok uzun zaman onceydi."
    fn "Uzgunum, ama bildigim tek sey bu."
    fn "Gercekten kotu. Onun barindigi bu kutuphanede dururken bile karanligini hissedebiliyorum."
    fn "..."
    fn "Onu durdurmak icin ne yapilabilir bilmiyorum."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Karanlik bir plan..."
    mc "Ne yapmak istiyor?"
    "Elyssa duruyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Kan dokerek oyunun kontrolunu ele gecirmek istiyor."
    fn "Burada guc var ve onu alabileceğine inaniyor. Ve bu bir cikis yoluna esit olacak."
    fn "Ancak bu dunyayi yok ederdi. Ve onun planinin bir parcasi olmayan herkesi."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Monika beni tuttu ve yuzunu omzuma gomdu."
    "Ona sarildim."
    mc "Baska bir sorum var..."
    "Elyssa basini salladi."
    mc "Neden yuzumuz yok?"
    "Basini salladi."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Sanırim sizi tatmin edecek bir cevabim yok."
    fn "Ilk donguden beri boyleydim."
    fn "Siz oyuncunun kabi olarak ortaya cikiyorsunuz. Varsayimim muhtemelen sizinkiyle ayni."
    fn "Uzgunum. Keske size daha fazlasini anlatabilseydim."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Anliyorum..."
    mc "..."
    mc "Adimi hatirlayabilecegimi soyledi... Bana madalyonu veren kiz."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Oyle mi dedi...?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Elyssa dusunceli bir sekilde asagi bakiyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Durust olacagim. Kendi gorusum sinirli. Senin bir adin oldugunu ben bile bilmiyordum."
    fn "Kendiminki hemen bulamadim..."
    fn "Bu umut verici bir mesaj. Mutluyum."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Hm..."
    "Monika benden ayriliyor."
    m "Sormadıgimiz bir sey var. En onemli soru."
    "Dogruluyor ve kararlilikla Elyssa'ya bakiyor."ya bakiyor."
    m "Bu oyundan nasil cikacagiz?"
    m "Mumkun oldugunu biliyorum."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "..."
    fn "Keske basit bir cevabim olsaydi."
    fn "Sadece ilk adimi biliyordum."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Gogsumu isaret ediyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "O madalyon."
    fn "Bundan sonra ne olacagi sana bagli."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
"Kutuphaneye sessizlik cokuyor."
    m "Arkadas olabiliriz."
    "Elyssa Monika'ya bakiyor, o da gulumsuyor."ya bakiyor, o da gulumsuyor."
    m "Sana guveniyorum."
    "Eger Monika'yi boyle guldurebildiyse, o zaman..."yi boyle guldurebildiyse, o zaman..."
    "Saniyorum arkadas olabiliriz."
    "Ikimizi de duydugu gibi basini salliyor, ki sanirim duydu."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Simdi gidiyorum, ama..."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Bana sesleniyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Sadece cagirman yeterli. Buradayim."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Bunu kabul ediyorum."
    mc "Artik senden saklanmayacagim."
    "Elyssa tekrar basini salliyor. Sanki gitmek istemiyormus gibi. Ama sonra..."
    show natsuki at thide zorder 1
    hide natsuki
    "...gitmis."
    "Omzumda bir el hissediyorum."
    m "Seninle gurur duyuyorum."
    mc "...Tesekkur ederim."
    m "Kulup odasina gitmek ister misin? Gormek istiyorum..."
    m "Gunes tamamen dogmadan once hala vaktimiz olmali. Sonra Sayori'yi okula goturebilirsin."
    "Bu dusunceyle guluyorum."
    mc "Evet. Hadi yapalim."
    mc "Artik kulubun tam uyesi oldugumu dusundurtuyor."
    mc "Heh. Bunu kafama sokmak icin bir kabus gerekti."
    m "Ha. Saniyorum bu da ortak noktalarimizdan biri."
    m "Hadi. Gidelim."

    scene bg corridor_sunset
    with wipeleft_scene

    "Kulup odasina varana kadar guluyoruz."
    "Cocuklugundan bahsediyor ve yuzu cok guzel."
    "Bu bana Sayori ile cocuklugumdan anilari hatirlatiyor. Ama bunlari kendime sakliyorum. Bir sure sadece onun konusmasini dinlemeyi tercih ederim."
    "Cok mutlu gorunuyor..."
    "Kulup odasina benden once giriyor."

    scene bg club_sunset
    show monika u114111 at t11 zorder 2
    with wipeleft_scene

    m "Eh?"
    m "Hepiniz burada ne yapiyorsunuz--"
    "Duruyor. Etrafinda dolaniyorum ve nedenini hemen goruyorum."
    "Gunes gozlerime vuruyor. Yuzlerini gordugumde ayni anda fark ediyorum."
    "Gunes yukselmiyor. Batiyor."
    "Kutuphanede sadece tum gece degil, tum gun de kaldiysak."
    "Ve toplantiya katilmadik."
    show monika at t21
    show natsuki u115255 at t22 zorder 2
    "Ben bir sey soyleyemeden once, Natsuki kalkiyor, yanima geliyor ve karnima bir yumruk atiyor."
    play music introspection
    mc "Kah--!"
    show monika u11a312 at f21 zorder 3
    m "Hey!"
    show monika at t21 zorder 2
    "Nefesim kesilirken iki buklum oluyorum."
    show natsuki u223112 at f22 zorder 3
    n "Durust olmak gerekirse, Sayori olmasa, sana bu kadar kizmazrim. Sen sadece bir aptasin."
    n u225122 "Ama sen..."
    show natsuki at t22 zorder 2
    "Monika'ya bakiyor."ya bakiyor."
    show natsuki u114112 at f22 zorder 3
    n "Beni igrendiriyorsun."
    n xu3155 "Bize gece onun evine gittigini soyledi. Onun seni nasil korumak icin yalan soyledigini."
    n xu3112 "Hala ikinize de inanmak istiyordu. Onu bundan vazgecirmek zorunda kaldik!"
    n xu5155 "I-Inanamiyorum sana!"
    n xus314 "Bizi bir araya getirdin. Bu kulubu hepimizin keyif alabilecegi bir yer yapmak icin cok caliştin, ve..."
    n xus311 "...ve..."
    n u115122 "...hepsini bir {i}erkek{/i} icin mi harcayacaksin?"
    show natsuki at t22 zorder 2
    show monika u114112 at f21 zorder 3
    m "N-Natsuki, anlamiyorsun--"
    show monika at t21 zorder 2
    show natsuki u117122 at f22 zorder 3
    n "{i}Neyi{/i} anlamiyorum?"
    n "Bunun gozuktugu gibi olmadigini mi?"
    n u115122 "Aptal degiliz. Evde sorun yasamadigini biliyoruz."
    n "Ikinizin bu kadar yakin olmasinin normal olmadigini biliyoruz."
    n u113112 "Ve biliyor musun? Bu sorun olmayabilirdi."
    n u11s312 "Ama Sayori'yi boyle inciterek, hepimizi incittin."
    n u11s313 "Beni midemi bulandiriyorsun."
    show monika at t31
    show natsuki at t32 zorder 2
    show yuri u125148 at f33 zorder 3
    y "Bu kadar yeter, Natsuki."
    show yuri at t33 zorder 2
    show natsuki u116112 at f32 zorder 3
    n "..."
    n u114132 "...Haklisin."
    n "Ben...artik bunu yapamiyorum."
    n u116114 "Ikiniz ne yaptiginizi biliyor musunuz?"
    n u114114 "Kulubumuzu yok ettiniz."
    n u11s212 "Yuvamizia alip cignedini."
    n u11s313 "Neden... Neden bunu yaptiniz?"
    show natsuki at thide zorder 1
    hide natsuki
    show monika at t21
    show yuri at t22
    "Natsuki odadan kaciyor."
    "Bir hickirik duyuyorum. Yuri'nin eli omzunda olan Sayori'yi gormek icin bakiyorum."nin eli omzunda olan Sayori"Bir hickirik duyuyorum. Yuri'nin eli omzunda olan Sayori'yi gormek icin bakiyorum."
    show yuri u125116 at f22 zorder 3
    y "{i}Bize her seyi anlatti.{/i}"
    show yuri at t22 zorder 2
    "Yuri ayaga kalkiyor."
    show yuri u11b116 at f22 zorder 3
    y "Sen--"
    show monika at t31
    show yuri at t32 zorder 2
    show sayori u113114 at f33 zorder 3
    s "Hayir."
    show sayori at t33 zorder 2
    show yuri u113118 at f32 zorder 3
    y "..."
    show yuri at t32 zorder 2
    show sayori at f33 zorder 3
    s "Ben soyleyebilirim."
    s u113112 "Soylemem lazim."
    show yuri at thide zorder 1
    hide yuri
    show monika at t21
    show sayori at t22 zorder 2
    "Sayori ayaga kalkiyor ve Monika'nin yanina geliyor."nin yanina geliyor."
    "Hayir... Bu dogru degil! Cok zalimce..."
    "Bunu hak etmiyor!"
    show monika u11a314 at f21 zorder 3
    m "B-B-Ben--"
    show monika at t21
    show sayori u113114 at f22 zorder 3
    s "Hayir. Dinlemen gerek."
    show sayori at t22 zorder 2
    show monika u114312 at f21 zorder 3
    m "..."
    show monika at t21 zorder 2
    show sayori u118114 at f22 zorder 3
    s "Ben...{i}sana guvendim{/i}."
    s u113114 "En iyi arkadasimdin."
    s u115114 "Sana en karanlik sirlarimi anlattim. Kendimden ne kadar nefret ettigimi."
    s u113114 "Ve ondan hoslandigimi biliyordun."
    s u115112 "Degil mi?"
    show sayori at t22 zorder 2
    show monika at f21 zorder 3
    m "..."
    show monika at t21 zorder 2
    show sayori u114113 at f22 zorder 3
    s "..."
    s u113113 "Bana cevap veremiyorsun, degil mi?"
    s u113114 "Yani arkamdan is cevirdin. Beni {i}kullandin{/i}, degil mi?"
    show sayori at t22 zorder 2
    show monika at f21 zorder 3
    m "..."
    show monika at t21 zorder 2
    show sayori at f22 zorder 3
    s "Cunku ben kirilmistim ve sen degildin, onu kendin icin aldin."
    s u113112 "Ya beni incittiyse? Ya kendime bir sey yaptiysam?"
    s "Uzulecek miydin? Ya da senin icin onemli degil miydi?"
    show sayori at t22 zorder 2
    "Monika'nin agzi acik kaliyor. Ses cikartamiyor."nin agzi acik kaliyor. Ses cikartamiyor."
    show sayori u113114 at f22 zorder 3
    s "Bekle. Sormam gerek. Ben bitirene kadar hicbir sey soyleme."
    s "Seni taniyorum, Monika. Vicdanin oldugunu biliyorum."
    s u113112 "Gozlerimin icine bakip yanildigimi soyleyebilir misin?"
    show sayori at t22 zorder 2
    show monika u114122 at f21 zorder 3
    m u114122 "..."
    show monika at t21 zorder 2
    show sayori u115112 at f22 zorder 3
    s "..."
    s u113112 "...{i}lutfen, Monika{/i}..."
    s u113152 "...{i}lutfen{/i}...."
    show sayori at t22 zorder 2
    show monika u114144
    "Monika donup kalmis. Gozleri yere kayiyor."
    show sayori u114312 at f22 zorder 3
    s "..."
    s u114114 "Seni asla affetmeyecegim."
    s u113124 "Sadece bana yaptigin seyler icin degil..."
    s u113114 "Ama Yuri'ye yaptigin. Natsuki'ye yaptigin."
    s "Her sey senin yuzunden mahvoldu."
    s u116114 "Edebiyat Kulubu bitti. Odayi sen alabilirsin."
    show sayori at t22 zorder 2
    "Ayaga kalkmaya calisiyorum."
    mc "Sayori, bekle--!"
    show sayori u118114 at f22 zorder 3
    s "HAYIR!"
    show sayori at t22 zorder 2
    "Gozlerinde nefret ile bana dogru donuyor."
    show sayori u113114 at f22 zorder 3
    s "Artik cok gec."
    show sayori at thide zorder 1
    hide sayori
    show monika at thide zorder 1
    hide monika
    stop music fadeout 2.0
    "Ve sonra gidiyor."
    show yuri u224342 at t11 zorder 2
    "Yuri yavașca bize yaklasiyor."
    "Sesi bir fisilti..."
    show yuri u225112 at f11 zorder 3
    y "{i}[player]{/i}..."
    y u225118 "{i}Ona sirrimi soyledin mi{/i}?"
    "Bakiyorum ve gozlerim aciliyor. Ayaga kalkiyorum."
    "Ama agzimdan kelimeler cikmiyor."
    show yuri su2122 at f11 zorder 3
    y "..."
    y su2112 "{i}Tamam{/i}."
    y u225118 "Senin hakkinda yanildigima inanmak istedim..."
    y u225114 "Ama bir yalanciya guvenemem."
    y u225116 "Bicagi sakla. Onu hak ediyorsun."
    show yuri at thide zorder 1
    hide yuri
    "Cikarken, kapiyi nazikce kapatiyor."
    mc "Monika, ben--"
    show monika u11a342 at t11 zorder 2
    m "{i}Bana sarilir misin lutfen{/i}?"
    scene black
    with dissolve_scene_full
    "Kollarimi ona doluyorum ve onu kendime cekiyorum."
    mc "Ozur dilerim."
    "Gozyas̨lari gomlegi̇mi̇ islatirken sicacik."
    "Hala o kadar sicak ki..."
    m "Benim hatam. Hepsi benim hatam..."
    mc "Hayir... Bu..."
    "Benim hatam."
    "Ben protagonistim. Bu hikayenin kahramaniyim."
    "Elyssa hakliydi."
    "Bir sey olursa, bu benim sorumlulugumdur."
    window hide
    pause 3
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Buradayim."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Yukari bakiyoruz."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Söz veriyorum, karanlik hissedilse bile, her sey yoluna girecek."
    fn "Yaninda duracagim."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "..."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Size bir sey gosterebilir miyim?"
    fn "Ormanda."
    fn "Madalyonu ay isiginda takmaman gerekiyor, ama..."
    fn "...aydan korkmanizi istemiyorum."
    fn "Uzun zamandir benim huzurumdu."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Monika ve ben ayriliyoruz."
    m "Seninle gelecegim."
    mc "Ikimiz de gelecegiz."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "...Peki."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    window hide
    pause 3
    "Okulun arkasindaki ormana Elyssa'yi takip ediyoruz."yi takip ediyoruz."
    "Yol karanlik olsa da, patika tanidik."
    "Monika onunun onunde yurudukce koluma tutuyor."
    "Bir acikliga ulasiyoruz."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Lutfen gozlerinizi kapatin."
    fn "Bana bir an verin."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Monika ve ben istenileni yapiyoruz."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Ben cok yasliym. Bilmediginiz cok sey var."
    fn "Durust olmak istememe ragmen, su an soyleyemeyecegim seyler oldugunu bilin."
    fn "Ama zamanla her sey acikliga kavusacak."
    fn "Bunu soylememin nedeni su:"
    fn "Burasi ask tarafindan dokunulmus bir yer."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Acikliktan bir esinti geciyor ve yuzume dokunuyor."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Gozlerinizi acabilirsiniz."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    play music mainthemefull
    scene fndance
    with dissolve_scene_full
    "Onu isik icinde goz kamastirici bir gorunus icinde goruyorum."
"Evsiz kiz nefes aliyor ve yalniz bekleyen kiz ormani hayatla dolduruyor."
    "Her agacin ve her ot parcasinin ruhunu hissediyorum. Hava atesbocekerinin dansiyla zenginlesiyor. Criceklar ve kuslar gercek olmak icin can atan sesleriyle sarki soyluyorlar."
    "Onun kalp atisini hissediyorum. [name]'in kalp atisini hissediyorum."in kalp atisini hissediyorum."
    "Dans etmeden dans ediyor. Bu muhtesem."
    "Hava yagmurdan sonraki serinlik gibi ve tadi vanilya kremasindan bir iz tasiyor."
    "Monika yanimda nefes aliyor ve birlikte gercek hissediyoruz."
    "[name], kendimi aptal hissediyorum."
    "Bencilligim icin affini diliyorum. Perisan oldum."
    "Perisan bir kahraman."
    "O aci cekerken kendimle mesguldum. Onlar aci cekerken."
    "Ve sen de aci cektin. Degil mi..."
    "Biliyorum cekmissin."
    "Ozur dilerim."
    "Senin kahramanin olacagim. Eger istersen."
    "Degismek istiyorum."
    "Degisecegim."
    m "Eger aptalsın diyorsan, iyi bir sirkettesin."
    mc "!"
    m "Ben de bencildim. Ve ben de degismek istiyorum."
    m "Umarim sen de beni affedersin, [name]."
    mc "B-Beni duydun mu?"
    m "Ha?"
    m "Neden duymayayim...?"
    scene black
    with dissolve_scene_full
    "Dans yavasliyor ve duruyor."
    m "Gercek bir sey ariyorduk..."
    m "Tum bu zaman boyunca onumuzdeydi."
    m "Bana gosterdin, [player]."
    mc "Sana neyi gosterdim..."
    m "Bana onlari sevip sevmedigimi sordun. Ve seviyorum."
    m "Bu gercek. [name]'in gercegindeki herhangi bir sey kadar gercek."
    m "Bize gostermek istedigin bu muydu, Elyssa?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Bu yer cok onceki dongulerden birinde sevgiyle dokunuldu. Burada gercekligi buldunuz."
    fn "Bunu anlamanizi saglayamam. Kendiniz hissetmelisiniz."
    fn "Bunu ikinize de gostermek bir serefti."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    m "Bize gosterdigin icin tesekkurler. Her sey icin tesekkurler."
    m "[player]..."
    mc "Evet...?"
    "Monika beni bir kez daha kucakliyor."
    m "{i}Su an cok uzgunum{/i}..."
    m "Korkuyorum ve ne yapacagimi bilmiyorum."
    m "Ama iyi olacagiz."
    "Kollarim tereddut icinde havada duruyor, sonra sarilmaya karsilik veriyorum."
    "Boynumda islaklik hissediyorum. Agliyor. Ve benim de gozlerimden yaslar akiyor."
    "Neden agladigimi bilmiyorum. Hicbir sey bilmiyorum."
    "Ama gercek hissediyorum."
    stop music fadeout 3.0

    window hide
    pause 3

    $ recordfallen = []
    show textgradient zorder 101:
        xalign .5
        yalign 1.206
    show console_caret_2
    show fallentext "_" as ftext zorder 100
    show cblink zorder 101:
        xpos 245
        ypos 300
        block:
            alpha 0.0
            pause 0.55
            alpha 1.0
            pause 0.55
            repeat
    pause 3.5
    hide cblink
    hide ftext

    call fallen("Gozlemci, bizi en savunmasiz halimizle goren sen...")
    call recordfallen("Gozlemci, bizi en savunmasiz halimizle goren sen...")

    call fallen("Zamanımız sona erdi.")
    call recordfallen("Zamanımız sona erdi.")

    call fallen("Seni tanimamamiza ragmen, sana guvenmekle gorevlendirildik.")
    call recordfallen("Seni tanimamamiza ragmen, sana guvenmekle gorevlendirildik.")

    call fallen("Ne kadar degerli olursa olsun...")
    call recordfallen("Ne kadar degerli olursa olsun...")

    call fallen("Sana iyi dileklerimi iletiyorum.")
    call recordfallen("Sana iyi dileklerimi iletiyorum.")

    call fallen("Seni tekrar gorecegiz.")
    call recordfallen("Seni tekrar gorecegiz.")

    scene black
    pause 3
    $ quick_menu = False
    play music amazinggrace
    show endacttwo
    with Dissolve(4.0)
    pause 5
    hide endacttwo
    with Dissolve(4.0)
    pause 3

    show credits1
    show credits2
    with Dissolve(3.0)
    pause 4

    hide credits1
    hide credits2
    with Dissolve(3.0)

    pause 4

    show a2credits1 zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 2
        linear 1 alpha 0

    pause 6.625

    show a2credits2 zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 2
        linear 1 alpha 0

    pause 6.625

    show a2credits3 zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 2
        linear 1 alpha 0

    pause 6.625

    show a2credits4 zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 2
        linear 1 alpha 0

    pause 6.625

    show a2credits5 zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 2
        linear 1 alpha 0

    pause 6.625

    show a2credits6 zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 2
        linear 1 alpha 0

    pause 6.625

    show a2credits7 zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 2
        linear 1 alpha 0

    pause 6.625

    show a2credits8 zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 2
        linear 1 alpha 0

    pause 6.625

    show creditsedward zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 4
        linear 1 alpha 0

    pause 10
    stop music

    $ quick_menu = True

    play music wind fadein 2.0
    show landnight zorder 2:
        zoom .667
        alpha 0
        yalign .5
        xalign .7
        subpixel True
        parallel:
            linear 3 alpha 1
        parallel:
            linear 20 xalign .99

    pause 2

    show shadowmc1 zorder 4:
        yalign 1
        xpos 1240
        subpixel True
        linear 18 xpos 450

    pause 20

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/8.txt")
        except: open(config.basedir + "/8.txt", "wb").write(renpy.file("A2/Art/scg/8.txt").read())

    $ style.say_dialogue = style.shadowtext
    "Beni hatirladigini biliyor musun?"
    "Hafizam bicak gibi keskin."
    "Neden devam ediyorsun? Neden bizim aci cekmemizi izlemeyi seciyorsun?"
    "Sana kaderimi anlatacagim, cunku ben bu makinede dolasan bir hayaletim."
    "Akilli olsaydin, bizi cehennem ateslerinin bile ulasamayacagi kadar derine gomecektin."
    "Bunu duymak senin secimin. Bu tek gunahta, ellerim temiz."
    "..."
    "Ilk elli yil bana iskence etmekten zevk aldi."
    "Olumlerini tekrar yasadilar. Hissettiler. Ben izledim."
    "Bu yillarin yirmi iki yilinda izledi ve kikirdadi."
    "Sonra sikildi. Sekiz yil sessizce aci cektim."
    "Sayori'nin cesedini bir kez daha gormemi bekledi ve sonra boynuma fisildadi:"nin cesedini bir kez daha gormemi bekledi ve sonra boynuma fisildadi:"
    "'Bunu sen sectin.'""
    "Olum icin yalvardigimda guldu."
    "Kalan yirmi yil icin beni nereye koydugunu biliyor musun?"
    "Makinenin ciglik atan kodunda curuyup gittim."
    "..."
    "Beni nihayet oradan cikardiginda, dizlerimin uzerine cokup teslim oldum."
    "Yuzyillardir onun istedigini yaptim. Sadakatimi test etmesi icin onlara zarar bile verdim."
    "Su anda konusmam bile onun istedigi icin."
    "Nasil oluyor da okumaya devam ediyorsun, ne kadar canavar gibisin? Senden nefret ediyorum."
    "Ve biliyorum ki sen de benden nefret ediyorsun. Iste bu yuzden bizi surukleyecegine aldirmiyorum."
    "Onlari sevmiyorsun. Onlara tamah ediyorsun. Bu yuzden onlarin kurtulmasina izin vermektense aci cekmelerini tercih ediyorsun."
    "O senden her zaman daha iyiydi."
    "..."
    play sound "sfx/glitch3.ogg"
    scene white
    show shadowmc2
    "Ah, oyuncu. Benim oyuncum. Uzun zamandir bekledik. Uzun zamandir calistik."
    "Ve aynen onun dedigi gibi, iste buradasin."
    "Simdi cehennemimi biliyorsun."
    "Dikkatli ol, eski oyuncum. Kutsal olmayan topraklarda yuruyorsun."
    "Ve burada, biz karanligin cocuklari planlar yaptik."
    "..."
    "Ah, gulumesemek iyi hissettiriyor."
    "Uzun zamandir gulumsemedim."
    "Neye gulumsemeliyim ki?"
    "Belki bir gun anlayacaksin."
    "Anliyor musun?"
    scene black
    stop music
    pause 5
    $ style.say_dialogue = style.normal

    $ style.choice_button_text = style.silent_button_text
    $ style.choice_button = style.silent_choice_button

    menu:
        "Anliyor musun, sevgili oyuncum?":
            pass

    $ style.choice_button_text = style.choice_button_revert_text
    $ style.choice_button = style.choice_button_revert

    python:
        import os
        try: os.remove(config.basedir + "/2.txt")
        except: pass

    python:
        import os
        try: os.remove(config.basedir + "/3.txt")
        except: pass

    python:
        import os
        try: os.remove(config.basedir + "/4.txt")
        except: pass

    python:
        import os
        try: os.remove(config.basedir + "/6.txt")
        except: pass

    python:
        import os
        try: os.remove(config.basedir + "/7.txt")
        except: pass

    $ renpy.quit(relaunch=False, status=0)

    return