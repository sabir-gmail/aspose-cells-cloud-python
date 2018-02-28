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
from asposecellscloud.apis.cells_hypelinks_api import CellsHypelinksApi
import AuthUtil
from asposecellscloud.models import Hyperlink

class TestCellsHypelinksApi(unittest.TestCase):
    """ CellsHypelinksApi unit test stubs """

    def setUp(self):
        self.api_client = AuthUtil.GetApiClient()
        self.api = asposecellscloud.apis.cells_hypelinks_api.CellsHypelinksApi(self.api_client)

    def tearDown(self):
        pass

    def test_cells_hypelinks_delete_worksheet_hyperlink(self):
        """
        Test case for cells_hypelinks_delete_worksheet_hyperlink

        Delete worksheet hyperlink by index.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        hyperlinkIndex = 0         
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_hypelinks_delete_worksheet_hyperlink(name, sheet_name,hyperlinkIndex,folder=folder)
        pass

    def test_cells_hypelinks_delete_worksheet_hyperlinks(self):
        """
        Test case for cells_hypelinks_delete_worksheet_hyperlinks

        Delete all hyperlinks in worksheet.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        hyperlinkIndex = 0         
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_hypelinks_delete_worksheet_hyperlinks(name, sheet_name,folder=folder)
        pass

    def test_cells_hypelinks_get_worksheet_hyperlink(self):
        """
        Test case for cells_hypelinks_get_worksheet_hyperlink

        Get worksheet hyperlink by index.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        hyperlinkIndex = 0         
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_hypelinks_get_worksheet_hyperlink(name, sheet_name,hyperlinkIndex,folder=folder)
        pass

    def test_cells_hypelinks_get_worksheet_hyperlinks(self):
        """
        Test case for cells_hypelinks_get_worksheet_hyperlinks

        Get worksheet hyperlinks.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        hyperlinkIndex = 0         
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_hypelinks_get_worksheet_hyperlinks(name, sheet_name,folder=folder)
        pass

    def test_cells_hypelinks_post_worksheet_hyperlink(self):
        """
        Test case for cells_hypelinks_post_worksheet_hyperlink

        Update worksheet hyperlink by index.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        hyperlinkIndex = 0         
        folder = "Temp"
        hyperlink = Hyperlink()
        hyperlink.address = 'http://wwww.aspose.com'
        AuthUtil.Ready(name, folder)
        result = self.api.cells_hypelinks_post_worksheet_hyperlink(name, sheet_name, hyperlinkIndex , hyperlink = hyperlink , folder=folder)
        pass

    def test_cells_hypelinks_put_worksheet_hyperlink(self):
        """
        Test case for cells_hypelinks_put_worksheet_hyperlink

        Add worksheet hyperlink.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        firstRow = 1      
        firstColumn =1 
        totalRows = 2 
        totalColumns = 3 
        address = 'http://www.aspose.com'    
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_hypelinks_put_worksheet_hyperlink(name, sheet_name,firstRow,firstColumn,totalRows,totalColumns,address,folder=folder)
        pass


if __name__ == '__main__':
    unittest.main()