import sys
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class FullscreenText(Gtk.Window):
    def __init__(self, text):
        super().__init__(title="LargeType")
        self.set_decorated(False)
        self.fullscreen()

        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.set_visual(visual)

        self.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 0.8))
        

        label = Gtk.Label()
        label.set_text(text)
        label.set_justify(Gtk.Justification.CENTER)
        label.set_halign(Gtk.Align.CENTER)
        label.set_valign(Gtk.Align.CENTER)
        label.set_line_wrap(True)
        label.set_max_width_chars(200)

        label.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse("white"))
        label.set_name("largetype")

        self.add(label)
        self.connect("key-press-event", lambda w, e: Gtk.main_quit())
        self.show_all()


if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Large Type by Herman Kopinga"
    win = FullscreenText(text)
    style_provider = Gtk.CssProvider()
    style_provider.load_from_path("/home/herman/.local/share/ulauncher/extensions/largetype/styles.css")
    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(), style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )

    Gtk.main()
te