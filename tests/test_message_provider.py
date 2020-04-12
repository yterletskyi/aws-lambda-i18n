from unittest import TestCase

import app


class TestMessageProvider(TestCase):
    mp = app.build_message_provider()

    def test_error_not_exist(self):
        request = {
            'headers': {
                'Accept-Language': 'uk'
            }
        }
        message = self.mp.message_for(request, 'SomeNotDefinedError')
        self.assertEqual(message, app.messages['UnknownError']['uk'])
