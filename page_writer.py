modules = [
    ("CMT102",""),
    ("CMT103","https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=650b64a2-9e94-4599-b927-1eef820d40e3"),
    ("CMT104",""),
    ("CMT105","https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=acfc5ad0-c8cd-4c13-97fd-b1bc49157827"),
    ("CMT106",""),
    ("CMT107","https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=50052841-a665-43f1-bd07-30a503912b98"),
    ("CMT108",""),
    ("CMT111","https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=ebbb89d0-dfac-407c-84a1-22daec0dc908"),
    ("CMT112","https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=3446edae-d762-49c4-8302-a8cf74a1f315"),
    ("CMT202",""),
    ("CMT205","https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=ba3a49c4-7fd3-4ea8-985e-c75fb0ab72fb"),
    ("CMT206","https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=c033da0c-012e-43e1-856f-b9da64ef6f01"),
    ("CMT207",""),
    ("CMT209",""),
    ("CMT212","https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=4b02ae8b-16da-4ffa-a50f-31e40682f85d"),
    ("CMT213","https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=4d8e28b8-127a-4905-80d8-2f54456df9b3"),
    ("CMT301","https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=b7683eda-c278-4fb5-b907-51886b9bf9c8"),
    ("CMT302",""),
    ("CMT303",""),
    ("CMT304",""),
    ("CMT306","https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=04f99bf3-4d14-4f18-ae3a-e1d69aae9cc7")
]

import requests

"""
<h2>Optional Modules</h2>
<h3>CMT302 - E-commerce &amp; Innovation</h3>
<a href="http://handbooks.data.cardiff.ac.uk/module/CMT302.html">Module Handbook</a>
<img src="img/coming_soon.png" alt="Video Coming Soon">
"""

with open('out.html', 'w') as outfile:
    for module in modules:

        handbook_data = 'http://handbooks.data.cardiff.ac.uk/module/%s' % (module[0])
        module_data = requests.get(handbook_data).json()

        print(module_data['module']['moduleName'])

        outfile.write('<h3>%s - %s</h3>\n' % (module[0], module_data['module']['moduleName']))
        outfile.write('<a href="%s">Module Handbook</a>\n' % ('%s.html' % handbook_data))

        if module[1]:
            outfile.write('<iframe src="%s" width="720" height="405" style="padding: 0px; border: 1px solid #464646;" frameborder="0"></iframe>\n' % (module[1]))
        else:
            outfile.write('<img src="img/coming_soon.png" alt="Video Coming Soon">\n')

        outfile.write('\n\n')
