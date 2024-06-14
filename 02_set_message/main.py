import os
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


APPID = 'com.github.taniyoshima.pyt_gtk4_alertdialog2'


@Gtk.Template(filename=os.path.dirname(__file__) + '/ui_file.ui')
class Gtk4TestTest(Gtk.ApplicationWindow):

    __gtype_name__ = "window"
    alertdialog = Gtk.Template.Child()

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)

    @Gtk.Template.Callback()
    def on_button1_clicked(self, button):
        self.alertdialog.set_message('Message1')
        self.alertdialog.set_detail('Message1を表示した\nGtk.AlertDialogです。')
        self.alertdialog.show(self)

    @Gtk.Template.Callback()
    def on_button2_clicked(self, button):
        self.alertdialog.set_message('Message2')
        self.alertdialog.set_detail('Message2を表示した\nGtk.AlertDialogです。')
        self.alertdialog.show(self)


class Gtk4TestApp(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)

    def do_activate(self):
        window = Gtk4TestTest(self)
        window.present()


def main():
    app = Gtk4TestApp()
    app.run()


if __name__ == '__main__':
    main()
