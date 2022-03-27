# Buat file config.py baru dalam dir dan impor yang sama, kemudian perpanjang kelas ini.
class Config(object):
	LOGGER = True
	
	# Must be filled!
	# Register here: https://my.telegram.org/apps
	api_id = 2171111
	api_hash = "fd7acd07303760c52dcc0ed8b2f73086"
	DATABASE_URL = "postgres://kottsxgfntflwf:ba539e7c8cc8f7ea779c6a815360ef86975df2f5ab3596b56a6afd052fa53535@ec2-44-194-92-192.compute-1.amazonaws.com:5432/dcmcmtkf3j0vao" # Your database URL

	# Version
	lang_code = "en" # Your language code
	device_model = "PC" # Device model
	system_version = "Linux" # OS system type

	# Required for some feature
	Command = ["!", "."] # Insert command prefix, if you insert "!" then you can do !ping
	# WORKER must be int (number)
	NANA_WORKER = 8
	# If True, send notification to user if Official branch has new update after running bot
	REMINDER_UPDATE = True

	# APIs token
	thumbnail_API = "ab333d1ebce60c50dde9af815b9490cc71a29a5e2a76" # Register free here: https://thumbnail.ws/
	screenshotlayer_API = "" # Register free here: https://screenshotlayer.com/
	lydia_API = ""

	# Load or no load plugins
	# userbot
	USERBOT_LOAD = []
	USERBOT_NOLOAD = []

	# Fill this if you want to login using session code, else leave it blank
	USERBOT_SESSION = "BQCE3qvLuM98iRLrUVb4mvHsyhoVr22KVg-leOvKrP1whNPudWGvvCSsodCVlbc5UOWyM3wK5U2WLin27FgQDY7n9_mrr7pZu-8rtw2V1FZuLhh-Fl-UPFajSVWUnfodJVn4bhWCXVwQx7rpGxJ5WbdYUZaRzw0aKiSFiu2M4YmED6F4J66NAvvtHsU51wvSkHrDGZj1aw4Ce-C-r2lntitJC7M5Oydq3gfd1WSz0kE_csLc8vo1Bgk-RSbKI3yYXzqAct3YgQRT1tV7ikjveE3fQRpg-dGvnWscrKhnnFChs5SPgLBcgjec9hVAu5d7-7SwBkZOR0DOmvkkZjfUePSKQPDjbQA"

	# Google drive API, open client_secrets.json file, copy all text, and paste into """{THIS IS API}"""
	#   If you dont have, leave it blank!
	GOOGLE_API_TEXT = """Replace this text with your API"""

	# Bitly API, register at https://dev.bitly.com/my_apps.html
	BITLY_API = ""

	# Pass True if you want to use test mode
	TEST_MODE = False
	

class Production(Config):
	LOGGER = False


class Development(Config):
	LOGGER = True
