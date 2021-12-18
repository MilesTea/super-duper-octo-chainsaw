import datetime


def logger(path):
	def _logger_(function):
		def new_function(*args, **kwargs):
			when = datetime.datetime.now()
			name = function.__name__
			str_args = str()
			if args:
				str_args += str(args)
			if kwargs:
				str_args += str(kwargs)
			result = function(*args, **kwargs)
			log = [f'When: {when}\n',
				   f'Function name: {name}\n',
				   f'Function arguments: {str_args}\n',
				   f'Function result: {result}\n']
			with open(path, 'a', encoding='utf-8') as file:
				file.writelines(log)
				file.write('\n')
			return result

		return new_function

	return _logger_


@logger(path='log.txt')
def flat_generator(raw_list):
	counter = 0
	length = len(raw_list)
	while counter < length:
		if isinstance(raw_list[counter], list):
			for item in flat_generator(raw_list[counter]):
				yield item
			counter += 1
		else:
			yield raw_list[counter]
			counter += 1


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

print(flat_generator(nested_list))
