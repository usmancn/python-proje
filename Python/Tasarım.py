
from customtkinter import*
from PIL import Image
from tkinter import ttk, messagebox

uygulama = CTk()
uygulama.geometry("1100x700")
uygulama.resizable(False, False)
set_appearance_mode("dark")

sifre_goster_icon = Image.open("resimler/sifre_goster.png")
sifre_goster_png = CTkImage(light_image=sifre_goster_icon, dark_image=sifre_goster_icon)

arama_icon = Image.open("resimler/search.png")
arama_png = CTkImage(light_image=arama_icon, dark_image=arama_icon)

anasayfa_icon = Image.open("resimler/anasayfa.png")
anasayfa_png = CTkImage(light_image=anasayfa_icon, dark_image=anasayfa_icon)

filmlerim_icon = Image.open("resimler/filmlerim.png")
filmlerim_png = CTkImage(light_image=filmlerim_icon, dark_image=filmlerim_icon)

filmlekle_icon = Image.open("resimler/filmekle.png")
filmlekle_png = CTkImage(light_image=filmlekle_icon, dark_image=filmlekle_icon)

cıkıs_icon = Image.open("resimler/cıkıs.png")
cıkıs_png = CTkImage(light_image=cıkıs_icon, dark_image=cıkıs_icon)

def girisSayfaStart():
    girisForm = CTkFrame(master=uygulama,fg_color="#8D6F3A",border_color="#FFCC70",border_width=2)
    girisForm.pack(expand=True)
    girisForm.configure(height=400,width=300,corner_radius=32)

    def sifre_goster():
        if sifre.cget("show") == "*":
            sifre.configure(show="")
        else:
            sifre.configure(show="*")

    def kayitOl_gecis():
        girisForm.destroy()
        kayitSayfa()

    def anaForm_gecis():
        girisForm.destroy()
        uygulamaSayfa()

    topG_lbl = CTkLabel(master=girisForm, text="Giriş Sayfası", font=("Tahoma",22,"bold"), text_color="#000000")
    topG_lbl.place(x=80, y=50)

    kullaniciAdi = CTkEntry(master=girisForm,placeholder_text="Kullanıcı Adı",width=160,height=30,text_color="#FFDA8E")
    kullaniciAdi.place(x=70,y=100)

    sifre = CTkEntry(master=girisForm, placeholder_text="Şifre", width=160, height=30,
                            text_color="#FFDA8E",show="*")
    sifre.place(x=70, y=150)

    giris_btn= CTkButton(master=girisForm,text="Giriş Yap",corner_radius=32,fg_color="#4D4D3D",hover_color="#A2A277",width=120,command=anaForm_gecis)
    giris_btn.place(x=87,y=200)

    hesapKayıt_lbl= CTkLabel(master=girisForm,text="Hesabın Yok Mu?",font=("Ariel",12),text_color="#000000")
    hesapKayıt_lbl.place(x=70,y=250)

    kayıtOl_btn = CTkButton(master=girisForm,text="Kayıt Ol",corner_radius=32,fg_color="transparent",hover_color="#896B38",width=10,command=kayitOl_gecis)
    kayıtOl_btn.place(x=160, y=252)

    sifre_goster_btn = CTkButton(master=girisForm, image=sifre_goster_png, width=20, height=20, text="", fg_color="transparent",
                                 hover_color="#896B38",command=sifre_goster)
    sifre_goster_btn.place(x=230, y=150)

