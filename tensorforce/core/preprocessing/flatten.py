# Copyright 2017 reinforce.io. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from tensorforce import util
from tensorforce.core.preprocessing import Preprocessor


class Flatten(Preprocessor):
    """
    Normalize state. Subtract minimal value and divide by range.
    """

    def __init__(self, scope='flatten', summary_labels=()):
        super(Flatten, self).__init__(scope=scope, summary_labels=summary_labels)

    def processed_shape(self, shape):
        return -1, util.prod(shape[1:])

    def tf_process(self, tensor):
        # Flatten tensor
        return tf.reshape(tensor=tensor, shape=self.processed_shape(util.shape(tensor)))
