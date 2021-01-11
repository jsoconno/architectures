# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Ci(_Onprem):
	_service_type = "ci"
	_icon_dir = "icons/onprem/ci"

class Gitlabci(_Ci):
	_icon = "gitlabci.png"
	_default_label = "Gitlabci"

class Teamcity(_Ci):
	_icon = "teamcity.png"
	_default_label = "Teamcity"

class Concourseci(_Ci):
	_icon = "concourseci.png"
	_default_label = "Concourseci"

class Zuulci(_Ci):
	_icon = "zuulci.png"
	_default_label = "Zuulci"

class Droneci(_Ci):
	_icon = "droneci.png"
	_default_label = "Droneci"

class Circleci(_Ci):
	_icon = "circleci.png"
	_default_label = "Circleci"

class Jenkins(_Ci):
	_icon = "jenkins.png"
	_default_label = "Jenkins"

class GithubActions(_Ci):
	_icon = "github-actions.png"
	_default_label = "Github Actions"

class Travisci(_Ci):
	_icon = "travisci.png"
	_default_label = "Travisci"

