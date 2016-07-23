var dates = {
    "hwk": [
	{% for asn in site.hwk %}
	{
	    "num" : "{{ asn.num }}",
	    "ready" :  "{{ asn.ready }}",
	    "desc" :  "{{ asn.desc }}",
	    "assigned" :  "{{ asn.assigned }}",
	    "due" :  "{{ asn.due }}",
	    "url" :  "{{ asn.url }}",
	},
	{% endfor %}
    ],
    "lab": [
	{% for asn in site.lab %}
	{
	    "num" : "{{ asn.num }}",
	    "ready" :  "{{ asn.ready }}",
	    "desc" :  "{{ asn.desc }}",
	    "assigned" :  "{{ asn.assigned }}",
	    "due" :  "{{ asn.due }}",
	    "url" :  "{{ asn.url }}",
	},
	{% endfor %}
    ],

    "lectures": [
	{% for lecture in site.lectures %}
	{
	    "url" : "{{ lecture.url }}",
	    "path" : "{{ lecture.path }}",
	    "week" : "{{ lecture.week }}",
	    "lecture_date" :  "{{ lecture.lecture_date }}",
	    "topic" :  "{{ lecture.topic }}",
	    "desc" :  "{{ lecture.desc }}",
	},
	{% endfor %}
    ],

    
};

