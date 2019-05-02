from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
import nltk

# If you get an error uncomment this line and download the necessary libraries
#nltk.download()

text = """  Before looking at what the American Dream is today, we need to look at its roots. The Declaration of Independence protects your opportunity to improve your life, no matter who you are. It boldly proclaims:

"We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness. That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed."
Our Founding Fathers introduced the revolutionary idea that each person's desire to pursue their idea of happiness was not self-indulgence, but a necessary driver of a prosperous society. They created a government to defend that right for everyone.

The pursuit of happiness became the driver of the entrepreneurial spirit that defines the American free market economy.

Of course, at that time "everyone" only meant white property-owners. Over time, Congress extended the right to slaves, women, and people without property. President Lincoln extended the American Dream to slaves with the Emancipation Proclamation. President Wilson extended it to women by supporting the 19th Amendment, giving women the right to vote.

President Johnson promoted Title VII of the Civil Rights Act of 1964. That extended the dream by protecting workers from discrimination by race, color, religion, sex (including pregnancy), or national origin. In 1967, Congress extended those rights to those older than 40. President Obama established the right to the pursuit of happiness through marriage regardless of sexual orientation. The Supreme Court supported that right in 2015. """

stemmer = SnowballStemmer("english")
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

freqTable = dict()
for word in words:
	word = word.lower()
	if word in stopWords:
		continue

	word = stemmer.stem(word)

	if word in freqTable:
		freqTable[word] += 1
	else:
		freqTable[word] = 1

sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
	for word, freq in freqTable.items():
		if word in sentence.lower():
			if sentence in sentenceValue:
				sentenceValue[sentence] += freq
			else:
				sentenceValue[sentence] = freq



sumValues = 0
for sentence in sentenceValue:
	sumValues += sentenceValue[sentence]

# Average value of a sentence from original text
average = int(sumValues / len(sentenceValue))


summary = ''
for sentence in sentences:
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
		summary += " " + sentence

print(summary)