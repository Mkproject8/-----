class script(object):
    START_TXT = """<b>๐ท๐ด๐ป๐พ {},
๐๐ โ๐ธ๐๐ผ โ๐ธ๐๐ผ ๐๐ ๐น๐ผ ๐โ๐๐ ๐ธ๐ <a href=https://t.me/{}>{}</a>,๐ โ๐ธโ โโ๐๐๐๐ป๐ผ ๐ธ ๐๐๐ ๐๐ฝ ๐๐๐๐๐ผ๐ ๐๐ ๐๐๐,๐๐๐๐ ๐ธ๐ป๐ป ๐๐ผ ๐๐ ๐๐๐โ ๐พโ๐๐โ ๐ธ๐ ๐ธ๐ป๐๐โ ,๐โ๐ผโ ๐๐ผ๐ผ ๐๐ โ๐๐๐ผโ๐๐๐ธ๐ ๐ธ๐น๐๐๐๐๐ ๐ฅ</b>"""
    COMMANDS_TXT = """๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐ผ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐."""
    ABOUT_TXT = """<b>โฎ ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด: {}</b>
<b>โฎ ๐ณ๐ด๐๐ด๐ป๐พ๐ฟ๐ด๐: <a href=https://t.me/doctor6689>๐แ ฯดแอฒฯดแก ๐</a></b>
<b>โฎ ๐ป๐ธ๐ฑ๐๐ฐ๐๐: ๐ฟ๐๐๐พ๐ถ๐๐ฐ๐ผ</b>
<b>โฎ ๐ป๐ฐ๐ฝ๐ถ๐๐ฐ๐ถ๐ด: ๐ฟ๐๐๐ท๐พ๐ฝ ๐น</b>
<b>โฎ ๐ณ๐ฐ๐๐ฐ ๐ฑ๐ฐ๐๐ด: ๐ผ๐พ๐ฝ๐ถ๐พ-๐ณ๐ฑ</b>
<b>โฎ ๐ฑ๐พ๐ ๐๐ด๐๐๐ด๐: ๐ท๐ด๐๐พ๐บ๐</b>
<b>โฎ ๐ฑ๐๐ธ๐ป๐ณ ๐๐๐ฐ๐๐๐: ๐3.0</b>
<b>โฎ ๐ถ๐๐พ๐๐ฟ: <a href=https://t.me/firstshowers>าแแกีอฒีแปฯดแแฌแกี๐ฅ</a></b>"""
    F_TXT = """แขแชแแฌ ฮฯด 3๐ฐ"""
    E_TXT = """แขแชแแฌ ฮฯด 2 ๐ฐ"""
    FONT_TXT = """<b>๐๐๐๐ป๐ธ๐๐ท ๐ต๐พ๐ฝ๐ ๐ผ๐พ๐ณ๐๐ป๐ด</b>
    
    <b>๐๐ท๐ธ๐ ๐ผ๐พ๐ณ๐๐ป๐ด ๐ฒ๐ฐ๐ฝ ๐ถ๐ธ๐๐ด ๐๐๐๐ป๐ธ๐๐ท ๐๐ด๐๐๐</b>
      <b>๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ</b>
      /font <๐๐ด๐๐>"""
    PASSGEN_TXT = """<b>๐ฟ๐ฐ๐๐๐๐พ๐๐ณ-๐ถ๐ด๐ฝ ๐ผ๐พ๐ณ๐๐ป๐ด</b>
  ๐๐ท๐ธ๐ ๐ผ๐พ๐ณ๐๐ป๐ด ๐ฒ๐ฐ๐ฝ ๐ถ๐ด๐ฝ ๐ฟ๐ฐ๐๐๐๐พ๐๐ณ
     <b>๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ</b>
   /genpw ๐๐ /genpassword"""

    SHARETXT_TXT = """๐ท๐๐๐: <๐>๐๐๐๐๐๐๐ ๐๐๐ก๐ ๐ผ๐๐๐๐๐ ๐๐๐ ๐๐ ๐๐๐๐๐๐ ๐ ๐๐๐๐ ๐๐ ๐๐๐๐๐ ๐๐๐ก๐ ๐๐ ๐๐๐ ๐๐๐๐๐๐๐๐.
<๐>๐ฒ๐๐๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐:โข /๐๐๐๐๐ (๐๐๐ก๐ ๐๐ ๐๐๐๐๐ข ๐๐ ๐๐๐๐๐๐๐)

<๐>๐ฝ๐พ๐๐ด:
โข lilly ๐๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐๐๐๐.
โข ๐๐๐๐๐ ๐๐๐๐๐๐๐๐ ๐ ๐๐๐๐ ๐๐ ๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐๐๐.
โข ๐๐๐๐๐ ๐๐๐๐๐๐๐๐ ๐๐๐ ๐๐ ๐๐๐๐ ๐๐ข ๐๐๐ข ๐๐๐๐๐ ๐๐๐๐๐๐."""

    SONG_TXT = """<b>๐๐พ๐ฝ๐ถ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐ผ๐พ๐ณ๐๐ป๐ด</b>
<b>๐๐พ๐ฝ๐ถ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐ผ๐พ๐ณ๐๐ป๐ด, ๐ต๐พ๐ ๐๐ท๐พ๐๐ด ๐๐ท๐พ ๐ป๐พ๐๐ด ๐ผ๐๐๐ธ๐ฒ. ๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐ด ๐๐ท๐ธ๐ ๐ต๐ด๐ฐ๐๐๐ด ๐ต๐พ๐ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐ฐ๐ฝ๐ ๐๐พ๐ฝ๐ถ ๐๐ธ๐๐ท ๐๐๐ฟ๐ด๐ ๐ต๐ฐ๐๐ ๐๐ฟ๐ด๐ด๐ณ.๐๐พ๐๐บ๐ ๐พ๐ฝ๐ป๐ ๐พ๐ฝ ๐ถ๐๐พ๐๐ฟ๐../</b>
<b>๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐</b>
โบโบ  /song or /music or /mp3 ๐๐พ๐ฝ๐ถ ๐ฝ๐ฐ๐ผ๐ด"""

    SHAZAM_TXT = """<b>๐๐ท๐ฐ๐๐ฐ๐ผ ๐ผ๐๐๐ธ๐ฒ ๐ต๐พ๐๐ฝ๐ณ๐ด๐ ๐ผ๐พ๐ณ๐๐ป๐ด</b>
- <b>๐ท๐ด๐ฟ๐ป=</b> ๐ท๐ด๐ป๐ฟ๐ ๐๐พ๐ ๐๐พ ๐๐ด๐ฒ๐พ๐ถ๐ฝ๐ธ๐๐ด | ๐ณ๐ธ๐๐ฒ๐พ๐๐ด๐ ๐ฐ ๐๐พ๐ฝ๐ถ
- <b>๐๐=</b> ๐๐ด๐ฝ๐ณ /Shazam (๐๐ด๐ฟ๐ป๐ ๐๐พ ๐ฐ ๐๐พ๐ฝ๐ถ ๐ต๐ธ๐ป๐ด)

<b>๐๐ท๐ฐ๐'๐ ๐๐ท๐ด ๐๐๐ด</b>
- ๐ณ๐พ ๐๐พ๐ ๐๐ฐ๐ฝ๐ ๐๐พ ๐บ๐ฝ๐พ๐ ๐ฐ ๐๐พ๐ฝ๐ถ ๐ฝ๐ฐ๐ผ๐ด ๐๐พ ๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐ท๐ด๐ฐ๐ ๐ธ๐ 
๐ณ๐พ๐ฝ'๐ ๐๐พ๐๐๐ ๐๐ด๐ฝ๐ณ /shazam"""
    LYRICS_TXT = """<b>๐ป๐๐๐ธ๐ฒ๐ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ณ๐ด ๐ผ๐พ๐ณ๐๐ป๐ด</b>
- ๐ธ๐ต ๐๐พ๐ ๐๐ฐ๐ฝ๐ ๐๐พ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ณ๐ด ๐ฐ ๐ป๐๐๐ธ๐ฒ, ๐ณ๐พ๐ฝ'๐ ๐๐ด๐ฐ๐๐ฒ๐ท ๐ต๐พ๐ ๐พ๐๐ท๐ด๐ ๐ฑ๐พ๐ ๐ท๐ด๐๐ด ๐ธ๐ ๐๐ท๐ด ๐ฐ๐ป๐ป ๐ธ๐ฝ ๐พ๐ฝ๐ด ๐ฑ๐พ๐
<b>๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ</b>
- /lyrics [๐๐พ๐ฝ๐ถ ๐ฝ๐ฐ๐ผ๐ด] - ๐๐พ ๐ถ๐ด๐ ๐๐ท๐ด ๐ป๐๐๐ธ๐ฒ๐
<b>๐๐๐ฐ๐ถ๐ด</b>
- ๐ฒ๐ฐ๐ฝ ๐ฑ๐ด ๐๐๐ด๐ณ ๐ฑ๐ ๐ด๐๐ด๐๐ ๐พ๐ฝ๐ด
- ๐๐พ๐๐บ๐ ๐พ๐ฝ๐ป๐ ๐ธ๐ฝ ๐ฑ๐พ๐ ๐ฟ๐ผ
<b>๐ฑ๐๐ถ</b>
๐๐พ๐ผ๐ด๐๐ธ๐ผ๐ด๐ ๐ธ๐ ๐๐ธ๐ป๐ป ๐๐ท๐พ๐ ๐ฐ๐ฝ ๐ด๐๐๐พ๐!"""
    IP_TXT = """<b>๐ธ๐ฟ ๐ฐ๐ณ๐ณ๐๐ด๐๐ ๐ต๐ธ๐ฝ๐ณ๐ด๐ ๐ผ๐พ๐ณ๐๐ป๐ด</b>
- ๐ธ๐ต ๐๐พ๐ ๐๐ฐ๐ฝ๐ ๐๐พ ๐ต๐ธ๐ฝ๐ณ ๐ณ๐ด๐๐ฐ๐ธ๐ป๐ ๐พ๐ต ๐ฐ ๐ธ๐ฟ ๐ฐ๐ณ๐ณ๐๐ด๐๐ ๐๐๐ด ๐๐ท๐ด ๐ผ๐พ๐ณ๐๐ป๐ด
<b>๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ</b>
- /ip [๐ธ๐ฟ ๐ฐ๐ณ๐ณ๐๐ด๐๐]
- ex /ip 192.180.0.1"""
    WIKI_TXT = """โ๐๐ธ๐บ๐ธ๐ฟ๐ด๐ณ๐ธ๐ฐ ๐ผ๐พ๐ณ๐๐ป๐ดโ
    
<b>๐ฑ๐ ๐๐๐ธ๐ฝ๐ถ ๐๐ท๐ธ๐ ๐ผ๐พ๐ณ๐๐ป๐ด ๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐ถ๐ด๐ ๐ธ๐ฝ๐ต๐พ๐๐ผ๐ฐ๐๐ธ๐พ๐ฝ ๐ต๐๐พ๐ผ ๐๐ธ๐บ๐ธ๐ฟ๐ด๐ณ๐ธ๐ฐ</b>

  <b>๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐</b>

/wiki ๐๐ /wikipedia {๐๐พ๐๐_๐๐ธ๐๐๐ป๐ด}"""
    FILE_TXT = """โค ๐๐๐ฅ๐ฉ: ๐๐ข๐ฅ๐ ๐๐ญ๐จ๐ซ๐ ๐๐จ๐๐ฎ๐ฅ๐../

<b> ๐๐ท๐ธ๐ ๐ผ๐พ๐ณ๐๐ป๐ด ๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐พ๐๐ด ๐ต๐ธ๐ป๐ด๐ ๐ธ๐ฝ ๐ผ๐ ๐ณ๐ฐ๐๐ฐ๐ฑ๐ฐ๐๐ด ๐ฐ๐ฝ๐ณ ๐ธ ๐๐ธ๐ป๐ป ๐ถ๐ธ๐๐ด ๐๐พ๐ ๐ฐ ๐ฟ๐ด๐๐ผ๐ฐ๐ฝ๐ด๐ฝ๐ ๐ป๐ธ๐ฝ๐บ  ๐๐พ ๐ฐ๐ฒ๐ฒ๐ด๐๐ ๐๐ท๐ด ๐๐ฐ๐๐ด๐ณ ๐ต๐ธ๐ป๐ด๐.๐ธ๐ต ๐๐พ๐ ๐๐ฐ๐ฝ๐ ๐๐พ ๐ฐ๐ณ๐ณ ๐ต๐ธ๐ป๐ด๐ ๐ต๐๐พ๐ผ ๐ฐ ๐ฟ๐๐ฑ๐ป๐ธ๐ฒ ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐ด๐ฝ๐ณ ๐๐ท๐ด ๐ต๐ธ๐ป๐ ๐ป๐ธ๐ฝ๐บ ๐พ๐ฝ๐ป๐  ๐พ๐ ๐๐พ๐ ๐๐ฐ๐ฝ๐ ๐๐พ ๐ฐ๐ณ๐ณ ๐ต๐ธ๐ป๐ด๐ ๐ต๐๐พ๐ผ ๐ฐ  ๐ฟ๐๐ธ๐๐ฐ๐๐ด ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐พ๐ ๐ผ๐๐๐ ๐ผ๐ฐ๐บ๐ด ๐ผ๐ด ๐ฐ๐ณ๐ผ๐ธ๐ฝ ๐พ๐ฝ ๐๐ท๐ด ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐พ ๐ฐ๐ฒ๐ฒ๐ด๐๐ ๐ต๐ธ๐ป๐ด๐...//</b>

โชผ ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐ โบ

โช /plink โบโบ <b>๐๐ด๐ฟ๐ป๐ ๐๐พ ๐ฐ๐ฝ๐ ๐ผ๐ด๐ณ๐ธ๐ฐ ๐๐พ ๐ถ๐ด๐ ๐ป๐ธ๐ฝ๐บ.</b>
โช /pbatch โบโบ <b>๐๐๐ด ๐๐พ๐๐ ๐ผ๐ด๐ณ๐ธ๐ฐ ๐ป๐ธ๐ฝ๐บ ๐๐ธ๐๐ท ๐๐ท๐ธ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ.</b>
โช /batch โบโบ <b>๐๐พ ๐ฒ๐๐ด๐ฐ๐๐ด ๐ป๐ธ๐ฝ๐บ ๐ต๐พ๐ ๐ผ๐๐ป๐๐ธ๐ฟ๐ป๐ด ๐ต๐ธ๐ป๐ด๐.</b>

โชผ ๐๐ฑ๐๐ฆ๐ฉ๐ฅ๐ โบ

<code>/batch https://t.me/LunaSupports/3 https://t.me/LunaSupports/8</code>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- ๐ถ๐ธ๐๐ด ๐๐พ๐๐ ๐ณ๐ด๐๐ฐ๐ธ๐ป๐
โข/whois :-give a user full details"""
    FUN_TXT ="""<b>Gแดแดแดs</b> 
    
<b>โก ๐น๐๐๐ ๐๐พ๐ผ๐ด ๐บ๐ธ๐ฝ๐ณ ๐พ๐ต ๐ต๐๐ฝ ๐๐ท๐ธ๐ฝ๐ถ'๐ โก</b>
 
๐ฃ. /dice - ๐๐พ๐ป๐ด ๐๐ท๐ด ๐ณ๐ธ๐ฒ๐ด 
๐ค. /Throw ๐๐ /Dart - ๐๐พ ๐ผ๐ฐ๐บ๐ด ๐ณ๐ฐ๐๐ 
3. /Runs - ๐๐พ๐ผ๐ด ๐๐ฐ๐ฝ๐ณ๐พ๐ผ ๐ณ๐ธ๐ฐ๐ป๐พ๐ถ๐๐ด๐ 
4. /Goal or /Shoot - ๐๐พ ๐ผ๐ฐ๐บ๐ด ๐ฐ ๐ถ๐พ๐ฐ๐ป ๐พ๐ ๐๐ท๐พ๐พ๐
5. /luck or /cownd - ๐๐ฟ๐ธ๐ฝ ๐ฐ๐ฝ๐ณ ๐๐๐ ๐๐พ๐๐ ๐ป๐๐ฒ๐บ"""
    MANUELFILTER_TXT = """๐ท๐ด๐ป๐ฟ: <b>๐ผ๐ฐ๐ฝ๐๐ด๐ป๐ต๐ธ๐ป๐๐ด๐</b>

- Filter is the feature were users can set automated replies for a particular keyword and LUNA will respond whenever a keyword is found the message

<b>NOTE:</b>
1. lilly should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    YTSEARCH_TXT = """<b>๐๐ ๐๐ธ๐ณ๐ด๐พ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐ผ๐พ๐ณ๐๐ป๐ด</b>

