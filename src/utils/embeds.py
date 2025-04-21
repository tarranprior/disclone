#! /usr/bin/env python3

"""
This module contains a basic factory for embed creation and functions
for message interaction components (Buttons, Dropdowns etc.)

Classes:
    - `EmbedFactory`:
            A class which represents the EmbedFactory function.

Functions:
    - `create()`:
            Creates an embed for display purposes.
    - `create_button()`:
            Creates a regular button for interaction responses.
    - `create_dropdown()`:
            Creates a dropdown menu for interaction responses.
"""

from typing import Tuple, Union

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
    ) -> None:
        """
        Initialises a new `EmbedFactory` object with optional parameters.

        :param self: -
            Represents this object.

        :param title: (Optional[String]) -
            Represents a title for the embed.
        :param description: (Optional[String]) -
            Represents a description for the embed.
        :param colour: (Optional[disnake.Colour]) -
            Represents a colour for the embed. Defaults to `disnake.Colour.og_blurple()`.
        :param infobox: (Optional[Dictionary]) -
            Represents the infobox (properties) to display in the embed.
        :param options: (Optional[List]) -
                Represents a list of options for the Select Menu.
        :param thumbnail_url: (Optional[String]) -
            Represents a URL for the embed's thumbnail.
        :param button_label: (Optional[String]) -
            Represents a label for the embed's button.
        :param button_url: (Optional[String]) -
            Represents a hyperlink (URL) for the embed's button.
        :param button_emoji: (Optional[Union[disnake.Emoji, disnake.PartialEmoji, String]]) -
            Represents an emoji for the embed's button.

        :return: (None)
        """

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
    ) -> Union[Tuple[disnake.Embed, View], disnake.Embed]:
        """
        Creates an embed for display purposes.
        Each paramater is optional and defaults to None.

        :param self: -
            Represents this object.
        :param title: Optional([String]) -
            Represents a title for the embed.
        :param description: Optional([String]) -
            Represents a description for the embed.
        :param colour: Optional([disnake.Colour]) -
            Represents a colour for the embed.
        :param infobox: Optional([Dictionary]) -
            Represents the infobox (properties) to display in the embed.
        :param options: Optional([List]) -
            Represents a list of options for the Select Menu.
        :param thumbnail_url: Optional([String]) -
            Represents a URL for the embed's thumbnail.
        :param button_label: Optional([String]) -
            Represents a label for the embed's button.
        :param button_url: (Optional[String]) -
            Represents a hyperlink (URL) for the embed's button.
        :param button_emoji: (Optional[Union[disnake.Emoji, disnake.PartialEmoji, String]]) -
            Represents an emoji for the embed's button.

        :return: (Union[Tuple[disnake.Embed, View], disnake.Embed]) -
            A tuple containing the Embed and View objects, or just the Embed object.
        """

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

            return embed, view
        return embed


def create_button(label, url) -> None:
    """
    Creates a regular button for interaction responses.

    :param label: (Optional[String]) -
        Represents a label for the button.
    :param emoji: (Optional[Union[disnake.Emoji, disnake.PartialEmoji, String]]) -
        Represents an emoji for the button.

    :return: (Button) -
        Newly created Button object.
    """

    button = Button(label=label, style=disnake.ButtonStyle.link, url=url)
    return button


def create_dropdown(options) -> None:
    """
    Creates a dropdown menu for interaction responses.

    :param options: (List[String]) -
        Represents a list of options (labels) for the dropdown.

    :return: (Select) -
        Newly created Select object.
    """
    
    dropdown = Select(placeholder="Select an option...", options=[])
    for option in options:
        dropdown.add_option(label=option)
    return dropdown
