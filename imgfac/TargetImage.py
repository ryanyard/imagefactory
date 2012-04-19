# encoding: utf-8

#   Copyright 2012 Red Hat, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from PersistentImage import PersistentImage
from props import prop


METADATA = ('base_image_id', 'target', 'parameters')

class TargetImage(PersistentImage):
    """ TODO: Docstring for TargetImage  """

    base_image_id = prop("_base_image_id")
    target = prop("_target")
    parameters = prop("_parameters")

    def __init__(self, image_id=None):
        super(TargetImage, self).__init__(image_id)
        self.base_image_id = None
        self.target = None
        self.parameters = None