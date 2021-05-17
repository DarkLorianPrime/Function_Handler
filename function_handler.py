
dict_for_methods = {}

def message_handler(*argss):
    def message_dec(fn):
        dict_for_methods[tuple(argss)] = fn

        def message_wrap(*args):
            return args

        return message_wrap

    return message_dec

for i in dict_for_methods:
	for z in i:
		if re.search(z, text):
			dict_for_methods[i](ARGUMENTS)