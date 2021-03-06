modules = {
    "CMT102": "",
    "CMT103": "https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=9039023b-2f6a-43f1-b498-5350e711c982",
    "CMT104": "",
    "CMT105": "https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=acfc5ad0-c8cd-4c13-97fd-b1bc49157827",
    "CMT106": "",
    "CMT107": "https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=50052841-a665-43f1-bd07-30a503912b98",
    "CMT108": "",
    "CMT111": "https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=ebbb89d0-dfac-407c-84a1-22daec0dc908",
    "CMT112": "https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=3446edae-d762-49c4-8302-a8cf74a1f315",
    "CMT202": "https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=360b3717-0492-4810-a8fe-03c289c1f9fa",
    "CMT205": "https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=ba3a49c4-7fd3-4ea8-985e-c75fb0ab72fb",
    "CMT206": "https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=c033da0c-012e-43e1-856f-b9da64ef6f01",
    "CMT207": "https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=a909e025-b20d-4412-835d-587315566301",
    "CMT209": "https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=9d765d94-dca7-444a-80d5-81a6ecf10d34",
    "CMT212": "https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=4b02ae8b-16da-4ffa-a50f-31e40682f85d",
    "CMT213": "https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=4d8e28b8-127a-4905-80d8-2f54456df9b3",
    "CMT301": "https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=b7683eda-c278-4fb5-b907-51886b9bf9c8",
    "CMT302": "https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=d92d85f8-0de0-4e73-a6eb-701798752076",
    "CMT303": "https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=33a0ef4d-43e6-436e-89dc-fae7547cf5a5",
    "CMT304": "",
    "CMT306": "https://cardiff.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=52ec9230-01ce-43a9-9ca0-503fb68c037a"
}

pfmsadsa_core = ['CMT304']
pfmsadsa_opt = ['CMT302', 'CMT306', 'CMT106', 'CMT209', 'CMT107', 'CMT105', 'CMT213', 'CMT202', 'CMT108', 'CMT206', 'CMT104', 'CMT111']

pfmscita_core = ['CMT302', 'CMT301', 'CMT103', 'CMT112', 'CMT207']
pfmscita_opt = ['CMT212', 'CMT202', 'CMT206']

pfmscmpa_core = ['CMT303', 'CMT103', 'CMT205', 'CMT112']
pfmscmpa_opt = ['CMT102', 'CMT302', 'CMT212', 'CMT111', 'CMT202', 'CMT206', 'CMT207']

pfmsdysa_core = ['MAT002', 'MAT014', 'CMT108']
pfmsdysa_opt = ['CMT112', 'CMT103', 'CMT209', 'CMT212', 'CMT111', 'CMT202', 'MAT005', 'MAT006', 'MAT007', 'MAT012']

pfmsispa_core = ['CMT301', 'CMT306', 'CMT105', 'CMT213', 'CMT104', 'CMT202']

pfmscdj_core = ['CMT112', 'CMT103']
pfmscdj_opt = ['CMT212', 'CMT111', 'CMT206']


import requests

"""
        <div id="CMT304">
        	<h3>CMT304 - Programming Paradigms</h3>
        	<a href="http://handbooks.data.cardiff.ac.uk/module/CMT304.html">Module Handbook</a>
        	<img src="img/coming_soon.png" alt="Video Coming Soon">
        	<a href="#top">Back to top</a>
        </div>
"""


def write_module_div(outfile, module, link):

    handbook_data = 'http://handbooks.data.cardiff.ac.uk/module/%s' % (module)
    module_data = requests.get(handbook_data).json()

    print(module_data['module']['moduleName'])

    ml_data = module_data['occurrences']['staff']['moduleLeader']

    semester = module_data['occurrences']['semester']['type']

    module_leader = "%s %s %s" % (ml_data['title'], ml_data['firstName'], ml_data['surname'])

    outfile.write('<div id="%s">\n' % (module))
    outfile.write('\t<h3>%s - %s</h3>\n' % (module, module_data['module']['moduleName']))
    outfile.write('\t<p><strong>Module Leader:</strong> %s</p>\n' % (module_leader))
    outfile.write('\t<p><strong>Semester: </strong>%s</p>\n' % (semester))
    outfile.write('\t<p>For module information, please see the <a href="%s">Module Handbook</a> and watch the video below</p>\n' % ('%s.html' % handbook_data))

    if link:
        outfile.write('\t<iframe src="%s" height="405" style="padding: 0px; border: 1px solid #464646;" frameborder="0"></iframe>\n' % (link))
    else:
        outfile.write('\t<img src="img/coming_soon.png" alt="Video Coming Soon">\n')

    outfile.write('\t<a href="#top">Back to top</a>\n')
    outfile.write('</div>\n')
    outfile.write('\n\n')


def do_programme(outfile, core, opt=None):

    outfile.write('<h2>Core Modules</h2>\n')
    for module in core:
        if modules.get(module):
            write_module_div(outfile, module, modules[module])
        else:
            write_module_div(outfile, module, "")

    if opt:
        outfile.write('<h2>Optional Modules</h2>\n')
        for module in opt:
            if modules.get(module):
                write_module_div(outfile, module, modules[module])
            else:
                write_module_div(outfile, module, "")

with open('pfmsadsa_out.html', 'w') as outfile:
    do_programme(outfile, pfmsadsa_core, pfmsadsa_opt)

with open('pfmscita_out.html', 'w') as outfile:
    do_programme(outfile, pfmscita_core, pfmscita_opt)

with open('pfmscmpa_out.html', 'w') as outfile:
    do_programme(outfile, pfmscmpa_core, pfmscmpa_opt)

with open('pfmsdsya_out.html', 'w') as outfile:
    do_programme(outfile, pfmsdysa_core, pfmsdysa_opt)

with open('pfmsispa_out.html', 'w') as outfile:
    do_programme(outfile, pfmsispa_core)

with open('pfmscdj_out.html', 'w') as outfile:
    do_programme(outfile, pfmscdj_core, pfmscdj_opt)
