"""
Copyright 2020 RPANBot

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from discord import CategoryChannel, TextChannel


from web.helpers.classes import Guild


def get_guild_icon(guild: Guild, size: int = 128, format: str = "jpg") -> str:
    if not guild.icon:
        return "https://discordapp.com/assets/322c936a8c8be1b803cd94861bdfa868.png"
    return f"https://cdn.discordapp.com/icons/{guild.id}/{guild.icon}.{format}?size={size}"


def is_text_channel(channel) -> bool:
    return isinstance(channel, TextChannel)


def is_category_channel(channel) -> bool:
    return isinstance(channel, CategoryChannel)
