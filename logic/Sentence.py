class Sentence(object):
	"""docstring for Sentence"""
	def __init__(self, content=[], score=0):
		super(Sentence, self).__init__()
		self.content = content
		self.score = score
		self.kw = []

	def __cmp__(self, other):
		return self.score.__cmp__(other.score)

	def getScore(self):
		return self.score
