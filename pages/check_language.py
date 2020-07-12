#from langdetect.detector_factory import detect
import cld2
title = "Mga Ranking Kagamitan Mga Mapagkukunan Blog Nangungunang 100 Mga Cryptocurrency ng Market Capitalization Rank	Pangalan Market Cap Presyo	Dami (24 na oras)	Umiikot na Supply Pagbabago (24h) Graph ng Presyo (7d)"
isReliable, textBytesFound, lang_lit = cld2.detect(title)
print(lang_lit)
#print (cld2.LANGUAGES)

