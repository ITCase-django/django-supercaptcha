django-supercaptcha
===================

Captchafield for Django (based on `supercaptcha`_)


Install
=======

.. code-block:: bash

  pip install django-supercaptcha

Add ``django-supercaptcha`` to INSTALLED_APPS:

.. code-block:: python

  INSTALLED_APPS = (
      'django-supercaptcha',
  )

.. important::
    `Pillow`_ must be installed


Usage
=====

.. code-block:: python

    class MySuperForm(forms.Form):
        captcha = django_supercaptcha.CaptchaField(label=u"no robots here")


All you need, to get captcha working is properly configured cache backend and a route:


.. code-block:: python

    url(r'^captcha/(?P<code>[\da-f]{32})/$', 'django_supercaptcha.draw')



Options
=======

.. list-table::
  :widths: 10 20 5

  * - CAPTCHA_SYMBOLS
    - string with all symbols, which should be used in captcha.
    - ``default``: ``123456789ABCDEFGHJKLMNPQRSTVXYZ``
  * - CAPTCHA_LENGTH
    - length if captcha code.
    - ``default``: ``4``
  * - CAPTCHA_FONTS
    - the tuple of tuples with name - fullpath pair for each font which should be used
    -
  * - CAPTCHA_FOREGROUND_COLORS
    - tuple of tuples with colors for text. use one if if you want single color, for example ((0,0,0),) for black color
    -
  * - CAPTCHA_BACKGROUND_COLOR`
    - background color,
    - ``deafult``: ``(255, 255, 255)``
  * - CAPTCHA_FILTER_CHAIN
    - PIL filters, for example `('BLUR', 'SHARPEN',)`
    - ``default``: ``[]``
  * - CAPTCHA_VERTICAL_JUMP
    - defines if letters should "jump",
    - ``default``: ``True``
  * - CAPTCHA_SIZE
    - tuple defining size of captcha image
    - ``default`: ``(120, 50)``
  * - CAPTCHA_ALT
    - "alt" for image tag,
    - ``default``: ``no robots here``
  * - CAPTCHA_TITLE
    - "title" for image tag,
    - ``default``: ``no robots here``
  * - CAPTCHA_FORMAT
    - controls which format will be used for image encoding
    - ``default``: ``('JPEG', 'image/jpeg')``
  * - CAPTCHA_CACHE_PREFIX
    - defines which prefix should supercaptcha use for dealing with cache
    - ``default``: ``captcha``
  * - CAPTCHA_DEFAULT_ERROR_MESSAGE
    - defines default error message for wrong code
    - ``default``: ``The code you entered is wrong``
  * - CAPTCHA_REFRESH
    - defines if CaptchaField should show refresh link
    - ``default``: ``True``
  * - CAPTCHA_REFRESH_LINK_TEXT`
    - defines text of refresh link
    - ``default``: ``refresh?``
  * - CAPTCHA_HTML_TEMPLATE`
    - defines template of ``CaptchaField``, see example in settings ``settings.py``
    -
  * - CAPTCHA_HTML_TEMPLATE_WITH_REFRESH`
    - defines template of ``CaptchaField`` with refresh link, see example in ``settings.py``
    -

.. _django: http://djangoproject.com/
.. _supercaptcha: https://github.com/barbuza/supercaptcha/
.. _pillow: http://python-pillow.org/