from unittest import TestCase

from aws_lambda_i18n import messages
from aws_lambda_i18n import message_provider


class TestMessageProvider(TestCase):

    def test_error_not_exist(self):
        request = {
            'headers': {
                'Accept-Language': 'uk'
            }
        }
        message = message_provider.message_for(request, 'SomeNotDefinedError')
        self.assertEqual(message, messages['UnknownError']['uk'])
