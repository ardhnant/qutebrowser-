import themes
import datetime
themes.setup(c, 'macchiato', True)

# Load autoconfig (important if you used GUI settings before)
config.load_autoconfig()

# Disable autoplay and notifications
c.content.autoplay = False
c.content.notifications.enabled = False

# GPU acceleration and Wayland-friendly performance flags
c.qt.args = [
    '--enable-gpu-rasterization',
    '--ignore-gpu-blocklist',
    '--force-dark-mode',
    '--enable-zero-copy',
    '--enable-features=WebContentsForceDark,WebRTCPipeWireCapturer',
    '--enable-blink-features=ForceDarkMode',
    '--disable-accelerated-2d-canvas',
    '--disable-features=DocumentPictureInPictureAPI',
    '--disable-background-timer-throttling',
    '--use-gl=desktop',
]

# Smooth scrolling and faster scroll speed
c.scrolling.smooth = True
c.scrolling.bar = "when-searching"
config.bind("j", "scroll-px 0 100", mode="normal")
config.bind("k", "scroll-px 0 -100", mode="normal")

#Enableing Downloading logs 
config.bind('yd', 'spawn --userscript log-download')

# Enable adblock with multiple filter lists
c.content.blocking.method = "both"
c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt"
]

#Removing all the adds from the yt homepage
import os
from qutebrowser.api import interceptor

def auto_run_yt_cleaner(info):
    url = info.request_url.toString()
    if "youtube.com" in url:
        os.system("~/.config/qutebrowser/userscripts/yt-cleaner.js &")

interceptor.register(auto_run_yt_cleaner)

config.bind('yd', 'spawn --userscript log-download')
