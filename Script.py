import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://www.google.com/')
    START_TXT = environ.get("START_TXT", "Please Set Welcome Message To View This")
    HELP_TXT = """<b>Hey {}
Here is the Help For My Commands</b>"""
    ONE_TXT = """<b>Hey {}
Here is the Help For My Commands</b>"""
    TWO_TXT = """<b>Hey {}
Here is the Help For My Commands</b>"""
    BIO_TXT = """ My Name: {}
Creator: <a href=https://t.me/kkhanyaseen>Yaseen</a>
Library: Pyrogram 
Language : Python"""
    ABOUT_TXT = """ My Name: {}
Creator: <a href=https://t.me/kkhanyaseen>Yaseen</a>
Library: Pyrogram 
Language : Python"""
    SOURCE_TXT =  """<b>NOTE:</b>
- ๐๐๐๐๐"""
    DONATION_TXT = """<b>๐๐จ๐ง๐๐ญ๐ข๐จ๐ง & ๐๐๐ข๐ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ข๐จ๐ง</b> 
โบโบ <b>๐๐จ๐ง๐๐ญ๐ข๐จ๐ง</b>
โชผ <b>๐๐จ๐ฎ ๐๐๐ง ๐๐จ๐ง๐๐ญ๐ ๐๐ง๐ฒ ๐๐ฆ๐จ๐ฎ๐ง๐ญ ๐๐จ๐ฎ ๐๐๐ฏ๐ ๐ณ. 
<b>โโโโโโโโโแ Payment Methods แโโโโโโโโโ
โฎ ๐๐ผ๐ผ๐ด๐น๐ฒ๐ฃ๐ฎ๐
โฎ ๐ฃ๐ฎ๐๐๐บ
โฎ ๐ฃ๐ต๐ผ๐ป๐ฒ๐ฃ๐ฒ
โฎ ๐ฃ๐ฎ๐๐ฃ๐ฎ๐น
_๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐จ๐ซ ๐๐ง๐จ๐ฐ ๐๐๐จ๐ฎ๐ญ ๐๐ก๐ ๐๐๐ฒ๐ฆ๐๐ง๐ญ ๐๐ง๐๐จ_
โโโโโโโโโโโโแ <a href=https://t.me/AboutAadhi><b>๊ช๊ชแฆ๊ซแป</b></a> แโโโโโโโโโโโโ
โบโบ <b>๐๐๐ข๐ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ข๐จ๐ง</b>
โชผ <b>๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐ข๐ญ๐ก ๐๐จ๐ฎ ๐๐จ๐ง๐ญ๐๐ง๐ญ ๐๐ก๐ข๐๐ก ๐๐จ๐ฎ ๐๐๐ง๐ญ ๐๐จ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ . 
<b>โโโโโโโโโแ Payment Methods แโโโโโโโโโ
โฎ ๐๐ผ๐ผ๐ด๐น๐ฒ๐ฃ๐ฎ๐
โฎ ๐ฃ๐ฎ๐๐๐บ
โฎ ๐ฃ๐ต๐ผ๐ป๐ฒ๐ฃ๐ฒ
โฎ ๐ฃ๐ฎ๐๐ฃ๐ฎ๐น
_๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐ข๐ญ๐ก ๐๐จ๐ฎ๐ซ ๐๐จ๐ง๐ญ๐๐ง๐ญ ๐๐ง๐ ๐๐ง๐จ๐ฐ ๐๐๐จ๐ฎ๐ญ ๐๐ก๐ ๐๐๐ฒ๐ฆ๐๐ง๐ญ ๐๐ง๐๐จ_
โโโโโโโโโโโโแ <a href=https://t.me/AboutAadhi><b>๊ช๊ชแฆ๊ซแป</b></a> แโโโโโโโโโโโโ"""
    PROMOTION_TXT = """<b>ใ ๐๐๐ข๐ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ข๐จ๐ง ใ</b>
โชผ <b>๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐ข๐ญ๐ก ๐๐จ๐ฎ ๐๐จ๐ง๐ญ๐๐ง๐ญ ๐๐ก๐ข๐๐ก ๐๐จ๐ฎ ๐๐๐ง๐ญ ๐๐จ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ . 
<b>โโโโโโโโโแ Payment Methods แโโโโโโโโโ
โฎ ๐๐ผ๐ผ๐ด๐น๐ฒ๐ฃ๐ฎ๐
โฎ ๐ฃ๐ฎ๐๐๐บ
โฎ ๐ฃ๐ต๐ผ๐ป๐ฒ๐ฃ๐ฒ
โฎ ๐ฃ๐ฎ๐๐ฃ๐ฎ๐น
_๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐ข๐ญ๐ก ๐๐จ๐ฎ๐ซ ๐๐จ๐ง๐ญ๐๐ง๐ญ ๐๐ง๐ ๐๐ง๐จ๐ฐ ๐๐๐จ๐ฎ๐ญ ๐๐ก๐ ๐๐๐ฒ๐ฆ๐๐ง๐ญ ๐๐ง๐๐จ_
โโโโโโโโโโโโแ <a href=https://t.me/AboutAadhi><b>๊ช๊ชแฆ๊ซแป</b></a> แโโโโโโโโโโโโ""" 
    FILE_TXT = """<b>Commands and Usage.</b>
/autofilter on - Enable auto filter.
/autofilter off - Disable auto filter.
/set_template - Set custom ษชแดแดส template."""
    WHOIS_TXT ="""<b>Commands and Usage</b>
/whois - For user details"""
    FUN_TXT ="""<b>Games</b> 
    
๐ฃ. /dice - Role The Dice
๐ค. /Throw ๐๐ /Dart - To Make Dart 
3. /Runs - Some Random Dialogues
4. /Goal or /Shoot - To Make a Goal or Shoot
5. /luck or /cownd - Spin And Try Your Luck"""
    DEPLOY_TXT = """<b>๐ท๐พ๐ ๐๐พ ๐ณ๐ด๐ฟ๐ป๐พ๐..? 
  
<b>โฎ Deploy Tutorial โบโบ</b> <i><b>https://youtu.be/kB9TkCs8cX0</b></i>
<b>๐ธ๐ต ๐๐พ๐ ๐๐ฐ๐ฝ๐ ๐๐ท๐ด ๐ฐ๐น๐ฐ๐-๐ฟ๐๐พ-๐ผ๐ฐ๐ ๐๐ด๐ฟ๐พ ๐ฒ๐พ๐ฝ๐๐ฐ๐ฒ๐ <a href=https://t.me/AboutAadhi>๐ฐ๐ฐ๐ณ๐ท๐ธ</a></b>
<b>๐๐ท๐ฐ๐๐ด ๐ฐ๐ฝ๐ณ ๐๐๐ฑ๐๐ฒ๐๐ธ๐ฑ๐ด</b>
๐ฒ๐๐ด๐ณ๐ธ๐๐ โบโบ <a href=https://t.me/MWUpdatez><b>๐ผ๐-๐๐ฟ๐ณ๐ฐ๐๐ด๐</b></a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and I will respond whenever a keyword is found the message

<b>NOTE:</b>
1. I should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """<b>Commands and Usage.</b>
</song Song Name>
๐ แดกแดสแดs แดษดสส แดษด ษขสแดแดแดs."""
    PIN_TXT ="""<b>Commands and Usage.</b>
