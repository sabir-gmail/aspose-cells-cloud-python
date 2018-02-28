# coding: utf-8

"""
    Web API Swagger specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)
import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_task_api import CellsTaskApi
import AuthUtil
from asposecellscloud.models import TaskDescription
from asposecellscloud.models import SplitWorkbookTaskParameter
from asposecellscloud.models import FileSource
from asposecellscloud.models import TaskData

class TestCellsTaskApi(unittest.TestCase):
    """ CellsTaskApi unit test stubs """

    def setUp(self):
        self.api_client = AuthUtil.GetApiClient()
        self.api = asposecellscloud.apis.cells_task_api.CellsTaskApi(self.api_client)

    def tearDown(self):
        pass

    def test_cells_task_post_run_task(self):
        """
        Test case for cells_task_post_run_task

        Run tasks  
        """
        name ='Book1.xlsx'
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        task1 = TaskDescription()
        task1.task_type = 'SplitWorkbook'
        param1 = SplitWorkbookTaskParameter()
        param1.destination_file_format = 'xlsx'
        fileSource = FileSource()
        fileSource.file_path = folder
        fileSource.file_source_type = 'CloudFileSystem'
        param1.destination_file_position = fileSource
        param1.split_name_rule = 'sheetname'
        workbook = FileSource()
        workbook.file_path = folder + "\\" + name
        workbook.file_source_type = 'CloudFileSystem'
        param1.workbook = workbook
        task1.task_parameter = param1
        taskData = TaskData()
        tasks = [task1]
        taskData.tasks = tasks
        result = self.api.cells_task_post_run_task(taskData)
        pass


if __name__ == '__main__':
    unittest.main()