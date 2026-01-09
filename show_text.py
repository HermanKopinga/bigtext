import sys
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class FullscreenText(Gtk.Window):
    def __init__(self, text):
        super().__init__(title="BigText")
        self.set_decorated(False)
        self.fullscreen()

        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.set_visual(visual)
            # Allow the window to be painted with an alpha channel
            self.set_app_paintable(True)

        self.set_name("bigtext-window")
        css = """
        #bigtext-window {
            background-color: rgba(0, 0, 0, 0.8);
        }
        /* add label color via CSS instead of using deprecated modify_fg */
        #bigtext {
            color: white;
        }
        """
        provider = Gtk.CssProvider()
        provider.load_from_data(css.encode())
        # use USER priority so this inline provider wins over any external stylesheet
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), provider,
            Gtk.STYLE_PROVIDER_PRIORITY_USER
        )

        label = Gtk.Label()
        label.set_text(text)
        label.set_justify(Gtk.Justification.CENTER)
        label.set_halign(Gtk.Align.CENTER)
        label.set_valign(Gtk.Align.CENTER)
        label.set_line_wrap(True)
        label.set_max_width_chars(200)

        label.set_name("bigtext")

        self.add(label)
        self.connect("key-press-event", lambda w, e: Gtk.main_quit())
        self.show_all()


if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Big Text by Herman Kopinga"
    win = FullscreenText(text)
    style_provider = Gtk.CssProvider()
    style_provider.load_from_path(".local/share/ulauncher/extensions/bigtext/styles.css")
    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(), style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )

    Gtk.main()
