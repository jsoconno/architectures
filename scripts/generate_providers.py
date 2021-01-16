import os
from pathlib import Path

heading_text = f'# Do not modify this file directly. It is auto-generated with Python.\n\n'

def format_text(text):
    return text.replace("-", " ").title().replace(" ", "")

root_dir = os.path.dirname(os.getcwd())
icons_dir = os.path.join(root_dir, "icons")
providers_dir = os.path.join(root_dir, "architectures", "providers")

init_file = os.path.join(providers_dir, "__init__.py")
with open(init_file, "w+") as f:
    f.write(heading_text)
    f.write(f'from architectures.core import Node\n\n')

providers = os.listdir(icons_dir)
for provider in providers:

    provider_fmt = format_text(provider)
    with open(init_file, "a+", newline="") as f:
        f.write(f'class _{provider_fmt}(_Node):\n')
        f.write(f'\t_provider = \"{provider}\"\n')
        f.write(f'\t_icon_dir = \"icons/{provider}\"\n\n')
        f.write(f'\tfontcolor = \"#ffffff\"\n\n')

    for subdir, dirs, files in os.walk(os.path.join(icons_dir, provider)):
        if files:
            provider_dir = os.path.join(providers_dir, provider)
            if not os.path.exists(provider_dir):
                os.mkdir(provider_dir)

            service_type = os.path.split(subdir)[1]
            service_type_fmt = format_text(service_type)

            service_file = os.path.join(provider_dir, service_type) + ".py"
            with open(service_file, "w+") as f:
                # Create service type class
                f.write(heading_text)
                f.write(f'from architectures.providers import _{provider_fmt}\n\n')
                f.write(f'class _{service_type_fmt}(_{provider_fmt}):\n')
                f.write(f'\t_service_type = \"{service_type}\"\n')
                f.write(f'\t_icon_dir = \"icons/{provider}/{service_type}\"\n\n')

            for service in files:
                raw_service = service.split(".")[0]
                service_fmt = format_text(raw_service)       
                with open(service_file, 'a+', newline='') as f:
                    # Create service type class
                    f.write(f'class {service_fmt}(_{service_type_fmt}):\n')
                    f.write(f'\t_icon = \"{service}\"\n')
                    f.write(f'\t_default_label = "{raw_service.replace("-", " ").title()}"\n\n')
