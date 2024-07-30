from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

from deeplx import translation


class DemoExtension(Extension):

    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        query = event.get_argument() or ""
        items = []
        results = translation(query)
        items.append(ExtensionResultItem(icon=results['icon'],
                                        name=results['res'],
                                        source_lang=results['source_lang'],
                                        target_lang=results['target_lang'],
                                        on_enter=CopyToClipboardAction(results['title'])))

        return RenderResultListAction(items)

if __name__ == '__main__':
    DemoExtension().run()
