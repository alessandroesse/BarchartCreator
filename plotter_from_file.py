from column_parser import ParseFile
from plotter_class import MyBarchartCreator

parser = ParseFile('t_400_700.csv')
columns = parser.parse()


n_attempt =list()
for i in range(0, len(columns[0])):
    n_attempt.append((i+1))

vals=dict()
vals[0]= [1,2,3,4,5,6,7,8,9,10]
vals[1]=[100,2,3,4,5,6,7,8,9,10]
mb= MyBarchartCreator(columns)
mb.values_to_label(vals)
mb.plot(limit=550)