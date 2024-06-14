import os
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


APPID = 'com.github.taniyoshima.pyt_gtk4_alertdialog3'


@Gtk.Template(filename=os.path.dirname(__file__) + '/ui_file.ui')
class Gtk4TestTest(Gtk.ApplicationWindow):

    __gtype_name__ = "window"
    alertdialog = Gtk.Template.Child()

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)

    @Gtk.Template.Callback()
    def on_button_clicked(self, button):
        self.alertdialog.choose(self, None, self.alert_choose)

    def alert_choose(self, alertdialog, result):

        num = alertdialog.choose_finish(result)
        match num:
            case 0:
                print('「A」もしくはEnterキーが押されました。')
            case 1:
                print('「B」が押されました。')
            case 2:
                print('「C」が押されました。')


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
