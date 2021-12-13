# coding:utf-8

import sys
from datetime import datetime
from workflow import Workflow


# http://www.zzvips.com/article/125930.html
def timestamp2string(timestamp):
    try:
        dt = datetime.fromtimestamp(timestamp / 1000)
        # str1 = dt.strftime("%Y-%m-%d %H:%M:%S.%f")
        return dt
    except Exception as e:
        print(e)
        return ''


def generate_feedback_results(result):
    wf = Workflow()
    kwargs = {
        'title': result,
        'subtitle': '',
        "valid": True,
        'arg': result
    }
    wf.add_item(**kwargs)
    wf.send_feedback()


if __name__ == '__main__':
    # timestamp = 1.617932071158E12
    timestamp = sys.argv[1]
    out = timestamp2string(float(timestamp))
    generate_feedback_results(str(out))
