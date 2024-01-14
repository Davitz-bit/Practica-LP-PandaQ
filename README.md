# PandaQ
PandaQ és un intèrpret de consultes SQL en Python.

## Dependències
Instalació de les dependències via terminal.
### ANTLR4
```bash
python3 -m pip install antlr4-python3-runtime
```
### Pandas
```bash
python3 -m pip install pandas
```
### Streamlit
```bash
python3 -m pip install streamlit
```

## Ús
### Pas 1:
Compilar la gramàtica de l'intèrpret.
```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor pandaq.g4
```
### Pas 2:
Executar l'intèrpret.
```bash
python3 -m streamlit run pandaq.py
```

## Consultes
### Comanda 1:
```bash
select * from taula;
```
Exemple:
```sql
select * from countries;
```

### Comanda 2:
```bash
select camp1, camp2... from taula;
```
Exemple:
```sql
select first_name, last_name from employees;
```
### Comanda 3:
```bash
select camp_no_calculat, camp_calculat as id from taula;
```
Exemple:
```sql
select first_name, salary, salary * 1.05 as new_salary from employees;
```

### Comanda 4:
```bash
select camps from taula order by camp1 [asc|desc], camp2 [asc|desc];
```
Exemple:
```sql
select * from countries order by region_id, country_name desc;
```

### Comanda 5:
```bash
select camps from taula where condició;
```
Exemple:
```sql
select * from countries where not region_id=1 and not region_id=3;
```

### Comanda 6:
```bash
select camps from taula1
inner join taula2 on 
      camp_taula_1 = camp_taula_2;
```
Exemples:
```sql
select first_name, department_name from employees
inner join departments on
department_id = department_id;
```
~~~~sql
select first_name, last_name, job_title, department_name
from employees inner join departments on department_id = department_id
inner join jobs on job_id = job_id;
~~~~

### Comanda 7:
```bash
id := consulta;
```
```bash
select * from id;
```
Exemple:
```sql
q := select first_name, last_name, job_title, department_name
from employees inner join departments on department_id = department_id
inner join jobs on job_id = job_id;
```
```sql
select first_name, last_name from q;
```

### Comanda 8:
```bash
id := consulta;
```
```bash
plot id ;
```
Exemple:
```sql
q := select first_name, last_name, salary, salary*1.05 as new_salary from employees
where department_id=5;
```
```sql
plot q;
```

### Comanda 9:
```bash
select camps from taula where camp in (consulta);
```
Exemple:
```sql
select employee_id, first_name, last_name from employees
where department_id in
(select department_id from departments where location_id = 1700)
order by first_name, last_name;
```


