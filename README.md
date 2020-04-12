# aws-lambda-i18n
Internationalization &amp; localization made easy for AWS lambda functions

The library is intended to use as an AWS Lambda Layer to localize backend API responses.

Usage:
1. Implement your use-case Lambda function to handle exceptions like this:

    ```python   
    try:
        token = token_retriver.retrieve(event)
        user_id = user_id_retriever.retrieve(token)
        appeals = provider.provide(user_id)
        return success({'appeals': appeals})
    except Exception as e:      
        message_provider = build_message_provider()
        if isinstance(e, UserNotFoundError):
            message = message_provider.message_for(event, 'UserNotFoundError')
        else:
            message = message_provider.message_for(event, 'UnknownError')            

        return error(message)   
    ```
           
2. Add respective messages to the `messages` dictionary in the `app` file:
    
   ```python
   
   messages = {
       'UserNotFoundError': {
            'en': 'User has not been not found. Please, contact support.',
            'uk': 'Користувача не знайдено. Зверніться до служби підтримки.',
            'ru': 'Пользователь не найден. Пожалуйста, свяжитесь со службой поддержки.'
        },
       'UnknownError': {
            'en': 'Unknown error happened. Please, contact support.',
            'uk': 'Сталася невідома помилка. Зверніться до служби підтримки.',
            'ru': 'Произошла неизвестная ошибка. Пожалуйста, свяжитесь со службой поддержки.'
       }
   }
   ```
  
  3. Upload the `aws_lambda_i18n.py` as an AWS Lambda Layer to your use-case Lambda function.
  

