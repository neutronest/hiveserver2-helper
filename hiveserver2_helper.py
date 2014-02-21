#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Copyright (c) 2014 neutronest <neutronest@gmail.com> <dongchao@xiaomi.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import pyhs2


class hiveserver2_helper(object):
    """
    this class is just the tool to connect and get data from xiaomi hive
    server 2

    before use it, you must pip install the lib "pyhs2" before.
    """
    
    def __init__(self):
        self.conn = None
        self.cur = None
        return

    def connect(self, config):
        """
        connect hiveServer2 with your config

        Parameters:
        -----------
        config : dict.
          | config['host'] The host ip of hive server 2
          | config['port'] The port of hive server 2
          | config['authMechanism'] Most time the value is "NOSASL"
          | config['user'] The connect user
          | config['password'] The connect password
          | config['database'] The database which you want to connect

        Returns:
        --------
        None
        """

        self.conn = pyhs2.connect(host=config['host'],
                                  port=config['port'],
                                  authMechanism=config['authMechanism'],
                                  user=config['user'],
                                  password=config['password'],
                                  database=config['database'])
        self.cur = self.conn.cursor()

    def execute_hql(self, hql):
        """
        execute the hql then get data

        Parameters:
        -----------
        hql: string
          | a string contain hive sql you give

        Returns:
        --------
        records: list
          | always is a Two-Dimensional list
          | example: [['xx', 'xx', ...],['xx', 'xx', ...]...  ]
        """
        self.cur.execute(hql)

        records = self.cur.fetch()
        return records

    ### close the conn
    def close(self):
        """simple close connect
        """
        self.conn.close()
        return
