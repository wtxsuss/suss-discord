import discord
import random

# ----------------- INTENTS -----------------
intents = discord.Intents.default()
intents.message_content = True  
client = discord.Client(intents=intents)

# ----------------- DATA -----------------
troll_emojis = ["😭","🥀","😂","🙏","💀","😙","😛","🤡","🥸","💩","😹","😼","🐒","🦍","🦧","🗿","🫦","💏","💋","🫄"]

warn_replies = [
    "da da njan ninte veetil keeri paniyum",
    "da nirthedda ban aakm",
    "berthe show errakalla",
    "nee run cheythalum njan warn kodukumda",
    "appo next step ban aanu da 👊",
    "koorey aayi orutana pannit, hehe",
    "myra ninte kona nirthiko",
    "nee anna umpikkan valarnittilla, aada irri",
    "berthe chora kali aaakaruth",
]

column1_triggers = [
    "bot","nee","hello","ente","pani","kidu","love","machu","hi","hii","etha","edee",
    "va","ba","athey","njan","indo","njn","game","aa","lla","inda","ninte","ede","daa",
    "da","baa","vaa","kallikan","set","enna","end","para","mone","mowne","mon","onn",
    "ha","hh","roblox","minecraft","games","fr","ok","real","sheriya","bi","bye", "ann", "anne",
    "nalla","bera","reply","ith","ara","ithe","araa","naala","dey","deyy","appo","ella","illa"
]

column1_replies = [
    "എന്താ മച്ചാനെ!","അതൊരു കിടിലൻ കാര്യമാണല്ലോ!","ഓട പൊടെ","നീ കോണക്കഷ്ണം","മൈരെ പൊട്ടി വീഴും ലോക്കൽ",
    "അടിപൊളി ചന്തച്ചാക്കാ","പൊട്ടും പൊക്കിരിയുമാ","നീന്തി നടക്കുന്ന ലോസ്‌ട്ടാ","തല്ലി പറക്കുന്ന ഉളുക്കൻ",
    "നിന്റെ സ്റ്റൈൽ കണ്ടിട്ട് നായക്കും ചിരിക്കും","ഓട, കോമാളിയടെ","പൊട്ടിച്ചു നടക്കുന്ന സീരോ",
    "പൊട്ടൻ പെണ്ണാടി","നീ ഒരു full-time കോണ supplier","ചന്തപ്പുള്ളിപ്പൊട്ടെ","ഓട, double action പൊക്കിരി",
    "തള്ളിപ്പോയി troll item","കിടിലൻ local പൊട്ടക്കഷ്ണം","നീ oru budget മുത്തേ","single use പൊട്ടപ്പുലി",
    "പൊട്ടും പൊട്ടി കിടക്കുന്ന clown","പൊട്ടി പൊളിച്ചു നടക്കുന്ന local piece","ഓട, കോണ supplier",
    "നീ full-time ലോസ്","പൊട്ടിക്കളിയൻ പൊട്ടെ","അടിച്ചു പൊളിക്കുന്ന fake master","കോണ battery low",
    "budget പൊട്ടപ്പുലി","troll material പൊട്ട","shining ലോസ്‌ക്കെട്ടി","പൊട്ടി പൊട്ടുന്ന clown show",
    "half ticket പൊട്ടെ","market പൊട്ടൻ മുത്തേ","scene എടുക്കുന്ന പൊട്ടപ്പുലി","ഓട, ലോസ് kiddo",
    "പൊട്ടിക്കളി piece set","double action പൊട്ടെ","ഓട, ചുമ്മാ പൊളി ലോസ്","പൊട്ടി പൊട്ടുന്ന cartoon",
    "time waste പൊട്ടപ്പുലി","പൊളിച്ച് നടക്കുന്ന clown master","combo offer പൊട്ടൻ","ഓട, 1GB ലോസ്",
    "mood breaker പൊട്ടെ","പൊട്ടി പൊട്ടുന്ന TikTok star","duplicate പൊട്ടൻ brand","ഓട, ലോസ് limited edition",
    "പൊട്ടി പൊട്ടുന്ന side hero","tension പൊട്ടക്കഷ്ണം","പൊളിച്ചടുക്കുന്ന പൊട്ടൻ","free trial പൊട്ടപ്പുലി",
    "24x7 കോണ പൊട്ടെ","പൊട്ടി പൊളിച്ച പൊക്കിരി","ലോസ് unlimited","അടിപൊളി പൊട്ടൻ","കോണ edit master",
    "ചിരി പൊട്ടുന്ന ലോസ്","പൊട്ടൻ CPU hang","bug പൊട്ടപ്പുലി","lagging clown","പൊട്ടിക്കളിയൻ കിടിലൻ",
    "കോണ auto-reply പൊട്ടെ","ലോസ് simulator","troll പൊട്ടൻ app","cartoon പൊട്ടപ്പുലി","കോണ overload പൊട്ടെ",
    "പൊട്ടൻ beta version","ലോസ് trial pack","അടിപൊളി scene piece","ഞാനോ? ഞാൻ bot ആണല്ലോ 🙃","കുരുക്കുള്ള കാര്യങ്ങളാണേ!"
]

column2_triggers = [
    "govinda","chami","pooren","pooran","choppa","lottee","lotta","punde","myre","kunne","naayi","myr",
    "myran","punda","pundachi","umpi","poori","nayinde","pari","chopa","kunna","pode","ass","black",
    "kona","konnakand","polayadi","tayyoli","tacholi","govindaa","poora","umb","umbiko","myren",
    "patti","fuck","fck","naayinde","poda","andi","nigga","pass","employed","unemployed","kunije",
    "kuni","racist","etha","bitch","kune","nndi"
]

column2_replies = [
    "ഓട മൈരെ","ninde andi myra","poda myreee","podda kunne","kunna ump","podda tayyoli","kunijj taruoo",
    "umpe umpe umbb","oru 3some ne book cheyatte","myran enna konakiin","nee anna umpikkan aayitilla machu",
    "pari","poi ump","poi ump myreee","kuneeee","myreee kuni","andi undota nink hehee","nee eethada punde",
    "myren enna umpikkunee","myreeeee","kuninj taroo myreee","konaadikkkand poda mwthee","poda pooorimone",
    "eethada ee pooran","poi umpiko","kandarollli pooran","poda pooori","kunna poorimowleee","coppee",
    "chopaa myreee","chellakella myreee","pacha poorimon"
]

# ----------------- EVENTS -----------------
@client.event
async def on_ready():
    print(f'✅ Bot logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if msg.startswith("/warn"):
        if message.mentions:
            warned_user = message.mentions[0].mention
            reply = random.choice(warn_replies)
            emoji = random.choice(troll_emojis)
            await message.channel.send(f"{warned_user} {reply} {emoji}")
        else:
            await message.channel.send("Mention cheyyada aale warn cheyyan pattilla da 🤡")

    elif client.user in message.mentions:
        await message.channel.send("enda machu, ink enna bende😼 oru kali edukattee💋")

    elif any(word in msg for word in column1_triggers):
        reply = random.choice(column1_replies)
        emoji = random.choice(troll_emojis)
        await message.channel.send(f"{reply} {emoji}")

    elif any(word in msg for word in column2_triggers):
        reply = random.choice(column2_replies)
        emoji = random.choice(troll_emojis)
        await message.channel.send(f"{reply} {emoji}")

# ----------------- RUN BOT -----------------
client.run("DISCORD_TOKEN")