<b>๐๐ ๐๐ธ๐ณ๐ด๐พ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐ผ๐พ๐ณ๐๐ป๐ด, ๐ต๐พ๐ ๐๐ท๐พ๐๐ด ๐๐ท๐พ ๐ป๐พ๐๐ด ๐ผ๐๐๐ธ๐ฒ. ๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐ด ๐๐ท๐ธ๐ ๐ต๐ด๐ฐ๐๐๐ด ๐ต๐พ๐ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐ฐ๐ฝ๐ ๐๐ธ๐ณ๐ด๐พ ๐๐พ๐ธ๐ฒ๐ด ๐ฐ๐ฝ๐ณ ๐ฑ๐ถ๐ผ ๐ป๐ธ๐บ๐ด ๐๐พ๐๐๐๐ฑ๐ด ๐๐ธ๐๐ท ๐๐๐ฟ๐ด๐ ๐ต๐ฐ๐๐ ๐๐ฟ๐ด๐ด๐ณ.๐๐พ๐๐บ๐ ๐พ๐ฝ๐ป๐ ๐พ๐ฝ ๐ถ๐๐พ๐๐ฟ๐../</b>

<b>๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐ด ๐๐ท๐ธ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ ๐ต๐พ๐ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ณ๐ธ๐ฝ๐ถ ๐๐ธ๐ณ๐ด๐พ๐ ๐ฐ๐ฝ๐ณ ๐๐พ๐ฝ๐ถ๐ ๐๐ธ๐๐ท ๐ท๐ด๐ป๐ฟ ๐พ๐ต ๐๐พ๐๐๐๐ฑ๐ด</b>

