from antlr4 import *
from pandaqLexer import pandaqLexer
from pandaqParser import pandaqParser
from pandaqVisitor import pandaqVisitor
import pandas as pd
import streamlit as st

class EvalVisitor(pandaqVisitor):
	def visitRootEstat(self, ctx):
		[ctx_simbol, k_assignacio, ctx_accio] = list(ctx.getChildren())
		simbol = self.visit(ctx_simbol)
		taula = self.visit(ctx_accio)
		st.session_state[simbol] = taula
		# Visualitzar taula
		with pagina:
			st.table(taula)
	def visitRootPlot(self, ctx):
		[k_plot, ctx_simbol, k_punticoma] = list(ctx.getChildren())
		simbol = self.visit(ctx_simbol)
		taula = st.session_state[simbol].select_dtypes(include="number")
		with pagina:
			grafic = taula.plot.line()
			st.pyplot(grafic.figure)
	def visitRootAccio(self, ctx):
		[ctx_accio, k_punticoma] = list(ctx.getChildren())
		taula = self.visit(ctx_accio)
		# Visualitzar taula
		with pagina:
			st.table(taula)
	def visitSeleccionar(self, ctx):
		[k_select, ctx_camps, k_from, ctx_nom_taula] = list(ctx.getChildren())
		# Obtenir dades
		# [[columna], [(columna,funcio,nom)]]
		camps_seleccionar, camps_calcular = self.visit(ctx_camps)
		nom_taula = self.visit(ctx_nom_taula)
		# Agafar taula
		taula = agafar_taula(nom_taula)
		taula_calcular = taula.copy(True)
		# Seleccionar camps
		taula = seleccionar_camps(taula, camps_seleccionar)
		# Calcular camps
		calcular_camps(taula, taula_calcular, camps_calcular)
		return taula
	def visitSeleccionarIOrdenar(self, ctx):
		[k_select, ctx_camps, k_from, ctx_nom_taula, k_order, k_by, ctx_ordre] = list(ctx.getChildren())
		# Obtenir dades
		# [[columna], [(columna,funcio,nom)]]
		camps_seleccionar, camps_calcular = self.visit(ctx_camps)
		nom_taula = self.visit(ctx_nom_taula)
		# [(columna, Boolean)] # True es Ascendent i False es Descendent
		ordres = self.visit(ctx_ordre)
		# Agafar taula
		taula = agafar_taula(nom_taula)
		taula_calcular = taula.copy(True)
		# Seleccionar camps
		taula = seleccionar_camps(taula, camps_seleccionar)
		# Calcular camps
		calcular_camps(taula, taula_calcular, camps_calcular)
		# Ordenar
		ordenar_taula(taula, ordres)
		return taula
	def visitSeleccionarICondicio(self, ctx):
		[k_select, ctx_camps, k_from, ctx_nom_taula, k_where, ctx_condicions] = list(ctx.getChildren())
		# Obtenir dades
		# [[columna], [(columna,funcio,nom)]]
		camps_seleccionar, camps_calcular = self.visit(ctx_camps)
		nom_taula = self.visit(ctx_nom_taula)
		# String
		condicions = self.visit(ctx_condicions)
		# Agafar taula
		taula = agafar_taula(nom_taula)
		taula_calcular = taula.copy(True)
		# Filtre
		filtrar_taula(taula, condicions)
		# Seleccionar camps
		taula = seleccionar_camps(taula, camps_seleccionar)
		# Calcular camps
		calcular_camps(taula, taula_calcular, camps_calcular)
		return taula
	def visitSeleccionarIInnerJoin(self, ctx):
		[k_select, ctx_camps, k_from, ctx_nom_taula, ctx_innerjoin] = list(ctx.getChildren())
		# Obtenir dades
		# [[columna], [(columna,funcio,nom)]]
		camps_seleccionar, camps_calcular = self.visit(ctx_camps)
		nom_taula = self.visit(ctx_nom_taula)
		# [(nom_taula, camp)]
		innerjoin = self.visit(ctx_innerjoin)
		# Agafar taula
		taula = agafar_taula(nom_taula)
		taula_calcular = taula.copy(True)
		# Inner Join
		taula = innerjoin_taula(taula, innerjoin)
		# Seleccionar camps
		taula = seleccionar_camps(taula, camps_seleccionar)
		# Calcular camps
		calcular_camps(taula, taula_calcular, camps_calcular)
		return taula
	def visitSeleccionarISubconsultaOrdenar(self, ctx):
		[k_select, ctx_camps, k_from, ctx_nom_taula, k_where, ctx_camp, k_in, k_obrirParentesi, ctx_accio, k_tancarParentesi, k_order, k_by, ctx_ordre] = list(ctx.getChildren())
		# Obtenir dades
		# [[columna], [(columna,funcio,nom)]]
		camps_seleccionar, camps_calcular = self.visit(ctx_camps)
		nom_taula = self.visit(ctx_nom_taula)
		camp_condicio = self.visit(ctx_camp)
		taula_subconsulta = self.visit(ctx_accio)
		# [(columna, Boolean)] # True es Ascendent i False es Descendent
		ordres = self.visit(ctx_ordre)
		# Agafar taula
		taula = agafar_taula(nom_taula)
		taula_calcular = taula.copy(True)
		# Filtrar camps
		subconsulta_taula(taula, taula_subconsulta, camp_condicio)
		# Seleccionar camps
		taula = seleccionar_camps(taula, camps_seleccionar)
		# Calcular camps
		calcular_camps(taula, taula_calcular, camps_calcular)
		# Ordenar
		ordenar_taula(taula, ordres)
		return taula
	def visitSeleccionarISubconsulta(self, ctx):
		[k_select, ctx_camps, k_from, ctx_nom_taula, k_where, ctx_camp, k_in, k_obrirParentesi, ctx_accio, k_tancarParentesi] = list(ctx.getChildren())
		# Obtenir dades
		# [[columna], [(columna,funcio,nom)]]
		camps_seleccionar, camps_calcular = self.visit(ctx_camps)
		nom_taula = self.visit(ctx_nom_taula)
		camp_condicio = self.visit(ctx_camp)
		taula_subconsulta = self.visit(ctx_accio)
		# Agafar taula
		taula = agafar_taula(nom_taula)
		taula_calcular = taula.copy(True)
		# Filtrar camps
		subconsulta_taula(taula, taula_subconsulta, camp_condicio)
		# Seleccionar camps
		taula = seleccionar_camps(taula, camps_seleccionar)
		# Calcular camps
		calcular_camps(taula, taula_calcular, camps_calcular)
		return taula
	def visitInnerJoinVariesTaules(self, ctx):
		[ctx_innerjoins1, ctx_innerjoins2] = list(ctx.getChildren())
		innerjoins1 = self.visit(ctx_innerjoins1)
		innerjoins2 = self.visit(ctx_innerjoins2)
		return innerjoins1 + innerjoins2
	def visitInnerJoinTaula(self, ctx):
		[k_inner, k_join, ctx_nom_taula, k_on, ctx_camp1, k_igual, ctx_camp2] = list(ctx.getChildren())
		nom_taula = self.visit(ctx_nom_taula)
		camp1 = self.visit(ctx_camp1)
		camp2 = self.visit(ctx_camp2)
		# Retorna nomes un camp perque camp1 = camp2
		return [(nom_taula, camp1)]
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
		[k_asterisc] = list(ctx.getChildren())
		return [None,[]]
	def visitSeleccionarTotsICalcularCamps(self, ctx):
		[k_asterisc, k_coma, ctx_campsSeleccionats] = list(ctx.getChildren())
		campsSeleccionats = self.visit(ctx_campsSeleccionats)
		return [None, campsSeleccionats]
	def visitSeleccionarICalcularCamps(self, ctx):
		[ctx_campsSeleccionats, k_coma, ctx_campsCalculats] = list(ctx.getChildren())
		campsSeleccionats = self.visit(ctx_campsSeleccionats)
		campsCalculats = self.visit(ctx_campsCalculats)
		return [campsSeleccionats, campsCalculats]
	def visitSeleccionarCamps(self, ctx):
		[ctx_campsSeleccionats] = list(ctx.getChildren())
		campsSeleccionats = self.visit(ctx_campsSeleccionats)
		return [campsSeleccionats, []]
	def visitCalcularCamps(self, ctx):
		[ctx_campsCalculats] = list(ctx.getChildren())
		campsCalculats = self.visit(ctx_campsCalculats)
		return [[], campsCalculats]
	def visitSeleccionarVarisCamps(self, ctx):
		[ctx_campsSeleccionats1, k_coma, ctx_campsSeleccionats2] = list(ctx.getChildren())
		campsSeleccionats1 = self.visit(ctx_campsSeleccionats1)
		campsSeleccionats2 = self.visit(ctx_campsSeleccionats2)
		return campsSeleccionats1 + campsSeleccionats2
	def visitSeleccionarUnCamp(self, ctx):
		[ctx_campSeleccionat] = list(ctx.getChildren())
		campSeleccionat = self.visit(ctx_campSeleccionat)
		return [campSeleccionat]
	def visitCalcularVarisCamps(self, ctx):
		[ctx_campsCalculats1, k_coma, ctx_campsCalculats2] = list(ctx.getChildren())
		campsCalculats1 = self.visit(ctx_campsCalculats1)
		campsCalculats2 = self.visit(ctx_campsCalculats2)
		return campsCalculats1 + campsCalculats2
	def visitCalcularUnCampMultiplicacio(self, ctx):
		[ctx_campCalculat, k_multiplicacio, ctx_expressio, k_as, ctx_nomCampCalculat] = list(ctx.getChildren())
		campCalculat = self.visit(ctx_campCalculat)
		operacio = "*"
		numero = self.visit(ctx_expressio)
		nomCampCalculat = self.visit(ctx_nomCampCalculat)
		return [(campCalculat, funcio_lambda(operacio, numero), nomCampCalculat)]
	def visitCalcularUnCampDivisio(self, ctx):
		[ctx_campCalculat, k_divisio, ctx_expressio, k_as, ctx_nomCampCalculat] = list(ctx.getChildren())
		campCalculat = self.visit(ctx_campCalculat)
		operacio = "/"
		numero = self.visit(ctx_expressio)
		nomCampCalculat = self.visit(ctx_nomCampCalculat)
		return [(campCalculat, funcio_lambda(operacio, numero), nomCampCalculat)]
	def visitCalcularUnCampSuma(self, ctx):
		[ctx_campCalculat, k_suma, ctx_expressio, k_as, ctx_nomCampCalculat] = list(ctx.getChildren())
		campCalculat = self.visit(ctx_campCalculat)
		operacio = "+"
		numero = self.visit(ctx_expressio)
		nomCampCalculat = self.visit(ctx_nomCampCalculat)
		return [(campCalculat, funcio_lambda(operacio, numero), nomCampCalculat)]
	def visitCalcularUnCampResta(self, ctx):
		[ctx_campCalculat, k_resta, ctx_expressio, k_as, ctx_nomCampCalculat] = list(ctx.getChildren())
		campCalculat = self.visit(ctx_campCalculat)
		operacio = "-"
		numero = self.visit(ctx_expressio)
		nomCampCalculat = self.visit(ctx_nomCampCalculat)
		return [(campCalculat, funcio_lambda(operacio, numero), nomCampCalculat)]
	def visitExpressionsAssociativesMultiplicacio(self, ctx):
		[k_obrirParentesi, ctx_expressio1, k_multiplicacio, ctx_expressio2, k_tancarParentesi] = list(ctx.getChildren())
		numero1 = self.visit(ctx_expressio1)
		numero2 = self.visit(ctx_expressio2)
		return numero1 * numero2
	def visitExpressionsAssociativesDivisio(self, ctx):
		[k_obrirParentesi, ctx_expressio1, k_divisio, ctx_expressio2, k_tancarParentesi] = list(ctx.getChildren())
		numero1 = self.visit(ctx_expressio1)
		numero2 = self.visit(ctx_expressio2)
		return numero1 / numero2
	def visitExpressionsAssociativesSuma(self, ctx):
		[k_obrirParentesi, ctx_expressio1, k_suma, ctx_expressio2, k_tancarParentesi] = list(ctx.getChildren())
		numero1 = self.visit(ctx_expressio1)
		numero2 = self.visit(ctx_expressio2)
		return numero1 + numero2
	def visitExpressionsAssociativesResta(self, ctx):
		[k_obrirParentesi, ctx_expressio1, k_resta, ctx_expressio2, k_tancarParentesi] = list(ctx.getChildren())
		numero1 = self.visit(ctx_expressio1)
		numero2 = self.visit(ctx_expressio2)
		return numero1 - numero2
	def visitExpressionsMultiplicacio(self, ctx):
		[ctx_expressio1, k_multiplicacio, ctx_expressio2] = list(ctx.getChildren())
		numero1 = self.visit(ctx_expressio1)
		numero2 = self.visit(ctx_expressio2)
		return numero1 * numero2
	def visitExpressionsDivisio(self, ctx):
		[ctx_expressio1, k_multiplicacio, ctx_expressio2] = list(ctx.getChildren())
		numero1 = self.visit(ctx_expressio1)
		numero2 = self.visit(ctx_expressio2)
		return numero1 / numero2
	def visitExpressionsSuma(self, ctx):
		[ctx_expressio1, k_multiplicacio, ctx_expressio2] = list(ctx.getChildren())
		numero1 = self.visit(ctx_expressio1)
		numero2 = self.visit(ctx_expressio2)
		return numero1 + numero2
	def visitExpressionsResta(self, ctx):
		[ctx_expressio1, k_multiplicacio, ctx_expressio2] = list(ctx.getChildren())
		numero1 = self.visit(ctx_expressio1)
		numero2 = self.visit(ctx_expressio2)
		return numero1 - numero2
	def visitExpressioNumero(self, ctx):
		[ctx_numero] = list(ctx.getChildren())
		numero = self.visit(ctx_numero)
		return numero
	def visitNumeroEnter(self, ctx):
		[ctx_numero] = list(ctx.getChildren())
		numero = int(ctx_numero.getText())
		return numero
	def visitNumeroDecimal(self, ctx):
		[ctx_partEntera, k_punt, ctx_partDecimal] = list(ctx.getChildren())
		partEntera = ctx_partEntera.getText()
		punt = k_punt.getText()
		partDecimal = ctx_partDecimal.getText()
		numero = float(partEntera + punt + partDecimal)
		return numero
	def visitParaula(self, ctx):
		[ctx_camp] = list(ctx.getChildren())
		camp = ctx_camp.getText()
		return camp