def kayitSayfa():

    def kayit_basarili():
        messagebox.showinfo("Başarılı", "Başarıyla kayıt olundu!")

    def girisYap_gecis():
        kayitForm.destroy()
        girisSayfa()

    kayitForm = CTkFrame(master=uygulama, fg_color="#8D6F3A", border_color="#FFCC70", border_width=2)
    kayitForm.pack(expand=True)
    kayitForm.configure(height=400, width=300,corner_radius=32)

    topK_lbl = CTkLabel(master=kayitForm, text="Kayıt Sayfası", font=("Tahoma", 22, "bold"), text_color="#000000")
    topK_lbl.place(x=75, y=50)

    kullaniciAdi = CTkEntry(master=kayitForm, placeholder_text="Kullanıcı Adı", width=160, height=30,
                            text_color="#FFDA8E")
    kullaniciAdi.place(x=70, y=100)

    sifre = CTkEntry(master=kayitForm, placeholder_text="Şifre", width=160, height=30,
                     text_color="#FFDA8E", show="*")
    sifre.place(x=70, y=150)

    kayıtOl_btn = CTkButton(master=kayitForm, text="Kayıt Ol", corner_radius=32, fg_color="#4D4D3D",
                          hover_color="#A2A277", width=120,command=kayit_basarili)
    kayıtOl_btn.place(x=87, y=200)

    hesapGiris_lbl = CTkLabel(master=kayitForm, text="Hesabın Var Mı?", font=("Ariel", 12), text_color="#000000")
    hesapGiris_lbl.place(x=70, y=250)

    girisYap_btn = CTkButton(master=kayitForm, text="Giriş Yap", corner_radius=32, fg_color="transparent",
                            hover_color="#896B38", width=10,command=girisYap_gecis)
    girisYap_btn.place(x=160, y=252)

