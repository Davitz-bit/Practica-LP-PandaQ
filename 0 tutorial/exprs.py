from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor
import traceback

class TreeVisitor(exprsVisitor):
	def __init__(self):
		self.nivell = 0
	def visitSuma(self, ctx):
		[expressio1, operador, expressio2] = list(ctx.getChildren())
		print('  ' *  self.nivell + '+')
		self.nivell += 1
		self.visit(expressio1)
		self.visit(expressio2)
		self.nivell -= 1
	def visitNumero(self, ctx):
		[numero] = list(ctx.getChildren())
		print("  " * self.nivell + numero.getText())
	def visitPotencia(self, ctx):
		[expressio1, operador, expressio2] = list(ctx.getChildren())
		print('  ' *  self.nivell + '^')
		self.nivell += 1
		self.visit(expressio1)
		self.visit(expressio2)
		self.nivell -= 1
	def visitMultiplicacio(self, ctx):
		[expressio1, operador, expressio2] = list(ctx.getChildren())
		print('  ' *  self.nivell + '*')
		self.nivell += 1
		self.visit(expressio1)
		self.visit(expressio2)
		self.nivell -= 1
	def visitResta(self, ctx):
		[expressio1, operador, expressio2] = list(ctx.getChildren())
		print('  ' *  self.nivell + '-')
		self.nivell += 1
		self.visit(expressio1)
		self.visit(expressio2)
		self.nivell -= 1
	def visitDivisio(self, ctx):
		[expressio1, operador, expressio2] = list(ctx.getChildren())
		print('  ' *  self.nivell + '/')
		self.nivell += 1
		self.visit(expressio1)
		self.visit(expressio2)
		self.nivell -= 1
	def visitParaula(self, ctx):
		[paraula] = list(ctx.getChildren())
		print("  " * self.nivell + paraula.getText())
	def visitAssignacio(self, ctx):
		[paraula, operador, expressio] = list(ctx.getChildren())
		print(paraula.getText(), operador)
		self.nivell += 1
		self.visit(expressio)
		self.nivell -= 1
	def visitEscriure(self, ctx):
		[accio, paraula] = list(ctx.getChildren())
		print(accio.getText(), paraula.getText())

