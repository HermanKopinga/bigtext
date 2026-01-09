from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
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
                                        name='Large type',
                                        description='Print full screen: %s' % text,
                                        on_enter=HideWindowAction()))

        if text:
            print ("duh <<<<<<<<<<<<<<<<<<<<<<<")
            #subprocess.Popen(['python3', '.local/share/ulauncher/extensions/largetype/show_text.py', text])

        return RenderResultListAction(items)
    


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):

        #logger.error('...')
        data = event.get_data()
        text = "123"
        subprocess.Popen(['python3', '.local/share/ulauncher/extensions/largetype/show_text.py', text])
        # do additional actions here...


if __name__ == '__main__':
    LargeType().run()