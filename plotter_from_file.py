import enum
from column_parser import ParseFile
from plotter_class import MyBarchartCreator

parser = ParseFile('t_400_700.csv')
columns = parser.parse()


n_attempt =list()
for i in range(0, len(columns[0])):
    n_attempt.append((i+1))

mb= MyBarchartCreator(columns)
mb.plot()