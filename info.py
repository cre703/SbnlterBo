import re
from os import environ
from Script import script
from time import time

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    value = str(value).lower()
    if value in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

def parse_size_to_bytes(value: str, default: int = 0) -> int:
    if value is None:
        return default
    raw = str(value).strip().lower()
    if not raw:
        return default
    m = re.fullmatch(r"(\d+(?:\.\d+)?)\s*([kmgtp]?b?)?", raw)
    if not m:
        return default
    number = float(m.group(1))
    unit = (m.group(2) or "b").rstrip("b")
    scale = {
        "": 1,
        "k": 1024,
        "m": 1024**2,
        "g": 1024**3,
        "t": 1024**4,
        "p": 1024**5,
    }
    return int(number * scale.get(unit, 1))

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# OMDB API Key - IMPORTANT FOR IMDB
OMDB_API_KEY = environ.get('OMDB_API_KEY', '')  # <-- ADD THIS LINE
if not OMDB_API_KEY:
    print("⚠️ WARNING: OMDB_API_KEY not set! IMDB features will not work.")

# Keep-Alive URL
KEEP_ALIVE_URL = environ.get("KEEP_ALIVE_URL", "")

# Hyper link
HYPER_MODE = is_enabled(environ.get('HYPER_MODE', False), False)

# Request fsub
REQUEST_FSUB_MODE = is_enabled(environ.get('REQUEST_FSUB_MODE', True), True)

# Bot settings
BOT_START_TIME = time()
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', False), False)
PICS = (environ.get('PICS', 'https://graph.org/file/2ed90a79eb533d86f8a0f.jpg https://graph.org/file/a0da24dacf4b7bec376a3.jpg https://graph.org/file/457aa9d0e485925088be6.jpg https://graph.org/file/041f7b57c6950070ba16e.jpg https://graph.org/file/f36511f6042d74d95b5df.jpg https://graph.org/file/a30d30b3bc49bd8745533.jpg https://graph.org/file/ce71502cf614059ce1de5.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]  # Removed hardcoded default
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]  # Removed hardcoded default
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
DEFAULT_AUTH_CHANNELS = [int(x) for x in environ.get("AUTH_CHANNEL", "").split() if x.lstrip('-').isdigit()]
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'mn_files')
DATABASE_URI2 = environ.get('DATABASE_URI2', "")
DATABASE_URI3 = environ.get('DATABASE_URI3', "")
DATABASE_URI4 = environ.get('DATABASE_URI4', "")
DATABASE_URI5 = environ.get('DATABASE_URI5', "")
DATABASE_NAME2 = environ.get('DATABASE_NAME2', DATABASE_NAME)
DATABASE_NAME3 = environ.get('DATABASE_NAME3', DATABASE_NAME)
DATABASE_NAME4 = environ.get('DATABASE_NAME4', DATABASE_NAME)
DATABASE_NAME5 = environ.get('DATABASE_NAME5', DATABASE_NAME)
POSTGRES_URI = environ.get('POSTGRES_URI', '')
POSTGRES_STORAGE_LIMIT_BYTES = parse_size_to_bytes(environ.get('POSTGRES_STORAGE_LIMIT_BYTES', '1GB'), 0)

# File Channel Settings
FILE_CHANNELS = [int(ch) for ch in environ.get('FILE_CHANNELS', '').split()]  # Removed hardcoded default
FILE_CHANNEL_SENDING_MODE = is_enabled(environ.get('FILE_CHANNEL_SENDING_MODE', True), True)
FILE_AUTO_DELETE_SECONDS = int(environ.get('FILE_AUTO_DELETE_SECONDS', 0))  # Default: 0 means no auto-delete

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '')) if environ.get('LOG_CHANNEL') else None
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', False), False)

# IMDB Settings - ENSURE THESE ARE CORRECT
IMDB = is_enabled(environ.get('IMDB', True), True)  # Default True
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', False), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", script.CUSTOM_FILE_CAPTION if hasattr(script, 'CUSTOM_FILE_CAPTION') else "")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "📂 <em>File Name</em>: <code>{file_name}</code>\n\n ♻ <em>File Size</em>:{file_size} \n\n <b><i>Latest Movies -</i> </b>")

