# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Gitops(_Onprem):
	_service_type = "gitops"
	_icon_dir = "icons/onprem/gitops"

class Argocd(_Gitops):
	_icon = "argocd.png"
	_default_label = "Argocd"

class Flagger(_Gitops):
	_icon = "flagger.png"
	_default_label = "Flagger"

class Flux(_Gitops):
	_icon = "flux.png"
	_default_label = "Flux"

