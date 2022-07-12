from newspaper import Article

import nltk
nltk.download('punkt')

artciles = {
    'lemonde.fr':     'https://www.lemonde.fr/international/article/2022/06/30/face-a-vladimir-poutine-emmanuel-macron-manie-la-diplomatie-des-fuites_6132651_3210.html',
    'lamontagne.fr':  'https://www.lamontagne.fr/chamalieres-63400/actualites/le-demenagement-de-l-imprimerie-de-la-banque-de-france-a-vic-le-comte-puy-de-dome-enfin-sur-les-rails_14159350/',
    'hankooktire.com': 'https://www.hankooktire.com/global/en/company/media-list/media-detail.600090.html',
    'continental.com': 'https://www.continental.com/en/press/press-releases/20220511-q1-2022/'
}

for key in artciles:

    f = open("scraped-articles/" + key + ".md" , "w")
    

    article = Article(artciles[key])
    article.download()
    article.parse()
    article.nlp()
    
    f.write('## url\n')
    f.write('[' + artciles[key] + '](' + artciles[key] + ')' + '\n')
    f.write('## title\n')
    f.write(article.title + '\n')
    f.write('## content\n')
    f.write(article.text + '\n')
    f.write('## summary\n')
    f.write(article.summary + '\n')
    f.write('## publish date\n')
    f.write(str(article.publish_date) + '\n')
    f.write('## keywords\n')
    f.write(str(article.keywords) + '\n')
    f.write('## authors\n')
    f.write(str(article.authors) + '\n')
    f.write('## top image\n')
    f.write('![](' + article.top_image + ')\n')
    f.write('## movies\n')
    f.write(str(article.movies) + '\n')
    f.close()

    print('* [' + key + '](scraped-articles/' + key + '.md)')