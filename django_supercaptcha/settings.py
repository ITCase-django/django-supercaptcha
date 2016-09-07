# -*- coding: utf-8 -*-

from os.path import join, dirname, abspath

from django.conf import settings


SELF_DIR = dirname(abspath(__file__))
FONTS_DIR = join(SELF_DIR, 'fonts')

SYMBOLS = getattr(settings, 'CAPTCHA_SYMBOLS',
                  '123456789ABCDEFGHJKLMNPQRSTVXYZ')
LENGTH = getattr(settings, 'CAPTCHA_LENGTH', 4)

AVAIL_FONTS = getattr(settings, 'CAPTCHA_FONTS', [
        ('boneca', join(FONTS_DIR, 'boneca.ttf')),
        ('acidic', join(FONTS_DIR, 'acidic.ttf')),
])

FOREGROUND_COLORS = getattr(settings, 'CAPTCHA_FOREGROUND_COLORS', (
    (0, 0, 0),
    (0x77, 0, 0),
    (0, 0x77, 0),
    (0, 0, 0x77),
))

COLORIZE_SYMBOLS = getattr(settings, 'CAPTCHA_COLORIZE_SYMBOLS', True)

BACKGROUND_COLOR = getattr(settings, 'CAPTCHA_BACKGROUND_COLOR',
                           (255, 255, 255))

FILTER_CHAIN = getattr(settings, 'CAPTCHA_FILTER_CHAIN', [])

VERTICAL_JUMP = getattr(settings, 'CAPTCHA_VERTICAL_JUMP', True)

SIZE = getattr(settings, 'CAPTCHA_SIZE', (120, 50))
ALT = getattr(settings, 'CAPTCHA_ALT', 'No robots here')
TITLE = getattr(settings, 'CAPTCHA_TITLE', 'No robots here')
FORMAT = getattr(settings, 'CAPTCHA_FORMAT', ('JPEG', 'image/jpeg'))

CACHE_PREFIX = getattr(settings, 'CAPTCHA_CACHE_PREFIX', 'captcha')

DEFAULT_ERROR_MESSAGE = getattr(settings, 'CAPTCHA_DEFAULT_ERROR_MESSAGE',
                                u'The code you entered is wrong')

REFRESH_LINK_TEXT = getattr(settings, 'CAPTCHA_REFRESH_LINK_TEXT',
                            u'refresh?')

REFRESH = getattr(settings, 'CAPTCHA_REFRESH', True)

HTML_TEMPLATE = getattr(
    settings,
    'CAPTCHA_HTML_TEMPLATE',
    """
    <div class="captcha">
        <div class="captcha-image">
            <span class="captcha-image__image">
                <img id="captcha_field_image"
                     width="%(width)s"
                     height="%(height)s"
                     src="%(src)s?%(rnd)s"
                     title="%(title)s"
                     alt="%(alt)s" />
            </span>
        </div>
        <div class="captcha-input">
            <input%(input_attrs)s maxlength="%(length)s"
                   class="captcha-input__input" />
        </div>
    </div>
    """
)

HTML_TEMPLATE_WITH_REFRESH = getattr(
    settings,
    'CAPTCHA_HTML_TEMPLATE_WITH_REFRESH',
    """
    <div class="captcha">
        <div class="captcha-image">
            <span class="captcha-image__image">
                <img id="captcha_field_image"
                     width="%(width)s"
                     height="%(height)s"
                     src="%(src)s?%(rnd)s"
                     title="%(title)s"
                     alt="%(alt)s" />
            </span>
            <a href="#refresh" class="captcha__link" onclick="var
               img=document.getElementById('captcha_field_image');
               img.src=img.src.substring(0,img.src.indexOf('?')+1)+Math.random();
               return false;">%(refresh_text)s</a>
        </div>
        <div class="captcha-input">
            <input%(input_attrs)s maxlength="%(length)s"
                   class="captcha-input__input" />
        </div>
    </div>
    """
)
