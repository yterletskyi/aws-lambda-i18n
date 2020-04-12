from unittest import TestCase

import aws_lambda_i18n


class TestMessageProvider(TestCase):
    mp = aws_lambda_i18n.build_message_provider()

    def test_error_not_exist(self):
        request = {
            'headers': {
                'Accept-Language': 'uk'
            }
        }
        message = self.mp.message_for(request, 'SomeNotDefinedError')
        self.assertEqual(message, aws_lambda_i18n.messages['UnknownError']['uk'])
