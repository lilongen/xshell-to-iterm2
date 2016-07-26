{
	"Profiles": [
		{% for profile in profiles %}
		{
			"Name": "{{ profile.name }}",
			"Guid": "{{ profile.name }}",
			"Custom Command": "Yes",
			"Command": "ssh root@{{ profile.ip }}",
			"Tags": {{ profile.tag }},
		},
		{% endfor %}
	]
}