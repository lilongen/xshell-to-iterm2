{
	"Profiles": [
		{% for profile in profiles %}
		{
			"Name": "{{ profile.name }}",
			"Guid": "{{ profile.name }}",
			"Custom Command": "Yes",
			"Command": "ssh {{ profile.username }}@{{ profile.ip }}{% if profile.port != "22" %} -P {{ profile.port }} {% endif %}",
			"Tags": {{ profile.tag }},
		},
		{% endfor %}
	]
}