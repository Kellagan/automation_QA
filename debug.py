data1 = ['notes', 'react', 'veu', 'private', 'wordFile']
data2 = ['Notes', 'React', 'Veu', 'Private', 'Word File.doc']

print(str(data1).replace(' ', '').lower())
print(str(data2).replace(' ', '').lower())
data1 = str(data1).replace(' ', '').replace('.doc', '').replace('-', '').lower()
data2 = str(data2).replace(' ', '').replace('.doc', '').replace('-', '').lower()

assert data1 == data2