class EvalVisitor(exprsVisitor):
	def visitRoot(self, ctx):
		[expressio] = list(ctx.getChildren())
		self.visit(expressio)
	# def visitExpressio(self, ctx):
	# 	[expressio] = list(ctx.getChildren())
	# 	self.visit(expressio)
	# def visitAccio(self, ctx):
	# 	[accio] = list(ctx.getChildren())
	# 	self.visit(accio)
	def visitSuma(self, ctx):
		[expressio1, operador, expressio2] = list(ctx.getChildren())
		expr1 = self.visit(expressio1)
		expr2 = self.visit(expressio2)
		if isinstance(expr1, str): expr1 = taula_simbols[expr1]
		if isinstance(expr2, str): expr2 = taula_simbols[expr2]
		return expr1 + expr2
	def visitNumero(self, ctx):
		[numero] = list(ctx.getChildren())
		return int(numero.getText())
	def visitPotencia(self, ctx):
		[expressio1, operador, expressio2] = list(ctx.getChildren())
		expr1 = self.visit(expressio1)
		expr2 = self.visit(expressio2)
		if isinstance(expr1, str): expr1 = taula_simbols[expr1]
		if isinstance(expr2, str): expr2 = taula_simbols[expr2]
		return expr1 ** expr2
	def visitMultiplicacio(self, ctx):
		[expressio1, operador, expressio2] = list(ctx.getChildren())
		expr1 = self.visit(expressio1)
		expr2 = self.visit(expressio2)
		if isinstance(expr1, str): expr1 = taula_simbols[expr1]
		if isinstance(expr2, str): expr2 = taula_simbols[expr2]
		return expr1 * expr2
	def visitResta(self, ctx):
		[expressio1, operador, expressio2] = list(ctx.getChildren())
		expr1 = self.visit(expressio1)
		expr2 = self.visit(expressio2)
		if isinstance(expr1, str): expr1 = taula_simbols[expr1]
		if isinstance(expr2, str): expr2 = taula_simbols[expr2]
		return expr1 - expr2
	def visitDivisio(self, ctx):
		[expressio1, operador, expressio2] = list(ctx.getChildren())
		expr1 = self.visit(expressio1)
		expr2 = self.visit(expressio2)
		if isinstance(expr1, str): expr1 = taula_simbols[expr1]
		if isinstance(expr2, str): expr2 = taula_simbols[expr2]
		return expr1 / expr2
	def visitParaula(self, ctx):
		[paraula] = list(ctx.getChildren())
		return paraula.getText()
	def visitAssignacio(self, ctx):
		[paraula, operador, expressio] = list(ctx.getChildren())
		nom = self.visit(paraula)
		taula_simbols[nom] = self.visit(expressio)
	def visitEscriure(self, ctx):
		[accio, expressio] = list(ctx.getChildren())
		expr = self.visit(expressio)
		if isinstance(expr, str): print(taula_simbols[expr])
		else: print(expr)
	def visitMenor(self, ctx):
		[expressio1, operador, expressio2] = list(ctx.getChildren())
		expr1 = self.visit(expressio1)
		expr2 = self.visit(expressio2)
		if isinstance(expr1, str): expr1 = taula_simbols[expr1]
		if isinstance(expr2, str): expr2 = taula_simbols[expr2]
		return expr1 < expr2
	def visitMenorigual(self, ctx):
		[expressio1, operador, expressio2] = list(ctx.getChildren())
		expr1 = self.visit(expressio1)
		expr2 = self.visit(expressio2)
		if isinstance(expr1, str): expr1 = taula_simbols[expr1]
		if isinstance(expr2, str): expr2 = taula_simbols[expr2]
		return expr1 <= expr2
	def visitMajor(self, ctx):
		[expressio1, operador, expressio2] = list(ctx.getChildren())
		expr1 = self.visit(expressio1)
		expr2 = self.visit(expressio2)
		if isinstance(expr1, str): expr1 = taula_simbols[expr1]
		if isinstance(expr2, str): expr2 = taula_simbols[expr2]
		return expr1 > expr2
	def visitMajorigual(self, ctx):
		[expressio1, operador, expressio2] = list(ctx.getChildren())
		expr1 = self.visit(expressio1)
		expr2 = self.visit(expressio2)
		if isinstance(expr1, str): expr1 = taula_simbols[expr1]
		if isinstance(expr2, str): expr2 = taula_simbols[expr2]
		return expr1 >= expr2
	def visitIgual(self, ctx):
		[expressio1, operador, expressio2] = list(ctx.getChildren())
		expr1 = self.visit(expressio1)
		expr2 = self.visit(expressio2)
		if isinstance(expr1, str): expr1 = taula_simbols[expr1]
		if isinstance(expr2, str): expr2 = taula_simbols[expr2]
		return expr1 == expr2
	def visitDiferent(self, ctx):
		[expressio1, operador, expressio2] = list(ctx.getChildren())
		expr1 = self.visit(expressio1)
		expr2 = self.visit(expressio2)
		if isinstance(expr1, str): expr1 = taula_simbols[expr1]
		if isinstance(expr2, str): expr2 = taula_simbols[expr2]
		return expr1 != expr2
	def visitCondicional(self, ctx):
		[k_if, condicional, k_then, accio, k_end] = list(ctx.getChildren())
		cond = self.visit(condicional)
		if cond:
			self.visit(accio)
	def visitMentre(self, ctx):
		[k_while, condicional, k_do, accio, expressio, k_end] = list(ctx.getChildren())
		while self.visit(condicional):
			self.visit(accio)
			self.visit(expressio)

# pila de diccionaris
taula_simbols = {}

while True:
	input_stream = InputStream(input('? '))
	lexer = exprsLexer(input_stream)
	token_stream = CommonTokenStream(lexer)
	parser = exprsParser(token_stream)
	tree = parser.root()

	if parser.getNumberOfSyntaxErrors() == 0:
		# visitorTree = TreeVisitor()
		# visitorTree.visit(tree)
		visitorEval = EvalVisitor()
		visitorEval.visit(tree)
	else:
		print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
		print(tree.toStringTree(recog=parser))