<b>๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐</b>

โบโบ  /search ๐๐ด๐ฐ๐๐ฒ๐ท๐ธ๐ฝ๐ถ ๐ฝ๐ฐ๐ผ๐ด 

๐๐พ๐๐บ๐ ๐พ๐ฝ๐ป๐ ๐พ๐ฝ ๐ถ๐๐พ๐๐ฟ

"""
    PIN_TXT ="""<b>PIN MODULE</b>
<b>๐ฟ๐ธ๐ฝ ๐ฐ ๐ผ๐ด๐๐๐ฐ๐ถ๐ด../</b>

<b>๐ฐ๐ป๐ป ๐๐ท๐ด ๐ฟ๐ธ๐ฝ ๐๐ด๐ป๐ฐ๐๐ด๐ณ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ ๐ฒ๐ฐ๐ฝ ๐ฑ๐ด ๐ต๐พ๐๐ฝ๐ณ ๐ท๐ด๐๐ด::</b>

<b>๐๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ ๐ฐ๐ฝ๐ณ ๐๐๐ฐ๐ถ๐ด๐</b>

โ /pin :- ๐๐พ ๐ฟ๐ธ๐ฝ ๐๐ท๐ด ๐ผ๐ด๐๐๐ฐ๐ถ๐ด ๐พ๐ฝ ๐๐พ๐๐ ๐ฒ๐ท๐ฐ๐๐
โ /unpin :- ๐๐พ ๐๐ฝ๐ฟ๐ธ๐ฝ ๐๐ท๐ด ๐ฒ๐๐๐๐ด๐ด๐ฝ๐ ๐ฟ๐ธ๐ฝ๐ฝ๐ด๐ณ ๐ผ๐ด๐๐ฐ๐ฐ๐ถ๐ด"""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

โข /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

โข These commands works on both pm and group.
โข These commands can be used by any group member."""
    TTS_TXT = """Help: <b> TTS ๐ค module:</b>

๐๐๐ฐ๐ฝ๐๐ป๐ฐ๐๐ด ๐๐ด๐๐ ๐๐พ ๐๐ฟ๐ด๐ด๐ฒ๐ท

<b>Commands and Usage:</b>

โข /tts <text> : convert text to speech

<b>NOTE:</b>

โข lilly should have admin privillage.
โข These commands works on both pm and group.
โข lilly can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>๐ Ping:</b>

๐ท๐ด๐ป๐ฟ๐ ๐๐พ ๐๐พ๐ ๐บ๐ฝ๐พ๐๐ ๐๐พ๐๐ ๐ฟ๐ธ๐ฝ๐ถ ๐ถ๐ผโโ๏ธ

<b>Commands:</b>

โข /alive - To check you are alive.
โข /commands - To get help.
โข /ping - To get your ping.
โข /repo - Source Code.
โข /channel - Channel Details.
โข /luna - Bot Link.
<b>๐นUsage๐น :</b>

โข This commands can be used in pms and groups
โข This commands can be used buy everyone in the groups and bots pm
โข Share us for more features"""
    TELE_TXT = """<b>โซ๏ธHELP: Telegraphโช๏ธ</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

๐น /telegraph ๐๐ /tgraph ๐๐ /tmedia- ๐๐ด๐ฝ๐ณ ๐ผ๐ด ๐ฟ๐ธ๐ฒ๐๐๐๐ด ๐พ๐ ๐๐ธ๐ณ๐ด๐พ ๐๐ฝ๐ณ๐ด๐ (5๐ผ๐ฑ)

<b>NOTE:</b>

โข This Command Is Available in goups and pms
โข This Command Can be used by everyone"""

    PRIVATEBOT_TXT = """<b>๐ฟ๐๐ธ๐๐ฐ๐๐ด ๐ฑ๐พ๐ ๐ต๐พ๐ ๐๐พ๐</b>
<b>โบโบ ๐ณ๐พ ๐๐พ๐ ๐๐ฐ๐ฝ๐ ๐ฐ ๐ฑ๐พ๐ ๐๐ฐ๐ผ๐ด ๐ป๐ธ๐บ๐ด ๐๐ท๐ธ๐</b>
<b>โบโบ ๐๐ธ๐๐ท ๐ฐ๐ป๐ป ๐๐พ๐๐ ๐ฒ๐๐ด๐ณ๐ธ๐๐</b>
<b>โบโบ ๐๐ธ๐๐ท ๐๐พ๐๐ ๐พ๐๐ฝ๐ด๐๐๐ท๐ธ๐ฟ</b>
<b>โบโบ ๐ฒ๐พ๐ฝ๐๐ฐ๐ฒ๐ ๐ผ๐ด <a href=https://t.me/AboutAadhi>๐ฐ๐ฐ๐ณ๐ท๐ธ</a></b>"""

    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """<b>Purge</b>
    
๐ณ๐ด๐ป๐ด๐๐ด ๐ป๐พ๐ ๐พ๐ต ๐ผ๐ด๐๐๐ฐ๐ถ๐ด๐ ๐ต๐๐พ๐ผ ๐ถ๐๐พ๐๐ฟ! 
    
 <b>ADMIN</b> 

โ /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>

-LILLY Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. LILLY supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Tamil_moviesdaa)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐พ๐ฝ/๐พ๐ต๐ต ๐ผ๐พ๐ณ๐๐ป๐ด..</b>

<b>๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐ธ๐ ๐๐ท๐ด ๐ต๐ด๐ฐ๐๐๐๐ด ๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐ฐ๐ฝ๐ณ ๐๐ฐ๐๐ด  ๐๐ท?? ๐ต๐ธ๐ป๐ด๐ ๐ฐ๐๐๐พ๐ผ๐ฐ๐๐ธ๐ฒ๐ฐ๐ป๐ป๐ ๐ต๐๐พ๐ผ ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐พ ๐ถ๐๐พ๐๐ฟ. ๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐ด ๐๐ท๐ด ๐ต๐พ๐ป๐ป๐พ๐๐ธ๐ฝ๐ถ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ ๐๐พ ๐พ๐ฝ ๐ฐ๐ฝ๐ณ ๐พ๐ต๐ต ๐๐ท๐ด ๐ฐ๐๐๐พ๐ต๐ธ๐ป๐๐ด๐ ๐ธ๐ฝ ๐๐พ๐๐ ๐ถ๐๐พ๐๐ฟ.../</b>

<b>๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ :-
<b>โบโบ /autofilter on - ๐ด๐ฝ๐ฐ๐ฑ๐ป๐ด ๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐ธ๐ฝ ๐๐ท๐ด ๐ถ๐๐พ๐๐ฟ๐.</b>
<b>โบโบ /autofilter off - ๐ณ๐ธ๐๐ฐ๐ฑ๐ป๐ด๐ณ ๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐ธ๐ฝ ๐๐ท๐ด ๐ถ๐๐พ๐๐ฟ๐.</b>
<b>โบโบ /set_template - ๐๐ด๐ ๐ฒ๐๐๐๐พ๐ผ ๐ธ๐ผ๐ณ๐ฑ ๐๐ด๐ผ๐ฟ๐ป๐ฐ๐๐ด ๐ต๐พ๐ ๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐.</b>
<b>โบโบ /get_template - ๐ถ๐ด๐ ๐ฒ๐๐๐๐ด๐ฝ๐ ๐ธ๐ผ๐ณ๐ฑ ๐๐ด๐ผ๐ฟ๐ป๐ฐ๐๐ด ๐พ๐ต ๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐.</b>"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. ๐พ๐ฝ๐ป๐ ๐ฐ๐ณ๐ผ๐ธ๐ฝ๐ ๐ฒ๐ฐ๐ฝ ๐ฐ๐ณ๐ณ ๐ฒ๐พ๐ฝ๐ฝ๐ด๐ฒ๐๐ธ๐พ๐ฝ.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
๐๐ท๐ด๐๐ด ๐ฐ๐๐ด ๐ด๐๐๐๐ฐ ๐ต๐ด๐ฐ๐๐๐๐ด๐ ๐พ๐ต 

<b>Commands and Usage:</b>
โข /id - <code>get id of a specifed user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
๐๐ท๐ธ๐ ๐ผ๐พ๐ณ๐๐ป๐ด ๐พ๐ฝ๐ป๐ ๐๐พ๐๐บ๐ ๐ต๐พ๐ ๐ผ๐ ๐ฐ๐ณ๐ผ๐ธ๐ฝ๐

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban_user  - <code>to ban a user.</code>
โข /unban_user  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """
โโโโโโโโโโโโโโโโโ
โโโโโโโโโโโโโโโโโ
<b>โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐:</b> <code>{}</code>
<b>โ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐:</b> <code>{}</code>
<b>โ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐:</b> <code>{}</code>
<b>โ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด:</b> <code>{}</code> ๐ผ๐๐ฑ
<b>โ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด:</b> <code>{}</code> ๐ผ๐๐ฑ"""
    DEVELOPER_TXT = """<b>๐พ๐๐ ๐ณ๐ด๐๐ด๐ป๐พ๐ฟ๐ด๐๐</b>
