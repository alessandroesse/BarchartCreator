from column_parser import ParseFile
from plotter_class import MyBarchartCreator

parser = ParseFile('t_400_700.csv')

# the columns are returned as a dictionary {0: [values]; 1: [values]}
columns = parser.parse()

#values to bind as label for each bar
vals=dict()
vals[0]= [3,0,0,0,0,0,0,1,2,0]
vals[1]=[1,0,2,0,1,0,0,1,1,4]

#instantiate
mb= MyBarchartCreator(columns)

#bind the label
mb.bind_labels(vals)

#elaborates and show
mb.plot(limit=550)