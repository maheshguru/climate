# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

'''
Classes:
    Metric - Abstract Base Class from which all metrics must inherit.
'''

from abc import ABCMeta, abstractmethod

class Metric():
    '''Abstrace Base Class from which all metrics must inherit.'''
    __metaclass__ = ABCMeta

    def __init__(self, unary=False):
        '''Default constructor for a Metric.

        :param unary: Flag marking if the metric expects one or two operands. \
                A "unary" metric processes only a single dataset at a time. \
                By default a metric is expected to take two datasets.
        :type unary: Bool
        '''
        self.isUnary = unary

    @abstractmethod
    def run(self, datasets):
        '''Run the metric for some given dataset(s)

        :param datasets: - The dataset(s) to be used in the current metric \
                run. If this is a "unary" metric then datasets[0] contains \
                the dataset to be used in the current run. If the metric is \
                binary, then datasets[0] contains the reference dataset and \
                datasets[1] contains the target dataset.
        :type datasets: Tuple
        :returns: A list containing the results of running the metric.
        :trype: List
        '''

class Bias(Metric):
    '''Calculate the bias between a reference and target dataset.'''

    def run(self, datasets):
        '''Calculate the bias between a reference and target dataset.

        .. note::
           Overrides Metric.run()

        :param datasets: The datasets to use in the current run. The \
                reference dataset is given in datasets[0] and the target \
                dataset is given in datasets[1].
        :type datasets: Tuple
        :returns: A list containing the difference between the reference \
                dataset and the target dataset.
        :rtype: List
        '''
        return [datasets[0] - datasets[1]]
