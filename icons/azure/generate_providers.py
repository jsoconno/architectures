import os
from pathlib import Path

def format_text(text):
    return text.replace("-", " ").title().replace(" ", "")

root_dir = os.path.dirname(__file__)
services = []

for subdir, dirs, files in os.walk(root_dir):

    for file in files:
        path = Path(os.path.join(subdir, file))

        services.append(str(path.parent).split("/")[-1])

        service_type = str(path.parent).split("/")[-1].title()
        service = str(path).split("/")[-1].replace(".png", "").replace("-", " ").title().replace(" ", "")

services = set(services)

for service in services:
    service_dir = f'{root_dir}/{service}'

    for subdir, dirs, files in os.walk(service_dir):

        path = Path(os.path.join(subdir))

        provider = str(path.parent).split("/")[-1]
        service_type = str(path).split("/")[-1]
        package_root = str(path.parent.parent.parent)
        services_file = f'{package_root}/architectures/providers/{provider}/{service_type}.py'

        provider_fmt = format_text(provider)
        service_type_fmt = format_text(service_type)

        with open(services_file, 'w+') as f:
            # Create service type class
            f.write(f'# Do not modify this file directly.  It is auto-generated with Python.\n\n')
            f.write(f'from architectures.providers import _{provider_fmt}\n\n')
            f.write(f'class _{service_type_fmt}(_{provider_fmt}):\n')
            f.write(f'\t_service_type = \"{service_type}\"\n')
            f.write(f'\t_icon_dir = \"icons/{provider}/{service_type}\"\n\n')

        for file in files:
            path = Path(os.path.join(subdir, file))
            service = str(path).split("/")[-1].replace(".png", "")
            service_fmt = format_text(service)

            # Create service class
            with open(services_file, 'a') as f:
                # Create service type class
                f.write(f'class {service_fmt}(_{service_type_fmt}):\n')
                f.write(f'\t_icon = \"{service}.png\"\n')
                f.write(f'\t_default_label = "{service.replace("-", " ").title()}"\n\n')

