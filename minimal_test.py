import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
import sys

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_title("TESTE")
    win.set_default_size(200, 200)
    label = Gtk.Label(label="SE VOCÊ VÊ ISSO, O GTK ESTÁ OK")
    win.set_child(label)
    win.present()

app = Gtk.Application(application_id='com.test.gtk')
app.connect('activate', on_activate)
app.run(sys.argv)
