documents = mallet.read.dir("docs_collection_baseform2_probka")


mallet.instances <- mallet.import(id.array = documents$id, 
                                  text.array = documents$text, stoplist.file = "pl.txt",
                                  token.regexp = "[A-za-zÄĂ“Ä„ĹšĹĹ»ĹąÄ†ĹÄ™ĂłÄ…Ĺ›Ĺ‚ĹĽĹşÄ‡Ĺ„]+")


topic.model <- MalletLDA(num.topics = 10)

topic.model$loadDocuments(mallet.instances)

vocabulary <- topic.model$getVocabulary()
word.freqs <- mallet.word.freqs(topic.model)

word.freqs %>%   top_n(100,term.freq) %>% select(words)
stylo(frequencies = doc.topics)

stylo(corpus.dir = "docs_collection_baseform2_probka")

corpus_parse <- load.corpus.and.parse(corpus.dir = "docs_collection_baseform2_probka", files = dir())

stop_words <-read.table("pl.txt", encoding = "UTF-8")
class(stop_words$V1)
corpus_parse_no_stop <- delete.stop.words(corpus_parse, stop.words = stop_words$V1)

gram_2 <- make.ngrams(corpus_parse_no_stop[[1]], 2)

gram_2_corp <- lapply(corpus_parse_no_stop, function(x) make.ngrams(x, 2))
gram_2_final <- melt(gram_2_corp)
lista_2_gram <- as.character(gram_2_final[,1])

freq_2_gram <- make.frequency.list(lista_2_gram, value = T, head = 50)
tabela_freq <- make.table.of.frequencies(gram_2_corp, names(freq_2_gram))

colnames(tabela_freq)
names(gram_2_corp)
gram_2_corp$`1890027476.txt.bas`

corpus_parse_no_stop[[1]]
gram_2_corpclc <- function() cat(rep("\n",50000))
corpus_parse_no_stop[[2]]




