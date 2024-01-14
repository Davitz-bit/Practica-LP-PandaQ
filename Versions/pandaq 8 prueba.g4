// Gramàtica per expressions senzillesfrom
grammar pandaq;

root		: par ':=' consulta										# rootEstat
			| 'plot' par ';'										# rootGrafic
			| consulta												# rootConsulta
;

consulta	: 'select' camps 'from' par subconsulta ';'				# consultaSubconsulta
			| 'select' camps 'from' par innerjoin ';'				# consultaInnerJoin
			| 'select' camps 'from' par filtre ';'					# consultaFiltre
			| 'select' camps 'from' par ordre ';'					# consultaOrdre
			| 'select' camps 'from' par ';'							# consultaTaula
;

subconsulta	: 'where' par 'in' '(' consulta ')' innerjoin;			# subconsultaInnerJoin
			| 'where' par 'in' '(' consulta ')' filtre				# subconsultaFiltre
			| 'where' par 'in' '(' consulta ')' ordre				# subconsultaOrdre
			| 'where' par 'in' '(' consulta ')'						# subconsultaTaula
;

innerjoin	: innerjoin innerjoin									# innerJoinVariesTaules
			| 'inner' 'join' par 'on' par '=' par filtre			# innerJoinFiltre
			| 'inner' 'join' par 'on' par '=' par ordre				# innerJoinOrdre
			| 'inner' 'join' par 'on' par '=' par					# innerJoinTaula
;

filtre		: filtre 'and' filtre									# filtreAnd
			| par '<' expr ordre									# filtreMenorOrdre
			| par '=' expr ordre									# filtreIgualOrdre
			| par '<' expr											# filtreMenor
			| par '=' expr											# filtreIgual
			| 'not' filtre											# filtreNot
;

ordre		: ordre ',' ordre										# ordreVarisCamps
			| par 'asc'												# ordreCampAcendent
			| par 'desc'											# ordreCampDescendent
			| par													# ordreCamp
;

camps		: '*'													# seleccionarTotsCamps
			| '*' ',' campssc										# seleccionarTotsICalcularCamps
			| campsnc ',' campssc									# seleccionarICalcularCamps
			| campsnc												# seleccionarCamps
			| campssc												# calcularCamps
;

campsnc		: campsnc ',' campsnc									# seleccionarVarisCamps
			| par													# seleccionarCamp
;

campssc		: campssc ',' campssc									# calcularVarisCamps
			| par '*' expr 'as' par									# calcularCampMultiplicacio
			| par '/' expr 'as' par									# calcularCampDivisio
			| par '+' expr 'as' par									# calcularCampSuma
			| par '-' expr 'as' par									# calcularCampResta
;

expr		: '(' expr '*' expr ')'									# expressionsAssociativesMultiplicacio
			| '(' expr '/' expr ')'									# expressionsAssociativesDivisio
			| '(' expr '+' expr ')'									# expressionsAssociativesSuma
			| '(' expr '-' expr ')'									# expressionsAssociativesResta
			| expr '*' expr											# expressionsMultiplicacio
			| expr '/' expr											# expressionsDivisio
			| expr '+' expr											# expressionsSuma
			| expr '-' expr											# expressionsResta
			| num													# expressioNumero
;

num			: DIGS													# numeroEnter
			| DIGS '.' DIGS											# numeroDecimal
;

par 		: WORD													# paraula
;

DIGS		: [0-9]+ ;
WS			: [ \t\n\r]+ -> skip ;
WORD		: [a-zA-Z\u0080-\u00FF\u005F]+ ;