# Better IMDB Template with more details
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", 
    "🎬 <b>IMDB Details</b>\n\n"
    "🏷 <b>Title</b>: <a href={url}>{title}</a>\n"
    "📅 <b>Year</b>: {year}\n"
    "⭐️ <b>Rating</b>: {rating}/10\n"
    "🎭 <b>Genres</b>: {genres}\n"
    "🎬 <b>Language</b>: {languages}\n"
    "🌍 <b>Country</b>: {country}\n"
    "🎥 <b>Director</b>: {directors}\n"
    "✍️ <b>Writer</b>: {writers}\n"
    "🎭 <b>Actors</b>: {actors}\n"
    "📝 <b>Plot</b>: <i>{plot}</i>")

LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", True), True)  # Changed default to True
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", True), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", "5")  # Default to 5 to avoid too long messages
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL)) if LOG_CHANNEL else None
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split() if ch]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', True), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', False), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', True), True)

# Enhanced LOG_STR with OMDB status
LOG_STR = "="*50 + "\n"
LOG_STR += "🔧 CURRENT BOT CONFIGURATIONS\n"
LOG_STR += "="*50 + "\n\n"

LOG_STR += f"🤖 IMDB Status: {'✅ ENABLED' if IMDB else '❌ DISABLED'}\n"
if IMDB:
    LOG_STR += f"🔑 OMDB API Key: {'✅ SET' if OMDB_API_KEY else '❌ MISSING - IMDB WILL NOT WORK'}\n"
LOG_STR += f"📝 IMDB Template: {'✅ CUSTOM' if environ.get('IMDB_TEMPLATE') else '✅ DEFAULT'}\n"
LOG_STR += f"📖 Long IMDB Description: {'✅ ENABLED' if LONG_IMDB_DESCRIPTION else '❌ DISABLED'}\n"
LOG_STR += f"🔍 Spell Check Mode: {'✅ ENABLED' if SPELL_CHECK_REPLY else '❌ DISABLED'}\n"
LOG_STR += f"📋 Max List Elements: {MAX_LIST_ELM}\n\n"

LOG_STR += f"📤 P_TTI_SHOW_OFF: {'✅ ENABLED' if P_TTI_SHOW_OFF else '❌ DISABLED'}\n"
LOG_STR += f"🔘 SINGLE_BUTTON: {'✅ ENABLED' if SINGLE_BUTTON else '❌ DISABLED'}\n"
LOG_STR += f"🛡️ PROTECT_CONTENT: {'✅ ENABLED' if PROTECT_CONTENT else '❌ DISABLED'}\n\n"

LOG_STR += f"💾 Database Status:\n"
LOG_STR += f"  - MongoDB: {'✅ CONNECTED' if DATABASE_URI else '❌ NOT SET'}\n"
LOG_STR += f"  - PostgreSQL: {'✅ CONNECTED' if POSTGRES_URI else '❌ NOT SET'}\n\n"

LOG_STR += f"📢 Channels:\n"
LOG_STR += f"  - Source Channels: {len(CHANNELS)} channel(s) configured\n"
LOG_STR += f"  - File Channels: {len(FILE_CHANNELS)} channel(s) configured\n"
LOG_STR += f"  - Log Channel: {'✅ SET' if LOG_CHANNEL else '❌ NOT SET'}\n\n"

LOG_STR += f"👥 Admins: {len(ADMINS)} admin(s) configured\n"
LOG_STR += f"👤 Auth Users: {len(AUTH_USERS)} user(s) configured\n"
LOG_STR += "="*50

# Print configuration on startup
print(LOG_STR)

# Warning if OMDB_API_KEY missing when IMDB is enabled
if IMDB and not OMDB_API_KEY:
    print("\n" + "="*50)
    print("⚠️  WARNING ⚠️")
    print("="*50)
    print("IMDB is ENABLED but OMDB_API_KEY is MISSING!")
    print("Please add OMDB_API_KEY in environment variables.")
    print("Get your free API key from: https://www.omdbapi.com/apikey.aspx")
    print("="*50 + "\n")
