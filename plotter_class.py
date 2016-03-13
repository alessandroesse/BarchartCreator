import pylab as plt
import numpy as np

class ParametersError(Exception):
        def __init__(self, message):
            # Call the base class constructor with the parameters it needs
            super(Exception, self).__init__(message)

class MyBarchartCreator(object):

    def __init__(self, data, N=10, is_dict=True, is_list=False):

        if is_dict == is_list:
            raise  ParametersError('wrong setting is_dict must be != from is_list')

        if is_dict:
            self.data_type= 1

        self.N= N
        if is_dict:
            assert isinstance(data, dict)
            self.data_to_plot = dict()
            counter = 0
            for k in data.keys():
                counter += 1
                self.data_to_plot[k]= tuple(data[k])
        self.has_labels = False

    def values_to_label(self, values, is_dict=True, is_list=False):
        if is_dict == is_list:
            raise  ParametersError('wrong setting is_dict must be != from is_list')
        if is_dict:
            assert isinstance(values, dict)
            if len(values[0]) != self.N:
                raise ParametersError('values to label don\'t match with data')
            self.label_values= values
            self.has_labels =True

    def plot(self, limit = None):

        ind = np.arange(self.N)  # the x locations for the groups
        width = 0.35       # the width of the bars
        fig, ax = plt.subplots()

        rects1 = ax.bar(ind, self.data_to_plot[0], width, color='r')
        rects2 = ax.bar(ind + width, self.data_to_plot[1], width, color='y')

        # add some text for labels, title and axes ticks
        ax.set_ylabel('Time')
        if limit is not None:
            ax.set_ylim(0, limit)
        ax.set_title('Used time per run to spread the configuration')
        ax.set_xticks(ind + width)
        ax.set_xlabel('# run')
        ax.set_xticklabels(('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))

        ax.legend((rects1[0], rects2[0]), ('AP stress (throttling 400us)', 'MP stress (throttling 200us/500us)'))

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


            autolabel(rects1,self.label_values[0])
            autolabel(rects2, self.label_values[1])

        plt.show()