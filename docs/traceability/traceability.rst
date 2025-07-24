Traceability
============

.. needtable:: Requirements Table
   :style: table
   :columns: id;title; implements

   results = []

   for need in needs.filter_types(['req']):
        results.append(need)

.. needtable:: Test Case Table
    :style: table
    :columns: id;tests

    results = []

    for need in needs.filter_types(['test']):
        if need['tests']:
            results.append(need)
            

            
.. needtable:: Unimplemented Requirements Table
    :style: table
    :columns: id;req;tests;implements

    results = []

    for need in needs.filter_types(['impl']):
        if need['tests']:
            results.append(need)

        


        
.. needtable:: Untested Requirements Table
    :style: table
    :columns: id;

    results = []

    for need in needs.filter_types(['test']):
        if not need['implements']:
            results.append(need)          