# ------------------------------
#    Funcions complementaries
# ------------------------------

def agafar_taula(nom_taula):
	taula = None
	if nom_taula in st.session_state:
		taula = st.session_state[nom_taula]
	else:
		taula = taules[nom_taula]
	return taula

def seleccionar_camps(taula, camps_seleccionar):
	if camps_seleccionar == None: # seleccionar la taula sencera
		return taula
	elif len(camps_seleccionar) > 0:
		return taula[camps_seleccionar]
	else:
		return pd.DataFrame()

def calcular_camps(taula, taula_calcular, camps_calcular):
	if len(camps_calcular) > 0:
		for camp, funcio, nom_camp in camps_calcular:
			camp_calculat = taula_calcular[camp].apply(funcio)
			taula.insert(len(taula.columns), nom_camp, camp_calculat)

def subconsulta_taula(taula, taula_subconsulta, camp_condicio):
	filtres = ""
	for valor in taula_subconsulta[camp_condicio]:
		valor = str(valor)
		if valor not in filtres:
			if len(filtres) > 0:
				filtres += " or "
			filtres += camp_condicio + " == " + valor			
	taula.query(filtres, inplace=True)

def innerjoin_taula(taula, innerjoin):
	for nom_taula_innerjoin, columna_innerjoin in innerjoin:
		taula_innerjoin = None
		if nom_taula_innerjoin in st.session_state:
			taula_innerjoin = st.session_state[nom_taula_innerjoin]
		else:
			taula_innerjoin = taules[nom_taula_innerjoin]
		taula = taula.merge(taula_innerjoin, on=columna_innerjoin)
	return taula

def filtrar_taula(taula, filtres):
	taula.query(filtres, inplace=True)

def ordenar_taula(taula, ordres):
	columnes_ordre=[columna for columna, sentit in ordres]
	sentit_ordre=[sentit for columna, sentit in ordres]
	taula.sort_values(columnes_ordre, ascending=sentit_ordre, inplace=True)

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

# --------------------
#    Inicialitzacio 
# --------------------

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

# -----------
#    Inici
# -----------

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

