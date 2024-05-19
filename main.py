meme_dict = { "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            'CREEPY': 'menakutkan, tidak menyenangkan'
            }
            
word = input('masukan sebuah kata: ')
word = word.upper()

for i in range(5):
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('gak ada di dicttionary')
 
