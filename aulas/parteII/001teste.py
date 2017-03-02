def read_meta_data(path):
	data = open(path,"rt")
	meta_data = []
	for line in data:
		line_data = line.split("\t")
		meta_data.append((line_data[0],
						  line_data[1],
						  line_data[2]))
		#meta_data.append(*line_data)
	data.close()
	return meta_data

print(read_meta_data("data/meta-data/Instituicao.txt"))