๐ถ๐๐๐"""
    LOG_TEXT_G = """ฮแฌแแแกฯดแฎแข
    
<b>โ ๐๐ซ๐จ๐ฎ๐ฉ โชผ {}(<code>{}</code>)</b>
<b>โ ๐๐จ๐ญ๐๐ฅ ๐๐๐ฆ๐๐๐ซ๐ฌ โชผ <code>{}</code></b>
<b>โ ๐๐๐๐๐ ๐๐ฒ โชผ {}</b>
"""
    LOG_TEXT_P = """ฮแฌแแฎีแฌแก
    
<b>โ ๐๐ - <code>{}</code></b>
<b>โ ๐๐๐ฆ๐ - {}</b>
"""
    REPORT_TXT = """โค ๐๐๐ฅ๐ฉ: Rแดแดแดสแด โ ๏ธ

๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐๐๐ ๐ ๐๐๐๐๐๐๐ ๐๐ ๐ ๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐๐๐๐๐๐๐๐ ๐๐๐๐๐. ๐ณ๐๐'๐ ๐๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐.

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช/report ๐๐ @admins - ๐ณ๐ ๐๐พ๐๐๐๐ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐บ๐ฝ๐๐๐๐ (๐๐พ๐๐๐ ๐๐ ๐บ ๐๐พ๐๐๐บ๐๐พ)."""

    CORONA_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ข๐๐๐๐ฝ

๐๐๐๐ ๐ฒ๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐  ๐๐๐๐๐ข ๐๐๐๐๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐ 

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช /covid - ๐๐๐พ ๐๐๐๐ ๐ผ๐๐๐๐บ๐๐ฝ ๐๐๐๐ ๐๐๐๐ ๐ผ๐๐๐๐๐๐ ๐๐บ๐๐พ ๐๐ ๐๐พ๐ ๐ผ๐๐๐๐ฝ๐พ ๐๐๐ฟ๐๐๐๐บ๐๐๐๐

โ๐ค๐๐บ๐๐๐๐พ:
<code>/covid ๐จ๐๐ฝ๐๐บ</code>"""

    URLSHORT_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ด๐๐ ๐๐๐๐๐๐๐พ๐

๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐๐ ๐ ๐๐๐ 

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช /short: ๐๐๐พ ๐๐๐๐ ๐ผ๐๐๐๐บ๐๐ฝ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐ ๐๐พ๐ ๐๐๐๐๐๐พ๐ฝ ๐๐๐๐๐

โ๐ค๐๐บ๐๐๐๐พ:
<code>/short https://youtu.be/CPuvm126KPA</code>"""

    VIDEO_TXT ="""๐ท๐ด๐ป๐ฟ ๐๐พ๐ ๐๐พ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐๐ธ๐ณ๐ด๐พ ๐ต๐๐พ๐ผ ๐๐พ๐๐๐๐ฑ๐ด.

โข ๐๐ด๐ข๐จ๐ฆ
๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ณ๐ด ๐ฐ๐ฝ๐ ๐๐ธ๐ณ๐ด๐พ ๐ต๐๐พ๐ผ ๐๐พ๐๐๐๐ฑ๐ด

๐๐ค๐ฌ ๐๐ค ๐๐จ๐
โข ๐๐บ๐ฑ๐ฆ /video or /mp4 ๐๐ฏ๐ฅ (https://youtu.be/9RVhig3kH3E)
โข ๐๐น๐ข๐ฎ๐ฑ๐ญ๐ฆ:
<code>/mp4 https://youtu.be/CPuvm126KPA</code>
<code>/video https://youtu.be/CPuvm126KPA</code>"""

    ZOMBIES_TXT = """๐ท๐ด๐ป๐ฟ ๐๐พ๐ ๐๐พ ๐บ๐ธ๐ฒ๐บ ๐๐๐ด๐๐

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
โข /inkick - command with required arguments and i will kick members from group.
โข /instatus - to check current status of chat member from group.
โข /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
โข /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
โข /dkick - to kick deleted accounts."""

    IMAGE_TXT = """โค ๐๐๐ฅ๐ฉ: Iแดแดษขแด

๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐ข ๐๐๐๐๐๐ข 

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช ๐น๐๐๐ ๐๐ด๐ฝ๐ณ ๐ผ๐ด ๐ฐ ๐ธ๐ผ๐ฐ๐ถ๐ด ๐๐พ ๐ด๐ณ๐ธ๐ โจ"""

    STICKER_TXT = """๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐ด ๐๐ท๐ธ๐ ๐ผ๐พ๐ณ๐๐ป๐ด ๐๐พ ๐ต๐ธ๐ฝ๐ณ ๐ฐ๐ฝ๐ ๐๐๐ธ๐ฒ๐บ๐ด๐๐ ๐ธ๐ณ.
โข ๐๐๐๐๐
๐๐พ ๐ถ๐ด๐ ๐๐๐ธ๐ฒ๐บ๐ด๐ ๐ธ๐ณ
 
  โญ ๐๐ค๐ฌ ๐๐ค ๐๐จ๐

โ ๐๐๐๐๐๐ข ๐๐ ๐๐๐๐๐๐๐ [/stickerid]"""

    YTTHUMB_TXT = """๐ท๐ด๐ป๐ฟ๐ ๐๐พ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐ฐ๐ฝ๐ ๐๐พ๐๐๐๐ฑ๐ด ๐๐ธ๐ณ๐ด๐พ ๐๐ท๐๐ผ๐ฑ๐ฝ๐ฐ๐ธ๐ป
    
โญ๐๐ค๐ฌ ๐๐ค ๐๐จ๐
๐๐บ๐ฑ๐ฆ /ytthumb ๐๐ฏ๐ฅ ๐๐ช๐ฅ๐ฆ๐ฐ ๐๐ช๐ฏ๐ฌ

โข ๐๐น๐ข๐ฎ๐ฑ๐ญ๐ฆ
<code>/ytthumb https://youtu.be/CPuvm126KPA</code>"""

    ABOOK_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ ๐๐ฝ๐๐๐ป๐๐๐

๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐ ๐ ๐ฟ๐ณ๐ต ๐๐๐๐ ๐๐ ๐ ๐๐๐๐๐ ๐๐๐๐ ๐ ๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐ โฏ

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช /audiobook: ๐ฑ๐พ๐๐๐ ๐๐๐๐ ๐ผ๐๐๐๐บ๐๐ฝ ๐๐ ๐บ๐๐ ๐ฏ๐ฃ๐ฅ ๐๐ ๐๐พ๐๐พ๐๐บ๐๐พ ๐๐๐พ ๐บ๐๐ฝ๐๐"""

    GTRANS_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ฆ๐๐๐๐๐พ ๐ณ๐๐บ๐๐๐๐บ๐๐พ๐

๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐๐๐๐๐๐ ๐ ๐๐๐ก๐ ๐๐ ๐บ๐๐ ๐๐๐๐๐๐๐๐๐ ๐ข๐๐ ๐ ๐๐๐. ๐๐๐๐ ๐๐๐๐๐๐๐ ๐ ๐๐๐๐ ๐๐ ๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐๐๐ โฏ

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช/tr - ๐ณ๐ ๐๐๐บ๐๐๐๐บ๐๐พ๐ ๐๐พ๐๐๐ ๐๐ ๐บ ๐๐๐พ๐ผ๐๐ฟ๐ผ ๐๐บ๐๐๐๐บ๐๐พ

โค ๐ญ๐๐๐พ:
๐ถ๐๐๐๐พ ๐๐๐๐๐ /tr ๐๐๐ ๐๐๐๐๐๐ฝ ๐๐๐พ๐ผ๐๐ฟ๐ ๐๐๐พ ๐๐บ๐๐๐๐บ๐๐พ ๐ผ๐๐ฝ๐พ

โ๐ค๐๐บ๐๐๐๐พ: /๐๐ ๐๐
โข ๐พ๐ = ๐ค๐๐๐๐๐๐
โข ๐๐ = ๐ฌ๐บ๐๐บ๐๐บ๐๐บ๐
โข ๐๐ = ๐ง๐๐๐ฝ๐"""

    RESTRIC_TXT = """โค ๐๐๐ฅ๐ฉ: Mแดแดแด ๐ซ

๐๐๐๐๐ ๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐๐ ๐ ๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐ ๐๐๐ ๐๐ ๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐๐๐๐๐ข.

โช/ban: ๐ณ๐ ๐ป๐บ๐ ๐บ ๐๐๐พ๐ ๐ฟ๐๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/unban: ๐ณ๐ ๐๐๐ป๐บ๐ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/tban: ๐ณ๐ ๐๐พ๐๐๐๐๐บ๐๐๐๐ ๐ป๐บ๐ ๐บ ๐๐๐พ๐.
โช/mute: ๐ณ๐ ๐๐๐๐พ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/unmute: ๐ณ๐ ๐๐๐๐๐๐พ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/tmute: ๐ณ๐ ๐๐พ๐๐๐๐๐บ๐๐๐๐ ๐๐๐๐พ ๐บ ๐๐๐พ๐.

โค ๐ญ๐๐๐พ:
๐ถ๐๐๐๐พ ๐๐๐๐๐ /tmute ๐๐ /tban ๐๐๐ ๐๐๐๐๐๐ฝ ๐๐๐พ๐ผ๐๐ฟ๐ ๐๐๐พ ๐๐๐๐พ ๐๐๐๐๐.

โ๐ค๐๐บ๐๐๐๐พ: /๐๐ป๐บ๐ 2๐ฝ ๐๐ /๐๐๐๐๐พ 2๐ฝ.
๐ธ๐๐ ๐ผ๐บ๐ ๐๐๐พ ๐๐บ๐๐๐พ๐: ๐/๐/๐ฝ. 
 โข ๐ = ๐๐๐๐๐๐พ๐
 โข ๐ = ๐๐๐๐๐
 โข ๐ฝ = ๐ฝ๐บ๐๐"""
    CREATOR_REQUIRED = """โ<b>๐๐พ๐ ๐ท๐ฐ๐๐ด ๐๐พ ๐ฑ๐ด ๐๐ท๐ด ๐ถ๐๐พ๐๐ฟ ๐ฒ๐๐ด๐ฐ๐๐ด๐ ๐๐พ ๐ณ๐พ ๐๐ท๐ฐ๐.</b>"""
      
    INPUT_REQUIRED = "โ **๐ฐ๐๐ถ๐๐ผ๐ด๐ฝ๐๐ ๐๐ด๐๐๐ธ๐๐ด๐ณ**"
      
    KICKED = """โ๏ธ ๐๐๐ฒ๐ฒ๐ด๐๐๐ต๐๐ป๐ป๐ ๐บ๐ธ๐ฒ๐บ๐ด๐ณ {} ๐ผ๐ด๐ผ๐ฑ๐ด๐๐ ๐ฐ๐ฒ๐ฒ๐พ๐๐ณ๐ธ๐ฝ๐ถ ๐๐พ ๐๐ท๐ด ๐ฐ๐๐ถ๐๐ผ๐ด๐ฝ๐๐ ๐ฟ๐๐พ๐๐ธ๐ณ๐ด๐ณ."""
      
    START_KICK = """๐ ๐๐ด๐ผ๐พ๐๐ธ๐ฝ๐ถ ๐ธ๐ฝ๐ฐ๐ฒ๐๐ธ๐๐ด ๐ผ๐ด๐ผ๐ฑ๐ด๐๐ ๐๐ท๐ธ๐ ๐ผ๐ฐ๐ ๐๐ฐ๐บ๐ด ๐ฐ ๐๐ท๐ธ๐ป๐ด..."""
      
    ADMIN_REQUIRED = """โ<b>๐ผ๐ด ๐ฐ๐ณ๐ผ๐ธ๐ฝ ๐ธ'๐ผ ๐ฝ๐พ๐ ๐ถ๐พ๐ธ๐ฝ๐ถ ๐ฐ๐ฝ๐๐๐ท๐ด๐๐ด ๐ฑ๐ธ๐ธ..๐ฐ๐ณ๐ณ ๐ผ๐ด ๐ฐ๐ถ๐ฐ๐ธ๐ฝ ๐๐ธ๐๐ท ๐ฐ๐ป๐ป ๐ฐ๐ณ๐ผ๐ธ๐ฝ ๐๐ธ๐ถ๐ท๐๐.</b>"""
      
    DKICK = """โ๏ธ  ๐บ๐ธ๐ฒ๐บ๐ด๐ณ {} ๐ณ๐ด๐ป๐ด๐๐ด๐ณ ๐ฐ๐ฒ๐ฒ๐พ๐๐ฝ๐๐ ๐๐๐ฒ๐ฒ๐ด๐๐๐ต๐๐ป๐ป๐."""
      
    FETCHING_INFO = """<b>๐ฝ๐พ๐ ๐ธ ๐ฒ๐ฐ๐ฝ ๐ฑ๐ด๐ฐ๐ ๐ด๐๐ด๐๐๐๐ท๐ธ๐ฝ๐ถ๐...</b>"""
      
    STATUS = """{}\n<b>๐ฒ๐ท๐ฐ๐ ๐ผ๐ด๐ผ๐ฑ๐ด๐ ๐๐๐ฐ๐๐๐</b>**\n\n```<i>๐๐ด๐ฒ๐ด๐ฝ๐๐ป๐``` - {}\n```๐๐ธ๐๐ท๐ธ๐ฝ ๐๐ด๐ฐ๐บ``` - {}\n```๐๐ธ๐๐ท๐ธ๐ฝ ๐ผ๐พ๐ฝ๐๐ท``` - {}\n```๐ป๐พ๐ฝ๐ถ ๐๐ธ๐ผ๐ด ๐ฐ๐ถ๐พ``` - {}\n๐ณ๐ด๐ป๐ด๐๐ด๐ณ ๐ฐ๐ฒ๐ฒ๐พ๐๐ฝ๐ - {}\n๐ฑ๐พ๐ - {}\n๐๐ฝ๐ฒ๐ฐ๐ฒ๐ท๐ด๐ณ - {}</i>
"""
