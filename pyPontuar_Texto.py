import spacy
nlp = spacy.load("pt_core_news_sm")

def punctuate(text):
    doc = nlp(text)
    punc_tokens = []
    for i, token in enumerate(doc):
        if i == len(doc) - 1 or doc[i + 1].text[0].isupper():
            punc_tokens.append(token.text + ".")
        else:
            punc_tokens.append(token.text)
    return " ".join(punc_tokens)

text = "Eu gosto de comer pizza e jogar video game"
text2 = "Neste exemplo, estamos usando o modelo pt_core_news_sm para processar o texto em português. O spaCy oferece recursos avançados para análise de linguagem natural, como identificação de entidades e sentenças, e pode ser uma ferramenta poderosa para pontuar texto. No entanto, você pode precisar ajustar as regras de pontuação de acordo com suas necessidades específicas."
punctuated_text = punctuate(text)
print(punctuated_text)
punctuated_text = punctuate(text2)
print(punctuated_text2)
