# metrics.py
# هذا الملف مسؤول عن تسجيل أداء كل Search Algorithm
# (الوقت وعدد العقد اللي اتوسعت)

import time


class Metrics:
    def __init__(self):
        """
        Constructor لبدء تسجيل الأداء
        - start_time: وقت بداية تشغيل الخوارزمية
        - nodes_expanded: عدد العقد اللي تم توسيعها أثناء البحث
        - time_taken: الزمن الكلي للتنفيذ (يتحسب في الآخر)
        """
        self.start_time = time.perf_counter()   # وقت بداية الخوارزمية
        self.nodes_expanded = 0         # عدد العقد المتوسعة
        self.time_taken = 0             # الزمن الكلي للتنفيذ

    def stop(self):
        """
        يتم استدعاء هذه الدالة بعد انتهاء الخوارزمية
        لحساب الزمن الكلي للتنفيذ
        """
        self.time_taken = (time.perf_counter() - self.start_time) * 1000


        # مثال للاستخدام:
        # metrics = Metrics()
        # ... أثناء البحث:
        # metrics.nodes_expanded += 1
        # ... بعد انتهاء البحث:
        # metrics.stop()
        # print("Nodes Expanded:", metrics.nodes_expanded)
