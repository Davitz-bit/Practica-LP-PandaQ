// Gramàtica per expressions senzilles
grammar pandaq;

root		: accio
;

accio		: 'select' camps 'from' par ';'							# seleccionar
			| 'select' camps 'from' par 'order' 'by' ordre ';'		# seleccionarIOrdenar
			| 'select' camps 'from' par 'where' condicio ';'		# seleccionarICondicio
;

condicio	: condicio 'and' condicio				# condicioAnd
			| 'not' condicio						# condicioNot
			| par '<' expr							# condicioMenor
			| par '=' expr							# condicioIgual
;

ordre		: ordre ',' ordre						# ordreVarisCamps
			| par 'asc'								# ordreCampAcendent
			| par 'desc'							# ordreCampDescendent
			| par									# ordreCamp
;

camps		: '*'									# seleccionarTotsCamps
			| '*' ',' campssc						# seleccionarTotsICalcularCamps
			| campsnc ',' campssc					# seleccionarICalcularCamps
			| campsnc								# seleccionarCamps
			| campssc								# calcularCamps
;

campsnc		: campsnc ',' campsnc					# seleccionarVarisCamps
			| par									# seleccionarUnCamp
;

campssc		: campssc ',' campssc					# calcularVarisCamps
			| par '*' expr 'as' par					# calcularUnCampMultiplicacio
			| par '/' expr 'as' par					# calcularUnCampDivisio
			| par '+' expr 'as' par					# calcularUnCampSuma
			| par '-' expr 'as' par					# calcularUnCampResta
;

expr		: '(' expr '*' expr ')'					# expressionsAssociativesMultiplicacio
			| '(' expr '/' expr ')'					# expressionsAssociativesDivisio
			| '(' expr '+' expr ')'					# expressionsAssociativesSuma
			| '(' expr '-' expr ')'					# expressionsAssociativesResta
			| expr '*' expr							# expressionsMultiplicacio
			| expr '/' expr							# expressionsDivisio
			| expr '+' expr							# expressionsSuma
			| expr '-' expr							# expressionsResta
			| num									# expressioNumero
;

num			: DIGS									# numeroEnter
			| DIGS '.' DIGS							# numeroDecimal
;

par 		: WORD									# paraula
;

DIGS	:	[0-9]+ ;
WS		:	[ \t\n\r]+ -> skip ;
WORD	:	[a-zA-Z\u0080-\u00FF\u005F]+ ;