/pin - To Pin The Message On Your Chat.
/unpin - To Unpin The Current Pinned Message."""
    PASTE_TXT = """<b>Commands and Usage.</b>
/paste [text] - paste the given text on Pasty
<b>NOTE:</b>
โข These commands works on both pm and group.
โข These commands can be used by any group member."""
    TTS_TXT = """<b>Commands and Usage.</b>
/tts <text> : convert text to speech
<b>NOTE:</b>
โข These commands works on both pm and group.
โข IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>Usage.</b>
/ping - To get your ping."""
    TELE_TXT = """<b>Commands and Usage.</b>
/telegraph - Send me Picture or Video Under (5MB)
<b>NOTE:</b>
This Command Is Available in goups and pms.
This Command Can be used by everyone."""

    PRIVATEBOT_TXT = """Hey {} I'm Alive."""

    JSON_TXT ="""<b>JSON:</b>
Bot returns json for all replied messages with /json
<b>Features:</b>
Message Editting JSON.
Pm Support.
Group Support."""
    PURGE_TXT = """<b>Usage.</b>
   
/purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- I Support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/kkhanyaseen)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<code>TOTAL FILES: {}</code>
<code>TOTAL USERS: {}</code>
<code>TOTAL CHATS: {}</code>
<code>USED STORAGE: {}</code>
<code>FREE STORAGE: {}</code>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
REPORT_TXT = """<b>Usage.</b>
/report ๐๐ @admins """

    CORONA_TXT = """/covid - Use This Command To know Covid informations.
