# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Aws

class _Cost(_Aws):
    _service_type = "cost"
    _icon_dir = "icons/aws/cost"

class SavingsPlans(_Cost):
    _icon = "savings-plans.png"
    _default_label = "Savings Plans"

class CostAndUsageReport(_Cost):
    _icon = "cost-and-usage-report.png"
    _default_label = "Cost And Usage Report"

class ReservedInstanceReporting(_Cost):
    _icon = "reserved-instance-reporting.png"
    _default_label = "Reserved Instance Reporting"

class Budgets(_Cost):
    _icon = "budgets.png"
    _default_label = "Budgets"

class CostExplorer(_Cost):
    _icon = "cost-explorer.png"
    _default_label = "Cost Explorer"