from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget, \
    TwoLineAvatarIconListItem, IRightBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.textfield import MDTextField
from kivy.uix.label import Label

import uuid


class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.all_data = []

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.screen = Builder.load_file("load.kv")
        return self.screen

    def add_new_todo(self, value):
        if value:
            item_id = str(uuid.uuid4())
            secondary = "To buyyy"
            self.all_data.append(
                {"value": value, "id": item_id, "secondary": secondary}
            )
            todo_list = self.screen.ids.todo_list  # get this from kv file MDList
            todo_list.add_widget(
                OneLineAvatarIconListItem(
                    #IconRightWidget(icon="checkbox-marked", on_release=lambda x: self.edit_icon(item_id, secondary)),
                    IconLeftWidget(icon="delete", on_release=lambda x: self.delete_icon(item_id)),
                    id=item_id,
                    text=value,
                    secondary_text=secondary,
                )
            )
        self.screen.ids.inputtodo.text = ""


    def delete_icon(self, item_id):
        for item in self.all_data:
            if item['id'] == item_id:
                self.all_data.remove(item)
                todo_list = self.screen.ids.todo_list
                for child in todo_list.children:
                    if child.id == item_id:
                        todo_list.remove_widget(child)


if __name__ == "__main__":
    MyApp().run()
