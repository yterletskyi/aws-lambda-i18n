# aws-lambda-i18n
Internationalization &amp; localization made easy for AWS lambda functions

The library is intended to use as an AWS Lambda Layer to localize backend API responses.

The library looks at the `Accept-Language` header of the HTTP request to determine what language to return message on.


Usage:
1. Implement your Lambda function to handle exceptions like this:

    ```python   
    try:
        ...
    except Exception as e:      
        from aws_lambda_i18n imort message_provider        
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
            'uk': 'Користувача не знайдено. Зверніться до служби підтримки.'            
        },
       'UnknownError': {
            'en': 'Unknown error happened. Please, contact support.',
            'uk': 'Сталася невідома помилка. Зверніться до служби підтримки.'            
       }
   }
   ```
  
  3. Upload the `aws_lambda_i18n.py` as an AWS Lambda Layer to your Lambda function.
  

