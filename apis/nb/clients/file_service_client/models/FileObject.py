#!/usr/bin/env python
#pylint: skip-file
"""
Copyright 2016 Cisco Systems

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

class FileObject(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'nameSpace': 'str',


            'id': 'str',


            'downloadPath': 'str',


            'fileFormat': 'str',


            'fileSize': 'str',


            'md5Checksum': 'str',


            'sha1Checksum': 'str',


            'name': 'str',


            'attributeInfo': 'object'

        }

        self.attributeMap = {

            'nameSpace': 'nameSpace',

            'id': 'id',

            'downloadPath': 'downloadPath',

            'fileFormat': 'fileFormat',

            'fileSize': 'fileSize',

            'md5Checksum': 'md5Checksum',

            'sha1Checksum': 'sha1Checksum',

            'name': 'name',

            'attributeInfo': 'attributeInfo'

        }


        #A group of file IDs contained in a common nameSpace

        self.nameSpace = None # str

        #file indentification number

        self.id = None # str

        #Absolute path of the file

        self.downloadPath = None # str

        #MIME Type of the File. e.g. text/plain, application/xml, audio/mpeg

        self.fileFormat = None # str

        #Size of the file in bytes

        self.fileSize = None # str

        #md5Checksum of the file

        self.md5Checksum = None # str

        #sha1Checksum of the file

        self.sha1Checksum = None # str

        #Name of the file

        self.name = None # str


        self.attributeInfo = None # object

