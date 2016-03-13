import pylab as plt
import numpy as np

class ParametersError(Exception):
        def __init__(self, message):
            # Call the base class constructor with the parameters it needs
            super(Exception, self).__init__(message)

class MyBarchartCreator(object):

    def __init__(self, data, title="", N=10, is_dict=True, is_list=False):

        if is_dict == is_list:
            raise  ParametersError('wrong setting is_dict must be != from is_list')

        if is_dict:
            self.data_type= 1

        self.title = title
        self.n_columns= len(data.keys())
        self.N= N
        if is_dict:
            assert isinstance(data, dict)
            self.data_to_plot = dict()
            counter = 0
            for k in data.keys():
                counter += 1
                self.data_to_plot[k]= tuple(data[k])
        self.has_labels = False
        self.has_legend = False

    def bind_labels(self, values, is_dict=True, is_list=False):
        if is_dict == is_list:
            raise  ParametersError('wrong setting is_dict must be != from is_list')
        if is_dict:
            assert isinstance(values, dict)
            if len(values[0]) != self.N:
                raise ParametersError('values to label don\'t match with data')
            self.label_values= values
            self.has_labels =True

    def bind_legend(self, tuple_string):
        assert(isinstance(tuple_string, tuple))
        self.legend = tuple_string
        self.has_legend = True

    def plot(self, limit = None, legends=None):
        """

        :param limit: to overcome the limit of a certain number
        :param legends: customize the legend
        :return: None
        """

        ind = np.arange(self.N) * 2 # the x locations for the groups
        width = 0.6 # the width of the bars
        fig, ax = plt.subplots()

        rects_list = list()

        colours = ['b', 'r', 'c', 'm', 'y', 'b']
        tot_col = len(colours)

        last_pos = ind
        cntr = 0
        for (k,i) in self.data_to_plot.iteritems():
            rects_list.append(ax.bar(last_pos, i, width, color=colours[cntr]))
            last_pos = ind+(width * (cntr+1))
            cntr = (cntr+1)%tot_col

        # add some text for labels, title and axes ticks
        ax.set_ylabel('Time (s)')

        if limit is not None:
            act_max = -1000
            for (k,i) in self.data_to_plot.iteritems():
                if act_max < max(i):
                    act_max = max(i)

            ax.set_ylim(0, act_max+limit)

        ax.set_title(self.title)
        ax.set_xticks(ind + (width))
        ax.set_xlabel('# run')
        ax.set_xticklabels(('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))

        if self.has_legend:
            ax.legend(tuple(rects_list), self.legend)

        if self.has_labels is True:

            def autolabel(rects, values):
                # attach some text labels
                counter = 0
                for rect in rects:
                    height = rect.get_height()
                    ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                            '%d' % int(values[counter]),
                            ha='center', va='bottom')
                    counter += 1

            for i in range(0, self.n_columns):
                autolabel(rects_list[i], self.label_values[i])
        plt.show()