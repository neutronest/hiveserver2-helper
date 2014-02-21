### hiveserver2-helper

This file is just using to connect hive server2 with a lib called "pyhs2".

**Make sure that you have pip install the pyhs2 library before using this short code.**

Enjoy the HiveServer2 Now!!!

### Example

    import sys

    sys.path.append("..")
    from hiveserver2_helper import hiveserver2_helper

    helper = hiveserver2_helper()
    helper.connect(config) ### the config is supported by youself.

    hql = "select * from XXX where ..." ### the hql you given
    records = helper.execute_hql(hql)
    for record in records:
        print record

