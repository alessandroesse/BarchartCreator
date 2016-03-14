from column_parser import ParseFile
from plotter_class import MyBarchartCreator

parser = ParseFile('t_400_700.csv')

# the columns are returned as a dictionary {0: [values]; 1: [values]}
columns = parser.parse()
#columns = dict()
#columns[2] = [100,100,100,100,100,100,100,100,100,100]

#values to bind as label for each bar
vals=dict()
vals[0] = [3,0,0,0,0,0,0,1,2,0]
vals[1] = [1,0,2,0,1,0,0,1,1,4]

#instantiate
mb = MyBarchartCreator(columns, title='Time required to spread the configuration (per run)')

#bind the label
mb.bind_labels(vals)
mb.bind_legend(('AP stress (throttling 400us)', 'MP stress (throttling 200us/800us)'))

#elaborates and show
mb.plot(limit=100)