Example:
<code>/covid India</code>"""

    URLSHORT_TXT = """This Command will Help You To short a Link.
<b>Usage: /short <link>
Example:
<code>/short https://t.me/ddrabit</code>"""

    VIDEO_TXT ="""<b>Youtube Video Downloader.</b>
<b>Usage:</b>
Type: /video <link>
Type: /mp4 <link>"""

    ZOMBIES_TXT = """<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>
<b>Commands and Usage.</b>
โข /inkick - command with required arguments and i will kick members from group.
โข /instatus - to check current status of chat member from group.
โข /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
โข /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
โข /dkick - to kick deleted accounts."""

    IMAGE_TXT = """<b>Commands and Usage.</b>
โข /imdb  - get the film information from IMDb source.
โข /search  - get the film information from various sources."""

    STICKER_TXT = """<b>Usage.</b>
/stickerid - Reply to any sticker for sticker id."""

    YTTHUMB_TXT = """<b>Youtube Video Thumbnail Downloader.</b>
Usage: /ytthumb <video link>
Example: /ytthumb https://youtu.be/UyzJ9KEoU0w"""

    ABOOK_TXT = """<b>You can convert a pdf file to a audio file with this command.</b>
<b>Commands and Usage.</b>
/audiobook - <b>Reply to PDF file to generate the audio.</b>"""

    GTRANS_TXT = """<b>Help: Gแดแดษขสแด Tสแดษดsสแดแดแดส
Tสแดษดsสแดแดแด แดแดxแดs แดแด แด sแดแดแดษชาษชแด สแดษดษขแดแดษขแด!
Cแดแดแดแดษดแดs แดษดแด Usแดษขแด: /tr [lang Code][reply] - แดสแดษดsสแดแดแด สแดแดสษชแดแด แดแดssแดษขแด แดแด sแดแดแดษชาษชแด สแดษดษขแดแดษขแด.
NOTE:
While Using /tr you should specify the language code.
Example:
โข en = english
โข ml = malayalam
โข hi = hindi
Type: /tr ml
For More Language Codes Click Here ๐</b>"""

    RESTRIC_TXT = """Some people need to be publicly banned; spammers, annoyances, or just trolls.
This module allows you to do that easily, by exposing some common actions, so everyone will see!
<b>Commands and Usage.</b>
/ban - Ban a user.
/unban - To unban a user.
/tban - Temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
/mute - To mute a user.
/unmute - To unmute a user.
/tmute - Temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks"""
    CREATOR_REQUIRED = """<b>You have To Be The Group Owner To Do That.</b>"""
      
    INPUT_REQUIRED = "**Arguments Required.**"
      
    KICKED = """โ๏ธ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """๐ฎ Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """<b>Im Not Admin Here. Add Me Again with all admin rights.</b>"""
      
    DKICK = """โ๏ธ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>Fetching User info...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
