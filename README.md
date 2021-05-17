# Function_Handler
Allows you to take functions and make a list of them.
# How to use it?
I have a great logger that works perfectly in collaboration with this handler. I will give an example with it, but you can use it without it.
🙃
``` python
dict_for_methods = {} - list of methods

def message_handler(*argss):
    def message_dec(fn):
        dict_for_methods[tuple(argss)] = fn

        def message_wrap(*args):
            return args

        return message_wrap

    return message_dec
    
@message_handler('replace', 'replace_it', 'реплейс', 'замени') # Specify here the names by which you will then call this function
@logger.logger('Replace func!') # Info for logger
def replace_time(lower):
    params = {'chat_id': 14, 'message': (time.time()) - int(lower), 'random_id': 0, 'access_token': vk_dark_api.token,
              'v': vk_dark_api.v}
    print(params)
    
@message_handler('Список', 'list', 'list_of_list', 'LISTLISTLIST') # Specify here the names by which you will then call this function
@logger.logger('Replace func!') # Info for logger
def replace_time(lower):
    params = {'LIIIIIIIIIST': lower}
    print(params)
    
text = input() #if text == LISTLISTLIST BAN BAN BAN, he send to you this.
for i in dict_for_methods:
  for z in i:
    if re.search(z, text):
      dict_for_methods[i](text)
      
```
This is convenient for various APIs, such as VK_API, TELEGRAM, DISCORD, ETC.
