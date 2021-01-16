# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _K8S

class _Compute(_K8S):
	_service_type = "compute"
	_icon_dir = "icons/k8s/compute"

class Cronjob(_Compute):
	_icon = "cronjob.png"
	_default_label = "Cronjob"

class Deploy(_Compute):
	_icon = "deploy.png"
	_default_label = "Deploy"

class Ds(_Compute):
	_icon = "ds.png"
	_default_label = "Ds"

class Job(_Compute):
	_icon = "job.png"
	_default_label = "Job"

class Pod(_Compute):
	_icon = "pod.png"
	_default_label = "Pod"

class Rs(_Compute):
	_icon = "rs.png"
	_default_label = "Rs"

class Sts(_Compute):
	_icon = "sts.png"
	_default_label = "Sts"

