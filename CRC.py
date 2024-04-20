class CRC:
	
	def __init__(self):
		# Initialize an empty string to store the encoded data
		self.encoded_data = ''
    
	def get_encoded_data(self):
		# Method to print the encoded data
		print(self.encoded_data)
    
	def xor(self, operand_a, operand_b):
		# Method to perform XOR operation between two binary strings
		result = []
		for i in range(1, len(operand_b)):
			if operand_a[i] == operand_b[i]:
				result.append('0')
			else:
				result.append('1')
		return ''.join(result)

	def calculate_crc(self, data, key):
		# Method to calculate the CRC remainder for given data and key
		key_length = len(key)
		tmp = data[:key_length]

		while key_length < len(data):
			if tmp[0] == '1':
				tmp = self.xor(key, tmp) + data[key_length]
			else:
				tmp = self.xor('0' * key_length, tmp) + data[key_length]
			key_length += 1

		if tmp[0] == "1":
			tmp = self.xor(key, tmp)
		else:
			tmp = self.xor('0' * key_length, tmp)

		crc_result = tmp
		return crc_result

	def encode_data(self, data, key):
		# Method to encode data using CRC
		key_length = len(key)
		appended_data = data + ('0' * (key_length - 1))
		remainder = self.calculate_crc(appended_data, key)
		encoded_data = data + remainder
		self.encoded_data += encoded_data
		print("Remainder: ", remainder)
		print("Data: ", encoded_data)

	def decode_data(self, data, key):
		# Method to decode data and check for errors using CRC
		key_length = len(key)
		recalculated_crc = self.calculate_crc(data, key)
		if recalculated_crc == '0' * (key_length - 1):
			print("No Error")
		else:
			print("Error")


if __name__ == "__main__":
	# Prompt the user to enter data and key
	data_input = input('Enter your Data : ')
	key_input = input('Enter your Key  : ')
	print('---------------')
	# Create an instance of the CRC class
	crc_instance = CRC()
	# Encode the input data using CRC
	crc_instance.encode_data(data_input, key_input)
	print('---------------')
	# Decode the encoded data and check for errors using CRC
	crc_instance.decode_data(crc_instance.encoded_data, key_input)
	print('---------------')
	# Print the encoded data
	crc_instance.get_encoded_data()
