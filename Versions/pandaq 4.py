from antlr4 import *
from pandaqLexer import pandaqLexer
from pandaqParser import pandaqParser
from pandaqVisitor import pandaqVisitor
import pandas as pd
import streamlit as st

class EvalVisitor(pandaqVisitor):
	def visitRoot(self, ctx):
		[accio] = list(ctx.getChildren())
		self.visit(accio)
	def visitSeleccionar(self, ctx):
		[k_select, ctx_camps, k_from, ctx_nom_taula, k_punticoma] = list(ctx.getChildren())
		# [llista columnes seleccionades, llista de columnes i operacions a aquestes]
		# [[columna],[(columna,(operacio, numero),nom)]] # operacio sera una funcio
		campsSeleccionats, campsCalculats = self.visit(ctx_camps)
		nom_taula = self.visit(ctx_nom_taula)

		pagina.empty()
		taula = pd.DataFrame()
		# camps seleccionats
		if campsSeleccionats == None: # seleccionar la taula sencera
			taula = taules[nom_taula]
		elif len(campsSeleccionats) > 0:
			taula = taules[nom_taula][campsSeleccionats]
		# camps calculats
		if len(campsCalculats) > 0:
			for camp, funcio, nom_camp in campsCalculats:
				operador = funcio[0]
				numero = funcio[1]
				taula.insert(len(taula.columns), nom_camp, taules[nom_taula][camp].apply(funcio_lambda(operador, numero)))
		# Visualitzar taula
		with pagina:
			st.table(taula)
	def visitSeleccionarIOrdenar(self, ctx):
		[k_select, ctx_camps, k_from, ctx_nom_taula, k_order, k_by, ctx_ordre, k_punticoma] = list(ctx.getChildren())
		# [llista columnes seleccionades, llista de columnes i operacions a aquestes]
		# [[columna],[(columna,(operacio, numero),nom)]] # operacio sera una funcio
		campsSeleccionats, campsCalculats = self.visit(ctx_camps)
		nom_taula = self.visit(ctx_nom_taula)
		# [(columna, True/False)] # True es Ascendent i False es Descendent
		ordres = self.visit(ctx_ordre)

		pagina.empty()
		taula = pd.DataFrame()
		# camps seleccionats
		if campsSeleccionats == None: # seleccionar la taula sencera
			taula = taules[nom_taula]
		elif len(campsSeleccionats) > 0:
			taula = taules[nom_taula][campsSeleccionats]
		# camps calculats
		if len(campsCalculats) > 0:
			for camp, funcio, nom_camp in campsCalculats:
				operador = funcio[0]
				numero = funcio[1]
				taula.insert(len(taula.columns), nom_camp, taules[nom_taula][camp].apply(funcio_lambda(operador, numero)))
		# df.sort_values(['a', 'b'], ascending=[True, False])
		columnes_ordre=[columna for columna, sentit in ordres]
		sentit_ordre=[sentit for columna, sentit in ordres]
		taula.sort_values(columnes_ordre, ascending=sentit_ordre, inplace=True)
		# Visualitzar taula
		with pagina:
			st.table(taula)
	def visitSeleccionarICondicio(self, ctx):
		[k_select, ctx_camps, k_from, ctx_nom_taula, k_where, ctx_condicions, k_punticoma] = list(ctx.getChildren())
		# [llista columnes seleccionades, llista de columnes i operacions a aquestes]
		# [[columna],[(columna,(operacio, numero),nom)]] # operacio sera una funcio
		campsSeleccionats, campsCalculats = self.visit(ctx_camps)
		nom_taula = self.visit(ctx_nom_taula)
		# "String de condicions"
		condicions = self.visit(ctx_condicions)

		pagina.empty()
		taula = pd.DataFrame()
		# camps seleccionats
		if campsSeleccionats == None: # seleccionar la taula sencera
			taula = taules[nom_taula]
		elif len(campsSeleccionats) > 0:
			taula = taules[nom_taula][campsSeleccionats]
		# camps calculats
		if len(campsCalculats) > 0:
			for camp, funcio, nom_camp in campsCalculats:
				operador = funcio[0]
				numero = funcio[1]
				taula.insert(len(taula.columns), nom_camp, taules[nom_taula][camp].apply(funcio_lambda(operador, numero)))
		# df.query("Discount >= 1000 & Discount <= 2000")
		print(condicions)
		taula.query(condicions, inplace=True)
		# Visualitzar taula
		with pagina:
			st.table(taula)
	def visitCondicioAnd(self, ctx):
		[ctx_condicions1, k_and, ctx_condicions2] = list(ctx.getChildren())
		condicions1 = self.visit(ctx_condicions1)
		condicions2 = self.visit(ctx_condicions2)
		return condicions1 + " and " + condicions2
	def visitCondicioNot(self, ctx):
		[k_not, ctx_condicions] = list(ctx.getChildren())
		condicions = self.visit(ctx_condicions)
		return "not " + condicions
	def visitCondicioMenor(self, ctx):
		[ctx_camp, k_menor, ctx_expressio] = list(ctx.getChildren())
		camp = self.visit(ctx_camp)
		numero = str(self.visit(ctx_expressio))
		return camp + " < " + numero
	def visitCondicioIgual(self, ctx):
		[ctx_camp, k_igual, ctx_expressio] = list(ctx.getChildren())
		camp = self.visit(ctx_camp)
		numero = str(self.visit(ctx_expressio))
		return camp + " == " + numero
	def visitOrdreVarisCamps(self, ctx):
		[ctx_campsOrdre1, k_coma, ctx_campsOrdre2] = list(ctx.getChildren())
		campsOrdre1 = self.visit(ctx_campsOrdre1)
		campsOrdre2 = self.visit(ctx_campsOrdre2)
		return campsOrdre1 + campsOrdre2
	def visitOrdreCampAcendent(self, ctx):
		[ctx_campOrdre, k_Ascendent] = list(ctx.getChildren())
		campOrdre = self.visit(ctx_campOrdre)
		return [(campOrdre, True)]
	def visitOrdreCampDescendent(self, ctx):
		[ctx_campOrdre, k_Descendent] = list(ctx.getChildren())
		campOrdre = self.visit(ctx_campOrdre)
		return [(campOrdre, False)]
	def visitOrdreCamp(self, ctx):
		[ctx_campOrdre] = list(ctx.getChildren())
		campOrdre = self.visit(ctx_campOrdre)
		return [(campOrdre, True)]
	def visitSeleccionarTotsCamps(self, ctx):
		print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
		[k_asterisc] = list(ctx.getChildren())
		return [None,[]]
	def visitSeleccionarTotsICalcularCamps(self, ctx):
		print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
		[k_asterisc, k_coma, ctx_campsSeleccionats] = list(ctx.getChildren())
		campsSeleccionats = self.visit(ctx_campsSeleccionats)
		return [None, campsSeleccionats]
	def visitSeleccionarICalcularCamps(self, ctx):
		print("cccccccccccccccccccccccccccccccccccccccc")
		[ctx_campsSeleccionats, k_coma, ctx_campsCalculats] = list(ctx.getChildren())
		campsSeleccionats = self.visit(ctx_campsSeleccionats)
		campsCalculats = self.visit(ctx_campsCalculats)
		return [campsSeleccionats, campsCalculats]
	def visitSeleccionarCamps(self, ctx):
		print("dddddddddddddddddddddddddddddddddddddddddd")
		[ctx_campsSeleccionats] = list(ctx.getChildren())
		campsSeleccionats = self.visit(ctx_campsSeleccionats)
		return [campsSeleccionats, []]
	def visitCalcularCamps(self, ctx):
		print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
		[ctx_campsCalculats] = list(ctx.getChildren())
		campsCalculats = self.visit(ctx_campsCalculats)
		print(ctx_campsCalculats.getText())
		print(campsCalculats)
		return [[], campsCalculats]
	def visitSeleccionarVarisCamps(self, ctx):
		print("ffffffffffffffffffffffffffffffffffffffffffffff")
		[ctx_campsSeleccionats1, k_coma, ctx_campsSeleccionats2] = list(ctx.getChildren())
		campsSeleccionats1 = self.visit(ctx_campsSeleccionats1)
		campsSeleccionats2 = self.visit(ctx_campsSeleccionats2)
		return campsSeleccionats1 + campsSeleccionats2
	def visitSeleccionarUnCamp(self, ctx):
		print("ggggggggggggggggggggggggggggggggggggggggggg")
		[ctx_campSeleccionat] = list(ctx.getChildren())
		campSeleccionat = self.visit(ctx_campSeleccionat)
		return [campSeleccionat]
	def visitCalcularVarisCamps(self, ctx):
		print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
		[ctx_campsCalculats1, k_coma, ctx_campsCalculats2] = list(ctx.getChildren())
		campsCalculats1 = self.visit(ctx_campsCalculats1)
		campsCalculats2 = self.visit(ctx_campsCalculats2)
		return campsCalculats1 + campsCalculats2
	def visitCalcularUnCampMultiplicacio(self, ctx):
		print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
		[ctx_campCalculat, k_multiplicacio, ctx_expressio, k_as, ctx_nomCampCalculat] = list(ctx.getChildren())
		campCalculat = self.visit(ctx_campCalculat)
		operacio = "*"
		numero = self.visit(ctx_expressio)
		nomCampCalculat = self.visit(ctx_nomCampCalculat)
		return [(campCalculat, (operacio, numero), nomCampCalculat)]
	def visitCalcularUnCampDivisio(self, ctx):
		print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
		[ctx_campCalculat, k_divisio, ctx_expressio, k_as, ctx_nomCampCalculat] = list(ctx.getChildren())
		campCalculat = self.visit(ctx_campCalculat)
		operacio = "/"
		numero = self.visit(ctx_expressio)
		nomCampCalculat = self.visit(ctx_nomCampCalculat)
		return [(campCalculat, (operacio, numero), nomCampCalculat)]
	def visitCalcularUnCampSuma(self, ctx):
		print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
		[ctx_campCalculat, k_suma, ctx_expressio, k_as, ctx_nomCampCalculat] = list(ctx.getChildren())
		campCalculat = self.visit(ctx_campCalculat)
		operacio = "+"
		numero = self.visit(ctx_expressio)
		nomCampCalculat = self.visit(ctx_nomCampCalculat)
		return [(campCalculat, (operacio, numero), nomCampCalculat)]
	def visitCalcularUnCampResta(self, ctx):
		print("llllllllllllllllllllllllllllllllllllllllllllllll")
		[ctx_campCalculat, k_resta, ctx_expressio, k_as, ctx_nomCampCalculat] = list(ctx.getChildren())
		campCalculat = self.visit(ctx_campCalculat)
		operacio = "-"
		numero = self.visit(ctx_expressio)
		nomCampCalculat = self.visit(ctx_nomCampCalculat)
		return [(campCalculat, (operacio, numero), nomCampCalculat)]
	def visitExpressionsAssociativesMultiplicacio(self, ctx):
		print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
		[k_obrirParentesi, ctx_expressio1, k_multiplicacio, ctx_expressio2, k_tancarParentesi] = list(ctx.getChildren())
		numero1 = self.visit(ctx_expressio1)
		numero2 = self.visit(ctx_expressio2)
		return numero1 * numero2
	def visitExpressionsAssociativesDivisio(self, ctx):
		print("nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
		[k_obrirParentesi, ctx_expressio1, k_divisio, ctx_expressio2, k_tancarParentesi] = list(ctx.getChildren())
		numero1 = self.visit(ctx_expressio1)
		numero2 = self.visit(ctx_expressio2)
		return numero1 / numero2
	def visitExpressionsAssociativesSuma(self, ctx):
		print("ooooooooooooooooooooooooooooooooooooooooooooooo")
		[k_obrirParentesi, ctx_expressio1, k_suma, ctx_expressio2, k_tancarParentesi] = list(ctx.getChildren())
		numero1 = self.visit(ctx_expressio1)
		numero2 = self.visit(ctx_expressio2)
		return numero1 + numero2
	def visitExpressionsAssociativesResta(self, ctx):
		print("ppppppppppppppppppppppppppppppppppppppppppp")
		[k_obrirParentesi, ctx_expressio1, k_resta, ctx_expressio2, k_tancarParentesi] = list(ctx.getChildren())
		numero1 = self.visit(ctx_expressio1)
		numero2 = self.visit(ctx_expressio2)
		return numero1 - numero2
	def visitExpressionsMultiplicacio(self, ctx):
		print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
		[ctx_expressio1, k_multiplicacio, ctx_expressio2] = list(ctx.getChildren())
		numero1 = self.visit(ctx_expressio1)
		numero2 = self.visit(ctx_expressio2)
		return numero1 * numero2
	def visitExpressionsDivisio(self, ctx):
		print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
		[ctx_expressio1, k_multiplicacio, ctx_expressio2] = list(ctx.getChildren())
		numero1 = self.visit(ctx_expressio1)
		numero2 = self.visit(ctx_expressio2)
		return numero1 / numero2
	def visitExpressionsSuma(self, ctx):
		print("ssssssssssssssssssssssssssssssssssssssssssssssss")
		[ctx_expressio1, k_multiplicacio, ctx_expressio2] = list(ctx.getChildren())
		numero1 = self.visit(ctx_expressio1)
		numero2 = self.visit(ctx_expressio2)
		return numero1 + numero2
	def visitExpressionsResta(self, ctx):
		print("ttttttttttttttttttttttttttttttttttttttttttttttttttt")
		[ctx_expressio1, k_multiplicacio, ctx_expressio2] = list(ctx.getChildren())
		numero1 = self.visit(ctx_expressio1)
		numero2 = self.visit(ctx_expressio2)
		return numero1 - numero2
	def visitExpressioNumero(self, ctx):
		print("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
		[ctx_numero] = list(ctx.getChildren())
		numero = self.visit(ctx_numero)
		print(numero)
		return numero
	def visitNumeroEnter(self, ctx):
		print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
		[ctx_numero] = list(ctx.getChildren())
		numero = int(ctx_numero.getText())
		return numero
	def visitNumeroDecimal(self, ctx):
		print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
		[ctx_partEntera, k_punt, ctx_partDecimal] = list(ctx.getChildren())
		partEntera = ctx_partEntera.getText()
		punt = k_punt.getText()
		partDecimal = ctx_partDecimal.getText()
		numero = float(partEntera + punt + partDecimal)
		print(numero)
		return numero
	def visitParaula(self, ctx):
		print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
		[ctx_camp] = list(ctx.getChildren())
		camp = ctx_camp.getText()
		print(camp)
		return camp
		
def funcio_lambda(op, num):
	funcio = None
	if op == "+":
		funcio = lambda x : x + num
	elif op == "-":
		funcio = lambda x : x - num
	elif op == "*":
		funcio = lambda x : x * num
	elif op == "/":
		funcio = lambda x : x / num
	return funcio

#select first_name, salary, salary * 1.05 as new_salary from employees;
taules = {}
taules["countries"] = pd.read_csv("./data/countries.csv")
taules["departments"] = pd.read_csv("./data/departments.csv")
taules["dependents"] = pd.read_csv("./data/dependents.csv")
taules["employees"] = pd.read_csv("./data/employees.csv")
taules["jobs"] = pd.read_csv("./data/jobs.csv")
taules["locations"] = pd.read_csv("./data/locations.csv")
taules["regions"] = pd.read_csv("./data/regions.csv")

query = st.text_area('Query:')
submit = st.button("Submit")
pagina = st.empty()

if submit:
	input_stream = InputStream(query)
	lexer = pandaqLexer(input_stream)
	token_stream = CommonTokenStream(lexer)
	parser = pandaqParser(token_stream)
	tree = parser.root()

	if parser.getNumberOfSyntaxErrors() == 0:
		visitorEval = EvalVisitor()
		visitorEval.visit(tree)
	else:
		print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
		print(tree.toStringTree(recog=parser))

