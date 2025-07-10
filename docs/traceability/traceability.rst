Traceability
============

.. needtable:: Requirements Table
   :style: table
   :columns: id;title

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
    :columns: id;

    results = []

    for need in needs.filter_types(['req']):
        if not need['implements']:
            results.append(need)

        


        
.. needtable:: Untested Requirements Table
    :style: table
    :columns: id;

    results = []

    for need in needs.filter_types(['test']):
        if not need['implements']:
            results.append(need)          