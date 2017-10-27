import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from shutil import copyfile
class Handler:
    def __init__(self, build):
        self.builder = build
        window = self.builder.get_object("main_window")
        window.show_all()

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onButtonPressed(self, button):
        print("Hello World!")
    
    def aboutClk(self, button):

        aboutWin = self.builder.get_object("aboutdialog1")
        aboutWin.show_all()
    
    def selMusic(self, button):

        musWin = self.builder.get_object("filechooserdialog")
        musWin.show_all()

    def getTitleLen(self, button):
        title = self.builder.get_object("title")
        length = self.builder.get_object("length")
        song_title = title.get_text()
        song_length = length.get_text()
        print song_title, song_length
	os.system("python rbm_chords.py")
	os.system("nautilus ./output_midi")


    def closeWin(self, widget):
        widget.destroy()

    def getFilename(self, button):
        filechooser = self.builder.get_object("filechooserdialog")
        filemove = filechooser.get_filenames()
	print filemove
        for files in filemove:
	    filename = files.split("/")[-1]
            print filename
            copyfile(files, "./Pop_Music_Midi/"+filename)
        

        
        

        

builder = Gtk.Builder()
builder.add_from_file("frontend2.glade")
builder.connect_signals(Handler(build=builder))
Gtk.main()
