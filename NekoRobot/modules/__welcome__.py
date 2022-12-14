"""
MIT License
Copyright (C) 2017-2019, Paul Larsen
Copyright (C) 2022-2023, Awesome-Gtash
Copyright (c) 2022-2023, White Tiger • Network, <https://github.com/Awesome-Gtash/OrekiRobot-2>
This file is part of @OrekiXProRobot (Telegram Bot)
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the Software), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from telethon import Button

from NekoRobot import tbot as tbot
from NekoRobot.events import register

PHOTO = "https://te.legra.ph/file/4b0e1482be7287843d876.mp4"


@register(pattern=("Welcome"))
async def awake(event):
    OREKI = f" Hey Welcome To The Group, I hope u get many friends in this group"
    BUTTON = [
        [
            Button.url("  Updates 📢", "https://telegram.dog/Tiger_Updates"),
            Button.url(" Support 🛡️", "https://telegram.dog/Tiger_SupportChat"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=OREKI, buttons=BUTTON)
