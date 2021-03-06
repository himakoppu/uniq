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

class ScalableGroupDTO(object):



    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'description': 'str',


            'identitySourceIpAddress': 'str',


            'createTime': 'int',


            'scalableGroupExternalHandle': 'str',


            'lastUpdateTime': 'int',


            'identitySourceType': 'str',


            'identitySourceId': 'str',


            'name': 'str',


            'id': 'str'

        }

        self.attributeMap = {

            'description': 'description',

            'identitySourceIpAddress': 'identitySourceIpAddress',

            'createTime': 'createTime',

            'scalableGroupExternalHandle': 'scalableGroupExternalHandle',

            'lastUpdateTime': 'lastUpdateTime',

            'identitySourceType': 'identitySourceType',

            'identitySourceId': 'identitySourceId',

            'name': 'name',

            'id': 'id'

        }


        #description

        self.description = None # str

        #identitySourceIpAddress

        self.identitySourceIpAddress = None # str

        #createTime

        self.createTime = None # int

        #scalableGroupExternalHandle

        self.scalableGroupExternalHandle = None # str

        #lastUpdateTime

        self.lastUpdateTime = None # int

        #identitySourceType

        self.identitySourceType = None # str

        #identitySourceId

        self.identitySourceId = None # str

        #name

        self.name = None # str

        #id

        self.id = None # str

