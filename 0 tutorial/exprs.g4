// Gramàtica per expressions senzilles
grammar exprs;
root: main

main : 	expr
		| act
		| comp
		| ctrl
		;
expr : 	<assoc=right> expr '^' expr			# potencia
		| expr '*' expr						# multiplicacio
		| expr '/' expr						# divisio
		| expr '+' expr						# suma
		| expr '-' expr						# resta
		| expr ':=' expr					# assignacio
		| NUM								# numero
		| WORD								# paraula
		;

act : 'write' expr							# escriure
		;

comp: expr '<' expr							# menor
	| expr '<=' expr						# menorigual
	| expr '>' expr							# major
	| expr '>=' expr						# majorigual
	| expr '='	expr						# igual
	| expr '<>' expr						# diferent
	;

ctrl: 'if' comp 'then' act 'end'			# condicional
	| 'while' comp 'do' act expr 'end'		# mentre
	;

NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip ;
WORD : [a-zA-Z\u0080-\u00FF]+ ;
