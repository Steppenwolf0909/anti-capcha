from twocaptcha import TwoCaptcha

solver = TwoCaptcha('7a12e1c410cdb7261261951423ea7f7a')

config = {
            'server':           '2captcha.com',
            'apiKey':           '7a12e1c410cdb7261261951423ea7f7a',
            'softId':            123,
            'callback':         'https://lessons.zennolab.com/captchas/hcaptcha/?level=easy',
            'defaultTimeout':    120,
            'recaptchaTimeout':  600,
            'pollingInterval':   10,
        }
solver = TwoCaptcha(**config)



result = solver.hcaptcha(sitekey='472fc7af-86a4-4382-9a49-ca9090474471',
  url='https://lessons.zennolab.com/captchas/hcaptcha/?level=easy')

print(result)

# http://2captcha.com/res.php?key=7a12e1c410cdb7261261951423ea7f7a&action=get&id=71265763992