# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Alibabacloud

class _Storage(_Alibabacloud):
	_service_type = "storage"
	_icon_dir = "icons/alibabacloud/storage"

class CloudStorageGateway(_Storage):
	_icon = "cloud-storage-gateway.png"
	_default_label = "Cloud Storage Gateway"

class FileStorageHdfs(_Storage):
	_icon = "file-storage-hdfs.png"
	_default_label = "File Storage Hdfs"

class FileStorageNas(_Storage):
	_icon = "file-storage-nas.png"
	_default_label = "File Storage Nas"

class HybridBackupRecovery(_Storage):
	_icon = "hybrid-backup-recovery.png"
	_default_label = "Hybrid Backup Recovery"

class HybridCloudDisasterRecovery(_Storage):
	_icon = "hybrid-cloud-disaster-recovery.png"
	_default_label = "Hybrid Cloud Disaster Recovery"

class Imm(_Storage):
	_icon = "imm.png"
	_default_label = "Imm"

class ObjectStorageService(_Storage):
	_icon = "object-storage-service.png"
	_default_label = "Object Storage Service"

class ObjectTableStore(_Storage):
	_icon = "object-table-store.png"
	_default_label = "Object Table Store"

