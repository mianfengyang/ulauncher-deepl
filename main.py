from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

from deeplx import translation
import json

class DemoExtension(Extension):

    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        query = event.get_argument() or ""
        data = {
                "text": query.split(" ")[2],
                "source_lang": query.split(" ")[1].split(":")[0],
                "target_lang": query.split(" ")[1].split(":")[1],
            }
        post_data = json.dumps(data)
        items = []
        results = translation(post_data)
        items.append(ExtensionResultItem(icon=results['icon'],
                                        name=results['alternatives'] + results["data"],
                                        on_enter=CopyToClipboardAction(results['data'])))

        return RenderResultListAction(items)

if __name__ == '__main__':
    DemoExtension().run()
