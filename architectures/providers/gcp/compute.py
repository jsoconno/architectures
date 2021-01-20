# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Gcp

class _Compute(_Gcp):
    _service_type = "compute"
    _icon_dir = "icons/gcp/compute"

class Functions(_Compute):
    _icon = "functions.png"
    _default_label = "Functions"

class KubernetesEngine(_Compute):
    _icon = "kubernetes-engine.png"
    _default_label = "Kubernetes Engine"

class Gpu(_Compute):
    _icon = "gpu.png"
    _default_label = "Gpu"

class ComputeEngine(_Compute):
    _icon = "compute-engine.png"
    _default_label = "Compute Engine"

class AppEngine(_Compute):
    _icon = "app-engine.png"
    _default_label = "App Engine"

class Run(_Compute):
    _icon = "run.png"
    _default_label = "Run"

class GkeOnPrem(_Compute):
    _icon = "gke-on-prem.png"
    _default_label = "Gke On Prem"

class ContainerOptimizedOs(_Compute):
    _icon = "container-optimized-os.png"
    _default_label = "Container Optimized Os"