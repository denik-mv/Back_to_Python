with open('sample.txt', mode='r') as sample_file:  # modes: r, w, a, r+, w+ etc.
    sample_data = sample_file.read()
print(sample_data)
