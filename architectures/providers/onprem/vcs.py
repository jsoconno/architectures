# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Vcs(_Onprem):
	_service_type = "vcs"
	_icon_dir = "icons/onprem/vcs"

class Git(_Vcs):
	_icon = "git.png"
	_default_label = "Git"

class Github(_Vcs):
	_icon = "github.png"
	_default_label = "Github"

class Gitlab(_Vcs):
	_icon = "gitlab.png"
	_default_label = "Gitlab"

