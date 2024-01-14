# PandaQ
PandaQ és un intèrpret de consultes SQL en Python.

## Dependències
Instalació de les dependències via terminal.
## ANTLR4
'''bash
python3 -m pip install antlr4-python3-runtime
'''
## Pandas
'''bash
python3 -m pip install pandas
'''
## Streamlit
'''bash
python3 -m pip install streamlit
'''

## Ús
### Pas 1:
Compilar la gramàtica de l'intèrpret.
'''bash
antlr4 -Dlanguage=Python3 -no-listener -visitor pandaq.g4
'''
### Pas 2:
Executar l'intèrpret.
'''bash
python3 -m streamlit run pandaq.py
'''

## Consultes
### Exemple 1:
'''mysql
select * from countries;
'''

### Exemple 2:
#### 2.1:
'''mysql
select first_name, last_name from employees;
'''
#### 2.2:
'''mysql
select first_name, salary, salary * 1.05 as new_salary from employees;
'''

### Exemple 3:
'''mysql
select * from countries order by region_id, country_name desc;
'''

### Exemple 4:
'''mysql
select * from countries where not region_id=1 and not region_id=3;
'''

### Exemple 5:
#### 5.1:
'''mysql
select first_name, department_name from employees
inner join departments on
department_id = department_id;
'''
#### 5.2:
'''mysql
select first_name, last_name, job_title, department_name
from employees inner join departments on department_id = department_id
inner join jobs on job_id = job_id;
'''

### Exemple 6:
'''mysql
q := select first_name, last_name, job_title, department_name
from employees inner join departments on department_id = department_id
inner join jobs on job_id = job_id;
'''
'''mysql
select first_name, last_name from q;
'''

### Exemple 7:
'''mysql
q := select first_name, last_name, salary, salary*1.05 as new_salary from employees
where department_id=5;
'''
'''mysql
plot q;
'''

### Exemple 8:
'''mysql
select employee_id, first_name, last_name from employees
where department_id in
(select department_id from departments where location_id = 1700)
order by first_name, last_name;
'''


