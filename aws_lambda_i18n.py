SUPPORTED_LANGUAGES = ['en', 'uk', 'ru']
DEFAULT_LANGUAGE = 'en'

messages = {
    'UnknownError': {
        'en': 'Unknown error happened. Please, contact administrator.',
        'uk': 'Сталася невідома помилка. Зверніться до адміністратора.',
        'ru': 'Произошла неизвестная ошибка. Пожалуйста, обратитесь к администратору.'
    }
}


class LanguageParser:

    def parse(self, accept_language):
        parts = accept_language.split(',')
        results = []
        for part in parts:
            bits = part.split(';')
            ietf = bits[0].split('-')
            results.append(
                dict(
                    lang=ietf[0].strip(),
                    quality=float(bits[1].strip().split('=')[1]) if 1 < len(bits) else 1.0,
                    region=ietf[1].strip() if 1 < len(ietf) else None
                )
            )
        sorted(results, key=lambda x: x["quality"], reverse=True)
        return results[0]['lang']


class SafeLanguageParser:

    def __init__(self, accept_language_parser) -> None:
        super().__init__()
        self.accept_language_parser = accept_language_parser

    def parse(self, accept_language):
        try:
            language = self.accept_language_parser.parse(accept_language)
        except Exception:
            language = 'unknown'

        if language not in SUPPORTED_LANGUAGES:
            language = DEFAULT_LANGUAGE

        return language


class AWSLocaleProvider:

    def __init__(self, accept_language_parser) -> None:
        super().__init__()
        self.accept_language_parser = accept_language_parser

    def provide(self, request):
        if 'headers' in request:
            if 'Accept-Language' in request['headers']:
                value = request['headers']['Accept-Language']
                return self.accept_language_parser.parse(value)

        return DEFAULT_LANGUAGE


class MessageProvider:

    def __init__(self, locale_provider) -> None:
        super().__init__()
        self.locale_provider = locale_provider

    def message_for(self, request, key):
        locale = self.locale_provider.provide(request)
        if key in messages:
            return messages[key][locale]

        return messages['UnknownError'][locale]


def build_message_provider() -> MessageProvider:
    return MessageProvider(
        AWSLocaleProvider(
            SafeLanguageParser(
                LanguageParser()
            )
        )
    )
