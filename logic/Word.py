class Word(object):
	"""docstring for Word"""
	def __init__(self, id, content):
		super(Word, self).__init__()
		self.content = content
		self.isUsed = False  #true: is used in summary
		self.id = id
		self.occurency = 0
		