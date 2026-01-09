from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
import subprocess
import logging

logger = logging.getLogger("ulauncher.extension.largetype")

class LargeType(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        text = event.get_argument()
        
        items = []
        items.append(ExtensionResultItem(icon='images/largetype.png',
                                        name='%s in BIG text' % text,
                                        description='on main monitor.',
                                        on_enter=ExtensionCustomAction(text, keep_app_open=True)))

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_data()
        subprocess.Popen(['python3', '.local/share/ulauncher/extensions/largetype/show_text.py', data])

if __name__ == '__main__':
    LargeType().run()