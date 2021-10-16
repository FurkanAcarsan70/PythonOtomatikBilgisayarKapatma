import tkinter as tk
from tkinter import messagebox
import os as OS
from os import *
#Sayfa Tasarımı
AnaSayfa = tk.Tk()
AnaSayfa.geometry("500x400+510+200")
AnaSayfa.title("PC Kapatma Programı")
AnaSayfa.iconphoto(False, tk.PhotoImage(file='C:/Users/Furkan/Downloads/Bilgisayarı Kapat.png'))
#Label, Entry ve Buton yerleşimi
Label = tk.Label(AnaSayfa, text = 'Kaç saat sonra kapatılacağını giriniz:')
Label.pack()
Label.place(relx = 0.3)
Saat = tk.Entry(AnaSayfa)
Saat.pack()
Saat.place(relx = 0.3, rely = 0.07)
Label2 = tk.Label(AnaSayfa, text = 'Kaç dakika sonra kapatılacağını giriniz:')
Label2.pack()
Label2.place(relx = 0.3 , rely = 0.13)
Dakika = tk.Entry(AnaSayfa)
Dakika.pack()
Dakika.place(relx = 0.3, rely = 0.19)
#Kapatma işlemi
def Kapat():
    saatSaniye = int(Saat.get())
    dakikaSaniye = int(Dakika.get())
    Mesaj = tk.messagebox.askquestion('Bilgisayarı kapat', 'Bilgisayarı kapatmak istediğinizden emin misiniz?')
    if (Saat != '' and Dakika != ''):
        if (Mesaj == 'yes'):
            saat = saatSaniye * 3600
            dakika = dakikaSaniye * 60
            topla = saat + dakika
            OS.system('shutdown -s -t %s'%topla)
            messagebox.showinfo('Kapatma Saati', f'Bilgisayar {saatSaniye} saat, {dakikaSaniye} dakika sonra kapanacaktır.')
Kapat = tk.Button(AnaSayfa, text = 'Bilgisayarı Kapat', command = Kapat)
Kapat.pack()
Kapat.place(relx = 0.03, rely = 0.7)
#Yeniden Başlatma işlemi
def YenidenBaşlat():
    saatSaniye = int(Saat.get())
    dakikaSaniye = int(Dakika.get())
    Mesaj = tk.messagebox.askquestion('Yeniden Başlatma', 'Bilgisayarı yeniden başlatmak istediğinizden emin misiniz?')
    if (Saat != '' and Dakika != ''):
        if (Mesaj == 'yes'):
            saat = saatSaniye * 3600
            dakika = dakikaSaniye * 60
            toplam = saat + dakika
            OS.system('shutdown /r -t %s'%toplam)
            messagebox.showinfo('Yeniden Başlatma Saati', f'Bilgisayar {saatSaniye} saat, {dakikaSaniye} dakika sonra yeniden başlatılacaktır.')
YenidenBaşlat = tk.Button(AnaSayfa, text = 'Yeniden Başlat', command = YenidenBaşlat)
YenidenBaşlat.pack()
YenidenBaşlat.place(relx = 0.8, rely = 0.7)
#İptal işlemi
def Kapatmaİptali():
    OS.system('shutdown -a')
    messagebox.showinfo('Kapatma İptali', 'Bilgisayarı kapatma iptal edildi.')
İptal = tk.Button(AnaSayfa, text = 'İptal Et', command = Kapatmaİptali)
İptal.pack()
İptal.place(relx = 0.23, rely = 0.7)
#Sayfa başlatma
AnaSayfa.mainloop()