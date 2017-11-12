import Sentence as S
# sentences : 	Sentence[]   
# topcount 	:	int			how many sentences for the summ

# sidenote: possible speedup with heap
def compute_summary(sentences=[], keywords=[], topcount=1):
	
	for s in sentences:
		for k in keywords:
			if k.content.lower() in s.content.lower():
				s.kw.append(k)
				s.score += 1
				k.occurency += 1
				if not k.isUsed:
					s.score +=10		#first sentence that uses a new keyword
					k.isUsed = True
				
	
	sorted_sentences = sorted(sentences, key=S.Sentence.getScore, reverse=True)
	summ = ""
	for i in range(0, topcount):
		summ += sorted_sentences[i].content + ". "


	return (sentences,summ)
	