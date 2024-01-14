from antlr4 import *
from pandaqLexer import pandaqLexer
from pandaqParser import pandaqParser
from pandaqVisitor import pandaqVisitor
import pandas as pd
import streamlit as st

class EvalVisitor(pandaqVisitor):
	def visitRootEstat(self, ctx):
		[ctx_simbol, k_assignacio, ctx_consulta] = list(ctx.getChildren())
		simbol = self.visit(ctx_simbol)
		taula = self.visit(ctx_consulta)
		st.session_state[simbol] = taula
	
	def visitRootGrafic(self, ctx):
		[k_grafic, ctx_simbol, k_punticoma] = list(ctx.getChildren())
		simbol = self.visit(ctx_simbol)
		taula = st.session_state[simbol].select_dtypes(include="number")
		grafic = taula.plot.line()
		with pagina:
			st.pyplot(grafic.figure)
	
	def visitRootConsulta(self, ctx):
		[ctx_consulta] = list(ctx.getChildren())
		taula = self.visit(ctx_consulta)
		# Visualitzar taula
		with pagina:
			st.table(taula)

	def visitConsultaSubconsulta(self, ctx):
		[k_select, ctx_camps, k_from, ctx_nom_taula, ctx_subconsulta, k_punticoma] = list(ctx.getChildren())
		# Obtenir dades
		# [[columna], [(columna,funcio,nom)]]
		camps_seleccionar, camps_calcular = self.visit(ctx_camps)
		nom_taula = self.visit(ctx_nom_taula)
		# [columna, taula]
		camp_filtre, taula_subconsulta = self.visit(ctx_subconsulta)
		# Agafar taula
		taula = agafar_taula(nom_taula)
		taula_calcular = taula.copy(True)
		# Filtrar camps
		subconsulta_taula(taula, taula_subconsulta, camp_filtre)
		# Seleccionar camps
		taula = seleccionar_camps(taula, camps_seleccionar)
		# Calcular camps
		calcular_camps(taula, taula_calcular, camps_calcular)
		return taula
	
	def visitConsultaInnerJoin(self, ctx):
		[k_select, ctx_camps, k_from, ctx_nom_taula, ctx_innerjoin, k_punticoma] = list(ctx.getChildren())
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
	
	def visitConsultaFiltre(self, ctx):
		[k_select, ctx_camps, k_from, ctx_nom_taula, ctx_filtre, k_punticoma] = list(ctx.getChildren())	
		# Obtenir dades
		# [[columna], [(columna,funcio,nom)]]
		camps_seleccionar, camps_calcular = self.visit(ctx_camps)
		nom_taula = self.visit(ctx_nom_taula)
		# String
		filtres = self.visit(ctx_filtre)
		# Agafar taula
		taula = agafar_taula(nom_taula)
		taula_calcular = taula.copy(True)
		# Filtre
		filtrar_taula(taula, filtres)
		# Seleccionar camps
		taula = seleccionar_camps(taula, camps_seleccionar)
		# Calcular camps
		calcular_camps(taula, taula_calcular, camps_calcular)
		return taula
	
	def visitConsultaOrdre(self, ctx):
		[k_select, ctx_camps, k_from, ctx_nom_taula, ctx_ordre, k_punticoma] = list(ctx.getChildren())
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
	
	def visitConsultaTaula(self, ctx):
		[k_select, ctx_camps, k_from, ctx_nom_taula, k_punticoma] = list(ctx.getChildren())
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
	
	def visitSubconsultaInnerJoin(self, ctx):
		[k_where, ctx_camp, k_in, k_obrirParentesi, ctx_consulta, k_tancarParentesi, ctx_innerjoin] = list(ctx.getChildren())
		camp_filtre = self.visit(ctx_camp)
		taula = self.visit(ctx_consulta)
		# [(nom_taula, camp)]
		innerjoin = self.visit(ctx_innerjoin)
		# Inner Join
		taula = innerjoin_taula(taula, innerjoin)
		return [camp_filtre, taula]

	def visitSubconsultaFiltre(self, ctx):
		[k_where, ctx_camp, k_in, k_obrirParentesi, ctx_consulta, k_tancarParentesi, ctx_filtre] = list(ctx.getChildren())
		camp_filtre = self.visit(ctx_camp)
		taula = self.visit(ctx_consulta)
		# String
		filtres = self.visit(ctx_filtre)
		# Filtre
		filtrar_taula(taula, filtres)
		return [camp_filtre, taula]

	def visitSubconsultaOrdre(self, ctx):
		[k_where, ctx_camp, k_in, k_obrirParentesi, ctx_consulta, k_tancarParentesi, ctx_ordre] = list(ctx.getChildren())
		camp_filtre = self.visit(ctx_camp)
		taula = self.visit(ctx_consulta)
		# [(columna, Boolean)] # True es Ascendent i False es Descendent
		ordres = self.visit(ctx_ordre)
		# Ordenar
		ordenar_taula(taula, ordres)
		return [camp_filtre, taula]

	def visitSubconsultaTaula(self, ctx):
		[k_where, ctx_camp, k_in, k_obrirParentesi, ctx_consulta, k_tancarParentesi] = list(ctx.getChildren())
		camp_filtre = self.visit(ctx_camp)
		taula = self.visit(ctx_consulta)
		return [camp_filtre, taula]
	
	def visitInnerJoinVariesTaules(self, ctx):
		[ctx_innerjoins1, ctx_innerjoins2] = list(ctx.getChildren())
		innerjoins1 = self.visit(ctx_innerjoins1)
		innerjoins2 = self.visit(ctx_innerjoins2)
		return innerjoins1 + innerjoins2
	
	def visitInnerJoinFiltre(self, ctx):
		[k_inner, k_join, ctx_nom_taula, k_on, ctx_camp1, k_igual, ctx_camp2, ctx_filtre] = list(ctx.getChildren())
		.
		nom_taula = self.visit(ctx_nom_taula)
		camp1 = self.visit(ctx_camp1)
		camp2 = self.visit(ctx_camp2)

	def visitInnerJoinFiltre(self, ctx):
		[k_inner, k_join, ctx_nom_taula, k_on, ctx_camp1, k_igual, ctx_camp2, ctx_ordre] = list(ctx.getChildren())
		.

	def visitInnerJoinTaula(self, ctx):
		[k_inner, k_join, ctx_nom_taula, k_on, ctx_camp1, k_igual, ctx_camp2] = list(ctx.getChildren())
		nom_taula = self.visit(ctx_nom_taula)
		camp1 = self.visit(ctx_camp1)
		camp2 = self.visit(ctx_camp2)
		# Retorna nomes un camp perque camp1 = camp2
		return [(nom_taula, camp1)]
	
	def visitFiltreAnd(self, ctx):
		[ctx_condicions1, k_and, ctx_condicions2] = list(ctx.getChildren())
		condicions1 = self.visit(ctx_condicions1)
		condicions2 = self.visit(ctx_condicions2)
		return condicions1 + " and " + condicions2

	def visitFiltreMenorOrdre(self, ctx):
		[ctx_camp, k_menor, ctx_expressio, ctx_ordre] = list(ctx.getChildren())
		.

	def visitFiltreIgualOrdre(self, ctx):
		[ctx_camp, k_igual, ctx_expressio, ctx_ordre] = list(ctx.getChildren())
		.
	
	def visitFiltreMenor(self, ctx):
		[ctx_camp, k_menor, ctx_expressio] = list(ctx.getChildren())
		camp = self.visit(ctx_camp)
		numero = str(self.visit(ctx_expressio))
		return camp + " < " + numero
	
	def visitFiltreIgual(self, ctx):
		[ctx_camp, k_igual, ctx_expressio] = list(ctx.getChildren())
		camp = self.visit(ctx_camp)
		numero = str(self.visit(ctx_expressio))
		return camp + " == " + numero
	
	def visitFiltreNot(self, ctx):
		[k_not, ctx_condicions] = list(ctx.getChildren())
		condicions = self.visit(ctx_condicions)
		return "not " + condicions
































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
	
	def visitSeleccionarCamp(self, ctx):
		[ctx_campSeleccionat] = list(ctx.getChildren())
		campSeleccionat = self.visit(ctx_campSeleccionat)
		return [campSeleccionat]
	
	def visitCalcularVarisCamps(self, ctx):
		[ctx_campsCalculats1, k_coma, ctx_campsCalculats2] = list(ctx.getChildren())
		campsCalculats1 = self.visit(ctx_campsCalculats1)
		campsCalculats2 = self.visit(ctx_campsCalculats2)
		return campsCalculats1 + campsCalculats2
	
	def visitCalcularCampMultiplicacio(self, ctx):
		[ctx_campCalculat, k_multiplicacio, ctx_expressio, k_as, ctx_nomCampCalculat] = list(ctx.getChildren())
		campCalculat = self.visit(ctx_campCalculat)
		operador = "*"
		numero = self.visit(ctx_expressio)
		nomCampCalculat = self.visit(ctx_nomCampCalculat)
		return [(campCalculat, funcio_lambda(operador, numero), nomCampCalculat)]
	
	def visitCalcularCampDivisio(self, ctx):
		[ctx_campCalculat, k_divisio, ctx_expressio, k_as, ctx_nomCampCalculat] = list(ctx.getChildren())
		campCalculat = self.visit(ctx_campCalculat)
		operador = "/"
		numero = self.visit(ctx_expressio)
		nomCampCalculat = self.visit(ctx_nomCampCalculat)
		return [(campCalculat, funcio_lambda(operador, numero), nomCampCalculat)]
	
	def visitCalcularCampSuma(self, ctx):
		[ctx_campCalculat, k_suma, ctx_expressio, k_as, ctx_nomCampCalculat] = list(ctx.getChildren())
		campCalculat = self.visit(ctx_campCalculat)
		operador = "+"
		numero = self.visit(ctx_expressio)
		nomCampCalculat = self.visit(ctx_nomCampCalculat)
		return [(campCalculat, funcio_lambda(operador, numero), nomCampCalculat)]
	
	def visitCalcularCampResta(self, ctx):
		[ctx_campCalculat, k_resta, ctx_expressio, k_as, ctx_nomCampCalculat] = list(ctx.getChildren())
		campCalculat = self.visit(ctx_campCalculat)
		operador = "-"
		numero = self.visit(ctx_expressio)
		nomCampCalculat = self.visit(ctx_nomCampCalculat)
		return [(campCalculat, funcio_lambda(operador, numero), nomCampCalculat)]
	
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
""" Funcions complementaries """
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

def subconsulta_taula(taula, taula_subconsulta, camp_filtre):
	filtres = ""
	for valor in taula_subconsulta[camp_filtre]:
		if valor not in filtres:
			if len(filtres > 0):
				filtres += " and "
			filtres.append(camp_filtre + " == " + valor)				
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
""" Inicialitzacio """
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
""" Inici """
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

