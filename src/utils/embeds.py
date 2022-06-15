import disnake
from disnake.ui import Button, Select, View

class EmbedFactory:
    def __init__(
            self,
            title: str = None,
            description: str = None,
            author: str = None,
            author_url: str = None,
            colour: disnake.Colour = 0xB4E3F9,
            infobox: dict = None,
            options: list = None,
            thumbnail_url: str = None,
            view: False = None,
            button_label: str = None,
            button_url: str = None,
    ):
        self.title = title
        self.description = description
        self.author = author
        self.author_url = author_url
        self.colour = colour
        self.infobox = infobox
        self.options = options
        self.thumbnail_url = thumbnail_url
        self.view = view
        self.button_label = button_label
        self.button_url = button_url

    def create(
            self,
            title: str = None,
            description: str = None,
            author: str = None,
            author_url: str = None,
            colour: disnake.Colour = None,
            options: list = None,
            thumbnail_url: str = None,
            view: bool = False,
            button_label: str = None,
            button_url: str = None,
    ):
        embed = disnake.Embed()
        embed.title = self.title if not title else title
        embed.description = self.description if not description else description
        embed.colour = self.colour if not colour else colour

        if view:
            view = View()
            if button_label:
                button = create_button(button_label, button_url)
                view.add_item(button)
            if options:
                dropdown = create_dropdown(options)
                view.add_item(dropdown)

            return(embed, view)
        return(embed)

'''
Creates a button for interaction responses.
:param label: (String) - Represents a label for the button.
:param url: (String) - Represents a hyperlink (URL) for the button.
'''
def create_button(label, url) -> None:
    button = Button(label=label, style=disnake.ButtonStyle.link, url=url)
    return(button)

'''
Creates a dropdown menu for interaction responses.
:param options: (List) - Represents a list of options (labels) for the dropdown.
'''
def create_dropdown(options) -> None:
    dropdown = Select(placeholder='Select an option.', options=[])
    for option in options:
        dropdown.add_option(label=option)
    return(dropdown)