def uygulamaSayfa():
    current_frame = None

    def show_frame(new_frame_func):
        nonlocal current_frame
        if current_frame:
            current_frame.destroy()
        current_frame = new_frame_func()

    def anaPage():
        anaForm = CTkFrame(master=uygulama, fg_color="#373737", border_color="#426E73", border_width=2)
        anaForm.pack(expand=True)
        anaForm.configure(height=900, width=1300, corner_radius=2)

        anaTop_lbl = CTkLabel(master=anaForm, text="Film Değerlendirme Sistemi", font=("Tahoma", 30, "bold"),
                               text_color="#DFDFDF", bg_color="#4BAFBA", width=810, height=60)
        anaTop_lbl.place(x=20, y=20)

        anaAlt_lbl = CTkLabel(master=anaForm, text="Hoş Geldiniz !!!", font=("Tahoma", 30, "bold"),
                               text_color="#DFDFDF", bg_color="#4BAFBA", width=810, height=60)
        anaAlt_lbl.place(x=20, y=615)

        return anaForm

    def filmlerimPage():

        def film_sil_onay():
            result = messagebox.askyesno("Onay", "Bu filmi silmek istiyor musunuz?")
            if result:
                messagebox.showinfo("Bilgi", "Film başarıyla silindi!")
            else:
                messagebox.showinfo("Bilgi", "Silme işlemi iptal edildi.")

        filmlerimForm = CTkFrame(master=uygulama, fg_color="#373737", border_color="#426E73", border_width=2)
        filmlerimForm.pack(expand=True)
        filmlerimForm.configure(height=900, width=1300, corner_radius=2)

        FilmlDuzenle_btn = CTkButton(master=filmlerimForm, text="Filmi Düzenle", text_color="#E5E5E5", font=("Tahoma", 16),
                                     corner_radius=15, fg_color="#3D858D",
                                     hover_color="#3E585B", width=180, height=40,command=lambda: show_frame(filmDuzenlePage))
        FilmlDuzenle_btn.place(x=210, y=550)

        FilmlSil_btn = CTkButton(master=filmlerimForm, text="Filmi Sil", text_color="#E5E5E5", font=("Tahoma", 16),
                                 corner_radius=15, fg_color="#3D858D",
                                 hover_color="#3E585B", width=180, height=40,command=film_sil_onay)
        FilmlSil_btn.place(x=450, y=550)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview",
                        background="#4E4E4E",
                        foreground="white",
                        rowheight=35,
                        fieldbackground="#4E4E4E",
                        font=("Arial", 14))

        style.configure("Treeview.Heading",
                        background="#3D858D",
                        foreground="white",
                        font=("Arial", 16, "bold"),
                        padding=(10, 5))

        style.map("Treeview", background=[("selected", "#0D3A3A")])

        filtreleme_lbl = CTkLabel(master=filmlerimForm, text="Filtrele:", font=("Arial", 21), text_color="#DFDFDF")
        filtreleme_lbl.place(x=150, y=150)

        filttur_combobox = CTkComboBox(master=filmlerimForm,
                                       values=["Türü", "Bilim Kurgu", "Komedi", "Drama", "Aksiyon"],
                                       width=125, fg_color="#3D858D", border_color="#FFFFFF",
                                       dropdown_fg_color="#3D858D",height=35)
        filttur_combobox.place(x=230, y=150)

        filtdurum_combobox = CTkComboBox(master=filmlerimForm, values=["Durum", "İzlenmiş", "İzlenmemiş", "İzlenecek"],
                                         width=125, fg_color="#3D858D", border_color="#FFFFFF",
                                         dropdown_fg_color="#3D858D",height=35)
        filtdurum_combobox.place(x=375, y=150)

        filtpuan_combobox = CTkComboBox(master=filmlerimForm, values=["Puan", "1", "2", "3", "4", "5"], width=125,
                                        fg_color="#3D858D", border_color="#FFFFFF", dropdown_fg_color="#3D858D",height=35)
        filtpuan_combobox.place(x=520, y=150)

        filtreleBtn = CTkButton(master=filmlerimForm, image=arama_png, width=20, height=20, text="",font=("Ariel",20),
                                fg_color="transparent",
                                hover_color="#A2A277")
        filtreleBtn.place(x=658, y=152)

        filmlerimTree = ttk.Treeview(filmlerimForm)
        filmlerimTree['columns'] = ("ad", "tur", "durum", "yıldız", "not")
        filmlerimTree.column("#0", width=0, stretch=NO)
        filmlerimTree.column("ad", width=200)
        filmlerimTree.column("tur", width=150)
        filmlerimTree.column("durum", width=150)
        filmlerimTree.column("yıldız", width=100)
        filmlerimTree.column("not", width=300)

        filmlerimTree.heading("ad", text="Filmin Adı")
        filmlerimTree.heading("tur", text="Tür")
        filmlerimTree.heading("durum", text="Durum")
        filmlerimTree.heading("yıldız", text="Puan")
        filmlerimTree.heading("not", text="Değerlendirme")

        filmlerimTree.insert("", "end", values=("Inception", "Bilim Kurgu", "İzlenmiş", "5", "Harika bir film"))

        filmlerimTree.place(x=80, y=250)

        filmTop_lbl = CTkLabel(master=filmlerimForm, text="Filmlerim", font=("Tahoma", 30, "bold"),
                               text_color="#DFDFDF", bg_color="#4BAFBA", width=810, height=60)
        filmTop_lbl.place(x=20, y=20)

        return filmlerimForm

    def filmEklePage():

        def ekleme_basarili():
            messagebox.showinfo("Başarılı", "Film başarıyla eklendi!")
            show_frame(filmlerimPage)

        filmEkleForm = CTkFrame(master=uygulama, fg_color="#373737", border_color="#426E73", border_width=2)
        filmEkleForm.pack(expand=True)
        filmEkleForm.configure(height=900, width=1300, corner_radius=2)

        filmAdi = CTkEntry(master=filmEkleForm, placeholder_text="Film Adı", width=170, height=40,font=("Ariel",18),
                                text_color="#DFDFDF",fg_color="#1E3D3D",border_color="#426E73")
        filmAdi.place(x=330, y=150)

        filmTur = CTkEntry(master=filmEkleForm, placeholder_text="Film Türü", width=170, height=40,font=("Ariel",18),
                           text_color="#DFDFDF",fg_color="#1E3D3D",border_color="#426E73")
        filmTur.place(x=330, y=205)

        filmdurum_combobox = CTkComboBox(master=filmEkleForm, values=["Durum", "İzlenmiş", "İzlenmemiş", "İzlenecek"],
                                         width=170, fg_color="#1E3D3D",
                                         dropdown_fg_color="#1E3D3D", height=40,font=("Ariel",18,),text_color="#DFDFDF",border_color="#426E73")
        filmdurum_combobox.place(x=330, y=260)

        filmpuan_combobox = CTkComboBox(master=filmEkleForm, values=["Puan", "1", "2", "3", "4", "5"], width=170,
                                        fg_color="#1E3D3D",  dropdown_fg_color="#1E3D3D",
                                        height=40,font=("Ariel",18),text_color="#DFDFDF",border_color="#426E73")
        filmpuan_combobox.place(x=330, y=318)

        degerlendirme_lbl = CTkLabel(master=filmEkleForm, text="Notlarım:", font=("Tahoma", 18, "bold"),
                                 text_color="#DFDFDF")
        degerlendirme_lbl.place(x=306, y=377)

        filmdegerlendirme_textbox = CTkTextbox(master=filmEkleForm,scrollbar_button_color="#426E73",corner_radius=12,border_color="#426E73",border_width=2,width=220,height=100, fg_color="#1E3D3D",text_color="#DFDFDF",font=("Ariel",18))
        filmdegerlendirme_textbox.place(x=306,y=410)

        FilmlEkle_btn = CTkButton(master=filmEkleForm, text="Filmi Ekle", text_color="#E5E5E5",
                                     font=("Tahoma", 16),
                                     corner_radius=8, fg_color="#4BAFBA",
                                     hover_color="#3E585B", width=180, height=40,command=ekleme_basarili)
        FilmlEkle_btn.place(x=325, y=550)

        ekleTop_lbl = CTkLabel(master=filmEkleForm, text="Film Ekleme Sayfası", font=("Tahoma", 30, "bold"),
                                     text_color="#DFDFDF",bg_color="#4BAFBA",width=810,height=60)
        ekleTop_lbl.place(x=20, y=20)

        return filmEkleForm

    def filmDuzenlePage():

        def duzenleme_basarili():
            messagebox.showinfo("Başarılı", "Film başarıyla duzenlendi!")
            show_frame(filmlerimPage)

        filmDuzenleForm = CTkFrame(master=uygulama, fg_color="#373737", border_color="#426E73", border_width=2)
        filmDuzenleForm.pack(expand=True)
        filmDuzenleForm.configure(height=900, width=1300, corner_radius=2)

        filmAdi = CTkEntry(master=filmDuzenleForm, placeholder_text="Film Adı", width=170, height=40,font=("Ariel",18),
                                text_color="#DFDFDF",fg_color="#1E3D3D",border_color="#426E73")
        filmAdi.place(x=330, y=150)

        filmTur = CTkEntry(master=filmDuzenleForm, placeholder_text="Film Türü", width=170, height=40,font=("Ariel",18),
                           text_color="#DFDFDF",fg_color="#1E3D3D",border_color="#426E73")
        filmTur.place(x=330, y=205)

        filmdurum_combobox = CTkComboBox(master=filmDuzenleForm, values=["Durum", "İzlenmiş", "İzlenmemiş", "İzlenecek"],
                                         width=170, fg_color="#1E3D3D",
                                         dropdown_fg_color="#1E3D3D", height=40,font=("Ariel",18,),text_color="#DFDFDF",border_color="#426E73")
        filmdurum_combobox.place(x=330, y=260)

        filmpuan_combobox = CTkComboBox(master=filmDuzenleForm, values=["Puan", "1", "2", "3", "4", "5"], width=170,
                                        fg_color="#1E3D3D",  dropdown_fg_color="#1E3D3D",
                                        height=40,font=("Ariel",18),text_color="#DFDFDF",border_color="#426E73")
        filmpuan_combobox.place(x=330, y=318)

        degerlendirme_lbl = CTkLabel(master=filmDuzenleForm, text="Notlarım:", font=("Tahoma", 18, "bold"),
                                 text_color="#DFDFDF")
        degerlendirme_lbl.place(x=306, y=377)

        filmdegerlendirme_textbox = CTkTextbox(master=filmDuzenleForm,scrollbar_button_color="#426E73",corner_radius=12,border_color="#426E73",border_width=2,width=220,height=100, fg_color="#1E3D3D",text_color="#DFDFDF",font=("Ariel",18))
        filmdegerlendirme_textbox.place(x=306,y=410)

        FilmlEkle_btn = CTkButton(master=filmDuzenleForm, text="Filmi Düzenle", text_color="#E5E5E5",
                                     font=("Tahoma", 16),
                                     corner_radius=8, fg_color="#4BAFBA",
                                     hover_color="#3E585B", width=180, height=40,command=duzenleme_basarili)
        FilmlEkle_btn.place(x=325, y=550)

        ekleTop_lbl = CTkLabel(master=filmDuzenleForm, text="Film Düzenleme Sayfası", font=("Tahoma", 30, "bold"),
                                     text_color="#DFDFDF",bg_color="#4BAFBA",width=810,height=60)
        ekleTop_lbl.place(x=20, y=20)

        return filmDuzenleForm

    def cıkıs_yap_onay():
        result = messagebox.askyesno("Çıkış", "Çıkış yapmak istiyor musunuz?")
        if result:
            uygulama.quit()

    seceneklerForm = CTkFrame(master=uygulama, fg_color="#4E4E4E", border_color="#426E73", border_width=2)
    seceneklerForm.pack(side="left",fill="y")
    seceneklerForm.configure(height=600, width=250, corner_radius=2)

    anaSayfa_btn = CTkButton(master=seceneklerForm, text="Ana Sayfa",font=("Tahoma",20,"bold"), corner_radius=0, fg_color="#4BAFBA",
                            hover_color="#3E585B", width=250,height=60,image=anasayfa_png,command=lambda: show_frame(anaPage))
    anaSayfa_btn.place(x=0, y=230)

    filmlerim_btn = CTkButton(master=seceneklerForm, text="Filmlerim",font=("Tahoma",20,"bold"), corner_radius=0, fg_color="#4BAFBA",
                            hover_color="#3E585B", width=250, height=60,image=filmlerim_png,command=lambda: show_frame(filmlerimPage))
    filmlerim_btn.place(x=0, y=295)

    filmEkle_btn = CTkButton(master=seceneklerForm, text="Film Ekle",font=("Tahoma",20,"bold"), corner_radius=0, fg_color="#4BAFBA",
                            hover_color="#3E585B", width=250, height=60,image=filmlekle_png,command=lambda: show_frame(filmEklePage))
    filmEkle_btn.place(x=0, y=360)

    cıkıs_btn = CTkButton(master=seceneklerForm, text="Çıkış Yap", font=("Tahoma", 20, "bold"), corner_radius=0,
                             fg_color="#4BAFBA",
                             hover_color="#3E585B", width=250, height=60, image=cıkıs_png,
                             command=cıkıs_yap_onay)
    cıkıs_btn.place(x=0, y=425)

    kullanici_lbl = CTkLabel(master=seceneklerForm, text="Kullanıcı Adı:", font=("Tahoma",18,"bold"), text_color="#DFDFDF")
    kullanici_lbl.place(x=10, y=150)

    #dinamik olarak kullanıcı adını almalı
    kullaniciAdi_lbl = CTkLabel(master=seceneklerForm, text="Username", font=("Tahoma",18),
                             text_color="#DFDFDF")
    kullaniciAdi_lbl.place(x=10, y=185)

    show_frame(anaPage)

girisSayfaStart()

uygulama.mainloop()
